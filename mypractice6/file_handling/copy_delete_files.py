import shutil
import os

# copy file
shutil.copy("sample.txt", "sample_copy.txt")

# delete file safely
if os.path.exists("sample_copy.txt"):
    os.remove("sample_copy.txt")
    print("File deleted")