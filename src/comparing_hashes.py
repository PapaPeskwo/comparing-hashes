import subprocess, os, platform

#os.system('cls' if os.name == 'nt' else 'clear') 

def generate_sha256(filename):
    if platform.system() != 'Windows':
        # Generate SHA-256 hash value of file using certutil command
        sha256 = subprocess.check_output(["sha256sum", filename]).split()[0]
        # Remove the newline character from the end of the hash value
        sha256 = sha256.decode("utf-8").rstrip()
        # Return the SHA-256 hash value as a string
        return sha256
    else:
        # Generate SHA-256 hash value of file using certutil command
        sha256 = subprocess.check_output(["certutil", "-hashfile", filename, "SHA256"]).split()[4]
        # Remove the newline character from the end of the hash value
        sha256 = sha256.decode("utf-8").rstrip()
        # Return the SHA-256 hash value as a string
        return sha256

def compare_hashes(filename, known_sha256):
    # Generate SHA-256 hash value of file using certutil command
    file_sha256 = generate_sha256(filename)
    # Print the known and file hash values
    print(f"\nKnown SHA-256 hash value: {known_sha256}")
    print(f"File SHA-256 hash value: {file_sha256}")
    if file_sha256 == known_sha256:
        print()
        print('+' + '=' * 98 + '+')
        print(f"The file {filename} is authentic.")
        print('+' + '=' * 98 + '+')
    else:
        print()
        print('!!!' + '=' * 94 + '!!!')
        print(f"THE FILE {filename} MAY HAVE BEEN TAMPERED WITH.")
        print('!!!' + '=' * 94 + '!!!')

# Take input from user for the file name and known SHA-256 hash value
filename = input("Enter the path to the filename:\n")
known_sha256 = input("Enter the known SHA-256 hash value:\n")

# Call the compare_hashes function with the user inputs
compare_hashes(filename, known_sha256)
