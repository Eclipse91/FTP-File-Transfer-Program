# FTP File Transfer Program

The FTP File Transfer program is designed to automate the transfer of files between a remote FTP server and local/internal network directories. It includes features for scheduling tasks, logging, and reading configuration parameters from a `config.ini` file.

## Files

### `main.py`

The main script for scheduling and running daily reports.

### `config_reader.py`

A class for reading and validating configuration parameters from a `config.ini` file.

### `ftp_file_transfer.py`

FTPFileTransfer facilitates the transfer of files between a remote FTP server and local/internal network directories.

## Requirements

- Python 3.6 or higher

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Eclipse91/FTP-File-Transfer-Program.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FTP-File-Transfer-Program
   ```

3. Explore Configuration Below
   Update the config.ini adding the parameters required
4. Run the application:

   ```bash
   python main.py
   ```
5.Check the `ftp_transfer_logger.log` file for program logs and any potential issues.

## Configuration:
   - Ensure that the config.ini file includes all the mandatory parameters (ftp_host, ftp_port, ftp_user, ftp_password, ftp_directory, schedule).
   - Add the optional parameter if you want (local_directory, internal_network_directory).
   - Ensure the data is formatted correctly (YYYY-MM-DD hh:mm:ss) and that it represents a timestamp occurring after the program execution time.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Notes

- Authentication issues or configuration problems will be logged for review.
- Ensure that the program is executed with the necessary permissions to access files and directories.

Feel free to contribute or report issues!
This README provides a clearer structure, concise information, and instructions for setting up and running the FTP-File-Transfer-Program. Adjust the content as needed for your project.

