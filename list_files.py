import os

def list_files(dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            full_path = os.path.join(dir_path, filename)
            print(full_path)

if __name__ == "__main__":
    start_dir = input("Enter the dir path to scan: ")
    if not os.path.exists(start_dir):
        print(f"path '{start_dir}' does not exist.")
    else:
        print(f"Listing all files under: {start_dir}\n")
        list_files(start_dir)
      
