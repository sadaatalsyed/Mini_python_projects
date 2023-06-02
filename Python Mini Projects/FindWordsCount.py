from collections import Counter
words=[]
with open('test.txt','r') as f:
    for line in f:
        words.extend(line.split())

counts=Counter(words)
top5=counts.most_common(5)
# print(words)
print(counts)
print(top5)