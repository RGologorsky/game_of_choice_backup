import numpy as np
import pandas as pd

import pathlib
import csv

# Parameters
b1 = 1.8
N, eps, beta = 100, 0.001, 2.0
num_timesteps = 5*(10**5)
c,  b2 = 1.0, 1.2
date = "date_2019_03_04_21_42_49"

# define folder name
data_folder = "data/game_comp//b1_{:.2f}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(b1, eps, beta, num_timesteps, c, b2, date)


img_format = "pdf"
img_folder = data_folder
img_filename  = "game_comp"

# check it exists
#pathlib.Path(img_folder).mkdir(parents=True, exist_ok=True) 

num_runs = 5
filenames = ["S_04_NA_game_b1_1.20", "S_04_NA_game_b1_1.80", \
			"S_08_EqualSay_G2_Default_game_b1_1.80", "S_12_EqualSay_G2_Default_game_b1_1.80", \
			"S_16_EqualSay_G2_Default_game_b1_1.80"]

labels = [
			"S_04_b1_1.20", \
			"S_04_b1_1.80", \
			"S_08_EqualSay_G2_Default_b1_1.80", \
			"S_12_EqualSay_G2_Default_b1_1.80", \
			"S_16_EqualSay_G2_Default_b1_1.80"
		]

timepoints = list(range(num_timesteps)) * num_runs

for i in range(5):
	game_dfs = []
	stem_fname = data_folder + filenames[i]

	all_runs = np.zeros(len(timepoints))

	for j in range(5):
		fname = stem_fname + "_run_{:d}.csv".format(j)

		start_index = j*num_timesteps
		end_index = (j+1)*num_timesteps

		print(start_index, end_index)

		with open(fname, 'r') as f:
		  reader = csv.reader(f)
		  all_runs[start_index:end_index] = list(reader)[0]

	print(len(all_runs))
	print(len(timepoints))

	game_df = pd.DataFrame(np.column_stack([timepoints, all_runs]), 
                               columns=['Timestep', 'Cooperation rate'])

	game_df["game"] = labels[i]
	game_df.to_csv(stem_fname + ".csv", index=False)

	game_dfs.append(game_df)

full_df = pd.concat(game_dfs)
full_df.to_csv(data_folder + "all.csv", index=False)