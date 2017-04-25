#!/bin/bash

set -e # Exit with nonzero exit code if anything fails

jekyll build

echo "I am in"
pwd
echo "home is $HOME"
ls -la
ls -la _site
ls -la out
mv _site/* out/
