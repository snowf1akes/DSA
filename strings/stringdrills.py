#string basics

s = 'hello world'
print(s[0]) #first char
print(s[-1]) #last char
print(s[2:5]) #slice from index 2 -> 4, so its 'llo' 
print(len(s)) #length of string
print(s.upper()) # HELLO WORLD (caps lock)
print(s.lower()) # hello world (lower case)



#reverse everything
#reverse a string
s = 'abcdef'
print(s[::-1])  #'fedcba'

#reverse first k characters
k = 3
print(s[:k][::-1] + s[k:]) #"cbadef" 
#before 3 = :3 and ::-1 means reverse and 3: means after index 3

#reverse last k characters
k = 3
print(s[:-k] + s[-k:][::-1]) # abcfed
      #everything before last 3 + last 3 reversed 

#reverse words in a sentence
sentence = 'hello world foo'
print(" ".join(sentence.split()[::-1])) # foo world hello



#split and join
#split by space
words = 'the quick brown fox'.split()
print(words) #['the', 'quick', 'brown', fox']

#split by comma
csv = 'a,b,c,d'
print(csv.split(",")) ['a', 'b', 'c', 'd']

#join list into string
print("-".join(["2026", "03", "11"])) # "2026-03-11"
print("".join(["h", "e", "l", "l", "o"])) #"hello"

#strip whitespace
messy = '   hello'
print(messy.strip())  #'hello'


#character frequency
from collections import Counter

#counter characters
s = 'aabbcc'
freq = Counter(s)
print(freq) # Counter({'c': 3, 'a': 2, 'b': 2})
print(freq.most_common(1)) # [('c', 3)]   
print(freq['a']) #2

#manual freq count
freq = {}
for c in s:
    freq[c] = freq.get(c,0) + 1
print(freq)  # {'a': 2, 'b': 2, 'c': 3}



#check palindrome
s = 'racecar'
print(s == s[::-1]) #true

s = 'hello'
print(s == s[::-1]) #false



#string to list and back
#!! strings are immutable !!
#convert to list, modify, convert back

s = 'hello'
chars = list(s)
chars[0] = "H"
result = "".join(chars)
print(result) # "hello"

#build string efficiently
parts = []
for i in range(5):
    parts.append(str(i))
result = "".join(parts)
print(result) #'01234'



#ASCII TRICKS
print(ord('a')) #97
print(ord('z')) # 122
print(chr(97)) #'a'

#get 0-25 index for a lower letter
c = 'f'
print(ord(c) - ord('a')) #5 

#check if character is a digit/letter
print('a'.isalpha()) # true
print('3'.isdigit()) # true
print('a'.isalnum()) # true



#STRING PRACTICE:

word = 'dcba'
results = [word]
for k in range(1, len(word) + 1):
    results.append(word[:k][::-1] + word[k:])
for k in range(1, len(word) +1):
    results.append(word[:-k] + word[-k:][::-1])
print(min(results))

#input2: try with "bca"
word = 'bca'
results = [word]
for k in range(1, len(word) + 1):
    results.append(word[:k][::-1] + word[k:])
for k in range(1, len(word) + 1):
    results.append(word[:-k] + word[-k:][::-1])
print(min(results))
#input3: try with 'zab'

word = 'zab'
results = [word]
for k in range(1, len(word) + 1):
    results.append(word[:k][::-1] + word[k:])
for k in range(1,len(word) + 1):
    results.append(word[:-k] + word[-k:][::-1])
print(min(results))



#common string methods cheat sheet
s = 'hello world'
s.find("World") # 6(index of first occurence, -1 if no found)
s.count("l") # 3
s.replace("World", "Python") # "Hello Python"
s.startswith("Hello") # True
s.endswith("ld") # True




