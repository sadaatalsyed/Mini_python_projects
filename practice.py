words=input().split()
print(words)
by_letters={}
for word in words:
    letter=word[0]
    if letter not in by_letters:
        by_letters[letter]=[word]
    else:
        by_letters[letter].append(word)
print(by_letters)

for key in by_letters:
    print(len(by_letters[key]))
