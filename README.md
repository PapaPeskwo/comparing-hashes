## Description
Open source projects usually provide a SHA256 hash value to compare to the program you're downloading. Comparing it manually is redundant, so this program was created to do that for you. With the updated script, a file explorer will open to select the file instead of manually entering the path. Only supports Windows 10 at the moment. 

## How to use
```bash
py comparing_hashes.py
```

Enter the provided SHA-256 hash value (provided by the company, most likely next to the download link). Afterwards, file explorer will open and you can select the downloaded file.

## Example
```bash
$ py comparing_hashes.py

---Select your file when the file explorer opens---
Enter the known SHA-256 hash value:
98e9feb991293b7ee5ccd5561604db1dc7c4b532546ecce7180fd80b7459aa5e

(File explorer opens, and user selects the file)

Known SHA-256 hash value: 98e9feb991293b7ee5ccd5561604db1dc7c4b532546ecce7180fd80b7459aa5e
File SHA-256 hash value: 98e9feb991293b7ee5ccd5561604db1dc7c4b532546ecce7180fd80b7459aa5e

+==================================================================================================+
The file:
C:\Users\<user>\Downloads\prometheus-2.43.0.windows-amd64.zip
is authentic.
+==================================================================================================+
```