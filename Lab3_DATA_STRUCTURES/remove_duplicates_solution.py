#!/usr/bin/python
# -*- coding: utf-8 -*-
def remove_duplicates(string):
    string = string.lower()
    a = set(string)
    b = list(string)
    value = len(b) - len(a)
    c = list(a)
    c.sort()
    result = (''.join(c), value)
    return result



			