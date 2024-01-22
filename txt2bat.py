import os
import numpy as np
import re

def batch_rename(file_dir, old_ext, new_ext):
    list_file = os.listdir(file_dir) # 返回指定目录
    for file in list_file:
        ext = os.path.splitext(file) # 返回文件名和后缀
        if old_ext == ext[1]:   # ext[1]是.doc,ext[0]是1
            newfile = ext[0] + new_ext
            os.rename(os.path.join(file_dir, file),
                      os.path.join(file_dir, newfile))

#E:\GNSSR_DATA\TDS-1\lonlat_numpy\201804\30
if __name__ == '__main__':
    batch_rename("E:\GNSSR_DATA\TDS-1\lonlat_numpy\\201804\\30", ".txt", ".bat")