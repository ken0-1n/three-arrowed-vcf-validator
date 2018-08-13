#! /usr/bin/env python

import sys, subprocess, os
from datetime import datetime

def validator_main(args):

    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    os.mkdir(args.output)
    basename = os.path.basename(args.input_vcf)

    print "-------vcf_validator--------"
    commands = ["vcf_validator_linux", "-i", args.input_vcf + "-o", args.output]
    # commands = ["vcf_validator", "-i", args.input_vcf, "-o", args.output]
    stdout_f = open(args.output +"/"+basename+".vcf_validator.stdout."+dt+".txt", 'w')
    stderr_f = open(args.output +"/"+basename+".vcf_validator.stderr."+dt+".txt", 'w')
    subprocess.Popen(commands, stdout=stdout_f, stderr=stderr_f)
    stdout_f.close()
    stderr_f.close()

    print "-------vcflib/vcfcheck--------"
    commands = ["vcfcheck", "-f", args.reference, args.input_vcf]
    # commands = ["/home/ec2-user/environment/tools/vcflib/bin/vcfcheck", "-f", args.reference, args.input_vcf]
    stdout_f = open(args.output +"/"+basename+".vcflib-vcfcheck.stdout."+dt+".txt", 'w')
    stderr_f = open(args.output +"/"+basename+".vcflib-vcfcheck.stderr."+dt+".txt", 'w')
    subprocess.Popen(commands, stdout=stdout_f, stderr=stderr_f)
    stdout_f.close()
    stderr_f.close()

    print "-------gatk ValidateVariants--------"
    commands = ["gatk", "-R", args.reference, "-V", args.input_vcf, "--validation-type-to-exclude ALLELES"]
    # commands = ["/home/ec2-user/environment/tools/gatk-4.0.7.0/gatk", "-R", args.reference, "-V", args.input_vcf, "--validation-type-to-exclude ALLELES"]
    stdout_f = open(args.output +"/"+basename+".gatk-validatevariants.stdout."+dt+".txt", 'w')
    stderr_f = open(args.output +"/"+basename+".gatk-validatevariants.stderr."+dt+".txt", 'w')
    subprocess.Popen(commands, stdout=stdout_f, stderr=stderr_f)
    stdout_f.close()
    stderr_f.close()
