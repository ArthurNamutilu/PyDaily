#!/usr/bin/python3
import sys

print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])
else:
    print("No arguments provided")
