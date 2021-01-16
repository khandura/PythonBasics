import os

PATH = r'D:\CODEBASE\files\LU_STRESS_LOSS'
DEST_PATH = r'D:\CODEBASE\files\dest'


def list_dir_and_files():
    root = next(os.walk(PATH))[0]
    print('root :', root)
    dirs = next(os.walk(PATH))[1]
    print('sub directories :', dirs)
    files = next(os.walk(PATH))[2]
    print('files :', files)


def loop_dir_rec():
    print('going to loop all sub directories and files within the path :', PATH)

    for root, sub_dirs, files in os.walk(PATH):
        print("root", root)

        # for root in roots:
        #     print('root :', root)
        # for sub_dir in sub_dirs:
        #     print('directory :', sub_dir)
        for file in files:
            print('file :', file)



loop_dir_rec()
# list_dir_and_files()
