import os
import requests as rq
import pandas as pd

from flask import (Flask)
app = Flask(__name__)

@app.route('/')
def root():
   print('Request on root')
   return "github deployment with oryx build"


@app.route('/test')
def test():
   print('test...')
   return "test...."

if __name__ == '__main__':
   app.run()