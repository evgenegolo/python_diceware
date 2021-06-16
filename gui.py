from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from database_handler import *



def create_main_window(window_title: str, window_dimensions: str) -> Tk:
    """
    Creating a new tkinter window and setting its title and dimensions
    :param window_title:  tkinter window title
    :param window_dimensions: tkinter window dimensions
    :return: Tk object reference
    """
    window = Tk()

    window.title(window_title)  # Gui Window Title
    window.geometry(window_dimensions)  # Setting windows size

    return window


def create_tree_view(parent: Tk, columns: tuple, height: int) -> Treeview:
    """
    Function creates a new TreeView
    :param parent: A parent window to display the TreeView at
    :param columns: TreeView columns
    :param height: TreeView screen height
    :return: TreeView object reference
    """
    tree = Treeview(parent, column=columns, show='headings', selectmode="extended", height=height)

    return tree


def fill_tree_view(data: list, tree: Treeview) -> bool:
    """
    Function fills an existing TreeView with given data (list of dictionaries which contain the data to display)
    :param data: Data to display
    :param tree: TreeView to display the data at
    :return: True if there is some data to display and the data format is valid and False otherwise
    """
    # Displaying column's names
    i = 1

    for item in tree.get_children():
        tree.delete(item)

    if len(data) > 0:
        for key in data[0].keys():
            tree.column(f"#{i}", anchor=CENTER)
            tree.heading(f"#{i}", text=key)
            i += 1

        # Adding record's information
        for record in data:
            tree.insert('', END, values=([val for val in record.values()]))

        return True
    return False


