import re
states=['Alabama','Georgia!','Georgia','georgia##?',
        'Florida','south carolina','West virginia?']
def list_clean_strings(strs):
    result=[]
    for value in strs:
        value=value.strip()
        cleaned=re.sub('[!#?]','',value)
        state=cleaned.title()
        result.append(state)
    return result
def set_clean_strings(strs):
    result=set()
    for value in strs:
        value=value.strip()
        cleaned=re.sub('[!#?]','',value)
        state=cleaned.title()
        result|={state}
        print(result)
    return result
print(set_clean_strings(states)) # this will return unique value as we expect in a set
print(list_clean_strings(states)) # this will return repetitive values

strings=['foo','cards','bard','aaaa','adab']
strings.sort(key=lambda x:len(set(list(x))))
print(strings)
unique_lettered=[len(set(list(x))) for x in strings]
print(unique_lettered)


