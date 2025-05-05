# Reset Summoners War

This script automates the process of resetting a Summoners War account while keeping the game updates intact. It is particularly useful for farming rerolls during events like the 11th Anniversary. The script uses ADB (Android Debug Bridge) to manage multiple devices simultaneously.

## Features

- Retrieve IDs of connected Android devices.
- Rename folders on the device.
- Clear app data for a specific package.
- Process multiple devices concurrently using multi-threading.

## Requirements

- Python 3.x
- [ADB (Android Debug Bridge)](https://developer.android.com/studio/releases/platform-tools) installed and added to the system PATH.
- Android devices

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/android-device-manager.git
    cd android-device-manager
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install ADB:
    - Download the [ADB platform tools](https://developer.android.com/studio/releases/platform-tools).
    - Extract the downloaded file.
    - Add the extracted folder to your system PATH.

## Usage

1. Ensure your Android devices are connected.
2. Run the script:
    ```sh
    python main.py
    ```

The script will:
1. Retrieve the IDs of all connected Android devices.
2. For each device, rename the specified folder.
3. Clear the app data for the specified package.
4. Rename the folder back to its original name.

## Configuration

You can modify the following variables in the `main.py` file to suit your needs:

- `original_folder_path`: The path of the folder to rename.
- `temporary_folder_path`: The temporary path to rename the folder to.
- `package_name`: The package name of the app whose data you want to clear.

## Note
I use Summoners War installed from the Huawei App Gallery. This allows skipping the first tutorial battle.

This script has been tested with LDPlayer, an Android emulator. Ensure that LDPlayer is configured to allow ADB access.
