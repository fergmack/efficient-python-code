import numpy as np 
import pandas as pd

baseball = [['ARI', 'NL', 2012, 734, 688, 81, 162, 0, 0.5], ['ATL', 'NL', 2012, 700, 600, 94, 162, 1, 0.58], ['BAL', 'AL', 2012, 712, 705, 93, 162, 1, 0.57], ['BOS', 'AL', 2012, 734, 806, 69, 162, 0, 0.43], ['CHC', 'NL', 2012, 613, 759, 61, 162, 0, 0.38], ['CHW', 'AL', 2012, 748, 676, 85, 162, 0, 0.52], ['CIN', 'NL', 2012, 669, 588, 97, 162, 1, 0.6], ['CLE', 'AL', 2012, 667, 845, 68, 162, 0, 0.42], ['COL', 'NL', 2012, 758, 890, 64, 162, 0, 0.4], ['DET', 'AL', 2012, 726, 670, 88, 162, 1, 0.54], ['HOU', 'NL', 2012, 583, 794, 55, 162, 0, 0.34], ['KCR', 'AL', 2012, 676, 746, 72, 162, 0, 0.44], ['LAA', 'AL', 2012, 767, 699, 89, 162, 0, 0.55], ['LAD', 'NL', 2012, 637, 597, 86, 162, 0, 0.53], ['MIA', 'NL', 2012, 609, 724, 69, 162, 0, 0.43], ['MIL', 'NL', 2012, 776, 733, 83, 162, 0, 0.51], ['MIN', 'AL', 2012, 701, 832, 66, 162, 0, 0.41], ['NYM', 'NL', 2012, 650, 709, 74, 162, 0, 0.46], ['NYY', 'AL', 2012, 804, 668, 95, 162, 1, 0.59], ['OAK', 'AL', 2012, 713, 614, 94, 162, 1, 0.58]]

baseball_df = pd.DataFrame(baseball)
baseball_df.columns = ['Team', 'League', 'Year', 'RS', 'RA', 'W', 'G', 'Playoffs', 'WP']

# You'd like to attempt to predict a team's win percentage for a given season by using the team's total runs scored in a season ('RS') and total runs allowed in a season ('RA') with the following function

def predict_win_perc(RS, RA):
  prediction = RS ** 2 / (RS ** 2 + RA ** 2)
  return np.round(prediction, 2)

  # 1 .iterrows()
  # Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.
  win_perc_preds_loop = [] 

  # Use a loop and .itertuples() to collect each row's predicted win percentage
  for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA 
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

    print(baseball_df.columns)

# 2 .apply()
# Apply predict_win_perc to each row of the DataFrame

win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), 
axis = 1)

print(win_perc_preds_apply)

# 3. using NumPy arrays
# Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc(). Save these predictions as win_perc_preds_np

win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)

baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

# Which is the fastest?
# Using NumPy arrays was the fastest approach, followed by the .itertuples() approach, and the .apply() approach was slowest.
