"""Cloud Foundry test"""
from flask import Flask
import os
import sys
import platform

app = Flask(__name__)

port = int(os.getenv("PORT", 8080))

@app.route('/')
def hello_world():
    sys.stdout.write('**** HELLO WORLD ****\n')
    return 'Hello World! I am running on port ' + str(port)

@app.route('/sys')
def sys_version():
    return sys.version

@app.route('/platform')
def platform_version():
    return platform.python_version()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
