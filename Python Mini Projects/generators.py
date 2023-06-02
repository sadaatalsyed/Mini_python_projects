import random
some_dict={1:'a',2:'b',3:'c',4:'d',5:'e'}

dict_iterator=iter(some_dict)
dict_iterator2=iter(some_dict)
list1=list[dict_iterator]
print(dict_iterator)
print(sum(dict_iterator))
print(list(dict_iterator2))

def squares(n=10):
    print(f'Generating squares from 1 to {n**2}')
    for i in range(1,n+1):
        yield i**2
gen=squares()
for x in gen:
    print(x,end="\t\t")



print(sum(x for x in range(20)))
print([random.randint(0, i) for i in range(1,10)])
print(dict((i**3,random.randint(0, i)) for i in range(1,10)))
