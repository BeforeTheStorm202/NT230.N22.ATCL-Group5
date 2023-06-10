# NT230.N22.ATCL-Group5
## Malware's Modus Operandi
Our implementation for the paper "Applying NLP techniques to malware detection in a practical environment" of Mamoru Mimura and Ryo Ito.

1. Construct a list of files and assign labels (make_csv.py).

2. Extract strings from files with the strings command on Linux (get_strings.py).

3. Split into train & test sets with the ratio of 60:40 (train_test_split.py).

4. Derive feature vectors from Doc2Vec model (Doc2Vec.ipynb)

5. Train 4 models from feature vectors extracted from Doc2Vec model.
