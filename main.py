from gui import *
from dicware import *

if __name__ == "__main__":
    # Setting the main window (title & dimensions)
    window = create_main_window("generator", '826x427')

    # Adding a new label's
    lbl_file = Label(window, text="File Path")
    lbl_txt = Label(window, text="number of words")

    # placing label's on the window grid
    lbl_file.grid(column=0, row=0)
    lbl_txt.grid(column=1, row=1)

    # Creating the input fields
    input_file_path = Entry(window)
    input_file_path.insert(0, 'diceware.txt')
    input_text_field = Entry(window)

    # placing the input fields on the window grid
    input_file_path.grid(column=1, row=0)
    input_text_field.grid(column=1, row=1)

    # Creating a button to trigger the password creation
    btn = Button(window, text="create password", fg="black", command=lambda: create_password(input_file_path.get(),
                                                                                             input_text_field.get(),
                                                                                             tree))
    btn.grid(column=2, row=0)

    # Creating a TreeView (the given tuple defines an amount of columns)
    tree = create_tree_view(window, ("1", "2", "3"), 20)
    tree.grid(column=3, row=0, rowspan=20)

    mainloop()
