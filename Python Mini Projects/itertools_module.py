import itertools
names=['Alan','Adam','Will','Albert']
first_letter=lambda x:x[0]
grouping=itertools.groupby(names,first_letter)
combo=itertools.combinations(names,2)
permutations=itertools.permutations(names,2)
products=itertools.product(*names,repeat=1)
for key,names in grouping:
    print(list(names),":",key)
for i,j in combo:
    tup=(i,j)
    print(tup,end="\t")
for i,j in permutations:
    tup=(i,j)
    print(tup,end="\t")
for i in products:
    print(i)

# print(tup)
# print(permutations)

