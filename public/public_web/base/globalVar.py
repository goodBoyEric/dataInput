# -*- coding:UTF-8 -*-
# !/usr/bin/env python3
# _author = liusong time = 2017/10/10 0010

import time
import string
from random import Random
from public.public_web.base.newRandom import NewRandom

# Random Data:int
def random_int_data():
    Itas_Random = Random()
    Itas_Random_int_four = Itas_Random.randint(a=0, b=9999)
    Itas_Random_int_six = Itas_Random.randint(a=9999, b=999999)
    Itas_Random_int_nine = Itas_Random.randint(a=999999, b=999999999)
    Itas_Random_int_eleven = Itas_Random.randint(a=999999999, b=99999999999)
    return Itas_Random_int_four, Itas_Random_int_six, Itas_Random_int_nine, Itas_Random_int_eleven

# Random Data:char
def random_char_data():
    Itas_New_Random = NewRandom()
    Itas_Random_Char_four = Itas_New_Random.new_choice(seq=string.ascii_lowercase+string.ascii_uppercase, char_length=4)
    Itas_Random_Char_six = Itas_New_Random.new_choice(seq=string.ascii_lowercase+string.ascii_uppercase, char_length=6)
    Itas_Random_Char_nine = Itas_New_Random.new_choice(seq=string.ascii_lowercase+string.ascii_uppercase, char_length=9)
    return Itas_Random_Char_nine, Itas_Random_Char_four, Itas_Random_Char_six

# time
currentDay = time.strftime("%d-%m-%Y", time.localtime())
currentMouth = time.strftime("%m-%Y", time.localtime())
currentMouth_firstDay = '01-' + time.strftime("%m-%Y", time.localtime())
# print(currentDay, currentMouth, currentMouth_firstDay)
