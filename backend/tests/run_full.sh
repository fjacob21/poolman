#!/bin/bash
cd ../src
python3 -m unittest discover -v -s ../tests/data
python3 -m unittest discover -v -s ../tests/generators/nhl
