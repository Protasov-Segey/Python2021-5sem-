#!/usr/bin/env python
# coding: utf-8

import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("--name", required = True, type = str)
parser.add_argument(" --country", required = True, type = str)
parser.add_argument("--petal-colour", required = True, choices = ["R", "W", "Y", "V", "B"])
parser.add_argument("--stem-length", reauired = True, type = int)
parser.add_argument("--with-thorns", default = False, type = bool)
parser.add_argument("--companion-plants", default = None, nargs='*')

with open('journal.txt', 'a') as file: 
    args = vars(parser.parse_args())
    json.dump(args, file)

