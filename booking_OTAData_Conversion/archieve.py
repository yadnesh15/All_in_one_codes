import os
from pathlib import Path
import shutil



# file = r"E:/Yadnesh/Staah Max/dd/dde.txt"
# target = r"E:/Yadnesh/"

# sp = os.path.join(file)
# tp = os.path.join(target,"{file}.archived")
# shutil.move(tp,target)

folder = r"E:\Yadnesh\st\InputData\file"
archive = r"E:\Yadnesh\st\InputData\archive"

def archive_file(file,source, target):

    t =xdate().strftime('%d%m%y%I%M%S%p')
    sp = os.path.join(source, file)
    tp = os.path.join(target, f'{t}_{file}.archived')
    os.replace(sp, tp)
    return None