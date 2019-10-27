# -*- coding: utf-8 -*-
from pivot_point import conf

def pp(h, l, c):
    return round((h + l + c) / 3, conf.digits)

def r1(pp, l):
    return round(pp * 2 - l, conf.digits)

def s1(pp, h):
    return round(pp * 2 - h, conf.digits)

def r2(pp, h, l):
    return round(pp + (h - l), conf.digits)

def s2(pp, h, l):
    return round(pp - (h - l), conf.digits)
