# three-arrowed-vcf-validator
Python tools for validating vcf file

## Quick Start
```
docker build -t three_arrowed_vcf_validator .
bash run.sh ${Input VCF} ${Output Directory} ${Reference Genome}
```

## Test Input VCF
```
# contain the REF Error
test/5929.fisher_comp_result.ref_error.vcf.gz 
# contain the format Error
test/5929.fisher_comp_result.format_error.vcf.gz 
# NOT contain errors
test/5929.fisher_comp_result.vcf.gz 

