#!/usr/bin/python3

import time

def main():
    print("Main Function")
    while True:
        oneHz(200)

def hz(freq):
    fq = float(1 / freq)
    t0 = time.time()
    print(freq, " Hz")
    while True:
        if(time.time() > (t0 + fq)):
            break

def oneHz(f):
    t0 = time.time()
    print("1 Hz")
    while True:
        hz(f)
        if(time.time() > (t0 + 1)):
            break

if __name__ == "__main__":
    main()
