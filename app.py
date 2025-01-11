import os
import sys
import platform
import ctypes

def is_windows():
    """
    Determine if the current operating system is Windows.

    Returns:
        bool: True if the operating system is Windows, False otherwise.
    """
    return sys.platform.startswith('win')


def is_unix():
    """
    Determine if the current operating system is Unix-based (Linux, macOS, etc.).

    Returns:
        bool: True if the operating system is Unix-based, False otherwise.
    """
    return os.name == 'posix'


def is_macos():
    """
    Determine if the current operating system is macOS.

    Returns:
        bool: True if the operating system is macOS, False otherwise.
    """
    return sys.platform == 'darwin'


def is_linux():
    """
    Determine if the current operating system is Linux.

    Returns:
        bool: True if the operating system is Linux, False otherwise.
    """
    return sys.platform.startswith('linux')


def is_admin():
    """
    Check if the current user has administrative privileges.

    - On Windows, checks for administrative rights.
    - On Unix-based systems (Linux, macOS, etc.), checks for superuser privileges.

    Returns:
        bool: True if the user has elevated privileges, False otherwise.
    """
    try:
        if is_windows():
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        elif is_unix():
            return os.geteuid() == 0
        else:
            print("Unsupported platform for privilege check.")
    except AttributeError:
        print("Error: Required functions not available on this platform.")
    except Exception as e:
        print(f"Unexpected error during privilege check: {e}")
    
    return False


def get_os_info():
    """
    Retrieve basic operating system information.

    Returns:
        dict: A dictionary containing OS name, version, and architecture.
    """
    return {
        "OS Name": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
    }


if __name__ == "__main__":
    os_info = get_os_info()
    print("Operating System Information:")
    for key, value in os_info.items():
        print(f"  {key}: {value}")
    
    if is_admin():
        print("You have elevated (administrative/superuser) privileges.")
    else:
        print("You do NOT have elevated privileges.")
