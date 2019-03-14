# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import pathlib

#strat = "S_08"

data_folder = "data/b1_effect/figs/all/" 
data_file   = "all_eps_1.00e-03_beta_2.00e+00_T_5.00e+05_c_1.00_b2_1.20_date_2019_03_08_17_11_57" \
                + ".csv"

img_folder = data_folder 
img_filename = "tri_transitions"
img_format = "pdf"


def plot_hue_transition():

    data = pd.read_csv(data_folder + data_file)

    # create img directory
    pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

    sns.set(style="darkgrid", palette="pastel")

    fig, axes = plt.subplots(nrows=1, ncols=3, sharey=True, sharex=True)

    transitions = [
        "EqualSay_G1_Default", \
        "EqualSay_G2_Default", \
        "Unilateral_Dictator", \
        "Random_Dictator", \
        "Random" \
    ]

    # labels = [
    #   "EqualSay_G1", \
    #   "EqualSay_G2", \
    #   "Unilateral_Dictator", \
    #   "Random_Dictator", \
    #   "Random" \
    # ]

    labels = [
        "Eq_G1", \
        "Eq_G2", \
        "UniD", \
        "RandD", \
        "Random" \
    ]

    # seaborn graph

    data_s4 = data.loc[data["strat_space"] == "S_04"]

    for i, transition in enumerate(transitions):
        data = data.replace(transition, labels[i])


    for i, strat in enumerate(["S_08", "S_12", "S_16"]):

        data_s = data.loc[data["strat_space"] == strat]

        ax = axes[i]
        ax.set_title("{:s}".format(strat))

        if i == 0:
            sns.lineplot(x="b1", y="C rate", ax=ax, data=data_s4, label = "Baseline_IPD") #, hue_order = hue_order)
        else:
            sns.lineplot(x="b1", y="C rate", ax=ax, data=data_s4)


        # data_t = data.loc[data["transition"] == transition]
        for j, transition in enumerate(labels):
            data_t = data_s.loc[data["transition"] == transition]
            
            if i == 0:
                sns.lineplot(x="b1", y="C rate", ax=ax, data=data_t, label = transition) #, hue_order = hue_order)
            else:
                sns.lineplot(x="b1", y="C rate", ax=ax, data=data_t)

        ax.set_xlabel(r"$b_1$" + " value")
        ax.set_ylabel("Cooperation rate")

    # set legend title/lables
    #leg = axes[2].get_legend()

    leg_title ="Voting Rule"

    #leg.set_title(leg_title)
    #plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", title = "Voting Rule")

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, bbox_to_anchor=(0,1.0,1.0,0.15), loc="lower left", \
                title = leg_title, mode="expand", ncol=6)
    #plt.title("Cooperation Rate Reproducability: " + r"$b_1 = $" + "{:.2f}".format(spec_b1), y = 1.18)
    fig.suptitle("Effect of Transition Structure on Cooperation Rates", y = 1.18)

    axes[0].legend_.remove()

    #print(leg.texts)

    #for t, l in zip(leg.texts, leg_labels): t.set_text(l)

    plt.savefig(img_folder + img_filename + ".{:s}".format(img_format), format=img_format, bbox_inches="tight")

plot_hue_transition()
# sns.lineplot(x="b1", y="C rate", ax=ax2, data=data_t) #, hue_order = hue_order)
            # sns.lineplot(x="b1", y="CoopSPE rate", ax=ax3, data=data_t, label = labels[i]) #, hue_order = hue_order)


    #g = sns.lineplot(x="b1", y="C rate", ax=ax1, hue="strat", data=data) #, hue_order = hue_order)
    #handles, labels = ax1.get_legend_handles_labels()

    #changed g to ax1
    # fig.suptitle("Effect of Transition Structrure on Cooperation Rates")
    # ax1.set_title("{:s}".format(strat))
    # ax1.set_xlabel("b1_value")
    # ax1.set_ylabel("Cooperation rate")


#leg.set_title(leg_title)
#for t, l in zip(leg.texts, leg_labels): t.set_text(l)

# d_transitions = [
#       "EqualSay_G2_Default", \
#       "Unilateral_Dictator", \
#       "Random_Dictator", \
#       "EqualSay_G1_Default", \
#       "NA", \
#       "Random" \

#   ]

#data_t = data.loc[data["transition"] == transition]
    
        # sns.lineplot(x="b1", y="1CC rate", ax=ax1, data=data_t) #, hue_order = hue_order)
        # sns.lineplot(x="b1", y="C rate", ax=ax2, data=data_t) #, hue_order = hue_order)
        # sns.lineplot(x="b1", y="CoopSPE rate", ax=ax3, data=data_t, label = labels[i]) #, hue_order = hue_order)


# parameters
# num_runs = 5
# num_timesteps = 5*(10**5)

# params_dict = {
#   "N": 100,
#   "eps": 0.001,
#   "beta": 2.0,
#   "strategy_type": "pure", # or "stochastic"
#   "max_attempts": 10**4,
# }


# c = 1.0
# b2 = 1.2

# c1 = c
# c2 = c


# eps, beta = params_dict["eps"], params_dict["beta"]

# eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
# beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
# ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

# game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
# sep = "\n\n"
# param_str = "Strategy Space: {:s}".format(strat) + sep + \
#           "Evolution Parameters:\n " + eps + beta + ts + sep + \
#           "Game Parameters:\n"  + game_param + sep + \
#           "(APPEND LATER:) UP TO {:d} Runs".format(num_runs)


# #plt.subplots_adjust(bottom=0.20, top=0.92)

# ax2.text(0.5, 0.5, param_str, horizontalalignment='center',
#             fontsize=12, multialignment='left',
#             bbox=dict(boxstyle="round", facecolor='#D8D8D8',
#             ec="0.5", pad=0.5, alpha=1), fontweight='bold')

# ax2.axis('off')
#plt.tight_layout()
#plt.savefig(img_folder + img_filename, format=img_format)

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