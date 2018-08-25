#!/usr/bin/python3
# -*- coding: utf-8 -*-

# kOS Stripper
#
# Author: Simon Lachaîne

import os


class Stripper(object):

    def __init__(self):
        self.source = ""
        self.dest = "D:\Games\Kerbal Space Program\Ships\Script"
        self.results = ""

    def get_source(self):
        print("kOS Stripper")
        self.source = input("Enter the path to the kOS script:\n>")

    def read_source(self):
        if os.path.isfile(self.source):
            with open(self.source, "r") as source_file:
                for line in source_file:
                    if line.startswith("//") or line.startswith("\n"):
                        pass
                    else:
                        clean_line = line.lstrip(" ").rstrip(" ")
                        self.results += clean_line

    def write_file(self):
        file_name = os.path.splitext(os.path.basename(self.source))[0] \
                    + "_" + os.path.splitext(os.path.basename(self.source))[1]

        with open(os.path.join(self.dest + os.sep, file_name), "w") as dest_file:
            dest_file.write(self.results)
        print(os.path.getsize(os.path.join(self.dest + os.sep, file_name)))


def main():
    """
    Program flow
    """
    app = Stripper()
    app.get_source()
    app.read_source()
    app.write_file()
    print("Program completed.")


if __name__ == "__main__":
    main()
