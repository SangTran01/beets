# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
"""Custom collections classes
"""


class IdentityFallbackDict(dict):
    """A dictionary which is "transparent" (maps keys to themselves) for all
    keys not in it.
    """
    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return key


class DefaultList(list):
    """A `list` which extends itself with the default value provided to the
    constructor when indexed further than its length.
    """
    def __init__(self, default):
        self._default = default

    def _fill(self, index):
        while len(self) <= index:
            self.append(self._default)

    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)
