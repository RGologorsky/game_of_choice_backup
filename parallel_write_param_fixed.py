import numpy as np
import time

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_8_Game, S_12_Game, S_16_Game

from simulation_evolution_avgs import *

import pandas as pd
import pathlib # to create directory if needed

from parameters import *
from helper_functions import save_dict, read_dict

from get_spe_list import *

import multiprocessing as mp


lst1 = [10**-4, 10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2]
lst2 = [2, 4, 8, 16, 32, 64, 128]

lst3 = [10**-1, 10**0, 10**1]
lst4 = [10**-4, 10**-3, 10**-2,10**-2, 10**-1]

lst5 = [10**-4]

param_to_change, param_list = ("N", lst2)

fixed_b1 = 1.8
hacky_spe_b1 = 1.84

transition = "EqualSay_G2_Default"
game = S_12_Game(c=c, b1=fixed_b1, b2=b2, game_transition_dynamics=transition)


# define folder name
folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
subfolder = "param_effect_fixed/{:s}/{:s}/".format(param_to_change, folder_timestamp)

data_folder = "data/{:s}".format(subfolder)
img_folder  = data_folder

def do_runs(param_value, params_dict, spe_d):

	data_filename = "{:s}{:s}_{:2f}.csv".format(data_folder, param_to_change, param_value) #get_filename(param_value)

	# pre-allocate dataframe
	num_df_rows = num_runs
	
	# create dataframe
	df = pd.DataFrame(index=np.arange(0, num_df_rows), \
					  columns=('b1', '1CC rate', '2CC rate', 'Game 1 rate', 'C rate', 'SPE rate', param_to_change))

	for run in range(num_runs):

		# announce what we are calculating
		print("{:s} = {:s}, Run: {:d}".format(param_to_change, str(param_value), run))
		
		# get data
		start_time = time.time()
		g1_cc_avg, g2_cc_avg, g1_game_avg, c_rate, spe_rate = \
			get_evolution_avgs(num_timesteps, params_dict, fixed_b1, spe_d)
		
		elapsed_time = time.time() - start_time

		print("Elapsed Time: {:.2f} min".format(elapsed_time/60.0))


		df.loc[run] = (fixed_b1, g1_cc_avg, g2_cc_avg,  g1_game_avg, c_rate, spe_rate, param_value)

	df['strat']       = str(game)
	df['strat_space'] = game.strat_str()
	df['transition']  = game.transition_str()

	params = ('N', 'eps', 'beta')
	for param in params:
		if param != param_to_change:
			df[param] = params_dict[param]

	df.to_csv(data_filename, index=False)
		

def save_params(folder, params_filename="params"):
	# create directory
	pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

	dict_to_save = {key: val for key, val in save_params_dict.items()}
	dict_to_save["game"] = str(game)
	
	params_filename = "{:s}{:s}".format(data_folder, params_filename)
	save_dict(dict_to_save, params_filename)

save_params(folder=data_folder)

print("\nData Folder: {:s}\n".format(data_folder))


# filenames within folder
def get_filename(param_value):
	return "{:s}{:s}_{:s}.csv".format(data_folder, param_to_change, str(param_value))


def parallel_write_param_fixed_data():

	params_dict["game"] = game

	# very hacky
	spe_d = get_spe_dict(transition, str(game), [hacky_spe_b1], eps)
	spe_d[fixed_b1] = spe_d[hacky_spe_b1]
	#print(spe_d)

	# # pre-allocate dataframe
	# num_df_rows = len(param_list) * num_runs
	
	# # create dataframe
	# df = pd.DataFrame(index=np.arange(0, num_df_rows), \
	# 				  columns=('b1', '1CC rate', '2CC rate', 'Game 1 rate', 'C rate', 'SPE rate', param_to_change))

	data_filename = "{:s}{:s}.csv".format(data_folder, param_to_change) #get_filename(param_value)

	
	row_index = 0

	jobs = []
	for param_value in param_list:
		params_dict[param_to_change] = param_value

		# set game, host strategy
		host_strat = (params_dict["eps"],) *  game.strat_len
		params_dict["host"] = host_strat

		p = mp.Process(target=do_runs, args=(param_value, params_dict, spe_d)) 
		p.start()
		# keep track of process, to wait for it later
		jobs.append(p)
	
	# wait until all jobs done
	for p in jobs:
		p.join()


	# add cols
	#df['CC rate'] = df['1CC rate'] + df['2CC rate']
	# df['strat']       = str(game)
	# df['strat_space'] = game.strat_str()
	# df['transition']  = game.transition_str()

	# params = ('N', 'eps', 'beta')
	# for param in params:
	# 	if param != param_to_change:
	# 		df[param] = params_dict[param]

	# df.to_csv(data_filename, index=False)


parallel_write_param_fixed_data()