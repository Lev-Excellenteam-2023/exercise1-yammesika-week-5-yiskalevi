# Yiska Levi

import os

sequence = "deep"


def list_file(path):
    files = [f for f in os.listdir(path)  # the function return all the file in this directory
             if os.path.isfile(os.path.join(path, f))  # check if each item in the list is a file
             and sequence in f]  # check if tha name of the file include the sequence
    return files

