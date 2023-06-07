# Comparing Hashes

Open source projects often provide SHA1, SHA256, or SHA512 hash values to compare with the program you're downloading. Comparing it manually is redundant, so this program was created to do that for you. It supports SHA1, SHA256, and SHA512 hash comparisons.

## How to use

```bash
python comparing_hashes.py
```

The program will prompt you to select the hash type (SHA1, SHA256, or SHA512) first. Then, enter the provided hash value (provided by the company, most likely next to the download link). Afterwards, a file explorer will open and you can select the downloaded file.

## Example

```bash
$ python comparing_hashes.py

Select a hash function:
1. SHA1
2. SHA256
3. SHA512
Enter choice: 2

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