# A list of integers that represents each Pokémon's generation has been loaded into your session called generations. You'd like to gather the counts of each generation and determine what percentage each generation accounts for out of the total count of integers.

from collections import Counter 

generations = [4, 1, 3, 5, 1, 3, 2, 1, 5, 3]

# counts number of elements in the list
gen_counts = Counter(generations)

# inefficent loop
for gen, count in gen_counts.items():
  # print(gen, count)
  total_count = len(generations)
  gen_percent = round(count / total_count * 100, 2)
  print(
    'Generation {}: count = {:3} percentage = {}'.format(gen, count, gen_percent)


  )

# Write a better for loop that places a one-time calculation outside (above) the loop. Use the exact same syntax as the original for loop (simply copy and paste the one-time calculation above the loop).
# Faster loops 
total_count = len(generations)

for gen, count in gen_counts.items():
# print(gen, count)
  gen_percent = round(count / total_count * 100, 2)
  print(
    'Generation {}: count = {:3} percentage = {}'.format(gen, count, gen_percent)
  )
