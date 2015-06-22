import logging
import argparse


def vw_accuracy(true_labels_file, pred_labels_file):
    logging.info('Computing accuracy from train file %s and prediction file %s', true_labels_file, pred_labels_file)
    n_correct = 0
    n_example = 0
    true_labels = open(true_labels_file, 'rb')
    pred_labels = open(pred_labels_file, 'rb')
    for line_true, line_pred in zip(true_labels, pred_labels):
        true_label = int(line_true.split()[0])
        pred_label = int(float(line_pred.split()[0]))
        if true_label == pred_label:
            n_correct += 1
        n_example += 1
    accuracy = n_correct/float(n_example)
    logging.info('Total examples : %s', n_example)
    logging.info('Accuracy %f %', accuracy*100)
    return accuracy

parser = argparse.ArgumentParser(description='Compute accuracy from train data file, and predicted labels in vw format')
parser.add_argument('train_file', help = 'Train file used to generate predictions')
parser.add_argument('pred_file', help = 'Predictions generated from Vowpal Wabbit (-p argument in command line)')
args = parser.parse_args()

vw_accuracy(args.train_file, args.pred_file)
