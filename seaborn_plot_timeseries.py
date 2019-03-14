# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import pathlib

from math import log10 # to format tick labels

# Parameters
b1 = 1.8
N, eps, beta = 100, 0.001, 2.0
num_timesteps = 5*(10**5)
c,  b2 = 1.0, 1.2
date = "date_2019_03_05_18_44_08"

num_runs = 50

# define folder name
data_folder = "data/game_comp//b1_{:.2f}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(b1, eps, beta, num_timesteps, c, b2, date)


filenames = [
	"S_04_NA_b1_1.20", \
	"S_04_NA_b1_1.80", \
	"S_08_EqualSay_G2_Default_b1_1.80", \
	"S_12_EqualSay_G2_Default_b1_1.80", \
	"S_16_EqualSay_G2_Default_b1_1.80"
]

labels = [
	r"S_04, $b_1$ = 1.20", \
	r"S_04, $b_1$ = 1.80", \
	r"S_08, Eq_G2", \
	r"S_12, Eq_G2", \
	r"S_16, Eq_G2"
]

data_format = "csv"

img_format = "pdf"
img_folder = data_folder
img_filename  = "game_comp2"

# read in data
dfs = []

for fname in filenames:
	data_file = data_folder + fname +"_avg_over_{:d}.{:s}".format(num_runs, data_format)
	# Load the dataset
	n_rows = num_timesteps #* num_runs
	skip = np.arange(n_rows)
	skip = np.delete(skip, np.arange(0, n_rows, 500))
	df = pd.read_csv(data_file, skiprows = skip)

	dfs.append(df)

	# print("Data has been read")

	# data_top = data.head() 
	# data_bottom = data.tail()

	# print("head")
	# print(data_top)
	# print("tail")
	# print(data_bottom)



# plot the data

# set plot style
sns.set(style="darkgrid", palette="pastel")

do_plot = True

if do_plot:
	#data = data[::100]
	fig, ax1 = plt.subplots(nrows=1, ncols=1)

	# seaborn graph
	for i, data in enumerate(dfs):
		g = sns.lineplot(x="Timestep", y="Cooperation rate", ax=ax1, data=data, label=labels[i])

	#handles, labels = ax1.get_legend_handles_labels()

	g.set_title("Game of Choice " + r"$vs.$" + " IPD game")
	g.set_xlabel("Timestep")
	g.set_ylabel("Cooperation Rate")

	# set legend location
	ax1.legend(bbox_to_anchor=(0,1), loc="upper left")
	#plt.subplots_adjust(right=0.70)

	# change x axis labels
	def format_tick(x):
		if int(x) == 0: return "0"

		log_pow = int(log10(abs(x)))
		base_int = int(x/(10**log_pow))

		return "{:d}e{:d}".format(base_int, log_pow)

	#print(ax1.get_xticks().tolist())
	ax1.set_xticklabels([format_tick(x) for x in ax1.get_xticks().tolist()])
	
	# new_labels =[r""]
	# leg =ax.get_legend()

	# for t, l in zip(leg.texts, new_labels): t.set_text(l)




	#ax1.set_xscale('log', basex=10)
	#ax1.set(xscale="log", basex=2)

	# df.plot(style='.-', markevery=5)

	# # lineplots
	# cc = sns.lineplot(x="b1", y="1CC rate", data=data_strat_space, ax = ax1, label = "1CC rate")
	# c  = sns.lineplot(x="b1", y="C rate", data=data_strat_space, ax = ax1, label = "C rate")
	# spe_rate  = sns.lineplot(x="b1", y="SPE rate", data=data_strat_space, ax = ax1, label = "SPE rate")

	# title = "{:s} {:s} Cooperation Rates".format(strat_space, transition)
	# ax1_xlabel = "b1 value"
	# ax1_ylabel = ""

	# # seaborn graph
	# ax1.set_title(title, fontsize=14, fontweight='bold')
	# ax1.set_xlabel(ax1_xlabel)
	# ax1.set_ylabel(ax1_ylabel)

	fig.subplots_adjust(hspace=1, wspace=1)

	plt.savefig(img_folder + img_filename + ".{:s}".format(img_format), format=img_format)

	#plt.show()
