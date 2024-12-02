import logging
import os

class Logger:
    def __init__(self):
        # Configurando os diretórios para os log
        self.log = 'log'
        self.debug = 'debug'
        self.error = 'error'
        
        # Criando os diretórios se não existirem
        os.makedirs(self.log, exist_ok=True)
        os.makedirs(self.debug, exist_ok=True)
        os.makedirs(self.error, exist_ok=True)
        
        # Configurando o logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Criando manipulador para log de erro, aviso e crítico
        error_log_handler = logging.FileHandler(os.path.join(self.error, 'dev_log_error_warning_critical.log'))
        error_log_handler.setLevel(logging.WARNING)
        error_log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(filename)s - %(message)s')
        error_log_handler.setFormatter(error_log_formatter)
        self.logger.addHandler(error_log_handler)

        # Criando manipulador para log de informação
        info_log_handler = logging.FileHandler(os.path.join(self.log, 'dev_log_info.log'))
        info_log_handler.setLevel(logging.INFO)
        info_log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(filename)s - %(message)s')
        info_log_handler.setFormatter(info_log_formatter)
        self.logger.addHandler(info_log_handler)

        # Criando manipulador para log de depuração
        debug_handler = logging.FileHandler(os.path.join(self.debug, 'dev_log_debug.log'))
        debug_handler.setLevel(logging.DEBUG)
        debug_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(filename)s - %(message)s')
        debug_handler.setFormatter(debug_formatter)
        self.logger.addHandler(debug_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
