'''
You work at a company that receives daily data files from external partners. 
These files need to be processed and analyzed, but first, they need to be 
transferred to the company's internal network.
The goal of this project is to automate the process of transferring the 
files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:
    Use the ftplib library to connect to the external FTP server and list the files in the directory.
    Use the os library to check for the existence of a local directory where the files will be stored.
    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.
    Use the shutil library to move the files from the local directory to the internal network.
    Use the schedule library to schedule the script to run daily at a specific time.
    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process.
'''
import logging
import sched
import time
from datetime import datetime, timedelta
from config_reader import ConfigReader
from ftp_file_transfer import FTPFileTransfer


def send_daily_reports(scheduler, ftp_transfer):
    # Get the current datetime
    current_datetime = datetime.now()
    tomorrow_with_time = current_datetime + timedelta(hours=24)

    # Schedule for the next day
    tomorrow = 24 * 3600 # seconds
    scheduler.enter(tomorrow, 1, send_daily_reports, (scheduler, ftp_transfer))
    logging.info(f'New schedule for tomorrow: {tomorrow_with_time}')
    
    # Initiate email sending
    ftp_transfer.transfer_files()

def main():
    # Logger
    log_file = 'ftp_transfer_logger.log'
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Program started')

    # Read Configuration
    parameters = ConfigReader()
    parameters.read_config_file()

    # Do not schedule or run if there are configuration issues
    if parameters.parameters:
        ftp_transfer = FTPFileTransfer(
        ftp_host = parameters.parameters['ftp_host'],
        ftp_port = parameters.parameters['ftp_port'],
        ftp_user = parameters.parameters['ftp_user'],
        ftp_password = parameters.parameters['ftp_password'],
        ftp_directory = parameters.parameters['ftp_directory'],
        local_directory = parameters.parameters['local_directory'],
        internal_network_directory = parameters.parameters['internal_network_directory']
        )
        login_success = ftp_transfer.check_ftp_reachability()
        
        # Avoid scheduling or executing tasks if login is not possible
        if login_success:
            # Run and Schedule
            scheduler = sched.scheduler(time.time, time.sleep)
            scheduled_time = time.mktime(time.strptime(parameters.parameters['schedule'], '%Y-%m-%d %H:%M:%S'))
            
            logging.info(f'New schedule: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(scheduled_time))}')    
            scheduler.enterabs(scheduled_time, 1, send_daily_reports, (scheduler, ftp_transfer))

            scheduler.run()
        else:
            print(f'Authentication issues detected in config.ini. See {log_file} for details.')
    else:
        print(f'Configuration issues detected in config.ini. See {log_file} for details.')

    logging.info('Program Ended')

if __name__ == '__main__':
    main()
