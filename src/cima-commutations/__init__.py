import os
import json
CIMA_H=[]

def load_cima_h():
    with open('cima_h.json') as data_file:
        CIMA_H = json.load(data_file)