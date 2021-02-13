# A for loop has been created to filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name:

poke_names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
poke_gens = [4, 1, 3, 5, 1]

gen1_gen2_name_lengths_loop = []

for name, gen in zip(poke_names, poke_gens):
  if gen < 3:
    name_length = len(name)
    poke_tuple = (name, name_length)
    gen1_gen2_name_lengths_loop.append(poke_tuple)

# print(gen1_gen2_name_lengths_loop)

# Eliminate the above for loop using list comprehension and the map() function:
# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name, gen in zip(poke_names, poke_gens) if gen < 3]
# print(gen1_gen2_pokemon)

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)
# print(name_lengths_map)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths =  [*zip(gen1_gen2_pokemon, name_lengths_map)]

# Use one line 
one_line = [(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]
# print(one_line)

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# You want to gather each Pokémon's total stat value (i.e., the sum of each row in stats) and each Pokémon's average stat value (i.e., the mean of each row in stats) so that you find the strongest Pokémon.

import numpy as np 
# The below for loop was written to collect these values:
names = np.array(['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl'])
stats = np.array([[ 90 ,  92 ,  75 ,  92  , 85 ,  60],
 [ 25 ,  20 ,  15 , 105 ,  55 ,  90],
 [ 65 , 130 ,  60 ,  75 ,  60 ,  75],
 [ 80 ,  70 ,  40 , 100 ,  60 , 145],
 [ 80 , 105 ,  65 ,  60 ,  75 , 130]]
)

poke_list = []

for pokemon, row in zip(names, stats):
  total_stats = np.sum(row)
  avg_stats = np.mean(row)
  poke_list.append((pokemon, total_stats, avg_stats))
   
# recreate the above loop using numpy 
# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]


print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokemon: \n{}'.format(top_3))
