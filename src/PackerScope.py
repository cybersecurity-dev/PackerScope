import os
import csv
import subprocess
import sys
import hashlib
import time
import pandas as pd


def get_sha256_hash(full_file_path):
    sha256_hash = hashlib.sha256()
    with open(full_file_path, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def csv_to_pkl(csv_file, pkl_file):
    df = pd.read_csv(csv_file)
    df.to_pickle(pkl_file)

def analyze_executables(input_folder, output_csv):
    # Create a list to store the results
    results = []

    # Iterate through each file in the folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        print(file_path)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            try:
                # Run the diec command on the file
                command = f'diec -rd --heuristicscan --verbose "{file_path}"'
                output = subprocess.run(command, shell=True, capture_output=True, text=True)

                # Parse the output to determine if the file is packed and identify the packer used
                packed_status = 'Not Packed'
                packer_name = 'None'
                if 'packer' in output.stdout.lower():
                    packed_status = 'Packed'
                    packer_name = output.stdout.split('Packer:')[1].split('\n')[0].strip()
                file_sha256_hash = get_sha256_hash(file_path)
                # Append the results (SHA256 File Checksum, filename, packed status, packer name) to the list
                results.append([file_sha256_hash, filename, packed_status, packer_name])
            
            except Exception as e:
                # In case of an error, append the filename with an error message
                results.append([filename, 'Error', str(e)])

    # Save the results to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SHA256', 'Filename', 'Packed Status', 'Packer Name'])
        writer.writerows(results)

    print(f'Results saved to {output_csv}')

def main(input_folder, output_csv, output_pkl):
    analyze_executables(input_folder, output_csv)
    csv_to_pkl(output_csv, output_pkl)


if __name__ == "__main__":
    print("[" + __file__ + "]'s last modified: %s" % time.ctime(os.path.getmtime(__file__)))
    # Check if a parameter is provided
    if len(sys.argv) == 4:
        in_dir = sys.argv[1]
        print(f"\n\nBinary Directory:\t\t{in_dir}")

        output_csv = sys.argv[2]
        print(f"CSV file will save:\t\t{output_csv}")

        output_pkl = sys.argv[3]
        print(f"PKL file will save:\t\t{output_pkl}")

        main(in_dir, output_csv, output_pkl)
    else:
        print("Usage: python3 PackerScope.py <input_folder> <output_csv> <output_pkl>")
        print("No input directory and/or output csv file, pkl file name provided.")
