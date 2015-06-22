import csv
import logging
import argparse


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s')


def generate_vw_file(input_file, output_file, type_of_file='train', label_col='Categorie3'):
    logging.info('Generating VW train file')
    logging.info('Input file - %s', input_file)
    logging.info('Type of file - %s', type_of_file)
    logging.info('Column used as a label - %s', label_col)
    input_data = open(input_file)
    output = open(output_file, 'wb')
    labels = []
    counter = 0
    for row in csv.DictReader(input_data, delimiter=';'):
        if type_of_file == 'train':
            label = row[label_col]
            if label not in labels:
                labels.append(label)
            label_int = labels.index(label) + 1
        else:
            label_int = 1
        line = "{0} {1}|D {2} |L {3} |P price:{4}\n".format(
            label_int,
            row['Identifiant_Produit'],
            row['Description'].replace(':', '').replace('|', ''),
            row['Libelle'].replace(':', '').replace('|', ''),
            row['prix'])
        output.write(line)
        counter += 1
        if counter % 10000 == 0:
            logging.info('Processed %s lines ...', counter)
            # break

    if type_of_file == 'train':
        labels_file = open('labels.txt', 'wb')
        logging.info('Number of labels : %s', len(labels))
        labels_file.write(
            '\n'.join("{0}:{1}".format(k, v) for v, k in enumerate(labels)))
        labels_file.close()
    input_data.close()
    output.close()


parser = argparse.ArgumentParser(description='Converts CDiscount data to VW format data')
parser.add_argument('input_file', help = 'Input CDiscount data (training.csv or test.csv)')
parser.add_argument('output_file', help = 'Output to write the Vowpal Wabbit formatted data to')
parser.add_argument('type_of_file', help = 'Type of input file (train or test)')
parser.add_argument('label_col', help = 'Column from csv file to use as label')
args = parser.parse_args()

generate_vw_file(args.input_file, args.output_file, args.type_of_file, args.label_col)
