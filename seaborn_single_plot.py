# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib

#from matplot_latexify import latexify

from math import sqrt
#latexify(fig_width=None, fig_height=None, columns=3)
fig_width = 8.0
golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
fig_height = fig_width*golden_mean # height in inches

fig_width = 12.0
fig_height = 6.5
figsize = (fig_width, fig_height)

date = "date_2019_03_06_14_15_32"
param_to_change = "N"

data_folder   = "data/param_effect_fixed/{:s}/{:s}/".format(param_to_change, date)
data_filename =  "all_{:s}.csv".format(param_to_change)

img_format = "pdf"
img_folder = data_folder
img_filename  = "{:s}.{:s}".format(param_to_change, img_format)

# check it exists
pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# set plot style
sns.set(style="darkgrid", palette="pastel")

# Load the dataset
beta_data = "data/param_effect_fixed/" + "beta/date_2019_03_06_12_12_00/all_beta.csv"
N_data    = "data/param_effect_fixed/" + "N/date_2019_03_06_14_15_32/all_N.csv"
eps_data  = "data/param_effect_fixed/" + "eps/date_2019_03_06_13_25_40/all_eps.csv"

#data = pd.read_csv(data_folder + data_filename)

beta_data = pd.read_csv(beta_data)
N_data    = pd.read_csv(N_data)
eps_data  = pd.read_csv(eps_data)

fig, ((ax1, ax2, ax3)) = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=figsize)

super_title = "Effect of Evolutionary Parameters on Cooperation Rates\n"
fig.suptitle(super_title, y = 0.99) #, fontsize=14, fontweight='bold')


#ax1.set(xscale="log", basex=2)
ax1.set_xscale('log', basex=10)
ax2.set_xscale('log', basex=2)
ax3.set_xscale('log', basex=10)

# seaborn graph
g1 = sns.lineplot(x="beta", y="1CC rate", ax=ax1, data=beta_data)#, label="1CC rate")
g1 = sns.lineplot(x="beta", y="C rate",   ax=ax1, data=beta_data)#, label="C rate")
g1 = sns.lineplot(x="beta", y="SPE rate", ax=ax1, data=beta_data)#, label = "SPE rate")

g2 = sns.lineplot(x="N", y="1CC rate", ax=ax2, data=N_data)#, label="1CC rate")
g2 = sns.lineplot(x="N", y="C rate",   ax=ax2, data=N_data)#, label="C rate")
g2 = sns.lineplot(x="N", y="SPE rate", ax=ax2, data=N_data)#, label = "SPE rate")

g3 = sns.lineplot(x="eps", y="1CC rate", ax=ax3, data=eps_data, label="1CC rate")
g3 = sns.lineplot(x="eps", y="C rate",   ax=ax3, data=eps_data, label="C rate")
g3 = sns.lineplot(x="eps", y="SPE rate", ax=ax3, data=eps_data, label = "SPE rate")

#g1.set_title("Effect of Selection on Cooperation")
g1.set_xlabel("Selection Pressure, {:s}".format(r'$\beta$'))

#g2.set_title("Effect of Population Size on Cooperation")
g2.set_xlabel("Population Size, {:s}".format(r'$N$'))

#g3.set_title("Effect of Noise  on Cooperation")
g3.set_xlabel("Noise Level, {:s}".format(r'$\epsilon$'))

g1.set_ylabel("Cooperation Rate")
#g2.set_ylabel("Cooperation Rate")
#g3.set_ylabel("Cooperation Rate")

# set legend location
ax3.legend(bbox_to_anchor=(1.04,1), loc="upper left")
#plt.subplots_adjust(right=0.70)
plt.tight_layout()
plt.savefig(img_folder + img_filename, format=img_format)

#plt.show()

# Game: S_02, Run: 0
# Elapsed Time: 14.08 min
# Game: S_02, Run: 1
# Elapsed Time: 21.87 min
# Game: S_02, Run: 2
# Elapsed Time: 25.33 min
# Game: S_02, Run: 3
# Elapsed Time: 20.50 min
# Game: S_02, Run: 4
# Elapsed Time: 19.79 min