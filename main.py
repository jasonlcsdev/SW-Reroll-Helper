import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed


def execute_adb_command(command, device_id):
    """Execute an ADB command on a specific device."""
    try:
        full_command = ["adb", "-s", device_id] + command
        subprocess.run(full_command, capture_output=True, text=True, check=True)
        print(f"Command executed successfully on {device_id}.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command on {device_id}:")
        print(e.stderr)


def get_device_ids():
    """Retrieve the IDs of connected Android devices."""
    try:
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)
        devices = result.stdout.splitlines()[1:]
        device_ids = [line.split()[0] for line in devices if line.strip()]
        return device_ids
    except subprocess.CalledProcessError as e:
        print("Error getting device IDs:")
        print(e.stderr)
        return []


def rename_folder(device_id, old_path, new_path):
    """Rename a folder on the device."""
    execute_adb_command(["shell", "mv", old_path, new_path], device_id)


def clear_app_data(device_id, package_name):
    """Clear the data of a specific app on the device."""
    execute_adb_command(["shell", "pm", "clear", package_name], device_id)


def process_device(device_id):
    """Process the device by renaming folders and clearing app data."""
    # Paths of the folders
    original_folder_path = "/storage/emulated/0/Android/data/com.com2us.smon.android.huawei.global.normal.huawei"
    temporary_folder_path = "/storage/emulated/0/Android/data/com.com2us.smon.android.huawei.global.normal.huawei1"

    # Package name of the Huawei Summoners War application
    package_name = "com.com2us.smon.android.huawei.global.normal.huawei"

    # Step 1: Rename the folder
    print(f"Renaming folder on {device_id}...")
    rename_folder(device_id, original_folder_path, temporary_folder_path)

    # Step 2: Clear the app data
    print(f"Clearing app data on {device_id}...")
    clear_app_data(device_id, package_name)

    # Step 3: Rename the folder back to its original name to restore
    print(f"Renaming folder back to its original name on {device_id}...")
    rename_folder(device_id, temporary_folder_path, original_folder_path)


def main():
    """Main function to process all connected devices."""
    devices = get_device_ids()

    with ThreadPoolExecutor(max_workers=len(devices)) as executor:
        futures = [executor.submit(process_device, device_id) for device_id in devices]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing a device: {e}")


if __name__ == "__main__":
    main()
