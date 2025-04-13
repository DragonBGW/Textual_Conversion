import os

# Check current working directory
print("Current working directory:", os.getcwd())

# Check if input.docx exists there
print("Files in this folder:", os.listdir())

print("Files in test_folder:", os.listdir('test_folder'))

