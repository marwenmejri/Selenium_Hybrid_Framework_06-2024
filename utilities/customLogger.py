import logging


class Logger:
    @staticmethod
    def sample_logger():
        # logging.basicConfig(level=logging.INFO,
        #                     filename="Logs/logs.log",
        #                     filemode="a",
        #                     format="%(asctime)s - %(name)s - %(filename)s | %(levelname)s : %(message)s",
        #                     datefmt='%m-%d-%Y %I:%M:%S %p')
        logger = logging.getLogger(name='custom_logger')
        logger.setLevel(level=logging.INFO)
        formatter = logging.Formatter(datefmt='%m-%d-%Y %I:%M:%S %p',
                                      fmt="%(asctime)s - %(name)s - %(filename)s | %(levelname)s : %(message)s")
        file_handler = logging.FileHandler(filename="Logs/logs.log",
                                           mode='a')
        file_handler.setFormatter(fmt=formatter)
        logger.addHandler(file_handler)
        return logger


# if __name__ == '__main__':
#     # l1 = Logger1()
#     logger_test = Logger.sample_logger()
#     logger_test.debug("Debug \t This is the first statement")
#     logger_test.info("Info \t This is the first statement")
#     logger_test.warning("Warning \t This is the first statement")
#     logger_test.error("Error \t This is the first statement")
#     logger_test.critical("Critical \t This is the first statement")
