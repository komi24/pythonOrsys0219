# -*- coding: utf-8 -*-

def mon_deco(f):
    def new_func():
        print("Hello")
        f()
        print("Bye")

    return new_func
    

@mon_deco
def ma_fonction():
    print("Hello world")


ma_fonction()
ma_fonction()
