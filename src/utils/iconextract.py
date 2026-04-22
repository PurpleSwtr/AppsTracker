import icoextract
from pathlib import Path
# import sys

def save_icon(filepath: Path, output_path: Path) -> bool:
    try:
        name = filepath.stem
        icon_output_path = Path(output_path) / f"{name}.ico"
        extractor = icoextract.IconExtractor(filepath)
        extractor.export_icon(icon_output_path)
        return True
    except Exception as e:
        print(e)
        return False

# if __name__ == "__main__":
#     exe_path = sys.argv[1]
#     out_path = sys.argv[2]

#     save_icon(exe_path, out_path)