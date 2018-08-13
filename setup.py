#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def get_version():
    with open(path.join(here, "tavv/version.py"), encoding = 'utf-8') as hin:
        for line in hin:
            if line.startswith("__version__"):
                version = line.partition('=')[2]
                return version.strip().strip('\'"')

    raise ValueError('Could not find version.')

setup(
    name = 'tavv',
    version = get_version(),
    description='Python tools for validating vcf file',
    url = 'https://github.com/ken0-1n/three-arrowed-vcf-validator',
    author = 'Kenichi Chiba',
    author_email = 'kechiba@ncc.go.jp',
    license = 'GPLv3',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],

    packages = find_packages(),
    # install_requires = ["GATK>=4.0.7.0", "vcf_validator>=0.8.0", "vcflib>=v1.0.0-rc1"],
    entry_points = {'console_scripts': ['tavv=tavv:main']}
)
