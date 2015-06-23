pypy shuffle.py ../data/training.csv ../data/training.shuffled.csv 1 1234
pypy to_vw_format.py ../data/training.shuffled.csv training.vw train Categorie3
pypy to_vw_format.py ../data/test.csv test.vw test Categorie3
vw training.vw -f model.vw --loss_function logistic -b 21 -P 1000 --oaa 5786
vw -t test.vw -i model.vw --loss_function logistic -b 21 -P 1000 -p preds.txt
pypy generate_submission.py preds.txt submission.csv