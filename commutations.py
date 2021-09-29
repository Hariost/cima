from config import CIMA_H

def lx(x):
 print('start lx')
 rec = next((item for item in CIMA_H if item["age"] == x), None)
 return 0 if rec is None else rec['lx']

def dx(x):
 rec = next((item for item in CIMA_H if item["age"] == x), None)
 return 0 if rec is None else rec['dx']


def __main__():
    print('Hello')
    print(lx(15))