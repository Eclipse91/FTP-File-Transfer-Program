import os
from ftplib import FTP
import shutil
from datetime import datetime
import logging

class FTPFileTransfer:
    '''
    FTPFileTransfer facilitates the transfer of files between a remote FTP server
    and local/internal network directories.

    Methods:
        - connect_to_ftp(): Connects to the FTP server and logs in, returning the FTP connection object.
        - list_files_on_ftp(ftp): Lists files in the specified FTP directory.
        - check_create_directory(directory): Checks if the directory exists, creates it if not.
        - create_time_dir(directory): Creates a directory with a timestamp and returns the path.
        - download_file_from_ftp(ftp, file, local_directory): Downloads a file from FTP and saves it locally.
        - move_files_to_internal_network(local_directory, internal_network_directory):
          Moves files from a local directory to the internal network directory.
        - transfer_files(): Transfers files from FTP to local and internal network directories.
        - check_ftp_reachability(): Checks if the FTP server is reachable and login is successful.

    Example Usage:
    ftp_transfer = FTPFileTransfer(
        ftp_host='example.com',
        ftp_port='21',
        ftp_user='username',
        ftp_password='password',
        ftp_directory='/remote_directory/',
        local_directory='/local_temp/',
        internal_network_directory='/internal_network/'
    )
    '''
    def __init__(self, ftp_host, ftp_port, ftp_user, ftp_password, ftp_directory,
                 local_directory, internal_network_directory):
        '''
        Initializes the FTPFileTransfer object with FTP connection details and directories.
        '''
        self.ftp_host = ftp_host
        self.ftp_port = int(ftp_port)
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password
        self.ftp_directory = ftp_directory
        self.local_directory = local_directory
        self.internal_network_directory = internal_network_directory

    def connect_to_ftp(self):
        '''
        Connects to the FTP server and logs in.
        '''
        ftp = FTP()
        ftp.connect(self.ftp_host, self.ftp_port)
        ftp.login(user=self.ftp_user, passwd=self.ftp_password)
        return ftp

    def list_files_on_ftp(self, ftp):
        '''
        Lists files in the specified FTP directory.
        '''
        try:
            ftp.cwd(self.ftp_directory)
            return ftp.nlst()
        except Exception as e:
            logging.error(f'The folder "{self.ftp_directory}" is not valid: {str(e)}')

    def check_create_directory(self, directory):
        '''
        Checks if the directory exists, creates it if not.
        '''
        if not os.path.exists(directory):
            os.makedirs(directory)

    def create_time_dir(self, directory):
        '''
        Creates a directory with a timestamp and returns the path.
        '''
        created_dir = directory + datetime.now().strftime('%Y%m%d %H%M%S')
        os.mkdir(created_dir)
        return created_dir

    def download_file_from_ftp(self, ftp, file, local_directory):
        '''
        Downloads a file from FTP and saves it locally.
        '''
        with open(os.path.join(local_directory, file), 'wb') as local_file:
            ftp.retrbinary(f'RETR {file}', local_file.write)

    def move_files_to_internal_network(self, local_directory, internal_network_directory):
        '''
        Moves files from a local directory to the internal network directory.
        '''
        created_dir = self.create_time_dir(internal_network_directory)
        for file in os.listdir(local_directory):
            shutil.move(os.path.join(local_directory, file), created_dir)

    def transfer_files(self):
        '''
        Transfers files from FTP to local and internal network directories.
        '''
        try:
            ftp = self.connect_to_ftp()
            files = self.list_files_on_ftp(ftp)
            self.check_create_directory(self.local_directory)
            self.check_create_directory(self.internal_network_directory)

            temporary_dir = self.create_time_dir(self.local_directory)
            for file in files:
                try:
                    self.download_file_from_ftp(ftp, file, temporary_dir)
                    logging.info(f'Transferred: {file}')
                except Exception as e:
                    logging.error(f'Error: {str(e)}')

            self.move_files_to_internal_network(temporary_dir, self.internal_network_directory)
            os.rmdir(temporary_dir)

        except Exception as e:
            logging.error(f'Error: {str(e)}')

    def check_ftp_reachability(self):
        '''
        Checks if the FTP server is reachable and login is successful.
        '''
        ftp = FTP()
        try:
            ftp.connect(self.ftp_host, self.ftp_port)
            logging.info(f'FTP server is reachable.')
        
        except Exception as e:
            logging.error(f'Connection error: {str(e)}')
            return False

        try:
            ftp.login(user=self.ftp_user, passwd=self.ftp_password)
            logging.info(f'Valid username and password.')

        except Exception as e:
            logging.error(f'Login error: {str(e)}')
            return False
        
        ftp.quit()
        return True
