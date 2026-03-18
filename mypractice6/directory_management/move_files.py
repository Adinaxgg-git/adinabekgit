import shutil

# move file
shutil.move("sample.txt", "test_dir/sample.txt")

# copy file back
shutil.copy("test_dir/sample.txt", "sample.txt")