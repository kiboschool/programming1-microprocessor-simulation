#!/usr/bin/env bash

# copy test file
cp ../test_*.py ./

zip -r gradescope.zip setup.sh requirements.txt run_autograder run_tests.py test_*.py chatgpt_test.py merge_results.py .env

# remove test file
rm ./test_*.py
