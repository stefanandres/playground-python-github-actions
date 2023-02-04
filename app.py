#!/usr/bin/env python

import os

from time import sleep


class App():
  def __init__(self, name):
    self.name = name

if __name__ == '__main__':
  i = 0
  app = App(os.getenv('APP_NAME', 'myapp'))

  while True and not os.getenv('INTEGRATION_TEST') == 'true':
    i += 1
    print(f"{i} - {app.name}")
    sleep(1)

  print(app.name)
