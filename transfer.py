#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import shutil
import urllib.parse

# TODO: Add parameters.
def move_files():

    """
    Transfers music files from path of playlist to specific folder.
    """
# TODO: Rewrite with 'with' form.
    fh = open('/home/km/Μουσική/xristougenniatika_new.m3u', 'r')
    text = fh.read()
    fh.close()

    pat = '/media/.+'
    results = re.findall(pat, text, re.MULTILINE)
    if not os.path.exists('/home/km/Μουσική/Christmas_Songs'):
        os.makedirs('/home/km/Μουσική/Christmas_Songs')
    for i in results:
        # str_test = str_test.replace(i, urllib.parse.unquote(i))
        newf = urllib.parse.unquote(i)
        d, f = os.path.split(newf)
        shutil.copy2(newf, os.path.join('/home/km/Μουσική/Christmas_Songs', f))


if __name__ == '__main__':
    move_files()
