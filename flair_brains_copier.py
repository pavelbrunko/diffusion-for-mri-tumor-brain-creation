import os
import shutil

def copy_flair_files(source_dir, target_dir):
    # Проходим по всем поддиректориям исходной директории
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Если в названии файла есть "flair"
            if "flair" in file:
                # Получаем полный путь к файлу
                source_file = os.path.join(root, file)
                # Копируем файл в целевую директорию
                shutil.copy(source_file, target_dir)
                print(f"Копирование файла {source_file} в {target_dir}")

# Пример использования
source_directory = "/Users/pavel/Desktop/archive/BraTS2020_ValidationData/MICCAI_BraTS2020_ValidationData"
target_directory = "/Users/pavel/Desktop/flair_brains"
copy_flair_files(source_directory, target_directory)
