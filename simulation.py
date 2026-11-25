"""Deterministic exploratory model, no empirical calibration."""
import json
def simulate(g=65,v=35,h=1.3,c=.35,m=.6,steps=40):
    if not (g>=0 and v>=0 and h>=0 and 0<=c<=1 and 0<=m<=1 and isinstance(steps,int) and steps>=0):
        raise ValueError("invalid parameters")
    q,a,d=0.,.15,.1
    rows=[]
    clip=lambda x:max(0.,min(1.,x))
    for t in range(steps+1):
        u=q/(q+200)
        rows.append(dict(t=t,q=q,a=a,d=d,u=u,risk=(a*u+d+u+a)/4))
        f=v/(g+v) if g+v else 0
        q=max(0,q+g*(1+h*a)-v)
        a=clip(a+.07*h*a*(1-a)+.04*u*(1-a)-.06*c*f*a)
        d=clip(d+.06*m*a*(1-d)-.15*c*f*d)
    return rows
if __name__=="__main__":
    print(json.dumps({"status":"EXPLORATORY","rows":simulate()},indent=2))
