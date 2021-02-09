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
