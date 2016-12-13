"""Cloud Foundry test"""
from flask import Flask
import os
import sys
import platform
import logging

app = Flask(__name__)

port = int(os.getenv('PORT', 8080))

@app.route('/')
def hello_world():
    sys.stdout.write('**** hello_world ****\n')
    sys.stdout.flush()
    return 'Hello World! I am running on port ' + str(port)

@app.route('/sys')
def sys_version():
    print('**** sys_version ****')
    return sys.version

@app.route('/platform')
def platform_version():
    app.logger.info('**** platform_version ****')
    return platform.python_version()

@app.route('/logtest')
def logtest():
    app.logger.debug('**** debug ****')
    app.logger.info('**** info ****')
    app.logger.warning('**** warning ****')
    app.logger.error('**** error ****')
    return 'Check the console'

if __name__ == '__main__':
    ch = logging.StreamHandler(sys.stdout)
    app.logger.addHandler(ch)
    app.logger.setLevel(logging.INFO)
    app.run(host='0.0.0.0', port=port)
