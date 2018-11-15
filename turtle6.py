#coding: utf-8
from turtle import *

def branch(length):
   
    if length < 10:
        return
    forward(length)
    left(30)
    branch(length/2)
    right(60)
    branch(length/2)
    left(30)
    forward(-length)

right(90)
branch(200)

input()

