import logging
from datetime import datetime
import os


class ConfigReader:
    '''
    A class for reading and validating configuration parameters from a config.ini file.
    '''

    def __init__(self):
        self.parameters = {}

    def read_config_file(self):
        '''
        Read the config.ini file and populate the parameters dictionary.
        '''
        try:
            with open('config.ini', 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = map(str.strip, line.split('='))
                        self.parameters[key] = value

        except FileNotFoundError:
            logging.error(f'Configuration file config.ini not found.')

        except Exception as e:
            logging.error(f'Error reading configuration file: {str(e)}.')

        else:
            if self.check_parameters():
                logging.info('Parameters config.ini are correct')
            else:
                logging.error('Configuration issue detected in config.ini.')
                
    def check_parameters(self):
        '''
        Check the validity of parameters.
        '''
        # Check the validity of the schedule
        if not self.validate_datetime_format(self.parameters.get('schedule')):
            logging.error('Invalid datetime', self.parameters.get('schedule'))
            self.parameters.clear()
            return False
        
        # Check the validity of the directory local_directory
        if not self.is_valid_folder(self.parameters.get('local_directory')):
            if self.parameters.get('local_directory') == '':
                self.parameters['local_directory'] = './local_network/'
            else:
                self.parameters.clear()            
                return False
        
        # Check the validity of the directory internal_network_directory
        if not self.is_valid_folder(self.parameters.get('internal_network_directory')):
            if self.parameters.get('internal_network_directory') == '':
                self.parameters['internal_network_directory'] = './internal_network/'
            else:
                self.parameters.clear()            
                return False
        
        return True

    def validate_datetime_format(self, datetime_str):
        '''
        Validate the format of a datetime string.
        '''
        try:
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            current_time = datetime.now()

            if datetime_object < current_time:
                return False
            
            return True

        except ValueError:
            return False

    def is_valid_folder(self, folder_path):
        '''
        Check the validity of a folder.
        '''
        return os.path.exists(folder_path) and os.path.isdir(folder_path)
