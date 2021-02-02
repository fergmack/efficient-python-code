# Convert funciton 
import numpy as np 
# %load_ext line_profiler 


heros = ['Batman', 'Superman', 'Spiderman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0, 85.0])

# convert cm to inches, and kg to pounds
def convert_units(heros, heights, weights):
  new_hts = [ht * 0.39370 for ht in heights]
  new_wts = [wt * 2.20462 for wt in weights]

  hero_data = {}

  for i, hero in enumerate(heros):
    hero_data[hero] = (new_hts[i], new_wts[i])

  return hero_data


print(convert_units(heros, hts, wts))
