import os
import shutil

def os_file_manager():
    while True:
        dir_path = input("Enter directory path: ").strip()

        if not os.path.isdir(dir_path):
            print("directory not found.")
            continue

        backup_path = os.path.join(dir_path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        copied_count = 0
        for filename in os.listdir(dir_path):
            if filename.endswith(".txt"):
                src = os.path.join(dir_path, filename)
                dst = os.path.join(backup_path, filename)
                shutil.copy2(src, dst)
                copied_count += 1

        print(f"Backup complete. {copied_count} .txt files copied to '{backup_path}")
        break
