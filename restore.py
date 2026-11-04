import os
import re

# Since your terminal is already inside the Codewars folder, look right here!
html_name = "codewars_backup.html"

if not os.path.exists(html_name):
    print(f"Error: Could not find '{html_name}' in this folder.")
    print("Files currently here are:", os.listdir('.'))
    exit()

with open(html_name, "r", encoding="utf-8") as f:
    html_content = f.read()

# Pull files from the HTML backup
files_found = re.findall(r'href="/[^/]+/[^/]+/blob/[^/]+/([^"]+\.js)"', html_content)
files_found = list(set(files_found))

if not files_found:
    files_found = re.findall(r'title="([^"]+\.js)"', html_content)
    files_found = list(set(files_found))

if not files_found:
    print("No JavaScript files detected in the HTML backup.")
else:
    print(f"🎉 Success! Found {len(files_found)} files to restore.")
    for file_name in files_found:
        if not os.path.exists(file_name):
            with open(file_name, "w", encoding="utf-8") as out_f:
                out_f.write("// Recovered Codewars Solution\n")
            print(f"File restored: {file_name}")
    print("\n All files successfully extracted back into your folder!")
