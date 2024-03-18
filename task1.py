import os
import shutil
import sys

def copy_files(src, dest, file_extension_map = {}):
        for item in os.listdir(src):
            item_path = os.path.join(src, item)

            if os.path.isdir(item_path):
                copy_files(item_path, dest, file_extension_map)
            else:
                file_extension = os.path.splitext(item)[1]

                if file_extension not in file_extension_map:
                    file_extension_map[file_extension] = os.path.join(dest, file_extension[1:])
                    os.makedirs(file_extension_map[file_extension], exist_ok=True)
            
                shutil.copy(item_path, file_extension_map[file_extension])

def main():
    try:
        src_dir = sys.argv[1]
        dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        copy_files(src_dir, dest_dir)
    except IndexError:
        print("Usage example: python task1.py <source dir path> [destination dir path]")
    except PermissionError as perm_err:
        print(f"Not enough permissions: {perm_err}")
    except FileNotFoundError as fnf_err:
        print(f"File/folder not found: {fnf_err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()