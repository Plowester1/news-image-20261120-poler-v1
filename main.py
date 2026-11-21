import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path("/output/entry.png")

def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)

if __name__ == "__main__":
    main()
