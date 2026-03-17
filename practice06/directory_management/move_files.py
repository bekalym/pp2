import shutil
import os

# создаём папку для копии
os.makedirs("backup_folder", exist_ok=True)

source = "../file_handling/sample.txt"
destination = "backup_folder/sample.txt"

shutil.copy(source, destination)

print("File copied to backup_folder.")