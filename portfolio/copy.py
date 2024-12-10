import os
from pathlib import Path
import shutil
import datetime

os.chdir(Path(__file__).parent)
SaveData = Path("../ドキュメント/PPSSPP/PSP/SAVEDATA")
BucKUpFolder = Path("../../仮置き/BuckUp")
dt = datetime.datetime.now()

ThisMonth = dt.strftime("%Y-%m")
ToDay = dt.strftime("%m-%d")

# for file in SaveData.glob('ULJM*'):

def copy_folder():
    if not SaveData.exists:
        print(f"Error:{SaveData}フォルダが見つかりません")
    else:
        destination_folder = BucKUpFolder/ThisMonth/ToDay
        os.makedirs(destination_folder,exist_ok=True)

        counter = 1
        while True:
            number_folder = destination_folder/str(counter)
            if not number_folder.exists():
                os.makedirs(number_folder)
                break
            counter += 1

        for item in SaveData.glob('ULJM*'):
            if item.is_dir():
                buckup_path = number_folder/item.name
                shutil.copytree(item,buckup_path)

def main():
    copy_folder()

if __name__ == "__main__":
    main()

