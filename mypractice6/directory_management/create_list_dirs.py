import os

# create nested directories
os.makedirs("test_dir/subdir", exist_ok=True)

# list files and folders
print(os.listdir("."))

# find .txt files
for file in os.listdir("."):
    if file.endswith(".txt"):
        print("Found:", file)