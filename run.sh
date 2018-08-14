#!/bin/sh

set -xv

IMAGE_NAME="three_arrowed_vcf_validator"
INPUT_VCF=$1
OUTPUT=$2
REFERENCE_GENOME=$3

CMDNAME=`basename $0`
if [ $# -ne 3 ]; then
  echo "Usage:  $CMDNAME {input_vcf} {output_dir} {reference_genome}" 1>&2
  exit 1
fi

if [ ! -e $INPUT_VCF ]; then
  echo "${INPUT_VCF} NOT found."
fi

if [ ! -e $REFERENCE_GENOME ]; then
  echo "${REFERENCE_GENOME} NOT found."
fi

mkdir -p $OUTPUT

INPUT_DIR=$(cd $(dirname $INPUT_VCF) && pwd)
OUTPUT_DIR=$(cd $OUTPUT && pwd)
REFERENCE_DIR=$(cd $(dirname $REFERENCE_GENOME) && pwd)

INPUT_BASE=`basename $INPUT_VCF`
REFERENCE_BASE=`basename $REFERENCE_GENOME`

# docker run --rm -it \
docker run -it \
  -v ${INPUT_DIR}:/local/input \
  -v ${OUTPUT_DIR}:/local/output \
  -v ${REFERENCE_DIR}:/local/reference \
  -w /local \
  ${IMAGE_NAME} tavv /local/input/$INPUT_BASE /local/output /local/reference/$REFERENCE_BASE

