# .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs, you can either split this tuple and use the index and row-values separately (as you did with for i,row in pit_df.iterrows()), or you can keep the result of .iterrows() in the tuple form (as you did with for row_tuple in pit_df.iterrows()).

# If using i,row, you can access things from the row using square brackets (i.e., row['Team']). If using row_tuple, you would have to specify which element of the tuple you'd like to access before grabbing the team name (i.e., row_tuple[1]['Team']).

# With either approach, using .iterrows() will still be substantially faster than using .iloc as you saw in the video.

import pandas as pd 

# sort out dataframe!!
pit_df = pd.DataFrame( [['PIT', 'NL', 2012, 651, 674, 79, 162, 0], ['PIT', 'NL', 2011, 610, 712, 72, 162, 0], ['PIT', 'NL', 2010, 587, 866, 57, 162, 0], ['PIT', 'NL', 2009, 636, 768, 62, 161, 0], ['PIT', 'NL', 2008, 735, 884, 67, 162, 0]]
)

for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))


# # Print the row and type of each row
# for row_tuple in pit_df.iterrows():
#     print('Pt1 -------------')
#     print(row_tuple[1]['Team'])
#     # print(type(row_tuple))

# print('===============')

# for i, row in pit_df.iterrows():
#     print('Pt 2 -------------')
#     print(row['Team'])
#     # print(type(row_tuple))


# --------------------------- PT 2 --------------------------
# Calculated run differential
def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

giants = [['SFG', 'NL', 2012, 718, 649, 94, 162, 1], ['SFG', 'NL', 2011, 570, 578, 86, 162, 0], ['SFG', 'NL', 2010, 697, 583, 92, 162, 1], ['SFG', 'NL', 2009, 657, 611, 88, 162, 0], ['SFG', 'NL', 2008, 640, 759, 72, 162, 0]]


giants_df = pd.DataFrame(giants)
giants_df.columns = ['Team' ,'League' , 'Year' ,  'RS'  , 'RA'  , 'W'   , 'G'  , 'Playoffs']

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    # ____.____(____)
    run_diffs.append(run_diff)
