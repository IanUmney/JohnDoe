# !/usr/bin/python

from JohnDoe import JohnDoe

def main():
    jd = JohnDoe(name="Mike Smith", age=37).create()
    print(jd)

if __name__=="__main__":
    main()
