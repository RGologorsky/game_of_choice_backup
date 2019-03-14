# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib

data_folder = "data/b1_effect/figs/all/" 
#data_file   = "all_eps_1.00e-03_beta_2.00e+00_T_5.00e+05_c_1.00_b2_1.20_date_2019_03_08_17_11_57"

# HIGH PRESSURE

# EQ G2
#data_file = "all_eps_1.00e-02_beta_1.00e+01_T_1.00e+06_c_1.00_b2_1.20_date_2019_03_04_08_03_01"

# EQ G1
data_file    = "all_eps_1.00e-02_beta_1.00e+01_T_1.00e+06_c_1.00_b2_1.20_date_2019_03_12_20_11_14"

data_file += ".csv"

img_folder = data_folder 
img_filename = "top_tri_coop" + "_high_pressure"
img_format = "pdf"

def plot_tri_coop(transition):

    data = pd.read_csv(data_folder + data_file)

    # create img directory
    pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

    sns.set(style="darkgrid", palette="pastel")

    fig, axes = plt.subplots(nrows=1, ncols=3, sharey=True, sharex=True)

    coops = [
        "C rate", \
        "1CC rate", \
        "CoopSPE rate", \
    ]

    # labels = [
    #    "C rate", \
    #     "1CC rate", \
    #     "CoopSPE rate", \
    # ]

    # seaborn graph

    data_t = data.loc[data["transition"] == transition]

    for i, strat in enumerate(["S_08", "S_12", "S_16"]): #enumerate(["S_08", "S_12", "S_16"]):

        data_s = data_t.loc[data_t["strat_space"] == strat]

        ax = axes[i]

        # data_t = data.loc[data["transition"] == transition]
        for j, coop in enumerate(coops):
            if i == 0:
                sns.lineplot(x="b1", y=coop, ax=ax, data=data_s, label = coop) #, hue_order = hue_order)
            else:
                sns.lineplot(x="b1", y=coop, ax=ax, data=data_s)

        ax.set_title("{:s}".format(strat))
        ax.set_xlabel(r"$b_1$" + " value")
        ax.set_ylabel("Cooperation rate")

    # set legend title/lables
    #leg = axes[0].get_legend()

    leg_title = "" # Cooperation Measure 

    #leg.set_title(leg_title)
    #lt.legend(bbox_to_anchor=(1.04,1), loc="upper left", title = "Voting Rule")
    #axes[0].legend(bbox_to_anchor=(1,0), loc="lower right")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, bbox_to_anchor=(0.10,0.82,0.76,0.05), loc="lower left", \
               title = leg_title, mode="expand", ncol=3)
    #plt.title("Cooperation Rate Reproducability: " + r"$b_1 = $" + "{:.2f}".format(spec_b1), y = 1.18)
    fig.suptitle("Cooperation under " + transition)

    axes[0].legend_.remove()

    #print(leg.texts)

    #for t, l in zip(leg.texts, leg_labels): t.set_text(l)

    plt.savefig(img_folder + img_filename + "_{:s}.{:s}".format(transition, img_format), format=img_format, bbox_inches="tight")


transition = "EqualSay_G1_Default" # "EqualSay_G1_Default"
plot_tri_coop(transition)

# date = "date_2019_03_04_08_03_01" #date_2019_02_24_19_50_14"
# strat_space = "S_12"
# transition = "EqualSay_G2_Default"

# data_filename =  "all.csv"

# Parameters
# N, eps, beta = 100, 0.001, 2.0
# num_timesteps = 5*(10**5)
# c,  b2 = 1.0, 1.2


# params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
# 		.format(eps, beta, num_timesteps, c, b2, date)

# data_folder   = "data/b1_effect/" + params

#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)

# print(data_folder)


# img_format = "pdf"
# img_folder = data_folder
# img_filename  = "{:s}_{:s}.{:s}".format(strat_space, transition, img_format)

# # check it exists
# pathlib.Path(data_folder).mkdir(parents=True, exist_ok=True) 


# # set plot style
# sns.set(style="darkgrid", palette="pastel")

# # Load the dataset
# data = pd.read_csv(data_folder + data_filename)

# data_strat_space = data.loc[data["strat_space"] == strat_space]

# fig, ax1 = plt.subplots(nrows=1, ncols=1)


#ax1.set_xscale('log', basex=10)
#ax1.set(xscale="log", basex=2)


# lineplots
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

# fig.subplots_adjust(hspace=1, wspace=1)

# plt.savefig(img_folder + img_filename, format=img_format)

#plt.show()
