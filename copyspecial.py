#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Paul Racisz, Ruben Espino"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    path_list = [
        os.path.abspath(os.path.join(dirname, files))
        for files in (os.listdir(dirname))
        if re.search(r'__(\w+)__', files)
    ]
    return path_list


def copy_to(path_list, dest_dir):
    """Copies files to destination folder"""
    try:
        os.makedirs(dest_dir)
    except OSError as error:
        print(error)
        exit(1)
    for path in path_list:
        file_name = os.path.basename(path)
        current_path = os.path.dirname(path)
        absolute_path = os.path.join(current_path, dest_dir, file_name)
        shutil.copyfile(path, absolute_path)
    return


def zip_to(path_list, dest_zip):
    """Zips the files in the path list to dest file """
    file_list = ''
    for path in path_list:
        file_list += path + ' '
    print("Command I'm going to do:")
    print('zip -j', dest_zip, file_list)
    try:
        subprocess.call(['zip', '-j', dest_zip] + path_list)
    except OSError as error:
        print(error)
        exit(1)
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='dir to search for files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if not ns:
        parser.print_usage()
        sys.exit(1)
    special_paths = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(special_paths, ns.todir)
    if ns.tozip:
        zip_to(special_paths, ns.tozip)
    if not ns.todir and not ns.tozip:
        print("\n".join(special_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
