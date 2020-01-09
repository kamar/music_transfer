#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib.parse


def correct_content(old_playlist='/home/km/Μουσική/xristougenniatika_new.m3u', pat='Christmas_.+'):

    """
    Corrects the playlist for  my car audio.
    """
    with open(old_playlist, "r", encoding="UTF-8") as fh:
        text = fh.read()
    # TODO: Error handling.
    # fh = open(old_playlist, "r")
    # text = fh.read()
    # fh.close()

    results = re.findall(pat, text)
    newtext = text

    for res in results:
        newtext = newtext.replace(res, urllib.parse.unquote(res))

    answer = input("Θέλετε να σώσετε την νέα Λίστα με το ίδιο όνομα (yes/no); [no] ")
    if answer.strip() == 'yes':
        print("Γράφω το αρχείο {}".format(old_playlist))
        fh = open(old_playlist, 'w')
        fh.write(newtext)
        fh.close()
    else:
        answer = ''
        d, f = os.path.split(old_playlist)
        answer = str(input("Δώστε όνομα αρχείου [προκαθορισμένο: {}]: ".format('new_{}'.format(f))))
        if answer:
            new_playlist = os.path.join(d, '{}'.format(answer.strip()))
        else:
            new_playlist = os.path.join(d, 'new_{}'.format(f))
        print("Γράφω το αρχείο {}.".format(new_playlist))
        fh = open(new_playlist, "w")
        fh.write(newtext)
        fh.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            correct_content(sys.argv[1])
        elif len(sys.argv) == 3:
            correct_content(sys.argv[1], sys.argv[2])
    else:
        correct_content()
