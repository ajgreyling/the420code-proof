import numpy as np, csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G_STRUCT = 6.7206038e-11   # AP28 structural (provisioned)
G_REAL   = 6.6719165e-11   # The Snap v0.2 realised
G_CODATA, U_CODATA = 6.67430e-11, 0.00015e-11

# id, year, value(e-11), u(e-11), method class, codata_input
D = [
 ("NIST-82",1982,6.67248,0.00043,"ToS",1),
 ("TR&D-96",1996,6.67290,0.00050,"ToS",1),
 ("LANL-97",1997,6.67398,0.00070,"ToS",1),
 ("UWash-00",2000,6.674255,0.000092,"AAF",1),
 ("BIPM-01",2001,6.67559,0.00027,"Servo/Cav strip",1),
 ("UWup-02",2002,6.67422,0.00098,"F-P cavity",1),
 ("MSL-03",2003,6.67387,0.00027,"Servo torsion",1),
 ("HUST-05",2005,6.67222,0.00087,"ToS",1),
 ("UZur-06",2006,6.67425,0.00012,"Beam balance",1),
 ("HUST-09",2009,6.67349,0.00018,"ToS",1),
 ("LENS-14",2014,6.67191,0.00099,"Atom interf.",1),
 ("BIPM-14",2014,6.67554,0.00016,"Servo/Cav strip",1),
 ("UCI-14",2014,6.67435,0.00013,"ToS (cryo)",1),
 ("HUST-T-18",2018,6.674184,0.000078,"ToS",1),
 ("HUST-A-18",2018,6.674484,0.000077,"AAF",1),
 ("JILA-18",2019,6.67260,0.00025,"Pendulum F-P",1),
 ("NIST-26",2026,6.67387,0.00038,"Servo/Cav strip",0),
]
ids=[d[0] for d in D]; yr=np.array([d[1] for d in D]); v=np.array([d[2] for d in D])*1e-11
u=np.array([d[3] for d in D])*1e-11; cls=[d[4] for d in D]; cd=np.array([d[5] for d in D],bool)

with open("G_dataset.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["id","year","G_e-11","u_e-11","ur_ppm","method_class","codata2022_input"])
    for d in D: w.writerow([d[0],d[1],f"{d[2]:.6f}",f"{d[3]:.6f}",f"{d[3]/d[2]*1e6:.0f}",d[4],d[5]])

ppm=lambda x: x*1e6
# --- field stats (16 CODATA inputs) ---
V,U=v[cd],u[cd]
w16=1/U**2; wm=np.sum(w16*V)/np.sum(w16)
chi2=np.sum(((V-wm)/U)**2); birge=np.sqrt(chi2/(len(V)-1))
rng=(V.max()-V.min())/wm
print(f"16 CODATA inputs: weighted mean {wm:.6e}, chi2 {chi2:.1f}, Birge {birge:.2f}")
print(f"full range {ppm(rng):.0f} ppm; unweighted SD {ppm(np.std(V,ddof=1)/wm):.0f} ppm")

# --- Candidate 1 implied leakages (all 17) ---
eta=1 - v/G_STRUCT
print(f"\nCandidate 1 implied leakage: mean {ppm(eta.mean()):.0f} ppm, SD {ppm(eta.std(ddof=1)):.0f} ppm, CV {eta.std(ddof=1)/eta.mean()*100:.1f}%")
classes=sorted(set(cls))
gm=eta.mean(); ssb=ssw=0
for c in classes:
    m=np.array([x==c for x in cls]); e=eta[m]
    ssb+=len(e)*(e.mean()-gm)**2; ssw+=np.sum((e-e.mean())**2)
    print(f"  {c:16s} n={len(e)} mean {ppm(e.mean()):.0f} ppm  (span {ppm(e.max()-e.min()):.0f})")
from scipy import stats as _st
k=len(classes); N=len(eta)
F=(ssb/(k-1))/(ssw/(N-k)); pval=_st.f.sf(F,k-1,N-k)
print(f"one-way ANOVA: F({k-1},{N-k}) = {F:.3f}, p = {pval:.3f}  ({sum(1 for c in classes if sum(x==c for x in cls)==1)} singleton classes)")
print(f"between-class share of variance: {ssb/(ssb+ssw)*100:.0f}%  (within: {ssw/(ssb+ssw)*100:.0f}%)")
print(f"between-class span of class means: {ppm(max(eta[np.array([x==c for x in cls])].mean() for c in classes)-min(eta[np.array([x==c for x in cls])].mean() for c in classes)):.0f} ppm vs common component {ppm(gm):.0f} ppm")

# --- three calibrations ---
g=lambda n: v[ids.index(n)]
print(f"\nCalibrations of demonstrated apparatus systematics:")
print(f"  same lab, two methods  (HUST-18 T vs A): {ppm(abs(g('HUST-A-18')-g('HUST-T-18'))/wm):.0f} ppm")
print(f"  same apparatus, 13 yr  (BIPM-01 vs -14): {ppm(abs(g('BIPM-14')-g('BIPM-01'))/wm):.1f} ppm")
bipm=(g('BIPM-01')/2+g('BIPM-14')/2)
print(f"  same apparatus, new site/team (BIPM->NIST-26): {ppm((bipm-g('NIST-26'))/wm):.0f} ppm")
print(f"  field full range (16): {ppm(rng):.0f} ppm; excluding BIPM pair: {ppm((V[~np.isin(np.array(ids)[cd],['BIPM-01','BIPM-14'])].max()-V.min())/wm):.0f} ppm")

# --- Candidate 3 residuals ---
r=v/G_REAL-1
nb=[i for i,n in enumerate(ids) if n not in ("BIPM-01","BIPM-14") and cd[i]]
Vn=v[nb]; Un=u[nb]; wn=1/Un**2; wmn=(wn*Vn).sum()/wn.sum()
print(f"weighted mean without BIPM pair: {wmn:.6e}; realised below full mean {ppm((wm-G_REAL)/wm):.0f} ppm, below no-BIPM mean {ppm((wmn-G_REAL)/wmn):.0f} ppm (relief {ppm((wm-G_REAL)/wm-(wmn-G_REAL)/wmn):.0f} ppm)")
i26=ids.index("NIST-26")
print(f"NIST-26: {ppm((v[i26]-G_REAL)/v[i26]):+.0f} ppm above realised = {(v[i26]-G_REAL)/u[i26]:+.2f} sigma_own; {(v[i26]-G_CODATA)/u[i26]:+.2f} sigma vs CODATA")
print(f"\nCandidate 3 residuals above realised value: mean {ppm(r.mean()):.0f} ppm, SD {ppm(r.std(ddof=1)):.0f} ppm")
print(f"  NIST-26: {ppm(r[ids.index('NIST-26')]):.0f} ppm above realised; {ppm((g('NIST-26')-G_CODATA)/G_CODATA):.0f} ppm vs CODATA")
print(f"strain ratio: required common leakage {ppm(gm):.0f} ppm / demonstrated apparatus ceiling 250 ppm = {gm*1e6/250:.0f}x")

# --- figure ---
cmap={"ToS":"#1f77b4","AAF":"#2ca02c","Servo/Cav strip":"#d62728","F-P cavity":"#9467bd",
      "Servo torsion":"#8c564b","Beam balance":"#e377c2","Atom interf.":"#ff7f0e",
      "ToS (cryo)":"#17becf","Pendulum F-P":"#bcbd22"}
fig,ax=plt.subplots(figsize=(9.2,5.4),dpi=160)
ax.axhspan((G_CODATA-U_CODATA)/1e-11,(G_CODATA+U_CODATA)/1e-11,color="#c8b98a",alpha=.5,lw=0)
ax.axhline(G_CODATA/1e-11,color="#8a7440",lw=1,ls="-")
ax.axhline(G_REAL/1e-11,color="#2f6f4f",lw=1.6,ls="--")
seen=set()
for i,d in enumerate(D):
    c=cmap[d[4]]; lab=d[4] if d[4] not in seen else None; seen.add(d[4])
    mk="s" if d[0]=="NIST-26" else "o"
    ax.errorbar(d[1],d[2],yerr=d[3],fmt=mk,ms=6 if mk=="s" else 5,color=c,capsize=2,lw=1.2,label=lab,zorder=3)
ax.annotate("NIST-26\n(BIPM apparatus replicated:\n−250 ppm)",xy=(2026,6.67387),xytext=(2017.2,6.6706),
            fontsize=8,ha="left",arrowprops=dict(arrowstyle="->",lw=.9))
ax.annotate("AP28 structural value 6.72060  (+0.69%, off scale ↑)",xy=(2027.5,6.6769),ha="right",fontsize=9,color="#7a1f1f")
ax.annotate("realised value 6.67192  (The Snap v0.2)",xy=(1983,6.67145),fontsize=9,color="#2f6f4f")
ax.annotate("CODATA 2022  6.67430(15)",xy=(1983,6.67435),fontsize=8,color="#8a7440")
ax.set_xlim(1980,2028); ax.set_ylim(6.6700,6.6772)
ax.set_xlabel("year of publication"); ax.set_ylabel("G  (10⁻¹¹ m³ kg⁻¹ s⁻²)")
ax.set_title("Seventeen determinations of G against the structural, realised, and recommended values")
ax.legend(fontsize=7,loc="upper left",ncol=2,framealpha=.9)
ax.grid(alpha=.25,lw=.5)
plt.tight_layout(); plt.savefig("G_landscape.png")
print("\nfigure written")
