#! /usr/bin/env python

import sys, subprocess, os
from datetime import datetime

dt = datetime.now().strftime("%Y%m%d%H%M%S")

def subprocess_exec(args,toolname,commands):
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    basename = os.path.basename(args.input_vcf)
    stdout_f = open(args.output +"/"+basename+"."+toolname+".stdout."+dt+".txt", 'w')
    stderr_f = open(args.output +"/"+basename+"."+toolname+".stderr."+dt+".txt", 'w')
    subprocess.Popen(commands, stdout=stdout_f, stderr=stderr_f)
    stdout_f.close()
    stderr_f.close()

def validator_main(args):
    commands = ["vcf_validator_linux", "-i", args.input_vcf + "-o", args.output]
    subprocess_exec(args,"vcf_validator",commands)

def vcfcheck_main(args):
    commands = ["vcfcheck", "-f", args.reference, args.input_vcf]
    subprocess_exec(args,"vcflib-vcfcheck",commands)

def gatk_main(args):
    commands = ["gatk","ValidateVariants","-R", args.reference, "-V", args.input_vcf, "--validation-type-to-exclude","ALLELES"]
    subprocess_exec(args,"gatk-validatevariants",commands)

def all_main(args):
    validator_main(args)
    vcfcheck_main(args)
    gatk_main(args)
