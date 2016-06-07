#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" Word Filter - cmd WordFilter.py inputFile outputFile """
from __future__ import print_function
from os import path
import unicodedata
import sys


def is_thai_alphabet(input_str):
    """
    check string is thai aplphabet
    //char -> character to check, return boolean
    """
    if len(input_str.strip()) == 0:
        return False
    for char in input_str.decode("utf-8"):
        try:
            if "THAI" not in unicodedata.name(char):
                return False
        except ValueError:
            return False
    return True

if __name__ == "__main__":

    INPUT_PATH = sys.argv[1]
    OUTPUT_PATH = sys.argv[2]

    if path.isfile(INPUT_PATH):  # check INPUT_PATH
        with open(INPUT_PATH, mode='r') as input_file:
            with open(OUTPUT_PATH, mode='w') as output_file:
                for line in input_file:  # read per line
                    LINE_OUTPUT = list()
                    for string in line.split("|"):
                        if is_thai_alphabet(string):
                            LINE_OUTPUT.append(string)
                    output_file.write("|".join(LINE_OUTPUT)+"\n")
