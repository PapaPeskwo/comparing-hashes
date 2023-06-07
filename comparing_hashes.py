import subprocess
import platform
import tkinter as tk
from tkinter import filedialog
from consolemenu import *
from consolemenu.items import *

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

def generate_sha512(filename):
    if platform.system() == "Windows":
        sha512 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA512"]).split()[-6]
    else:
        sha512 = subprocess.check_output(["sha512sum", filename]).split()[0]

    sha512 = sha512.decode("utf-8").rstrip()
    return sha512

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
    input("\nPress Enter to return to menu.")

def open_file_dialog(known_hash, hash_function):
    filename = filedialog.askopenfilename()
    compare_hashes(filename, known_hash, hash_function)

def hash_sha1():
    known_hash = input("\nEnter the known SHA-1 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha1)

def hash_sha256():
    known_hash = input("\nEnter the known SHA-256 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha256)

def hash_sha512():
    known_hash = input("\nEnter the known SHA-512 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha512)

# Create the menu
menu = ConsoleMenu("Hash Comparison", "Select a hash function")

# Create some items

item_sha1 = FunctionItem("SHA1", hash_sha1)
item_sha256 = FunctionItem("SHA256", hash_sha256)
item_sha512 = FunctionItem("SHA512", hash_sha512)

# Add the items to the menu
menu.append_item(item_sha1)
menu.append_item(item_sha256)
menu.append_item(item_sha512)

# Finally, show the menu
menu.show()
