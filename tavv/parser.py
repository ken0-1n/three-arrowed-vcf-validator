#! /usr/bin/env python
from run import *
import argparse
from version import __version__

def create_parser():
    parser = argparse.ArgumentParser(prog = "tavv")
    parser.add_argument("--version", action = "version", version = "%(prog)s " + __version__)
    subparsers = parser.add_subparsers()

    #################################
    ####  VCF-Validator
    subparser = subparsers.add_parser("vcfvalidator")
    subparser.add_argument("input_vcf", metavar = "target.vcf", default = None, type = str,
                        help = "the path to the input_vcf_file")
    subparser.add_argument("output", metavar = "output_directory", default = None, type = str, 
                        help = "the path to the output directory")
    subparser.set_defaults(func = validator_main)

    #################################
    ####  vcflib/vcfchecker 
    subparser = subparsers.add_parser("vcfchecker")
    subparser.add_argument("input_vcf", metavar = "target.vcf", default = None, type = str,
                        help = "the path to the input_vcf_file")
    subparser.add_argument("output", metavar = "output_directory", default = None, type = str, 
                        help = "the path to the output directory")
    subparser.add_argument("reference", metavar = "reference.fa", default = None, type = str,
                        help = "the path to the reference genome sequence")
    subparser.set_defaults(func = vcfcheck_main)

    #################################
    ####  GATK ValidateVariants 
    subparser = subparsers.add_parser("gatk")
    subparser.add_argument("input_vcf", metavar = "target.vcf", default = None, type = str,
                        help = "the path to the input_vcf_file")
    subparser.add_argument("output", metavar = "output_directory", default = None, type = str, 
                        help = "the path to the output directory")
    subparser.add_argument("reference", metavar = "reference.fa", default = None, type = str,
                        help = "the path to the reference genome sequence")
    subparser.set_defaults(func = gatk_main)

    #################################
    #### All
    subparser = subparsers.add_parser("all")
    subparser.add_argument("input_vcf", metavar = "target.vcf", default = None, type = str,
                        help = "the path to the input_vcf_file")
    subparser.add_argument("output", metavar = "output_directory", default = None, type = str, 
                        help = "the path to the output directory")
    subparser.add_argument("reference", metavar = "reference.fa", default = None, type = str,
                        help = "the path to the reference genome sequence")
    subparser.set_defaults(func = all_main)

    return parser
