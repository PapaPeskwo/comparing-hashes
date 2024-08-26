import subprocess
import platform
import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def generate_sha1(filename):
    if platform.system() == "Windows":
        sha1 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA1"]).split()[-6]
    else:
        sha1 = subprocess.check_output(["sha1sum", filename]).split()[0]
    sha1 = sha1.decode("utf-8").rstrip()
    return sha1

def generate_sha224(filename):
    if platform.system() == "Windows":
        sha224 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA224"]).split()[-6]
    else:
        sha224 = subprocess.check_output(["sha224sum", filename]).split()[0]
    sha224 = sha224.decode("utf-8").rstrip()
    return sha224

def generate_sha256(filename):
    if platform.system() == "Windows":
        sha256 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA256"]).split()[-6]
    else:
        sha256 = subprocess.check_output(["sha256sum", filename]).split()[0]
    sha256 = sha256.decode("utf-8").rstrip()
    return sha256

def generate_sha384(filename):
    if platform.system() == "Windows":
        sha384 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA384"]).split()[-6]
    else:
        sha384 = subprocess.check_output(["sha384sum", filename]).split()[0]
    sha384 = sha384.decode("utf-8").rstrip()
    return sha384

def generate_sha512(filename):
    if platform.system() == "Windows":
        sha512 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA512"]).split()[-6]
    else:
        sha512 = subprocess.check_output(["sha512sum", filename]).split()[0]
    sha512 = sha512.decode("utf-8").rstrip()
    return sha512

def generate_md5(filename):
    if platform.system() == "Windows":import subprocess
    import platform
    import os
    import time
    from rich.console import Console
    from rich.panel import Panel
    
    console = Console()
    
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
    
    def generate_md5(filename):
        if platform.system() == "Windows":
            md5 = subprocess.check_output(["certutil", "-hashfile", filename, "MD5"]).split()[-6]
        else:
            md5 = subprocess.check_output(["md5sum", filename]).split()[0]
        md5 = md5.decode("utf-8").rstrip()
        return md5
    
    def compare_hashes(filename, known_hash, hash_function):
        file_hash = hash_function(filename)
        known_hash_panel = Panel(f"[bold]Known hash value:[/bold] {known_hash}", border_style="bold green")
        file_hash_panel = Panel(f"[bold]File hash value:[/bold] {file_hash}", border_style="bold green")
        console.print(known_hash_panel)
        console.print(file_hash_panel)
        if file_hash == known_hash:
            result_panel = Panel(f"The file: \n{filename} \nis authentic.", title="Result", border_style="bold green")
        else:
            result_panel = Panel(f"THE FILE: \n{filename} \nMAY HAVE BEEN TAMPERED WITH.", title="Result", border_style="bold red")
        console.print(result_panel)
        input("\nPress Enter to return to menu.")
    
    def open_file_dialog(known_hash, hash_function):
        filename = input("\nEnter the path to the file:\n").strip()
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
    
    def hash_md5():
        known_hash = input("\nEnter the known MD5 hash value:\n").lower().strip()
        open_file_dialog(known_hash, generate_md5)
    
    # Menu
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu_text = """
        Hash Comparison
        Select a hash function
        1. MD5
        2. SHA1
        3. SHA256
        4. SHA512
        5. Exit
        """
        console.print(Panel(menu_text, title="Menu", border_style="bold green"))
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            hash_md5()
        elif choice == '2':
            hash_sha1()
        elif choice == '3':
            hash_sha256()
        elif choice == '4':
            hash_sha512()
        elif choice == '5':
            print("Exiting.")
            break
        else:
            error_panel = Panel("Invalid choice. Please enter a number between 1 and 5.", border_style="bold red")
            console.print(error_panel)
            time.sleep(2)
        md5 = subprocess.check_output(["certutil", "-hashfile", filename, "MD5"]).split()[-6]
    else:
        md5 = subprocess.check_output(["md5sum", filename]).split()[0]
    md5 = md5.decode("utf-8").rstrip()
    return md5

def compare_hashes(filename, known_hash, hash_function):
    file_hash = hash_function(filename)
    known_hash_panel = Panel(f"[bold]Known hash value:[/bold] {known_hash}", border_style="bold green")
    file_hash_panel = Panel(f"[bold]File hash value:[/bold] {file_hash}", border_style="bold green")
    console.print(known_hash_panel)
    console.print(file_hash_panel)
    if file_hash == known_hash:
        result_panel = Panel(f"The file: \n{filename} \nis authentic.", title="Result", border_style="bold green")
    else:
        result_panel = Panel(f"THE FILE: \n{filename} \nMAY HAVE BEEN TAMPERED WITH.", title="Result", border_style="bold red")
    console.print(result_panel)
    input("\nPress Enter to return to menu.")

def open_file_dialog(known_hash, hash_function):
    filename = input("\nEnter the path to the file:\n").strip()
    compare_hashes(filename, known_hash, hash_function)

def hash_sha1():
    known_hash = input("\nEnter the known SHA-1 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha1)

def hash_sha224():
    known_hash = input("\nEnter the known SHA-224 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha224)

def hash_sha256():
    known_hash = input("\nEnter the known SHA-256 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha256)

def hash_sha384():
    known_hash = input("\nEnter the known SHA-384 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha384)

def hash_sha512():
    known_hash = input("\nEnter the known SHA-512 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_sha512)

def hash_md5():
    known_hash = input("\nEnter the known MD5 hash value:\n").lower().strip()
    open_file_dialog(known_hash, generate_md5)

# Menu
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_text = """
    Hash Comparison
    Select a hash function
    1. MD5
    2. SHA1
    3. SHA224
    4. SHA256
    5. SHA384
    6. SHA512
    7. Exit
    """
    console.print(Panel(menu_text, title="Menu", border_style="bold green"))
    choice = input("\nEnter your choice (1-7): ")
    if choice == '1':
        hash_md5()
    elif choice == '2':
        hash_sha1()
    elif choice == '3':
        hash_sha224()
    elif choice == '4':
        hash_sha256()
    elif choice == '5':
        hash_sha384()
    elif choice == '6':
        hash_sha512()
    elif choice == '7':
        print("Exiting.")
        break
    else:
        error_panel = Panel("Invalid choice. Please enter a number between 1 and 7.", border_style="bold red")
        console.print(error_panel)
        time.sleep(2)