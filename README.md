# beat-saber-ml

# py and package versions/env info
- python version 3.10.12 - maybe not

- check out cntk instead of tensorflow?


# tutorials and learning materials
https://github.com/microsoft/ML-For-Beginners

https://github.com/microsoft/AI-For-Beginners


# PLEASE DO NOT PUSH ANYTHING FROM ddc_research_fork/ddc/data
# steps i used to run the DDC stuff (demo)
1. Clone repo https://github.com/jb410817/ddc_research_fork
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
1. ```./sml_onset_1_chart.sh speirmix```
2. ```./sml_onset_1_chart.sh speirmix```
3. ```./sml_onset_2_train.sh speirmix```
4. ```./sml_sym_2_mark.sh speirmix 5```
