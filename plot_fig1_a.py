import numpy as np
import matplotlib
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
from matplotlib import rc,rcParams

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
b = np.random.uniform(0,2,nsim)
rp = np.random.uniform(0,1,nsim)
for i in range(nsim):
    if b[i] < 1 + rp[i]:
        idx.append(i)

plt.plot(b,rp,'.',markersize=5,alpha=0.1,color='black')
plt.plot(b[idx],rp[idx],'.',markersize=5,color='black')
b = np.linspace(1.,2.,10)
p = b-1.
plt.plot(b,p,'--',color='cornflowerblue',linewidth=1.5)
plt.xlabel(r'$b = (a/R_*)\cos i$')
plt.ylabel(r'$p = R_p/R_*$')
plt.text(1.55,0.35,r'$b > 1 + p$',fontsize=20)

# Plot quadrilateral:
plt.plot(0.,0.,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
plt.text(0.-0.025,0.-0.015,'A',fontsize=15)
plt.plot(1.0,0.,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
plt.text(1.0-0.025,0.-0.015,'D',fontsize=15)
plt.plot(0.,1.0,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
plt.text(0.-0.025,1.0-0.015,'B',fontsize=15)
plt.plot(2.0,1.0,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
plt.text(2.0-0.025,1.0-0.015,'E',fontsize=15)
plt.plot(1.0,1.0,'o',markerfacecolor='cornflowerblue',markeredgecolor='black',markersize=25,linewidth=15)
plt.text(1.0-0.025,1.0-0.015,'C',fontsize=15)
plt.tight_layout()
plt.savefig("fig_1a.pdf", dpi=300)
plt.savefig("fig_1a.eps", dpi=300)
plt.savefig("fig_1a.png", dpi=300)
