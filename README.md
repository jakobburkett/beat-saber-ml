# beat-saber-ml

# py and package versions/env info
- python version 3.10.12 - maybe not

- check out cntk instead of tensorflow?


# tutorials and learning materials
https://github.com/microsoft/ML-For-Beginners

https://github.com/microsoft/AI-For-Beginners


# PLEASE DO NOT PUSH ANYTHING FROM ddc_research_fork/ddc/data
# steps i used to run the DDC stuff (demo)
1. Clone repo https://github.com/jakobburkett/ddc_research_fork
2. ```cd ddc_fork```
3. ```python3 -m venv .venv```
4. ```source .venv/bin/activate```
5. ```pip3 install -r ./requirements.txt```
6. ```cd infer```
7. open docker desktop (for wsl usage)
8. ```./docker_serve.sh```
9. ```deactivate``` when done with virtual environment

## (building dataset)
1. ```cd ddc_research_fork/ddc```
2. ```cd data/raw/speirmix```
3. download and extract/unzip speirmix from https://zenius-i-vanisher.com/v5.2/viewsimfilecategory.php?categoryid=897
4. ```cd ../../../scripts```
5. ```./smd_1_extract.sh speirmix```
6. ```./smd_2_filter.sh speirmix```
7. ```./smd_3_dataset.sh speirmix```
8. ```./smd_4_analyze.sh speirmix```

## training
1. ```./sml_onset_0_extract.sh speirmix```
2. ```./sml_onset_1_chart.sh speirmix```
3. ```./sml_onset_2_train.sh speirmix```
4. ```./sml_sym_2_train.sh speirmix```
5. ```./sml_sym_2_mark.sh speirmix 5```


## NOTES
1. Lots of errors. WIll update requiremnts.txt soon
2. Cuda 10, tensorflow 1.13 (oldest possible) with some minor modifications
3. Changing batch size didn't fix issue, however I changed the pad_size to match the batch_size to remove a matrix shape mismatch when you change the batch size from 256.
4. I was still getting the Blas Gemm error, but I removed ~/.nv cache folder and it hasnt crashed yet. But is taking forever to get to the point it was when it usually crashes
5. run ./sml_sym_1_chart.sh BEFORE sml_sym_2_train.sh
