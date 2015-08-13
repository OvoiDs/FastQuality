#!/usr/bin/env python
# encoding: utf-8
# Author: Yannick BOURSIN - elipsoid@gmail.com

import sys
from argparse import ArgumentParser

def fastqQuality(sequence, shift):
    qualArray = []
    for el in sequence:
        qualArray.append(ord(el) + shift)
    return ''.join([chr(x) for x in qualArray])

parser = ArgumentParser()
parser.add_argument("-i", dest="input", help="Please give the path to your FASTQ file")
parser.add_argument("-s", dest="shift", type=int, default=33, help="Please indicate how to shift the quality scores (e.g.: -33)")
args = parser.parse_args()
input = args.input
shift = args.shift

a = open(input, "r")

counter = 1
line = a.readline()
while line != "":
    if (counter % 3 == 0):
        line = fastqQuality(line.rstrip('\n'), shift) + '\n'
    sys.stdout.write(line)




