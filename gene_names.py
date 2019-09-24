#!/usr/bin/python
import sys
import re

gene_array = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        if re.search(r'.*\t.*\tgene\t', line):
            gene_name = re.search(r'gene_name\s\"(.*?)\";', line).group(1)
            chromosome = re.search(r'^(.*?)\t', line).group(1)
            starting_position = re.search(r'\t(\d*?)\t', line).group(1)
            ending_position = re.search(r'\t\d*\t(\d*?)\t', line).group(1)
            gene_array.append({"geneName": gene_name, "chr": chromosome, "startPos": int(starting_position),
                               "endPos": int(ending_position)})

print gene_array
