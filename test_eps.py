import numpy as np
import time

from class_two_games import S_8_Game, S_12_Game, S_16_Game
from find_spe_functions import *

import pathlib # create directory as needed

from helper_functions import save_dict, read_dict

from pprint import pprint

# Parameters
c=1.00
b2=1.20

transitions = [
	#"EqualSay_G1_Default",
	#"Random_Dictator",
	#"Player1_Dictator",
	"EqualSay_G2_Default",
    #"EqualSay_G1_Default",
    #"Player1_Dictator",
    #"Random",
]

transition = transitions[0]

# 1.0 - 10**(-2) = 0.99 -> exponent = num decimal places
delta = 1.0 - 10**(-5)
S08_game  = S_8_Game(c=c,   b1=1.8, b2=b2, game_transition_dynamics=transition)
S12_game = S_12_Game(c=c,  b1=1.8, b2=b2, game_transition_dynamics=transition)
S16_game = S_16_Game(c=c,  b1=1.8, b2=b2, game_transition_dynamics=transition)

games = [S08_game, S12_game, S16_game]

s_08_strat = (1,0,0,1, 1,0,0,0)
s_12_strat = (1,0,0,0, 0,0,0,1, 1,0,0,0)

v_s08 = S08_game.get_stationary_dist(s_08_strat, s_08_strat, S08_game.f)
v_s12 = S12_game.get_stationary_dist(s_12_strat, s_12_strat, S12_game.f)

print("v_s08: ", v_s08[0])
print("v_s12: ", v_s12[0])

s_08_strat_allc2 = (1,1,1,1, 0,0,0,0)
s_08_strat_allc1 = (1,1,1,1, 1,1,1,1)

s_08_strat_alld = (0,0,0,0, 0,0,0,0)

v_s08_allcd = S08_game.get_stationary_dist(s_08_strat_allc1, s_08_strat_alld, S08_game.f)
v_s08_alldc = S08_game.get_stationary_dist(s_08_strat_alld, s_08_strat_allc1, S08_game.f)


print("v_s08 ALLC vs ALLD: ", tuple(round(x,2) for x in v_s08_allcd))
print("v_s08 ALLD vs ALLC: ", tuple(round(x,2) for x in v_s08_alldc))

def epss_it(eps, lst):
	return tuple(eps + (1-2*eps) * x for x in lst)

epss = 0.001
s_08_strat = epss_it(epss, (1,0,0,1, 1,0,0,0))
s_12_strat = epss_it(epss, (1,0,0,0, 0,0,0,1, 1,0,0,0))

v_s08 = S08_game.get_stationary_dist(s_08_strat, s_08_strat, S08_game.f)
v_s12 = S12_game.get_stationary_dist(s_12_strat, s_12_strat, S12_game.f)

print("eps v_s08: ", tuple(round(x,2) for x in v_s08))
print("eps v_s12: ", tuple(round(x,2) for x in v_s12))

s_08_strat_allc2 = epss_it(epss, (1,1,1,1, 0,0,0,0))
s_08_strat_allc1 = epss_it(epss, (1,1,1,1, 1,1,1,1))

s_08_strat_alld = epss_it(epss, (0,0,0,0, 0,0,0,0))

v_s08_allcd = S08_game.get_stationary_dist(s_08_strat_allc1, s_08_strat_alld, S08_game.f)
v_s08_alldc = S08_game.get_stationary_dist(s_08_strat_alld, s_08_strat_allc1, S08_game.f)


print("eps v_s08 allcd: ", tuple(round(x,9) for x in v_s08_allcd))
print("eps v_s08 alldc: ", tuple(round(x,9) for x in v_s08_alldc))

folder_timestamp = time.strftime("date_%Y_%m_%d_%H_%M_%S")
params_str = "c_{:.2f}_b2_{:.2f}_delta_{:.10f}".format(c, b2, delta)

#b1_list = np.arange(1.0, 3.2, 0.14)

game = S_12_Game(c=1.0, b1=1.8, b2=1.2, game_transition_dynamics="EqualSay_G1_Default")
s1 = epss_it(epss, (1,1,1,1, 0,0,0,0))
s2 = epss_it(epss, (0,0,0,0, 0,0,0,0))

v = S08_game.get_stationary_dist(s1, s2, game.f)
v_act   = [v[0],v[1], v[6], v[7]]
v_predict = [
	(1-epss)*epss     * (2*epss - epss**2), \
	(1-epss)*(1-epss) * (2*epss - epss**2), \
	(epss)  *epss     * (1 - epss)**2, \
	(epss)  *(1-epss) * (1 - epss)**2
]

print("eps v   [1CC, 1CD ...2 DC, 2DD]: ", v_act)
print("predict [1CC, 1CD ...2 DC, 2DD]: ", v_predict)
print("diff [1CC, 1CD ...2 DC, 2DD]: ", [v_act[i] - v_predict[i] for i in range(4)])

epss = 0.05
s = epss_it(epss, (1,0,0,0, 1,1,1,1, 1,1,0,0))
v = game.get_stationary_dist(s, s, game.f)
pi_s = game.get_payoffs(s, s)[0]
print(pi_s)

s2 = (epss_it(epss, (1,0,0,0,1,1,1,1,1,1,1,0)))
pi_s2 = game.get_payoffs(s2, s2)[0]
print(pi_s2)

print(pi_s2 - pi_s)
#print("eps v suspicious s: ", tuple(round(x,4) for x in v))
#pprint(game.generate_transition_matrix(s, s, game.f))


def run(b1_list):
	parent_folder = "data/full_coop_spe/transitions/{:s}/{:s}/{:s}/"\
						.format(transition, params_str, folder_timestamp)

	print("Parent folder: ", parent_folder)

	# print parameters
	print("Parameters: delta = {:.10f}, c={:.2f}, b2 = {:.2f}".format(delta, c, b2))

	for game in games:

		print("game = {:s}".format(str(game)))
	
		folder = parent_folder + "{:s}/".format(str(game))

		# create directory
		pathlib.Path(folder).mkdir(parents=True, exist_ok=True) 

		for b1 in b1_list:

			print("b1 = {:.2f}".format(b1))

			# reset b1 value
			game.reset_b1(b1)

			# time it
			start_time = time.time()
			full_coop_spe_lst = find_all_coop_spe(game, delta, transition)
			elapsed_time = time.time() - start_time

			print("Elapsed Time: {:.2f} min. {:s}, find all coop SPE ({:d})."
					.format(elapsed_time/60.0, str(game), len(full_coop_spe_lst)))

			# filename = folder + "b1_{:.2f}_num_strat_{:d}.csv".format(b1, len(full_coop_spe_lst))
			filename = folder + "b1_{:.2f}.csv".format(b1)

			with open(filename,'ab') as f:
			    np.savetxt(f, full_coop_spe_lst, fmt="%d", delimiter=",")

#run(b1_list)