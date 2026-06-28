import zipfile
import os

zip_path = "Addadshashanammu.zip"
extract_dir = "Addadshashanammu"

with zipfile.ZipFile(zip_path, 'r') as zf:
    zf.extractall(extract_dir)

for root, dirs, files in os.walk(extract_dir):
    for name in files:
        path = os.path.join(root, name)
        if "." not in name:
            with open(path, "rb") as f:
                data = f.read()
            try:
                text = data.decode('utf-8', errors='ignore')
                if 'picoCTF{' in text:
                    print(f"Flag found in {path}:")
                    start = text.index('picoCTF{')
                    end = text.index('}', start) + 1
                    print(text[start:end])
            except Exception:
                continue
