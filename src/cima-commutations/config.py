import os
import json
CIMA_H = []
import os.path
def load_cima_h():
  with open(os.path.dirname(__file__) + '/../cima_h.json','r') as data_file:
    CIMA_H = json.load(data_file)
  return CIMA_H



if __name__ == '__main__':
  load_cima_h()