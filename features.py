from __future__ import print_function
from sys import argv

#suffixes
suff = []
with open("f.suffixes") as f:
    suff = [i.strip().lower() for i in f.readlines()]
    
#languages
lang = []
with open("f.languages") as f:
    lang = [i.strip().lower() for i in f.readlines()]
    
#countries
coun = []
with open("f.countries") as f:
    coun = [i.strip().lower() for i in f.readlines()]
    
#numbers
numb = []
with open("f.numbers") as f:
    numb = [i.strip().lower() for i in f.readlines()]
    
#genres
genr = []
with open("f.genres") as f:
    genr = [i.strip().lower() for i in f.readlines()]

with open(argv[1]) as f:
	lines = enumerate(f)
	hasNext = True
	while hasNext:
		try:
			sentence = []
			while True:
				i, w = lines.next()
				w = w.strip()
				if len(w) > 0:
					sentence.append(w)
				else:
					break
		except StopIteration:
			hasNext = False
		
		for i, w in enumerate(sentence):
			suffix = 0
			for s in suff:
				if w.endswith(s):
					suffix = s
			numbers = 0
			for s in numb:
				if s in w:
					numbers = 1
					break
			print(1 if w in lang else 0, 1 if w in coun else 0, 1 if w in genr else 0, numbers, suffix,
				  w[-3:] if len(w) > 3 else 0, w[-2:] if len(w) > 3 else 0, w[-1] if len(w) > 3 else 0,
				  i + 1, len(sentence) - i, sep="\t")
		
		print()

# CUSTOM FEATURES
# 1. is a known language name
# 2. is a known country name
# 3. is a known genre name
# 4. is a number-realted word
# 5. known suffix in the end or 0
# 6. last 3 chars if longer than 3 else 0
# 7. last 2 chars if longer than 3 else 0
# 8. last char if longer than 3 else 0
# 9. ordinal position in sentence
# 10. inverse ordinal position in sentence