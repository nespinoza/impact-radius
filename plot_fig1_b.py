import numpy as np
import matplotlib
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
from matplotlib import rc,rcParams

pl = 0.
pu = 1.

# Set seaborn contexts:
sns.set_context("talk")
sns.set_style("ticks")

# Fonts:
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
matplotlib.rcParams.update({'font.size':12})
plt.rc('legend', **{'fontsize':7})

# Ticks to the outside:
rcParams['axes.linewidth'] = 1.2 
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

fig = plt.figure(figsize=(8, 6)) 
ax = fig.add_subplot(111)

nsim = 5000
idx = []
r1 = np.random.uniform(0,1,nsim)
r2 = np.random.uniform(0,1,nsim)
b = np.zeros(len(r1))
p = np.zeros(len(r2))
Ar = (pu-pl)/(2.+pl+pu)
for i in range(nsim):
    if r1[i]>Ar:
        b[i] = (1+pl)*(1+((r1[i]-1.)/(1.-Ar)))
        p[i] = (1.-r2[i])*pl + r2[i]*pu
    else:
        q1 = r1[i]/Ar
        q2 = r2[i]
        b[i] = (1+pl) + np.sqrt(q1)*q2*(pu-pl)
        p[i] = pu + (pl-pu)*np.sqrt(q1)*(1.-q2)
plt.plot(b,p,'.',markersize=5,color='black')
bline = np.linspace(1.+pl,1+pu,10)
pline = bline-1.
plt.plot(bline,pline,'--',color='cornflowerblue',linewidth=1.5)
plt.xlabel(r'$b = (a/R_*)\cos i$')
plt.ylabel(r'$p = R_p/R_*$')
plt.text(1.55,0.35,r'$b > 1 + p$',fontsize=20)

# Plot quadrilateral:
#plt.plot(0.,0.,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
#plt.text(0.-0.025,0.-0.015,'A',fontsize=15)
#plt.plot(1.0,0.,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
#plt.text(1.0-0.025,0.-0.015,'D',fontsize=15)
#plt.plot(0.,1.0,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
#plt.text(0.-0.025,1.0-0.015,'B',fontsize=15)
#plt.plot(2.0,1.0,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
#plt.text(2.0-0.025,1.0-0.015,'E',fontsize=15)
#plt.plot(1.0,1.0,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
#plt.text(1.0-0.025,1.0-0.015,'C',fontsize=15)
plt.tight_layout()
plt.savefig("fig_1b.pdf", dpi=300)
plt.savefig("fig_1b.eps", dpi=300)
plt.savefig("fig_1b.png", dpi=300)
