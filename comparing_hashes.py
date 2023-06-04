import subprocess
import platform
import tkinter as tk
from tkinter import filedialog

def generate_sha1(filename):
    if platform.system() == "Windows":
        sha1 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA1"]).split()[-6]
    else:
        sha1 = subprocess.check_output(["sha1sum", filename]).split()[0]

    sha1 = sha1.decode("utf-8").rstrip()
    return sha1

def generate_sha256(filename):
    if platform.system() == "Windows":
        sha256 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA256"]).split()[-6]
    else:
        sha256 = subprocess.check_output(["sha256sum", filename]).split()[0]

    sha256 = sha256.decode("utf-8").rstrip()
    return sha256

def compare_hashes(filename, known_hash, hash_function):
    file_hash = hash_function(filename)
    print(f"\nKnown hash value: {known_hash}")
    print(f"File hash value: {file_hash}")
    if file_hash == known_hash:
        print()
        print('+' + '=' * 98 + '+')
        print(f"The file: \n{filename} \nis authentic.")
        print('+' + '=' * 98 + '+')
    else:
        print()
        print('!!!' + '=' * 94 + '!!!')
        print(f"THE FILE: \n{filename} \nMAY HAVE BEEN TAMPERED WITH.")
        print('!!!' + '=' * 94 + '!!!')

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

print("\n---Select your file when the file explorer opens---")
hash_type = int(input("\nEnter the type of hash (1)SHA1 or (2)SHA256):\n"))
known_hash = input("\nEnter the known hash value:\n").lower().strip()
filename = open_file_dialog()

if hash_type == 1:
    compare_hashes(filename, known_hash, generate_sha1)
elif hash_type == 2:
    compare_hashes(filename, known_hash, generate_sha256)
else:
    print("Invalid hash type. Please select SHA1 or SHA256.")
