FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    python \
    g++ \
    make \
    cmake \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev \
    dpkg-dev \
    ragel \
    tar \
    unzip \
    wget \
    bzip2 \
    openjdk-8-jre \
    git \
    python-pip \
    && mkdir -p /tools \
    && mkdir -p /tools/vcf_validator 

RUN pip install setuptools

ENV PATH $PATH:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.171-8.b10.38.amzn1.x86_64/jre/bin
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.171-8.b10.38.amzn1.x86_64/jre

RUN cd /tools \
    && wget https://github.com/broadinstitute/gatk/releases/download/4.0.7.0/gatk-4.0.7.0.zip \
    && unzip gatk-4.0.7.0.zip \
    && rm gatk-4.0.7.0.zip

RUN cd /tools/vcf_validator \
    && wget https://github.com/EBIvariation/vcf-validator/releases/download/v0.8/vcf_validator_linux \
    && chmod 750 vcf_validator_linux 

RUN cd /tools \
    && git clone --recursive https://github.com/vcflib/vcflib.git \
    && cd vcflib \
    && make

RUN cd /tools \
    && git clone --recursive https://github.com/ken0-1n/three-arrowed-vcf-validator.git \
    && cd three-arrowed-vcf-validator \
    && python setup.py install

ENV PATH $PATH:/tools/gatk-4.0.7.0:/tools/vcf_validator:/tools/vcflib/bin


