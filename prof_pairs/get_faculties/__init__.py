import itertools
import importlib
import pathlib
import sys

from . import utd_cs
def import_all():
    # TODO: populate this dynamically, by searching the file path
    return [utd_cs]

def get_faculty(module):
    if hasattr(module, 'get_faculties'):
        a = list(module.get_faculties())
        print(module)
        print(repr(a)[:100])
        return a
    else:
        return []

def get_faculties():
    return itertools.chain.from_iterable(map(get_faculty, import_all()))

__all__ = ['get_faculties']
