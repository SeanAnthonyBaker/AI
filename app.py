from flask import Flask
import copy
import json
from typing import Iterable, Dict, Any

import streamlit as st
from streamlit_ace import st_ace

app = Flask(__name__)

st.write("Hello, World!")

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ =='__main__':
    app.run()