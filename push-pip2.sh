#!/bin/sh

mv requirements.txt.0 requirements.txt
mv runtime.txt.2 runtime.txt

cf push flask-pip2

mv runtime.txt runtime.txt.2
mv requirements.txt requirements.txt.0
