import os
import sys
import platform
import ctypes
from typing import Dict


def detect_platform() -> str:
    """
    Detect the current platform and return it as a string.

    Returns:
        str: One of 'Windows', 'Linux', 'macOS', 'Unix', or 'Unknown'.
    """
    if sys.platform.startswith('win'):
        return 'Windows'
    elif sys.platform.startswith('linux'):
        return 'Linux'
    elif sys.platform == 'darwin':
        return 'macOS'
    elif os.name == 'posix':
        return 'Unix'
    return 'Unknown'


def has_admin_privileges() -> bool:
    """
    Check if the current user has administrative privileges.

    Returns:
        bool: True if the user has elevated privileges, False otherwise.
    """
    platform_name: str = detect_platform()
    try:
        if platform_name == 'Windows':
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        elif platform_name in ['Linux', 'macOS', 'Unix']:
            return os.geteuid() == 0
        else:
            print(f"Unsupported platform: {platform_name}")
    except AttributeError:
        print("Error: Required functionality not available on this platform.")
    except Exception as e:
        print(f"Unexpected error during privilege check: {e}")
    
    return False


def get_os_info() -> Dict[str, str]:
    """
    Retrieve detailed operating system information.

    Returns:
        Dict[str, str]: A dictionary containing the OS name, version, release, and architecture.
    """
    return {
        "OS Name": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.architecture()[0],
    }


def print_system_info() -> None:
    """
    Print detailed operating system information to the console.
    """
    os_info: Dict[str, str] = get_os_info()
    print("Operating System Information:")
    for key, value in os_info.items():
        print(f"  {key}: {value}")


def main() -> None:
    """
    Main function to run the privilege check and print system information.
    """
    print_system_info()

    if has_admin_privileges():
        print("\nYou have elevated (administrative/superuser) privileges.")
    else:
        print("\nYou do NOT have elevated privileges.")


if __name__ == "__main__":
    main()
