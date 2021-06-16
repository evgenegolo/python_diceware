from files import *
from gui import  *
from database_handler import *
from os.path import exists, isfile
from random import randint

LEN_OF_WORD = 5
R_MIN = 1
R_MAX = 6

def create_password (file: str, words_amount: int, tree: Treeview):
    """
    Generating password with adding to database
    :param tree:
    :param file: path to text file
    :param words_amount: number of words
    :return: None
    """
    insert_password(dice_ware(file, int(words_amount)), tree)


def dice_ware(file: str, words_amount: int) -> str:
    """
    Creating password using DiceWare algorithm
    :param path: path to text file
    :param words_amount: number of words
    :return: generated password
    """
    if int(words_amount) <= 0:
        messagebox.showwarning(message="number of words cant be zero or negative")
    else:
        if not check_file(file):
            messagebox.showwarning(message="wrong file path")
        else:
            return "".join([read_file(file, "".join([str(randint(R_MIN, R_MAX)) for i in range(LEN_OF_WORD)]))for j in range(words_amount)])


def insert_password(password: str, tree: Treeview) -> None:
    """
    insert a new password to the db
    the current date from sql function
    :param tree:
    :param password: password for adding to database
    :return: None
    """
    if password != "":
        fetch_records(f"INSERT INTO saved_pass(password, date) VALUES('{password}', CURDATE())")

    fill_tree_view(fetch_records("SELECT * FROM saved_pass"), tree)
