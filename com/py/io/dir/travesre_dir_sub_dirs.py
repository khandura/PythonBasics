import glob
import os.path
import pandas as pd
import shutil
import time

SOURCE_DIR = r'D:\CODEBASE\files\LU_STRESS_LOSS'
DESTI_DIR = r'D:\CODEBASE\files\dest'


def read_file_recursively():
    print("reading files at path ", SOURCE_DIR)
    files = list(glob.iglob(SOURCE_DIR + '/**/*Lu_Portfolio_*.csv', recursive=True))
    for file in files:
        print(f" file {file} : Created: {time.ctime(os.path.getmtime(file))}")

    print('After sorting')
    files.sort(key=lambda x: os.path.getmtime(x))
    for file in files:
        print(f" file {file} : Created: {time.ctime(os.path.getmtime(file))}")
        copy_files_to_safe_zone(file)

    for file in glob.iglob(DESTI_DIR + '/**/*Lu_Portfolio_*.csv', recursive=True):
        print(f" file {file} : Created: {time.ctime(os.path.getmtime(file))}")


def copy_files_to_safe_zone(file):
    print(f'copying file {file} to safe location {DESTI_DIR}')
    shutil.copy2(file, DESTI_DIR)
    update_and_rewrite_file(file)


def update_and_rewrite_file(file):
    file_data = pd.read_csv(file)
    file_data.loc[:, 'COL1'] = "AGAIN UPDATED"
    print('rewriting the updated file : ', file)
    file_data.to_csv(file, index=False)


read_file_recursively()
