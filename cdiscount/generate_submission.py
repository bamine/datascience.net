import logging
import argparse


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s')


def generate_submission(vw_predictions_file, submission_file, labels_dict_file='labels.txt'):
    vw_predictions = open(vw_predictions_file)
    submission = open(submission_file, 'wb')
    submission.write('Id_Produit;Id_Categorie\n')
    labels_dict = [(line.strip().split(':')[0],line.strip().split(':')[1])
        for line in open(labels_dict_file).readlines()]
    for pred in vw_predictions:
        product_id = pred.strip().split()[1]
        category_id = int(float(pred.strip().split()[0]))
        submission.write('{0};{1}\n'.format(product_id,category_id))

    vw_predictions.close()
    submission.close()


parser = argparse.ArgumentParser(description='Generate submission file from VW predictions file')
parser.add_argument('vw_predictions_file', help = 'VW predictions file')
parser.add_argument('submission_file', help = 'name of the output predictions file')
args = parser.parse_args()

generate_submission(args.vw_predictions_file, args.submission_file)