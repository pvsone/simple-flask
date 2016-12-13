#!/bin/sh

mv requirements.txt.0 requirements.txt
mv runtime.txt.3 runtime.txt

cf push flask-pip3

mv runtime.txt runtime.txt.3
mv requirements.txt requirements.txt.0
