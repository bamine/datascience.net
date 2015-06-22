pypy to_vw_format.py ~/kaggle/cdiscount/data/training.csv training.vw train Categorie3
pypy to_vw_format.py ~/kaggle/cdiscount/data/test.csv test.vw test Categorie3
pypy training.vw training.shuffled.vw --random_seed 1234
vw training.vw -f model.vw --loss_function logistic -b 21 -P 10000 --oaa 5786
vw -t test.vw -i model.vw --loss_function logistic -b 21 -P 10000 -p preds.txt
pypy generate_submission.py preds.txt submission.csv
