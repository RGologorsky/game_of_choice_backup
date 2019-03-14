strat = "S_12"
test = False

from merge_csvs_all import merge_csvs_all
from seaborn_plot_hue_transition import plot_hue_transition

merge_csvs_all(strat, test)
plot_hue_transition(strat,test)

