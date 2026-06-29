import re

file_path = "file"

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

clean = re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', content)

match = re.search(r'picoCTF\{[^}]+\}', clean)
if match:
    print("Flag found:", match.group(0))
else:
    print("Flag not found.")
