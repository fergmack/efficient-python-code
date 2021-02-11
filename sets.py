# get unique instances of primary types
primary_types = ['grass', 'pyscic', 'dark', 'bug', 'grass']

# using loop
unique_types = []

for prim_type in primary_types:
  if prim_type not in unique_types:
    unique_types.append(prim_type)

print(unique_types)
print('--------')
# using a set, which is much faster
unique_types_set = set(primary_types)
print(unique_types_set)


# Compare function to set
names = ['Forretress', 'WormadamSandy Cloak', 'Croagunk', 'Mime Jr.', 'Camerupt']
primary_types = ['Bug', 'Bug', 'Poison', 'Psychic', 'Fire']
generations = [2, 4, 4, 4, 3]

def find_unique_items(data):
  uniques = [] 
  
  for item in data:
    if item not in uniques:
      uniques.append(item)

  return uniques

unique_names_set = set(names)

print(sorted(find_unique_items(names)) == sorted(unique_names_set))
