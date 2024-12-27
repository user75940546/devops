#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

function code_style {
  echo -e ${RED} "$(date '+%Y-%m-%d %H:%M:%S') Running code style tests..." ${NC} | tee /proc/1/fd/1
  black --check tests > >(tee -a /proc/1/fd/1) 2>&1
}

function linting {
  echo -e ${RED} "$(date '+%Y-%m-%d %H:%M:%S') Running linting..." ${NC} | tee /proc/1/fd/1
  pylint --rcfile=tests/.pylintrc tests > >(tee -a /proc/1/fd/1) 2>&1
}

function integration_tests {
  echo -e ${RED} "$(date '+%Y-%m-%d %H:%M:%S') Running integration tests..." ${NC} | tee /proc/1/fd/1
  pytest tests/integration_tests/test_upload_file.py > >(tee -a /proc/1/fd/1) 2>&1
}

function selenium_tests {
  echo -e ${RED} "$(date '+%Y-%m-%d %H:%M:%S') Running selenium tests..." ${NC} | tee /proc/1/fd/1

  exec -a xvfb Xvfb :1 -screen 0 1920x1080x16 &> xvfb.log  &

  DISPLAY=:1.0
  export DISPLAY

  pytest tests/selenium_tests/test_opop.py > >(tee -a /proc/1/fd/1) 2>&1

  rcode=$?
  kill $(pgrep -f xvfb)
  exit ${rcode}
}

case "$1" in
  --all)
    echo -e ${RED} "$(date '+%Y-%m-%d %H:%M:%S') Running tests:" ${NC} | tee /proc/1/fd/1
    code_style
    linting
    integration_tests
    selenium_tests
    ;;
  --test)
    case "$2" in
      code_style)
        code_style
        ;;
      linting)
        linting
        ;;
      integration)
        integration_tests
        ;;
      selenium)
        selenium_tests
        ;;
      *)
        echo "$(date '+%Y-%m-%d %H:%M:%S') Use 'code_style'; 'linting'; 'selenium'; 'integration'" | tee /proc/1/fd/1
        exit 1
        ;;
    esac
    ;;
  *)
    echo "Usage: $0 --all | --test [code_style|linting|selenium|integration]" | tee /proc/1/fd/1
    exit 1
    ;;
esac
