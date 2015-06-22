SET VW_PATH=C:\src\vw\vowpal_wabbit\vowpalwabbit\x64\Debug
pypy to_vw_format.py ../data/training.csv training.vw train Categorie3
pypy to_vw_format.py ../data/test.csv test.vw test Categorie3
"%VW_PATH%\vw.exe" training.vw -f model.vw --loss_function logistic -b 10 -P 100 --oaa 500
"%VW_PATH%\vw.exe" -t test.vw -i model.vw --loss_function logistic -b 10 -P 100 -p preds.txt
pypy generate_submission.py preds.txt submission.csv