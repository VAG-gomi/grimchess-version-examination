from pathlib import Path
import hashlib, json, zipfile, subprocess, re, shutil, os

CURRENT=Path('/home/ubuntu/comparison-current')
OLD=Path('/home/ubuntu/comparison-old')
OUT=Path('/home/ubuntu/GRIMCHESS-VERSION-EXAMINATION')
for d in ['scripts','results/apk','results/source','results/build','results/engine','results/architecture','inputs','docs']:
 (OUT/d).mkdir(parents=True,exist_ok=True)

def sha(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
def blob(repo,rel):
 return subprocess.check_output(['git','hash-object',str(repo/rel)],text=True).strip()
def files_under(repo,root):
 base=repo/root; return {p.relative_to(base).as_posix():p for p in base.rglob('*') if p.is_file() and '.git' not in p.parts}
def cmp_files(a,b):
 out=[]; keys=sorted(set(a)|set(b))
 for k in keys:
  if k not in a: status='ADDED'; ah=None; bh=sha(b[k])
  elif k not in b: status='REMOVED'; ah=sha(a[k]); bh=None
  else:
   ah=sha(a[k]); bh=sha(b[k]); status='BYTE-IDENTICAL' if ah==bh else 'MODIFIED'
  out.append({'path':k,'status':status,'old_sha256':ah,'current_sha256':bh,'old_size':a[k].stat().st_size if k in a else None,'current_size':b[k].stat().st_size if k in b else None})
 return out

def apk_info(p,eid,repo,rel):
 with zipfile.ZipFile(p) as z:
  entries=[]
  for n in sorted(z.namelist()):
   d=z.read(n); entries.append({'path':n,'size':len(d),'sha256':hashlib.sha256(d).hexdigest()})
  return {'evidence_id':eid,'repository':repo,'path':rel,'sha256':sha(p),'size_bytes':p.stat().st_size,'zip_entry_count':len(entries),'dex_entries':[x for x in entries if x['path'].endswith('.dex')],'js_entries':[x for x in entries if x['path'].lower().endswith(('.js','.js.map'))],'wasm_entries':[x for x in entries if x['path'].lower().endswith(('.wasm','.wasm.gz'))],'native_entries':[x for x in entries if '/lib/' in x['path'] and x['path'].endswith(('.so','.so.gz'))],'stockfish_entries':[x for x in entries if 'stockfish' in x['path'].lower()],'configuration_entries':[x for x in entries if any(s in x['path'].lower() for s in ['manifest','capacitor','package.json','config','gradle'])],'all_entries':entries}

def source_map(repo,kind):
 if kind=='current': return files_under(repo,Path('src/src'))
 return files_under(repo,Path('recovered-source/grimchess-mobile/src'))
def map_selected(repo,kind):
 if kind=='current': roots=[Path('src'),Path('build-config')]
 else: roots=[Path('recovered-source/grimchess-mobile')]
 out={}
 for root in roots:
  for rel,p in files_under(repo,root).items():
   # current build config and source canonical namespace; old mobile root
   key=rel if kind=='current' else rel
   out[key]=p
 return out

# APK records.
cur_apk=CURRENT/'artifacts/GrimChess-Current-Forensic-F1.apk'
old_apks=sorted((OLD/'artifacts/apk').glob('*.apk'))
apks=[apk_info(cur_apk,'CURRENT-F1','VAG-gomi/grimchess-f1-forensic','artifacts/GrimChess-Current-Forensic-F1.apk')]
for p in old_apks:
 eid=p.name.split('__',1)[0]; apks.append(apk_info(p,eid,'VAG-gomi/grimchess-old-forensic',f'artifacts/apk/{p.name}'))
(OUT/'results/apk/apk_inventory.json').write_text(json.dumps(apks,indent=2)+'\n')
# Pair comparisons with exact archive entry differences.
pairs=[]
for old in apks[1:]:
 cur=apks[0]; oa={x['path']:x for x in old['all_entries']}; ca={x['path']:x for x in cur['all_entries']}
 rows=[]
 for path in sorted(set(oa)|set(ca)):
  if path not in oa: st='ADDED'
  elif path not in ca: st='REMOVED'
  elif oa[path]['sha256']==ca[path]['sha256'] and oa[path]['size']==ca[path]['size']: st='BYTE-IDENTICAL'
  else: st='MODIFIED'
  rows.append({'path':path,'status':st,'old_size':oa.get(path,{}).get('size'),'current_size':ca.get(path,{}).get('size'),'old_sha256':oa.get(path,{}).get('sha256'),'current_sha256':ca.get(path,{}).get('sha256')})
 pairs.append({'old_evidence_id':old['evidence_id'],'current_evidence_id':'CURRENT-F1','old_apk_sha256':old['sha256'],'current_apk_sha256':cur['sha256'],'entry_results':rows,'counts':{s:sum(x['status']==s for x in rows) for s in ['BYTE-IDENTICAL','ADDED','REMOVED','MODIFIED']}})
(OUT/'results/apk/current_vs_old_apk_pairs.json').write_text(json.dumps(pairs,indent=2)+'\n')
# Source comparison canonical relative namespaces.
oldsrc=source_map(OLD,'old'); cursrc=source_map(CURRENT,'current')
source_rows=cmp_files(oldsrc,cursrc)
(OUT/'results/source/source_comparison.json').write_text(json.dumps(source_rows,indent=2)+'\n')
# Build comparison using manifests/config files by basename and selected paths.
def pick(repo,kind):
 candidates=[]
 if kind=='old': base=repo/'recovered-source/grimchess-mobile'
 else: base=repo
 for p in base.rglob('*'):
  if p.is_file() and '.git' not in p.parts and any(x in p.name.lower() for x in ['package.json','package-lock.json','pnpm-lock.yaml','tsconfig.json','vite.config.ts','capacitor.config.ts','build.gradle','variables.gradle','settings.gradle','gradle.properties','gradle-wrapper.properties']): candidates.append(p)
 return candidates
oldb={p.name+':'+str(p.relative_to(OLD/'recovered-source/grimchess-mobile')):p for p in pick(OLD,'old')}
curb={p.name+':'+str(p.relative_to(CURRENT)):p for p in pick(CURRENT,'current')}
build_rows=cmp_files(oldb,curb)
(OUT/'results/build/build_comparison.json').write_text(json.dumps(build_rows,indent=2)+'\n')
# Engine-specific exact comparison.
def engine_files(repo,kind):
 root=repo/'recovered-source/grimchess-mobile' if kind=='old' else repo/'src'
 candidates={}
 for p in root.rglob('*'):
  if not p.is_file() or '.git' in p.parts: continue
  s=str(p).lower()
  if any(k in s for k in ['stockfish','stockfishadapter','engine','predictionmap','paradox']): candidates[p.relative_to(root).as_posix()]=p
 return candidates
eold=engine_files(OLD,'old'); ecur=engine_files(CURRENT,'current')
engine_rows=cmp_files(eold,ecur)
(OUT/'results/engine/engine_comparison.json').write_text(json.dumps(engine_rows,indent=2)+'\n')
# Deterministic summary.
def counts(rows): return {s:sum(x['status']==s for x in rows) for s in ['BYTE-IDENTICAL','ADDED','REMOVED','MODIFIED']}
summary={'pinned_inputs':{'current_commit':'f7cd9a89e8c4f6366c7ed7a778ae3acf0b89e180','old_commit':'6fbdc09a604ecb373981e1f4b2787b56a86076b4'},'apk_count_current':1,'apk_count_old':4,'source_counts':counts(source_rows),'build_counts':counts(build_rows),'engine_counts':counts(engine_rows),'apk_pair_entry_counts':{x['old_evidence_id']:x['counts'] for x in pairs},'current_earlier_identity':{'sha256':'61a00ce9c1fb54a995cd6351eb15add9a46a5b60774a2264c4fa4b9e3f301fc3','relationship':'This hash is byte-identical to OLD-APK-002; the pinned Current repository does not contain it as a Current artifact.'}}
(OUT/'results/SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
# Copy script itself into repo after it is generated by caller.
print(json.dumps(summary,indent=2))
