"""Reproduce both exploratory sweeps using the repository Python model."""
import sys, itertools, json, csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root))
from simulation import simulate
out=Path(sys.argv[1] if len(sys.argv)>1 else "reproduced")
out.mkdir(parents=True,exist_ok=True)
p1={"default":[65,35,1.3,0.35,0.6],"runaway":[80,15,2.5,0.1,0.8],"bounded":[40,120,0.8,0.9,0.6],"innovation":[80,110,2,0.8,0.05],"zero activity":[0,0,0,1,0],"no mismatch":[80,15,2.5,0.1,0],"no feedback":[80,15,0,0.1,0.8]}
p2={"No correction":[12,0,1.3,0,0.6],"Partial review":[12,6,1.3,0.35,0.6],"Equal throughput":[12,12,1.3,0.7,0.6],"Review surplus":[12,24,1.3,0.9,0.6],"Strong independent correction":[12,36,1.3,1,0.6],"Low mismatch / partial review":[12,6,1.3,0.35,0],"No explicit gain / partial review":[12,6,0,0.35,0.6]}
for name,presets in [("TLON-SIM-001",p1),("EFMW-TLON-002",p2)]:
    (out/(name+"-presets.json")).write_text(json.dumps({n:{"parameters":p,"trajectory":simulate(*p,steps=400)} for n,p in presets.items()}))
keys=["q","a","d","u","risk"]
with (out/"sweep-001.csv").open("w",newline="") as f:
    w=csv.writer(f);w.writerow(["g","v","h","c","m"]+[k+str(t) for t in (40,400) for k in keys])
    for p in itertools.product([0,5,20,40,65,80,100],[0,15,35,65,100,120,150],[0,.5,1,1.3,2,2.5,3],[0,.1,.35,.8,1],[0,.05,.3,.6,1]):
        r=simulate(*p,steps=400)
        w.writerow([*p,*[r[t][k] for t in (40,400) for k in keys]])
sweep=[]
for v,h,c,m in itertools.product([0,6,12,18,24,30,36],[0,.5,1.3,2,3],[0,.35,.7,1],[0,.3,.6,1]):
    sweep.append(dict(v=v,h=h,c=c,m=m,**simulate(12,v,h,c,m,steps=400)[400]))
(out/"sweep-002.json").write_text(json.dumps(sweep))
