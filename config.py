import os
import json
CIMA_H = []

def load_cima_h():
  with open('cima_h.json','r') as data_file:
    CIMA_H = json.load(data_file)




if __name__ == '__main__':
  print('Trigger main')
  load_cima_h()