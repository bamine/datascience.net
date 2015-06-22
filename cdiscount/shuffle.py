import sys
import random
import argparse
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s')

parser = argparse.ArgumentParser(description='Shuffle large text file')
parser.add_argument('input_file', help='Input file to shuffle')
parser.add_argument('output_file', help='Output file')
parser.add_argument(
    '--preserve_headers', type=int, help='Whether to keep header (first line)')
parser.add_argument(
    '--lines_in_memory', type=int, help='Max lines to keep in memory')
parser.add_argument('--random_seed', type=int, help='Random seed')
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

if args.preserve_headers:
    preserve_headers = args.preserve_headers
else:
    preserve_headers = 0

if args.lines_in_memory:
    lines_in_memory = args.lines_in_memory
else:
    lines_in_memory = 25000

logging.info("caching %s lines at a time...", lines_in_memory)

if args.random_seed:
    random_seed = args.random_seed
    random.seed(random_seed)
    logging.info("random seed: %s", random_seed)

# first count

logging.info("counting lines...")

i_f = open(input_file)
o_f = open(output_file, 'wb')

if preserve_headers:
    headers = i_f.readline()
    o_f.write(headers)

counter = 0
for line in i_f:
    counter += 1

    if counter % 100000 == 0:
        logging.info("Counted %s lines", counter)

logginginfo("Number of lines in file %s", counter)

logging.info("shuffling file %s...", input_file)

order = range(counter)
random.shuffle(order)

epoch = 0

while order:

    current_lines = {}
    current_lines_count = 0

    current_chunk = order[:lines_in_memory]
    current_chunk_dict = {x: 1 for x in current_chunk}        # faster "in"
    current_chunk_length = len(current_chunk)

    order = order[lines_in_memory:]

    i_f.seek(0)
    if preserve_headers:
        i_f.readline()

    count = 0

    for line in i_f:
        if count in current_chunk_dict:
            current_lines[count] = line
            current_lines_count += 1
            if current_lines_count == current_chunk_length:
                break
        count += 1
        if count % 100000 == 0:
            print count

    logging.info("writing...")

    for l in current_chunk:
        o_f.write(current_lines[l])

    lines_saved = current_chunk_length + epoch * lines_in_memory
    epoch += 1
    logging.info("pass %s complete (%s/%s lines saved)", epoch, lines_saved, counter)
