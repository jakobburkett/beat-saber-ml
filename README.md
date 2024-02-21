# beat-saber-ml

# py and package versions/env info
- python version 3.10.12 - maybe not

- check out cntk instead of tensorflow?


# tutorials and learning materials
https://github.com/microsoft/ML-For-Beginners

https://github.com/microsoft/AI-For-Beginners

# steps i used to run the DDC stuff (demo)
1. Clone repo https://github.com/jb410817/ddc_fork
2. ```cd ddc_fork```
3. ```python3 -m venv .venv```
4. ```source .venv/bin/activate```
5. ```pip3 install -r ./requirements.txt```
6. ```cd infer```
7. open docker desktop (for wsl usage)
8. ```./docker_serve.sh```
9. ```deactivate``` when done with virtual environment

## (building dataset) (WIP for writing this, be careful <3)
1. ```cd ddc_fork```
2. ```mkdir data```
3. ```cd data```
4. ```mkdir raw```
5. ```mkdir json_raw```
6. ```mkdir json_filt```
7. ```cd raw```
8. ```mkdir speirmix```
9. ```cd speirmix```
10. download and extract/unzip speirmix from https://zenius-i-vanisher.com/v5.2/viewsimfilecategory.php?categoryid=897
11. ```cd ../../../scripts```
12. ```./smd_1_extract.sh speirmix```
13. ```./smd_2_filter.sh speirmix```
14. ```./smd_3_dataset.sh speirmix```
15. ```./smd_4_analyze.sh speirmix```
