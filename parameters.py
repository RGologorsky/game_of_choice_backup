import numpy as np
import pathlib 

from class_one_games import S_2_Game, S_4_Game
from class_two_games import S_8_Game, S_12_Game, S_16_Game

from helper_functions import get_params

# Parameters
num_runs = 5
num_timesteps = 10*(10**5)

b1_list = np.arange(1.0, 3.2, 0.14)
#b1_list = np.arange(1.42, 2.54, 0.14)

c = 1.0
b2 = 1.2

# HIGH PRESSURE
params_dict = {
	"N": 100,
	"eps": 0.01,
	"beta": 10.0,
	"strategy_type": "pure", # or "stochastic"
	"c": c,
	"b2": b2,
}

# params_dict = {
# 	"N": 100,
# 	"eps": 0.001,
# 	"beta": 2.0,
# 	"strategy_type": "pure", # or "stochastic"
# 	"c": c,
# 	"b2": b2,
# }


c1 = c
c2 = c

N, eps, beta = get_params(["N", "eps", "beta"], params_dict)

transitions = [
	#"NA",
	"EqualSay_G2_Default",
    #"EqualSay_G1_Default",
    #"Unilateral_Dictator",
    #"Random_Dictator",
    #"Random",
]

# b1_list = np.arange(1.0, 3.2, 0.14)

games   = [
			#S_2_Game(c=1.0, b1=1.2), 
			#S_4_Game(c=1.0, b1=2.0), 
			#S_8_Game(c=1.0, b1=2.0, b2=1.2,  game_transition_dynamics=transitions[0]), 
			S_12_Game(c=1.0, b1=2.0, b2=1.2, game_transition_dynamics=transitions[0]), 
			S_16_Game(c=1.0, b1=2.0, b2=1.2, game_transition_dynamics=transitions[0]), 
		]


save_params_dict = {

	# test params
	"num_runs": num_runs,
	"num_timesteps": num_timesteps,

	# evolutionary params
	"N": 100,
	"eps": 0.001,
	"beta": 2.0,
	"strategy_type": "pure", # or "stochastic"
	
	# game params
	"c": c,
	"b2": b2,
	"c1": c,
	"c2": c,
}

# define folder name
def get_b1_effect_folder(timestamp, directory="data/b1_effect"):
	folder = "{:s}/eps_{:.2e}_beta_{:.2e}_T_{:.2e}_c_{:.2f}_b2_{:.2f}/{:s}/"\
		.format(directory, eps, beta, num_timesteps, c, b2, timestamp)

	# create directory
	pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 
	return folder