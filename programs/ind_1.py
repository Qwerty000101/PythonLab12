#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def skobka(s):
    if s.find("(") ==-1 and s.rfind(")") == -1:
        return True
    elif (s.find("(") == -1 or s.rfind(")") == -1
          or s.rfind(")") < s.find("(")):
        
        return False
    else:
        return skobka(s[s.find("(")+1:s.rfind(")")])


if __name__ == '__main__':
    while True:
        n = input("Введите строку:\n")
        if n == "exit":
            break
        print(skobka(n))
