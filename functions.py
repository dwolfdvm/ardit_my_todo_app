FILEPATH = 'todos.txt'


# A script, imported it is referred to as module
# Below example of a conditional for internal operations only

def get_todos(filepath=FILEPATH):  # filepath is a parameter
    """Reads a default text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_arg)

    # Write the to-do items list in the default text file
    # With a default for write, must flip parameters, then also must flip arguments below as well
    # use this conditional below to hide key operations when exported


if __name__ == "__main__":
    print("hello")  # An example. Only runs inside functions.py
