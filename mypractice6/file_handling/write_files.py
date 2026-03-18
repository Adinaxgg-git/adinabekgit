# create and write file
with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is a sample file\n")

# append data
with open("sample.txt", "a") as f:
    f.write("Appended line\n")