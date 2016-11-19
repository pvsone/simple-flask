#!/bin/sh

mv environment.yml.2 environment.yml

cf push flask-conda2 -b python_buildpack

mv environment.yml environment.yml.2
