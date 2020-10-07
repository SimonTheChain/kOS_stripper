#!/usr/bin/python3
# -*- coding: utf-8 -*-

# kOS Stripper
#
# Author: Simon Lachaîne

import os
import time

from colorama import init
from colorama import deinit


class Stripper(object):
    """
    Manages kOS code operations
    """
    def __init__(self):
        self.source_dir = "C:\\Users\Smoky05\PycharmProjects\kOS"
        self.source_file = ""
        self.destination = "D:\games\steamapps\common\Kerbal Space Program\Ships\Script"
        self.results = ""

    @property
    def full_path(self):
        """
        Creates the full path from the base directory and the file name
        :return:
        """
        return os.path.join(self.source_dir + os.sep, self.source_file)

    def read_source(self):
        """
        Strips the kOS source file
        :return:
        """
        if os.path.isfile(self.full_path):
            with open(self.full_path, "r") as source_file:
                for line in source_file:
                    if line.startswith("//") or line.startswith("\n"):
                        pass
                    else:
                        clean_line = line.lstrip(" ").rstrip(" ")
                        self.results += clean_line

    def write_file(self):
        """
        Writes the results of the strip operation to file
        :return:
        """
        file_name = os.path.splitext(os.path.basename(self.full_path))[0] \
            + "_" + os.path.splitext(os.path.basename(self.full_path))[1]

        with open(os.path.join(self.destination + os.sep, file_name), "w") as dest_file:
            dest_file.write(self.results)

        if os.path.isfile(os.path.join(self.destination + os.sep, file_name)):
            print(os.path.getsize(os.path.join(self.destination + os.sep, file_name)))


class StripperInterface(object):
    """

    """
    def __init__(self):
        self.stripper = Stripper()

    @staticmethod
    def hello():
        """
        Shows title
        :return: Sleep time
        """
        print("\n{}kOS Stripper{}\n".format(
            '\x1b[1;37;44m',
            '\x1b[0m'))

    @staticmethod
    def goodbye():
        """
        Shows credits and exits
        :return: Sleep time
        """
        print("\n\n{}Coded by Simon Lachaîne{}\n\n".format(
            '\x1b[1;37;44m',
            '\x1b[0m'))
        time.sleep(1)

    def get_source_files(self):
        """
        Creates a list of all *.ks files in the source directory
        :return:
        """
        source_files = []

        for root, dirs, files in os.walk(self.stripper.source_dir):
            for f in files:
                if os.path.splitext(f)[1] == ".ks":
                    source_files.append(os.path.basename(f))
            break

        return source_files

    def set_source_file(self, source_files):
        """
        Asks the user to choose the file to process
        :return:
        """
        if source_files:
            print("\n\n{}Choose the file to process:{}\n\n".format(
                "\x1b[1;37;42m",
                '\x1b[0m'))

            for index, f in enumerate(source_files):
                print("[{index}] {filename}".format(index=index, filename=f))

            source_file_index = int(input("\n> "))
            source_file = source_files[source_file_index]
            self.stripper.source_file = source_file

        else:
            print("\n{}No *.ks files found in the source directory{}".format(
                '\x1b[1;37;41m',
                '\x1b[0m'))


def main():
    """
    Program flow
    """
    init()

    repeat = True
    while repeat:
        app = StripperInterface()
        app.hello()
        app.set_source_file(app.get_source_files())
        app.stripper.read_source()
        app.stripper.write_file()

        while True:
            question = input("\nProcess completed; Rerun the program? (y/n)\n> ")

            if question.lower() == "y" or question.lower() == "yes":
                # app.reset_app()
                break

            elif question.lower() == "n" or question.lower() == "no":
                app.goodbye()
                repeat = False
                break

            else:
                print("\n{}Please answer 'y' or 'n'{}".format(
                    '\x1b[1;37;41m',
                    '\x1b[0m'))

    print("Program completed.")
    deinit()
    raise SystemExit


if __name__ == "__main__":
    main()
