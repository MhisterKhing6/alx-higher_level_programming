#!/usr/bin/python3
import sys
save_to_jason = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Add all command line argument to a json file and save them"""
save_to_jason(sys.argv[1:], "add_item.json")
load_from_json_file("add_item.json")

