# FTP File Transfer Program

## Overview

The FTP File Transfer program is designed to automate the transfer of files between a remote FTP server and local/internal network directories. It includes features for scheduling tasks, logging, and reading configuration parameters from a `config.ini` file.

## Files

### `main.py`

The main script for scheduling and running daily reports.

### `config_reader.py`

A class for reading and validating configuration parameters from a `config.ini` file.

### `ftp_file_transfer.py`

#### Class: `FTPFileTransfer`

FTPFileTransfer facilitates the transfer of files between a remote FTP server and local/internal network directories.

## Requirements

- Python 3.6 or higher
- Required Python packages can be installed using `pip install -r requirements.txt`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/FTP-File-Transfer-Program.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FTP-File-Transfer-Program
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Explore Configuration Below
   Update the config.ini adding the parameters required
5. Run the application:

   ```bash
   python main.py
   ```
6.Check the `ftp_transfer_logger.log` file for program logs and any potential issues.

## Configuration:
   - Ensure that the config.ini file includes all the mandatory parameters (ftp_host, ftp_port, ftp_user, ftp_password, ftp_directory, schedule).
   - Add the optional parameter if you want (local_directory, internal_network_directory).
   - Ensure the data is formatted correctly (YYYY-MM-DD hh:mm:ss) and that it represents a timestamp occurring after the program execution time.

## Notes

- Authentication issues or configuration problems will be logged for review.
- Ensure that the program is executed with the necessary permissions to access files and directories.

Feel free to customize the configuration parameters and adjust the program according to your specific requirements.

```

Feel free to make further adjustments to fit your preferences or provide more details.

## License

This project is licensed under the [GNU GENERAL PUBLIC LICENSE](LICENSE).