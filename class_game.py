import numpy as np

from helper_functions import numpy_isclose

class Game:
    # Identity matrix of the same size as the transition matrix. This allows calculating it once
    # only at runtime.
    eye = NotImplemented

    def strat_str(self):
        return "S_{:02d}".format(self.strat_len)

    def transition_str(self):
        return "{:s}".format(self.game_transition_dynamics)

    def __str__(self):
        return "S_{:02d}_{:s}".format(self.strat_len, self.game_transition_dynamics)

    def reset_b1(self, b1):
        self.b1 = b1
        self.set_payoffs()


    def get_stationary_dist(self, s1, s2, f=None, tolerance=1e-15):
        
        #print("in get stationary distr: f(2,3) = ", f(2,3))
        # if (s1,s2) in self.v_dict:
        #     return self.v_dict[(s1, s2)]
        
        Q = self.generate_transition_matrix(s1, s2, f)

        #Q is stochastic, guranteed to have left eigenvector v w/ eigenvalue 1
        # v satisfies Q'v = v, i.e. (Q' - I)v = 0, v = null(A) w/ A = Q' - v.

        A = Q.T - self.eye
        u, s, vh = np.linalg.svd(A)
        null_space = np.compress(s <= tolerance, vh, axis=0)

        v = null_space[0]
        v = np.absolute(v/sum(v))
        return v

        # try:
        #     v = null_space[0]
        #     v = np.absolute(v/sum(v))

        #     # Check that every value in v and in v * Q are close
        #     assert all(numpy_isclose(a, b) for a, b in zip(v, np.matmul(v, Q)))

        # except Exception as e:
        #     print("Get stationary distribution failed. s1 = {:}, s2 = {:}.".format(s1, s2)) 
        #     print("Q \n {:}".format(Q))
        #     raise(e)

        # save v
        # self.v_dict[(s1, s2)] = v
        # return v


    def get_unilateral_stationary_dist(self, s1, s2):

        (f1, f2) = self.f

        v1 = self.get_stationary_dist(s1, s2, f1)
        v2 = self.get_stationary_dist(s1, s2, f2)

        return (v1 + v2)/2.0


    # calculates average payoffs
    def get_payoffs(self, s1, s2):

        if self.game_transition_dynamics == "Unilateral_Dictator":
            v = self.get_unilateral_stationary_dist(s1, s2)
        else:
            v = self.get_stationary_dist(s1, s2, self.f)

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        return (s1_payoff, s2_payoff)

    # calculate average payoffs, probability of mutual cooperative state and game 1 state
    def get_stats(self, s1, s2):

        if self.game_transition_dynamics == "Unilateral_Dictator":
            v = self.get_unilateral_stationary_dist(s1, s2)
        else:
            v = self.get_stationary_dist(s1, s2, self.f)

        s1_payoff = np.dot(v, self.p1_payoffs)
        s2_payoff = np.dot(v, self.p2_payoffs)

        # player 1 cooperates in states 1CC and 1CD, 2CC and 2CD
        # player 2 cooperates in states 1CC and 1DC, 2CC and 2DC

        #s1_single_c_rate = v[0] + v[1] + v[4] + v[5]
        #s2_single_c_rate = v[0] + v[2] + v[4] + v[6]
        
        g1_cc_rate = v[0] #+ v[4] if self.num_states == 8 else v[0]
        g2_cc_rate = v[4] if self.num_states > 4 else 0

        g1_game_rate = sum(v[0:4]) # 1CC, 1CD, 1DC, 1DD

        # player avg coop rate - v1CC+(v1CD+v1DC)/2+v2CC+(v2CD+v2DC)/2

        two_player_c_rate = 2*v[0] + v[1] + v[2]
        if self.num_states > 4:
            two_player_c_rate += 2*v[4] + v[5] + v[6]

        player_c_rate = two_player_c_rate/2.0

        return (s1_payoff, s2_payoff, g1_cc_rate, g2_cc_rate, g1_game_rate, player_c_rate)

    # each specifc game class must implement these two methods
    def generate_transition_matrix(self, s1, s2):
        pass

    def set_payoffs(self):
        pass
