# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/10/10 0010

from random import Random
import string


class NewRandom(Random):
    def __init__(self):
        Random.__init__(self)

    def new_choice(self, seq=string.ascii_lowercase + string.ascii_uppercase, char_length=None):
        random_char_list = ''
        for i in range(0, char_length):
            try:
                i = self._randbelow(len(seq))
                random_char_list = random_char_list + seq[i]
            except ValueError:
                raise IndexError('Cannot choose from an empty sequence')
        return random_char_list


class RandomData(NewRandom):
    def __init__(self):
        NewRandom.__init__(self)
        self.itas_random_int_four = NewRandom.randint(self, a=1000, b=9999)
        self.itas_random_int_six = NewRandom.randint(self, a=100000, b=999999)
        self.itas_random_int_nine = NewRandom.randint(self, a=100000000, b=999999999)
        self.itas_random_int_eleven = NewRandom.randint(self, a=10000000000, b=99999999999)

        self.itas_random_char_four = NewRandom.new_choice(self, char_length=4)
        self.itas_random_char_six = NewRandom.new_choice(self, char_length=6)
        self.itas_random_char_nine = NewRandom.new_choice(self, char_length=9)

    @property
    def itas_random_int_four_function(self):
        return self.itas_random_int_four

    @property
    def itas_random_int_six_function(self):
        return self.itas_random_int_six

    @property
    def itas_random_int_nine_function(self):
        return self.itas_random_int_nine

    @property
    def itas_random_int_eleven_function(self):
        return self.itas_random_int_eleven

    @property
    def itas_random_char_four_function(self):
        return self.itas_random_char_four

    @property
    def itas_random_char_six_function(self):
        return self.itas_random_char_six

    @property
    def itas_random_char_nine_function(self):
        return self.itas_random_char_nine
