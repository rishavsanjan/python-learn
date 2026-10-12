import shutil
from pathlib import Path

file_groups = {
    
}

folder = Path("test_files")

if folder.exists() and folder.is_dir():
    for item in folder.iterdir():
        if item.is_file():
            print(item.name, " - ", item.suffix)
            extension = item.suffix

            if extension not in file_groups:
                file_groups[extension] = []

            file_groups[extension].append(item.name)
else:
    print("Does not exist")

for extension, files in file_groups.items():
    extension_folder = folder / extension
    extension_folder.mkdir(exist_ok=True)
    print(extension, ":", files)

    for file in files:  
        print(file)
        source = Path(f"test_files/{file}")
        destination = Path(f"test_files/{extension}")
        shutil.move(source, destination)

print("Files organized successfully!")


