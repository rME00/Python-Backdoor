"""
https://github.com/xp4xbox/Python-Backdoor

@author    xp4xbox
"""
from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    return parser.parse_args()
