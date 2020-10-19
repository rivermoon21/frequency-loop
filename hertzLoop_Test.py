#!/usr/bin/python3

'''
import time

t0= time.clock()
print(t0)
print("Hello")
time.sleep(2)
t1 = time.clock() - t0
print(t1)
print("Time elapsed: ", t1 - t0) # CPU seconds elapsed (floating point)

'''

'''
import threading
import time

class Counter():
    def __init__(self, increment):
        self.next_t = time.time()
        self.i=0
        self.done=False
        self.increment = increment
        self.run()

    def run(self):
        print("hello ", self.i)
        self.next_t+=self.increment
        self.i+=1
        if not self.done:
            threading.Timer( self.next_t - time.time(), self.run).start()

    def stop(self):
        self.done=True

a=Counter(increment = 1)
time.sleep(5)
a.stop()

'''

'''
import time

def tenhz():
  time1 = time.time()
  print ("Ten Hz")
  while True:
    if time.time() > (time1 + 0.1):  # check to see if a tenth of a second has passed
      break
  
def onehz():
  time1 = time.time()
  print ("One Hz")
  while True:
    tenhz()
    if time.time() > (time1 + 1):  # check to see if a second has passed
      break
  
while True:
  print("root")
  onehz()

'''

import time

def procedure():
   time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print(time.clock(), "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print ((time.time() - t0), "seconds wall time")
