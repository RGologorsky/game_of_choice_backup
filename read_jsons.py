import numpy as np
from helper_functions import read_dict
from get_spe_list import *

from pprint import pprint


# Parameters
num_runs = 5

# N, eps, beta = 100, 0.001, 2.0
# num_timesteps = 5*(10**5)

N, eps, beta = 100, 0.01, 10.0
num_timesteps = 10*(10**5)
c,  b2 = 1.0, 1.2

b1_val = 3.10
b1_list =[b1_val]

# Folder
date = "date_2019_03_08_17_11_57" #
#date = "date_2019_03_12_20_11_14"

params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(eps, beta, num_timesteps, c, b2, date)

transition_str = "EqualSay_G2_Default" #"Unilateral_Dictator" #"EqualSay_G2_Default"
strat_space = "S_12"

game_str = strat_space + "_" + transition_str

# undo epsilon
def undo_eps(arr):
	return tuple(int(round(1/(1-2*eps)*(x-eps),2)) for x in arr)



most_common_20_d = {}

for run_id in range(num_runs):
	# read data
	filename = "data/b1_effect/" + params + game_str + "_run_{:d}_b1_{:.2f}".format(run_id, b1_val)
	
	d     = read_dict(filename)

	if transition_str in ["EqualSay_G1_Default", "EqualSay_G2_Default"]:
		spe_d = get_pure_spe_dict(transition_str, game_str, b1_list)
	else:
		spe_d = {b1: [] for b1 in b1_list}

	# get top 20 strat across all runs
	most_common = sorted(d, key=d.get, reverse=True) #[:50]
	vals = [d[key] for key in most_common]

	for i, strat in enumerate(most_common):
		
		val = vals[i]

		if strat in most_common_20_d: most_common_20_d[strat] += val
		else:       most_common_20_d[strat] = val

# get top 10 strat across all runs
most_common = sorted(most_common_20_d, key=most_common_20_d.get, reverse=True)[:30]	
most_common_clean = [undo_eps(eval(s)) for s in most_common]
vals = [most_common_20_d[key]/num_runs for key in most_common]

pers = ["avg {:.2f}%".format(val/num_timesteps * 100) for val in vals]
cspes = [strat in spe_d[b1_val] for strat in most_common_clean]

#pprint(most_common)
#pprint(vals)
print("b1 = {:.2f}, {:s}".format(b1_val, transition_str))
# pprint(most_common_clean)
# pprint(pers)
# pprint(cspes)

pprint(list(enumerate(most_common_clean)))
pprint(list(enumerate(pers)))
pprint(list(enumerate(cspes)))
#data_filename =  "{:s}_{:s}.csv".format(strat_space, transition)

# params = "eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
# 		.format(eps, beta, num_timesteps, c, b2, date)