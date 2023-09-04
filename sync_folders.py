import os
import shutil
import time
import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Folder synchronization program")
    parser.add_argument("source_folder", help="Source folder path")
    parser.add_argument("replica_folder", help="Replica folder path")
    parser.add_argument("sync_interval", type=int, help="Sync interval (seconds)")
    parser.add_argument("log_file", help="Log file path")
    args = parser.parse_args()

    source_folder = args.source_folder
    replica_folder = args.replica_folder
    sync_interval = args.sync_interval
    log_file = args.log_file

    while True:
        try:
            # Synchronize folders
            sync_folders(source_folder, replica_folder, log_file)

            # Wait for a while before syncing again
            time.sleep(sync_interval)
        except KeyboardInterrupt:
            print("Program stopped.")
            break


def sync_folders(source_folder, replica_folder, log_file):
    # Get lists of all files in source and replica folders
    source_files = set(os.listdir(source_folder))  #Use the set method for deduplication
    replica_files = set(os.listdir(replica_folder))

    # Find files to copy
    files_to_copy = source_files - replica_files

    # Find files to delete
    files_to_delete = replica_files - source_files

    # Copy files and log the actions
    for file in files_to_copy:
        src_path = os.path.join(source_folder, file)  #use join to build file path
        dest_path = os.path.join(replica_folder, file)
        shutil.copy(src_path, dest_path)
        log(f"Copied file: {file}", log_file)

    # Delete files and log the actions
    for file in files_to_delete:
        file_path = os.path.join(replica_folder, file)
        os.remove(file_path)
        log(f"Deleted file: {file}", log_file)


def log(message, log_file):
    # Log the message to the log file
    with open(log_file, "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

    # Print the message to the console
    print(message)


if __name__ == "__main__":
    main()
