# README
Alessandro battisti, 189545
## Second LUS assignment

### Data
The original data is in the files NLSPARQL.*, divided in test and training.

The __additional features__ are computed by the script __features.py__

The script __extract__ builds the files __train__ and __test__ starting from the 4 NLSPARQL.* files and adding the additional features.

ADDITIONAL FEATURES:
1. is a known language name
2. is a known country name
3. is a known genre name
4. is a number-realted word
5. known suffix in the end or 0
6. last 3 chars if longer than 3 else 0
7. last 2 chars if longer than 3 else 0
8. last char if longer than 3 else 0
9. ordinal position in sentence
10. inverse ordinal position in sentence

### Models
A model's features are represented through a file named in the form __feat.*__.

The report explains a subset of the present files, the ones not mentoned contain comments or are attempt not worth explaining in the report.

### Training
To train a model the script __full__ can be used: it takes as parameter the number corresponding to the feature description.

This script generates three files:
- model.* containing the binary learned model
- results.* containing the classified data
- eval.* containing the conlleval.pl output

### Visualizing the misclassified phrases
The script __check.py__ extract from __results.*__ the wrong phrases and prints them. Each I-tag belongs to the first precedin B-tag.

It takes as argument the file name from where to read results (__results.*__).

### Cross validation
A script for cross validation is present: __cross.py__. This script is in python3.

Usage: cross.py n-of-folds complete-train-set-file {r for shuffle|n for not} features-file

### Example: model 19
    # Build train and test sets
    sh extract
    # train-test-eval
    sh full 19
    # view errors
    sh python check.py results.19

### Hyper-params tuning
To tune the f (cutoff freq) parameter the script __full-tune-f__ is available; so for the c parameter (cost) __full-tune-c__. They take as arguments the number of the model description (where to read the features) and the parameter to use.

### Membership features sets
The files named __f.*__ contain the sets used by __feature.py__ to build the membership features.


