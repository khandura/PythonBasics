import shutil
import os

# make sure that these directories exist
dir_src = "E:\\workspaces\\dir1\\"
dir_dst = "E:\\workspaces\\dir2\\"

for file in os.listdir(dir_src):
    print
    file
    src_file = os.path.join(dir_src, file)
    dst_file = os.path.join(dir_dst, file)

    shutil.copy2(src_file, dst_file)
