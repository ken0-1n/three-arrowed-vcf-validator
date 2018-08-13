#! /usr/bin/env python
from run import *
import argparse
from version import __version__

def create_parser():
    parser = argparse.ArgumentParser(prog = "tavv")
    parser.add_argument("--version", action = "version", version = "%(prog)s " + __version__)
    parser.add_argument("input_vcf", metavar = "target.vcf", default = None, type = str,
                        help = "the path to the input_vcf_file")
    parser.add_argument("output", metavar = "output_directory", default = None, type = str, 
                        help = "the path to the output directory")
    parser.add_argument("reference", metavar = "reference.fa", default = None, type = str,
                        help = "the path to the reference genome sequence")

    return parser

