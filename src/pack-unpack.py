import os
import subprocess
import sys

def pack_pe_files(directory, upx_path="upx"):
    """
    Pack all PE files in a directory using UPX.
    
    Args:
        directory (str): The path to the directory containing PE files.
        upx_path (str): Path to the UPX executable (default assumes it's in PATH).
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_pe_file(file_path):
                print(f"Packing {file_path}...")
                try:
                    subprocess.run([upx_path, "-9", file_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Failed to pack {file_path}: {e}")
                except FileNotFoundError:
                    print("Error: UPX is not installed or not found in PATH.")
                    sys.exit(1)

def is_pe_file(file_path):
    """
    Check if a file is a PE file by reading its magic number.
    
    Args:
        file_path (str): Path to the file to check.

    Returns:
        bool: True if the file is a PE file, False otherwise.
    """
    try:
        with open(file_path, "rb") as f:
            magic = f.read(2)
        return magic == b"MZ"  # PE files start with the "MZ" signature
    except Exception as e:
        print(f"Error checking file {file_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pack_pe_files.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    pack_pe_files(directory)
