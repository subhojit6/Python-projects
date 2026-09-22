import os
import shutil

folder_path = "C:/Users/subho/Downloads/my documents"

EXTENSION_MAP = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "heic": "Images",
    "pdf": "Documents",
    "xml": "Documents",
    "pptx": "Documents",
    "zip": "Zip_files",
    "mp3": "Music",
}

def list_files(folder_path):
    return os.listdir(folder_path)

def get_extension(file_name):
    file_extension = os.path.splitext(file_name)[1]
    extension = file_extension[1:].lower()
    return extension

def get_category(extension):
        category = EXTENSION_MAP.get(extension, "Other")
        return category
        
def organize_folder(folder_path):
     for i in list_files(folder_path):
        if os.path.isfile(folder_path + "/" + i):
            extension = get_extension(i)
            category = get_category(extension)

            destination_folder = folder_path + "/" + category
            os.makedirs(destination_folder, exist_ok=True)

            source_path = folder_path + "/" + i
            destination_path = destination_folder + "/" + i

            try:
                shutil.move(source_path, destination_path)
                print(f"Moved {i} -> {category}/")
            except Exception as error:
                print(f"Skipped {i}: {error}")
        else:
             print(f"{i} is a Directory")

organize_folder(folder_path)


