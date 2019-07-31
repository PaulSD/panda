#!/usr/bin/env python
import time
from panda import Panda
	
if __name__ == "__main__":
  panda_serials = Panda.list()
  pandas = []
  for ps in panda_serials:
    pandas.append(Panda(serial=ps))

  while True:
    for panda in pandas:
      print(panda.health())
    print("\n")
    time.sleep(0.5)

