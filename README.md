## Description
Open source projects usually provide a SHA256 hash value to compare to the program you're downloading. Comparing it manually is redundant, so this program was created to do that for you.
## How to use
```
py src/comparing_hashes.py
```
Copy the path to the downloaded file, don't extract it yet.
Copy the provided SHA-256 hash value (provided by the comapny, most likely next to the download link)

## Example
```
$ py src/comparing_hashes.py
Enter the path to the filename:
C:\Users\user\Downloads\prometheus-2.43.0.windows-amd64.zip
Enter the known SHA-256 hash value:
98e9feb991293b7ee5ccd5561604db1dc7c4b532546ecce7180fd80b7459aa5e

Known SHA-256 hash value: 98e9feb991293b7ee5ccd5561604db1dc7c4b532546ecce7180fd80b7459aa5e
File SHA-256 hash value: 98e9feb991293b7ee5ccd5561604db1dc7c4b532546ecce7180fd80b7459aa5e

+==================================================================================================+
The file C:\Users\DELLi-Tomi\Downloads\prometheus-2.43.0.windows-amd64.zip is authentic.
+==================================================================================================+

```
