# Loops vs Pandas broadcasting
# The broadcasting comes from numpy, simply put it describes the rules of the output that will result when you do operations within the n-dimensional arrays (could be panels, dataframes, series) or scalar values.
import pandas as pd 
import numpy as np

baseball = [['ARI', 'NL', 2012, 734, 688, 81, 162, 0], ['ATL', 'NL', 2012, 700, 600, 94, 162, 1], ['BAL', 'AL', 2012, 712, 705, 93, 162, 1], ['BOS', 'AL', 2012, 734, 806, 69, 162, 0], ['CHC', 'NL', 2012, 613, 759, 61, 162, 0], ['CHW', 'AL', 2012, 748, 676, 85, 162, 0], ['CIN', 'NL', 2012, 669, 588, 97, 162, 1], ['CLE', 'AL', 2012, 667, 845, 68, 162, 0], ['COL', 'NL', 2012, 758, 890, 64, 162, 0], ['DET', 'AL', 2012, 726, 670, 88, 162, 1]]

baseball_df = pd.DataFrame(baseball)
baseball_df.columns = ['Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', 'Playoffs']

print(baseball_df)

def calc_win_perc(wins, games_played):
  win_perc = wins / games_played
  return np.round(win_perc, 2)

win_percs_list = []

# loop over each row and apply the function

print("="*15)
for i in range( len(baseball_df)):
  row = baseball_df.iloc[i]
  # print(row)
  wins = row['W']
  games_played = row['G']

  win_perc = calc_win_perc(wins, games_played)

  win_percs_list.append(win_perc)

# add new win percentage column to the 
baseball_df['WP'] = win_percs_list
print(baseball_df)

# function to draw seperating lines
def sep():
  print("="*25)

# =================================================
# Let's update this analysis to use arrays instead of the .iloc method.

# Use the right method to collect the underlying 'W' and 'G' arrays of baseball_df and pass them directly into the calc_win_perc() function. Store the result as a variable called win_percs_np.

# Use one line instead of a looop. It's much faster
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

sep()
print(win_percs_np)
sep()
# get rid of column WP to add it back
baseball_df.drop(['WP'], axis = 1, inplace=True)
print(baseball_df)

baseball_df['WP'] = win_percs_np
sep()
print(baseball_df)
