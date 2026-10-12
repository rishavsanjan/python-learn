from pathlib import Path

file_groups = {
    
}

folder = Path("test_files")

if folder.exists():
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
    print(extension, ":", files)
