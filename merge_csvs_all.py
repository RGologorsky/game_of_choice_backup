import pandas as pd
import glob

def merge_csvs_all(data_folder, output_filename):

	csv_files = glob.glob(data_folder + "*.csv")
	print("Merging " + str(len(csv_files)) + " files.")

	df_list = []
	for filename in sorted(csv_files):
		df = pd.read_csv(filename)
		df_list.append(df)
	
	full_df = pd.concat(df_list)
	full_df.to_csv(output_filename, index=False)

# Parameters

# N, eps, beta = 100, 0.001, 2.0
# num_timesteps = 5*(10**5)

N, eps, beta = 100, 0.01, 10.0
num_timesteps = 10*(10**5)
c,  b2 = 1.0, 1.2

date = "date_2019_03_12_20_11_14"

params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(eps, beta, num_timesteps, c, b2, date)


params_str =  "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}".format(eps, beta, num_timesteps, c, b2)

#data_folder = "data/b1_effect/figs/S_04/u/"
data_folder = "data/b1_effect/" + params
output_folder = data_folder
output_filename = output_folder + "all_" + params_str + "_" + date + ".csv"

merge_csvs_all(data_folder, output_filename)


# data_folder = "data/b1_effect/{:s}".format(params)
# output_folder = data_folder
# output_filename = "all_{:s}_date_{:s}".format(params, date)

# output_params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}_{:s}"\
# 		.format(eps, beta, num_timesteps, c, b2, date)

# output_filename = output_folder + output_params + ".csv"


#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)


# data_folder   = "data/b1_effect/" + params

# param_to_change = "N"
# data_folder = "data/param_effect_fixed/" + "N/date_2019_03_06_14_15_32/"
# print(data_folder)