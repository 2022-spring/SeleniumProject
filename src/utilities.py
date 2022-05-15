import time
import yaml
from os.path import abspath, dirname

ROOT_DIR = dirname(abspath(__file__))


def load_yaml_file(filepath):
    try:
        print("****** reading yaml file *******************")
        with open(filepath, 'r') as stream:
            file_content = yaml.safe_load(stream)
        # return file_content
    except FileNotFoundError as err:
        print("Incorrect file path is provided")
        print(f"FileNotFoundError: {err}")
        raise
    else:
        print("Else statement in try except, only after try block")
        return file_content
    finally:
        print("Finally: This will execute whatever happens")


def get_str_seconds():
    # 20220424_103856
    return time.strftime("%Y/%m/%d_%H:%M:%S", time.localtime())


def get_timestamp():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())
