import os

os.makedirs("test_folder/subfolder", exist_ok=True)
print("Nested directories created.")

items = os.listdir(".")
print("Files and folders in current directory:")
for item in items:
    print(item)