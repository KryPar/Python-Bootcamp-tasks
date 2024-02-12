import os
import shutil

print("This program helps user automatically sort files into categorized folders.")

target_directory = input("Which directory do you want to organize, insert path: ")

files = os.listdir(target_directory)

mapping = {
    '.pdf': 'Dokumenty',
    '.jpg': 'Obrázky',
    '.png': 'Obrázky',
    '.mp3': 'Hudba',
    '.avi': 'Videa',
    '.docx': 'Dokumenty',
    '.xlsx': 'Dokumenty',
    '.pptx': 'Prezentace'
}

for file in files:
    file_path = os.path.join(target_directory, file)
    if os.path.isfile(file_path):  # Kontrola, zda je položka soubor
        file_extension = os.path.splitext(file)[1]
        if file_extension in mapping:
            target_folder = mapping[file_extension]
            target_folder_path = os.path.join(target_directory, target_folder)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path)
            shutil.move(file_path, target_folder_path)
        else:
            # Vytvoření složky ostatní a přesunutí do složky ostatní 
            other_folder_path = os.path.join(target_directory, "Ostatní")
            if not os.path.exists(other_folder_path):
                os.makedirs(other_folder_path)
            shutil.move(file_path, other_folder_path)

print("Vše je hotovo.")

