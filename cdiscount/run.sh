pypy to_vw_format.py ../data/training.csv training.vw train Categorie3
pypy to_vw_format.py ../data/test.csv test.vw test Categorie3
vw train.vw -f model.vw --loss_function logistic -b 21 -P 10000 --oaa 5786
vw -t test.vw -i model.vw --loss_function logistic -b 21 -P 10000 -p preds.txt
pypy generate_submission.py preds.txt submission.csv
