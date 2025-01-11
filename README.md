# has-super-access

**has-super-access** is a Python project designed to determine the current operating system and check whether the user has administrative or superuser privileges. It provides easy-to-use functions for checking platform details and user access rights across different operating systems, including Windows, Linux, macOS, and Unix-based systems.

## Features

- Detects the current operating system (Windows, Linux, macOS, or Unix).
- Checks if the user has administrative or superuser privileges.
- Displays detailed information about the operating system including name, version, release, and architecture.
- Cross-platform compatibility (Windows, Linux, macOS).

## Requirements

- Python 3.x
- `platform`, `os`, `sys`, and `ctypes` standard Python libraries

## Installation

To get started with the project, clone the repository:

```bash
git clone https://github.com/BaseMax/has-super-access.git
cd has-super-access
```

Ensure you have Python 3.x installed. You can install Python from [here](https://www.python.org/downloads/).

## Usage

To run the script and check your system information and administrative privileges, execute the following command in your terminal or command prompt:

```bash
python app.py
```

### Example Output

#### On Windows (with elevated privileges):

```
Operating System Information:
  OS Name: Windows
  OS Version: 10.0.26100
  OS Release: 11
  Architecture: 64bit

You have elevated (administrative/superuser) privileges.
```

#### On Windows (without elevated privileges):

```
Operating System Information:
  OS Name: Windows
  OS Version: 10.0.26100
  OS Release: 11
  Architecture: 64bit

You do NOT have elevated privileges.
```

## Functions

- `detect_platform()`: Detects the current platform and returns a string representing the operating system.
- `has_admin_privileges()`: Checks if the current user has administrative or superuser privileges.
- `get_os_info()`: Retrieves detailed operating system information (name, version, release, architecture).
- `print_system_info()`: Prints the operating system information in a readable format.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Contributions are welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

MIT License

(c) Copyright 2025, Max Base
