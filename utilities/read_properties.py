import configparser

config = configparser.RawConfigParser()
config.read(filenames='Configuration/config.ini')


def get_username():
    return config.get(section="common info", option="username")


def load_value(section, option):
    """
    Load a specific value from the configuration file.

    :param section: Section name.
    :param option: Option name.
    :return: Value of the specified option.
    """
    # value = config.get(section, option)
    return config.get(section, option)


# username = load_value(section='common info', option='username')
# print(username)
# print(load_value(section='common info', option='password'))
# print(load_value(section='common info', option='port'))
