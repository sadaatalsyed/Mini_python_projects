all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
names_of_es=[]
es=[name for names in all_data for name in names if name.count('a')>=2 or name.__contains__('e')]
names_of_es.extend(es)
print(names_of_es)

list_of_tuples=[(1,2,3),(4,5,6),(7,8,9)]
flattened= [ x for tup in list_of_tuples for x in tup]
print(flattened)

seperate_tuples= [[x for x in tup] for tup in list_of_tuples]
print(seperate_tuples)





