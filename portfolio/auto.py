from pathlib import Path
import datetime
import os

os.chdir(Path(__file__).parent)
folder = Path("../../仮置き/BuckUp")
dt = datetime.datetime.now()

year = dt.strftime("%Y")
month = dt.strftime("%m")
day = dt.strftime("%d")

ThisMonth = dt.strftime("%Y-%m")
ToDay = dt.strftime("%m-%d")

def check_folder(fol):
    if not fol.exists():
        print(f"フォルダ'{fol}'が存在しません")
        return False
    
    month_folder = fol/ThisMonth
    if not month_folder.exists():
        os.makedirs(month_folder,exist_ok=True)

    day_folder = month_folder/ToDay
    if not day_folder.exists():
        os.makedirs(day_folder,exist_ok=True)

def main():
    check_folder(folder)

if __name__ == "__main__":
    main()