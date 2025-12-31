from FoxDot import *

def basic_drums(d):
    d >> play("x-o-", dur=0.25)

def broken_drums(d):
    d >> play("x(o-)", dur=0.25)
