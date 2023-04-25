import subprocess, platform
import tkinter as tk
from tkinter import filedialog

def generate_sha256(filename):
    if platform.system() == "Windows":
        sha256 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA256"]).split()[-6]
    else:
        sha256 = subprocess.check_output(["sha256sum", filename]).split()[0]

    sha256 = sha256.decode("utf-8").rstrip()
    return sha256

def compare_hashes(filename, known_sha256):
    file_sha256 = generate_sha256(filename)
    print(f"\nKnown SHA-256 hash value: {known_sha256}")
    print(f"File SHA-256 hash value: {file_sha256}")
    if file_sha256 == known_sha256:
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
known_sha256 = input("\nEnter the known SHA-256 hash value:\n").lower().strip()
filename = open_file_dialog()

compare_hashes(filename, known_sha256)
