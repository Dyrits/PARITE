from os import path
import logging as lg

lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):
    directory = path.dirname(path.dirname(__file__))
    path_to_file = path.join(directory, "data", data_file)
    try:
        with open(path_to_file, "r") as file:
            preview = file.readline()
        lg.info(preview)
    except FileNotFoundError:
        lg.warning("The file has not been found.")


if __name__ == "__main__":
    launch_analysis('current_mps.csv')
