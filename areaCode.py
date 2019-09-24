#!/usr/bin/python
import re

phone = "602-343-8747"
match = re.search(r'^\d{0,3}', phone)

if match:
    print match.group()
