import shutil, platform

py_version = platform.python_version()
import os,sys

if py_version < '3.8':
    exit('anda menggunakan python version %s silahkan upgrade ke 3.9++'%(py_version))


os.system("python3 DARK.py")

