import numpy as np
import pandas as pd

import pathlib
import csv

# Parameters
b1 = 1.8
N, eps, beta = 100, 0.001, 2.0
num_timesteps = 5*(10**5)
c,  b2 = 1.0, 1.2
date = "date_2019_03_05_18_44_08"

# define folder name
data_folder = "data/game_comp//b1_{:.2f}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(b1, eps, beta, num_timesteps, c, b2, date)


img_format = "pdf"
img_folder = data_folder
img_filename  = "game_comp"

# check it exists
#pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

num_runs = 50
filenames = ["S_04_NA_b1_1.20", "S_04_NA_b1_1.80", \
			"S_08_EqualSay_G2_Default_b1_1.80", "S_12_EqualSay_G2_Default_b1_1.80", \
			"S_16_EqualSay_G2_Default_b1_1.80"]

labels = [
			"S_04_b1_1.20", \
			"S_04_b1_1.80", \
			"S_08_EqualSay_G2_Default_b1_1.80", \
			"S_12_EqualSay_G2_Default_b1_1.80", \
			"S_16_EqualSay_G2_Default_b1_1.80"
		]

timepoints = list(range(num_timesteps))

for i in range(len(filenames)):
	#game_dfs = []
	stem_fname = data_folder + filenames[i]

	avgs = np.zeros(num_timesteps, dtype='float64')

	for j in range(num_runs):
		fname = stem_fname + "_run_{:d}.csv".format(j)

		with open(fname, 'r') as f:
		  reader = csv.reader(f)
		  str_list  = list(reader)[0]

		  avgs += [float(x) for x in str_list]

	game_df = pd.DataFrame(np.column_stack([timepoints, avgs/num_runs]), 
                               columns=['Timestep', 'Cooperation rate'])

	game_df["game"] = labels[i]
	game_df.to_csv(stem_fname + "_avg_over_{:d}".format(num_runs) + ".csv", index=False)

	print("Completed the average of ", labels[i])

	#game_dfs.append(game_df)

#full_df = pd.concat(game_dfs)
#full_df.to_csv(data_folder + "all.csv", index=False)