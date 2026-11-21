import hashlib
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path("/output/entry.png")

def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_hash = hashlib.sha256(SRC.read_bytes()).hexdigest()
    dst_hash = hashlib.sha256(DST.read_bytes()).hexdigest()
    if src_hash != dst_hash:
        raise RuntimeError("copy mismatch")

if __name__ == "__main__":
    main()
