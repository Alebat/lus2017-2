from sys import argv
from random import shuffle

assert len(argv) == 5, "command folds train_file {r|n} features"

with open(argv[2]) as lines:
	sentences = []
	sentence = []
	for i in lines:
		i = i.strip()
		if len(i) > 0:
			sentence.append(i)
		else:
			sentences.append(sentence)
			sentence = []

folds = int(argv[1])
if argv[3] == "r":
	shuffle(sentences)

size = len(sentences) / folds
for i in range(folds):
	with open("xval-train-" + str(i), "w") as tr:
		with open("xval-test-" + str(i), "w") as te:
			for ii in range(folds):
				file = te if i == ii else tr
				for s in sentences[size * i: size * (i+1)]:
					for l in s:
						file.write(l)
						file.write("\n")


from subprocess import call
from os import system as run

for i in range(folds):
	tr = "xval-train-" + str(i)
	te = "xval-test-" + str(i)
	run ("crf_learn -f 1 -c 1 -e 0.001 -a CRF-L2 -p 8 %s %s xval-model.%d" % (argv[4], tr, i))
	run ("crf_test -m xval-model.%d test > xval-results.%d" % (i, i))
	run ('./conlleval.pl -d "\t" < xval-results.%d > xval-eval.%d' % (i, i))

for i in range(folds):
	run ("head -n 2 xval-eval.%d" % i)
