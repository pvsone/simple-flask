#!/bin/sh

mv environment.yml.3 environment.yml

cf push flask-conda3

mv environment.yml environment.yml.3
