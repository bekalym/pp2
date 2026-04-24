import shutil
import os

shutil.copy("sample.txt", "copy_sample.txt")
print("File copied.")

os.remove("copy_sample.txt")
print("File deleted.")