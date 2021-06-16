from dicware import *
import re
import os

def read_file(path: str, code: str) -> str:
    """
    Search word in file using code
    :param path: path of file
    :param code: code of word in file
    :return: word from file
    """
    part = ""
    with open(path, 'r') as file:
        file.seek(0)
        for line in file:
            if code in line:
                x = re.split('\t|\n', line)
                part = x[1]
    return part


def check_file(path: str) -> bool:
    """
    Check if file is valid
    :param path: path to file
    :return: True if file is valid, else False
    """
    return os.path.exists(path) and os.path.isfile(path)
