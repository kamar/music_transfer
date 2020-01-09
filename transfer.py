#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import shutil
import urllib.parse

def move_files(path_to_playlist='/home/km/Μουσική/xristougenniatika_new.m3u', pat = '/media/.+'):

    """
    Transfers music files from path of playlist to specific folder.
    @path_to_playlist:  The path of the playlist.
    @pat:               The pattern (regex) to search.
    """

    with open(path_to_playlist) as fh:
        text = fh.read()

    # fh = open(path_to_playlist, 'r')
    # fh.read()
    # fh.close()

    pat = pat
    results = re.findall(pat, text, re.MULTILINE)
    if not os.path.exists('/home/km/Μουσική/Christmas_Songs'):
        os.makedirs('/home/km/Μουσική/Christmas_Songs')

    for i in results:
        # str_test = str_test.replace(i, urllib.parse.unquote(i))
        newf = urllib.parse.unquote(i)
        d, f = os.path.split(newf)
        print("Copy {0} to {1}".format(os.path.join(d, f), \
            os.path.join('/home/km/Μουσική/Christmas_Songs', f)))
        shutil.copy2(newf, os.path.join('/home/km/Μουσική/Christmas_Songs', f))


if __name__ == '__main__':
    move_files()
