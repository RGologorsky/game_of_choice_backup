# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# g = sns.catplot(x="time", y="pulse", hue="kind", data=exercise)

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
import pathlib # to create directory if needed


# b1 rate
spec_b1 = 1.84

# Load dataset
data_folder = "data/b1_effect/figs/all/" 
data_file   = "all_eps_1.00e-03_beta_2.00e+00_T_5.00e+05_c_1.00_b2_1.20_date_2019_03_08_17_11_57" \
                + ".csv"

img_folder = data_folder 
img_format = "pdf"
img_filename = "b1_{:.2f}_time_variance3.{:s}".format(spec_b1, img_format)

data = pd.read_csv(data_folder + data_file)
data =  data.loc[round(data["b1"],2) == spec_b1]
data = data.loc[data["strat_space"] != "S_04"]

# plot coop data
fig, ax = plt.subplots(nrows=1, ncols=1)

# make seaborn graph
sns.set(style="ticks")
sns.despine()

color_palette_without_s4 = sns.color_palette("pastel")[1:]

# "data/num_timesteps/runs_5_eps_1.00e-03_beta_2.00e+00/date_2019_02_03/data_num_timesteps.csv"

# g = sns.boxplot(x="strat_space", y="C rate", 
#           hue="transition", data=data, ax = ax, showmeans=True)

transitions = [
        "EqualSay_G1_Default", \
        "EqualSay_G2_Default", \
        "Unilateral_Dictator", \
        "Random_Dictator", \
        "Random" \
    ]

leg_labels = [
        "Eq_G1", \
        "Eq_G2", \
        "UniD", \
        "RandD", \
        "Random" \
    ]

# leg_labels = [
#         "EqualSay_G1", \
#         "EqualSay_G2", \
#         "Unilateral_Dictator", \
#         "Random_Dictator", \
#         "Random" \
#     ]

#data['transition'] = data['transition'].map({'female': 1, 'male': 0})

for i, transition in enumerate(transitions):
    data = data.replace(transition, leg_labels[i])

g = sns.barplot(x="strat_space", y="C rate", data=data, ax = ax,
            hue="transition", hue_order = leg_labels, \
            palette = color_palette_without_s4)

ax.set_xlabel("Strategy Space")
ax.set_ylabel("Cooperation Rate")

means = data.groupby(["transition", "strat_space"])['C rate'].mean().values
stds  = data.groupby(["transition", "strat_space"])['C rate'].std().values

# HECKY HACKY 
map_y_to_mean = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:12,
    7:13,
    8:14,
    9:6,
    10:7,
    11:8,
    12:9,
    13:10,
    14:11
}

def add_value_labels(ax, spacing=5):

    # For each bar: Place a label
    for i, rect in enumerate(ax.patches):
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        mean = means[map_y_to_mean[i]]
        std  = stds[map_y_to_mean[i]]

        # HECKY HACKY 
        # if i in (9,10,11):
        #     mean = means[i+3]
        #     std  = stds[i+3]

        # if i in (12,13,14):
        #     mean = means[i-3]
        #     std  = stds[i-3]

        print("i = ", i, ", y = ", y_value, ", mean = ", mean, ", diff: ", y_value - mean)


        # Number of points between bar and label. Change to your liking.
        space = spacing + std * 200
        
        # Vertical alignment for positive values

        # Use Y value as label and format number with one decimal place
        #label = "{:.1f}".format(y_value)

        label = "{:.2f}".format(mean) + r"$\pm$" + "{:.2f}".format(std)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va='top',                   # Vertically align label differently for
            color='gray',               # positive and negative values 
            rotation=0,                
            fontsize=8)                            


# Call the function above. All the magic happens there.
add_value_labels(ax, spacing = 10)

# set legend title/lables
leg = g.get_legend()

leg_title ="Voting Rule"


#leg.set_title(leg_title)
#plt.legend(bbox_to_anchor=(0,1.00), loc="upper left", title = leg_title)
plt.legend(bbox_to_anchor=(0,1,1.0,0.15), loc="lower left", title = leg_title, mode="expand", ncol=5)
plt.title("Fixed Slice: " + r"$b_1 = $" + "{:.2f}".format(spec_b1), y = 1.18)
# for i, label in enumerate(leg_labels):
#     print(leg.legendHandles[i])
#     leg.legendHandles[i].set_text(label)

# print(leg.texts)
# print(leg.get_texts())
# #print(g.legend.texts)

# for t, l in zip(leg.get_texts(), leg_labels): 
#     t.set_text(l)
#     t.set_fontsize(fontsize=10)

# print(leg.texts)

# def annotateBars(row, ax=ax): 
#   for p in ax.patches:
#        ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
#            ha='center', va='center', fontsize=8, color='gray', rotation=90, xytext=(0, 20),
#            textcoords='offset points')


#data.apply(annotateBars, ax=ax, axis=1)

plt.tight_layout()
plt.savefig(img_folder + img_filename, format = img_format)

#plt.show()

# new_labels = [r"$2*10^5$", r"$3*10^5$", r"$10^6$"];
# leg =ax.get_legend()

# for t, l in zip(leg.texts, new_labels): t.set_text(l)

# handles, labels = g.get_legend_handles_labels()
# print(handles)
# print(labels)
#sns.despine(offset=10)


# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']
# g.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1, labels=my_labels, title="No. Timesteps")
# g._legend(loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)

# g._legend.set_title('No. Timesteps')
# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']


#ax.legend(loc='lower right') #, labels = my_labels)

# Put a legend to the right side
#ax1.legend(handles=[leg], loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)



# for t, l in zip(g._legend.texts, my_labels):
#   print("t is ", t, "l is ", l) 
#   t.set_text(l)

# print("t", g._legend.texts)


# m1 = data.groupby([strat, ts])['1CC rate'].median().values
# mL1 = [str(np.round(s, 2)) for s in m1]

# means = data.groupby([strat, ts])['1CC rate'].mean().values
# stds = data.groupby([strat, ts])['1CC rate'].std().values

#str_means = ["{:.2f}".format(s) for s in means]
#str_stds  = ["{:.2f}".format(s) for s in stds]

#str_labels = ["{:.2f}".format(means[i]) + r"$\pm$" + "{:.2f}".format(stds[i]) for i in range(len(means))]
# for patch in ax.patches:
#   print("width ", patch.get_width())

# width = ax.patches[0].get_width()
# print("patch width: ", width)

# ind = 0
# nudge = 1.0/6.0
# up_nudge = 0
# side_nudge = 5.0/10 * nudge

# for tick in range(len(g.get_xticklabels())):
#   #g.text(tick+  -3*nudge + side_nudge, m1[ind+0]+ up_nudge, mL1[ind+0], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
#   #g.text(tick+  -2*nudge + side_nudge, m1[ind+1]+ up_nudge, mL1[ind+1], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
#   #g.text(tick+  -1*nudge + side_nudge, m1[ind+2]+ up_nudge, mL1[ind+2], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
#   #g.text(tick+   1*nudge - side_nudge, m1[ind+3]+ up_nudge, mL1[ind+3], horizontalalignment='center', color='black', weight='semibold', fontsize="8")
#   # g.text(tick+   2*nudge - side_nudge, m1[ind+4]+ up_nudge, mL1[ind+4],  horizontalalignment='center', color='black', weight='semibold', fontsize="8")
#   # g.text(tick+   3*nudge - side_nudge, m1[ind+5]+ up_nudge, mL1[ind+5],  horizontalalignment='center', color='black', weight='semibold', fontsize="8")
#   if tick != 0:
#       g.text(tick+2*nudge + side_nudge, means[ind+4]+up_nudge, str_labels[ind+4],  horizontalalignment='center', color='black', weight='bold', fontsize="10")
#       g.text(tick+3*nudge + side_nudge, means[ind+5]+up_nudge, str_labels[ind+5],  horizontalalignment='center', color='black', weight='bold', fontsize="10")
    

#   ind += 6

# # fix first tick
# tick = 0
# ind = 0
# g.text(tick+2.8*nudge, means[ind+4]-0.10*nudge, str_labels[ind+4],  \
#   horizontalalignment='center', color='black', weight='bold', fontsize="10")

# g.text(tick+3*nudge + side_nudge, means[ind+5]+up_nudge, str_labels[ind+5],  \
#   horizontalalignment='center', color='black', weight='bold', fontsize="10")
#g.legend([r"$10^3$", r"$10^4$", r"$10^5$", r"$2*10^5$", r"$3*10^5$", r"$10^6$"]);

# g = sns.stripplot(x=strat, y="1CC rate", hue=ts,
#                     data=data, jitter=True,
#                     palette="Set2", dodge=True)

# medians = data.groupby([strat])['1CC rate'].median().values
# median_labels = [str(np.round(s, 2)) for s in medians]


# pos = range(len(medians))
# for tick,label in zip(pos,ax.get_xticklabels()):
#   print("label ", label)
#   print("medians", median_labels[tick])

#   ax.text(pos[tick], medians[tick] + 0.5, median_labels[tick], 
#       horizontalalignment='center', size='x-small', color='b', weight='semibold')


#new_labels = [r"$10^3$", r"$10^4$", r"$10^5$", r"$2*10^5$", r"$3*10^5$", r"$10^6$"]



# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']
# g.legend(handles=handles, loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1, labels=my_labels, title="No. Timesteps")
# g._legend(loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)

# g._legend.set_title('No. Timesteps')
# my_labels = ['1.00e+03', '1.00e+04', '1.00e+05', '2.00e+05', '3.00e+05', '1.00e+06']


#ax.legend(loc='lower right') #, labels = my_labels)

# Put a legend to the right side
#ax1.legend(handles=[leg], loc='upper right', bbox_to_anchor=(1.25, 0.5), ncol=1)



# for t, l in zip(g._legend.texts, my_labels):
#   print("t is ", t, "l is ", l) 
#   t.set_text(l)

# print("t", g._legend.texts)


# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import time

# from class_one_games import S_2_Game, S_4_Game
# from class_two_games import S_8_Game, S_12_Game, S_16_Game
# from simulation_evolution_avgs import *

# import pandas as pd
# import pathlib # to create directory if needed

# # Parameters
# num_runs = 5
# num_timesteps = 3*(10**5)

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

# folder = "data/b1_effect/long_time_two_game/eps_1.00e-03_beta_2.00e+00_T_3.00e+05_c_1.00_b2_1.20/date_2019_02_05/"
# filename = "S_08_df.csv"

# img_folder = "imgs/b1_effect/long_time/"
# img_filename = "S_08.png"
    
# # create img directory
# pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

# def plot_one_b1_effect_data():

#   # seaborn data
#   sns.set(style="darkgrid", palette="pastel")
#   data = pd.read_csv(folder + filename)

#   # parameters
#   eps, beta = get_params(["eps", "beta"], params_dict)

#   eps = r"$\epsilon$"  + " = {:2.2e}\n ".format(eps)
#   beta = r"$\beta$"    + " = {:2.2e}\n ".format(beta)
#   ts = r"$T$"             + " = {:2.2e}".format(num_timesteps)

#   game_param = "b2 = {:.2f}\nc1 = c2 = {:.2f}".format(b2, c1)
#   sep = "\n\n"
#   param_str = "Evolution Parameters:\n " + eps + beta + ts + sep + \
#               "Game Parameters:\n"  + game_param + sep + \
#               "{:d} Runs".format(num_runs)

    
#   # plot CC data
#   fig, ((ax1, ax2, ax3, ax4)) = plt.subplots(nrows=1, ncols=4, figsize = (24,6))
#                                                   # sharex='col', sharey='row',
                                                     

#   ax4.text(0.5, 0.5, param_str, horizontalalignment='center',
#             fontsize=12, multialignment='left',
#             bbox=dict(boxstyle="round", facecolor='#D8D8D8',
#             ec="0.5", pad=0.5, alpha=1), fontweight='bold')

#   ax4.axis('off')


#   super_title = "Effect of b1 on the Evolution of Cooperation"

#   fig.suptitle(super_title, fontsize=14, fontweight='bold')

#   # axes labels
#   ax_xlabel = "b1 value"
    
#   ax1_ylabel = "Game 1 Rate"
#   ax2_ylabel = "1CC Rate"
#   ax3_ylabel = "2CC Rate"

#   # lineplots
#   game1_g = sns.lineplot(x="b1", y="Game 1 rate", hue="strat", data=data, ax = ax1)
#   cc1_g = sns.lineplot(x="b1", y="1CC rate", hue="strat", data=data, ax = ax2)
#   cc2_g = sns.lineplot(x="b1", y="2CC rate", hue="strat", data=data, ax = ax3)
    
#   # set labels
#   cc1_g.set_xlabel(ax_xlabel)
#   cc2_g.set_xlabel(ax_xlabel)
#   game1_g.set_xlabel(ax_xlabel)


#   fig.subplots_adjust(hspace=1, wspace=1)
#   #plt.tight_layout()


#   fig.savefig(img_folder + img_filename, dpi=300)

#   plt.show()

# plot_one_b1_effect_data()
