import os, time
import shutil
import subprocess
import sys
import lzma

def is_pe_file(file_path) -> bool:
    try:
        with open(file_path, "rb") as f:
            magic = f.read(2)
        return magic == b"MZ"  # PE files start with the "MZ" signature
    except Exception as e:
        print(f"Error checking file {file_path}: {e}")
        return False

def pack_with_upx(directory, upx_path="upx") -> bool:
    output_dir = os.path.dirname(directory) + "_upx/"
    print(f"Files will save into: {output_dir}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_pe_file(file_path):
                # Determine relative path for saving in the output directory
                relative_path = os.path.relpath(file_path, directory)
                packed_file_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output subdirectories exist
                os.makedirs(os.path.dirname(packed_file_path), exist_ok=True)

                # Copy the original file to the output directory
                shutil.copy2(file_path, packed_file_path)

                print(f"Packing {packed_file_path}...")
                try:
                    subprocess.run([upx_path, "-9", "--force", packed_file_path], check=True)
                    print(f"Files saved into: {output_dir}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to pack {packed_file_path}: {e}")
                    return False
                except FileNotFoundError:
                    print("Error: UPX is not installed or not found in PATH.")
                    sys.exit(1)
    return True

def pack_with_mpress(directory, mpress_path="mpress") -> bool:
    output_dir = os.path.dirname(directory) + "_mpress/"
    print(f"Files will save into: {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_pe_file(file_path):
                # Determine relative path for saving in the output directory
                relative_path = os.path.relpath(file_path, directory)
                packed_file_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output subdirectories exist
                os.makedirs(os.path.dirname(packed_file_path), exist_ok=True)

                # Copy the original file to the output directory
                shutil.copy2(file_path, packed_file_path)

                print(f"Packing {packed_file_path}...")
                try:
                    subprocess.run(["wine", mpress_path, packed_file_path], check=True)
                    print(f"Files saved into: {output_dir}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to pack {packed_file_path}: {e}")
                    return False
                except FileNotFoundError:
                    print("Error: MPRESS is not installed or not found in PATH.")
                    sys.exit(1)
    return True

def pack_with_pecompact(directory, pecompact_path="pecompact") -> bool:
    output_dir = os.path.dirname(directory) + "_pecompact/"
    print(f"Files will save into: {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_pe_file(file_path):
                # Determine relative path for saving in the output directory
                relative_path = os.path.relpath(file_path, directory)
                packed_file_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output subdirectories exist
                os.makedirs(os.path.dirname(packed_file_path), exist_ok=True)

                # Copy the original file to the output directory
                shutil.copy2(file_path, packed_file_path)

                print(f"Packing {packed_file_path}...")
                try:
                    subprocess.run(["wine", pecompact_path, packed_file_path], check=True)
                    print(f"Files saved into: {output_dir}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to pack {packed_file_path}: {e}")
                    return False
                except FileNotFoundError:
                    print("Error: PECompact is not installed or not found in PATH.")
                    sys.exit(1)
    return True

def pack_with_molebox(directory, molebox_path="molebox") -> bool:
    output_dir = os.path.dirname(directory) + "_molebox/"
    print(f"Files will save into: {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_pe_file(file_path):
                # Determine relative path for saving in the output directory
                relative_path = os.path.relpath(file_path, directory)
                packed_file_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output subdirectories exist
                os.makedirs(os.path.dirname(packed_file_path), exist_ok=True)

                # Copy the original file to the output directory
                shutil.copy2(file_path, packed_file_path)

                print(f"Packing {packed_file_path}...")
                try:
                    subprocess.run(["wine", molebox_path, packed_file_path], check=True)
                    print(f"Files saved into: {output_dir}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to pack {packed_file_path}: {e}")
                    return False
                except FileNotFoundError:
                    print("Error: PECompact is not installed or not found in PATH.")
                    sys.exit(1)
    return True

def pack_with_petite(directory, petite_path="petite") -> bool:
    output_dir = os.path.dirname(directory) + "_petite/"
    print(f"Files will save into: {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_pe_file(file_path):
                # Determine relative path for saving in the output directory
                relative_path = os.path.relpath(file_path, directory)
                packed_file_path = os.path.join(output_dir, relative_path)
                
                # Ensure the output subdirectories exist
                os.makedirs(os.path.dirname(packed_file_path), exist_ok=True)

                # Copy the original file to the output directory
                shutil.copy2(file_path, packed_file_path)

                print(f"Packing {packed_file_path}...")
                try:
                    subprocess.run(["wine", petite_path, packed_file_path], check=True)
                    print(f"Files saved into: {output_dir}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to pack {packed_file_path}: {e}")
                    return False
                except FileNotFoundError:
                    print("Error: PECompact is not installed or not found in PATH.")
                    sys.exit(1)
    return True

def main(binary_dir):
    print("----------PACKER----------START----------")
    #pack_with_upx(binary_dir)
    #pack_with_mpress(binary_dir)
    #pack_with_pecompact(binary_dir)
    #pack_with_molebox(binary_dir)
    #pack_with_petite(binary_dir)
    print("----------PACKER---------- END ----------")

if __name__ == "__main__":
    print("[" + __file__ + "]'s last modified: %s" % time.ctime(os.path.getmtime(__file__)))
    # Check if a parameter is provided
    if len(sys.argv) == 2:
        in_dir = sys.argv[1]
        if not os.path.exists(in_dir):
            print(f"Directory: '{in_dir}' does not exist.")
            exit()
        print(f"\n\nBinary Directory:\t\t{in_dir}")
        main(in_dir)
    else:
        print("No input directory provided.")
        print("Usage: python pack-unpack.py <directory>")