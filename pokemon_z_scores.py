import numpy as np

names = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron', 'Aipom', 'Alakazam', 'Alomomola', 'Altaria']

hps = np.array([ 80.0 , 60.0 ,131.0 , 62.0 , 71.0 ,109.0 , 45.0 , 53.0 , 73.0,  60.0])

print(hps)

# A list of 10 Pokémon has been loaded into your session as names. Each Pokémon's corresponding Health Points is stored in a NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each Pokémon's HP is from the mean of all HPs.

# The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based on their z-scores:

poke_zscores = []
for name, hp in zip(names, hps):
  hp_avg = hps.mean() 
  hp_std = hps.std()

  z_score = (hp - hp_avg) / hp_std
  poke_zscores.append((name, hp, z_score))

print(poke_zscores)

highest_hp_pokemon = []

for name, hp, zscore in poke_zscores:
  if zscore > 2:
    highest_hp_pokemon.append((name, hp, zscore))

print(highest_hp_pokemon)
