#!/usr/bin/env python3

import os
import sys

arguments = {
    "lang": None,
    "count": None,
}
for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
print(arguments)
print(arguments["lang"])
print(arguments["count"])
