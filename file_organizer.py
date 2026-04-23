
########FILE ORGANIZER#######


from pathlib import Path
import shutil

# Folder base
source_folder = Path('/Users/emilianopadilla/Downloads/file_organizer')

# Folder base de destino
base_destination = Path('/Users/emilianopadilla/Downloads')

# Mapeo para los folders dependiendo de la extension

EXTENSION_MAP = {
    ".py": "code_files",
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".mp4": "videos",
    ".doc": "documents",
    ".pdf": "documents",
    ".txt": "documents"
}

for file in source_folder.iterdir():
    if file.is_file():
        ext = file.suffix.lower()

        # Nombre del folder
        folder_name = EXTENSION_MAP.get(ext, "other")

        # Constructor del nombre del folder
        destination_folder = base_destination / folder_name
        destination_folder.mkdir(exist_ok=True)

        # Construccion de la direccion completa con el file
        destination = destination_folder / file.name

        # Para mover el file
        shutil.move(file, destination)

        print(f"Moving {file.name} → {folder_name}/")


#this is part of the test branch