
# A for loop has been created to filter the Pokémon that belong to generation one or two, and collect the number of letters in each Pokémon's name:

poke_names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl']
poke_gens = [4, 1, 3, 5, 1]

gen1_gen2_name_lengths_loop = []

for name, gen in zip(poke_names, poke_gens):
  if gen < 3:
    name_length = len(name)
    poke_tuple = (name, name_length)
    gen1_gen2_name_lengths_loop.append(poke_tuple)

print(gen1_gen2_name_lengths_loop)

# Eliminate the above for loop using list comprehension and the map() function:
# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name, gen in zip(poke_names, poke_gens) if gen < 3]
print(gen1_gen2_pokemon)

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)
print(name_lengths_map)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths =  [*zip(gen1_gen2_pokemon, name_lenghts_map)]

# Use one line 
[(name, len(name)) for name,gen in zip(poke_names, poke_gens) if gen < 3]
