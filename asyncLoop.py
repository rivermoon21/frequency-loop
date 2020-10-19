#!/usr/bin/python3
import time
import asyncio

start = time.time()

def tic():
    return 'at %1.2f seconds' % (time.time() - start)

async def hz400():
    print('400Hz loop started work: {}'.format(tic()) )
    time4 = time.time()
    while True:
        await asyncio.sleep(0)
        if time.time() > time4 + 0.0025:
            print('400Hz loop ended work: {}'.format(tic()))
            time4 = time.time()

async def hz10():
    # Busy waits for a tenth of a second, but we don't want to stick around...
    print('10Hz loop started work: {}'.format(tic()))
    time1 = time.time()
    while True:
      # do some work here
      await asyncio.sleep(0)
      if time.time() > time1 + 0.1:
        print('10Hz loop ended work: {}'.format(tic()))
        time1 = time.time()

async def hz1():
    # Busy waits for a second, but we don't want to stick around...
    print('1 Hz loop started work: {}'.format(tic()))
    time2 = time.time()
    while True:
      # do some work here
      await asyncio.sleep(0)
      if time.time() > time2 + 1:
        print(" ")
        print('1 Hz loop ended work: {}'.format(tic()))
        print(" ")
        time2 = time.time()

async def gr3():
    print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    time3 = time.time()
    while True:
      # do some work here
      if time.time() > time3 + 20:
        print("Done!")
      await asyncio.sleep(0)

def main():
    ioloop = asyncio.get_event_loop()
    tasks = [
        ioloop.create_task(hz400()),
        ioloop.create_task(hz10()),
        ioloop.create_task(hz1()),
        ioloop.create_task(gr3())
    ]
    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()

if __name__ == "__main__":
    main()
