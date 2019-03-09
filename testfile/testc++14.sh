#!/bin/bash

RED="\e[31m"
DEFAULT="\e[39m"
GREEN="\e[32m"

TESTFOLDER=TEST

INPUT_NAME="$1.in."
OUTPUT_NAME="$1.out."
MY_NAME="$1.my."
BIN="$TESTFOLDER/$1"
EXECMD="./$BIN"

mkdir -p ${TESTFOLDER}
file="$1".cpp
if [[ ! -f "$file" ]]; then
    echo "$file not found."
    exit
fi

if ! clang++ -o ${BIN} ${file} -std=gnu++14 -O2 -g -Wall -Wcomma
then
    exit
fi

rm -R ${MY_NAME}* &>/dev/null

i=0
while [[ -f "$INPUT_NAME$i" ]] && [[ -f "$OUTPUT_NAME$i" ]]
do
  input="$INPUT_NAME$i"
  output="$OUTPUT_NAME$i"
  myoutput="$TESTFOLDER/$MY_NAME$i"

  if ! `which time` -o time.out -f "( %es )" ${EXECMD} < ${input} > ${myoutput}; then
    echo -e ${RED}"Sample test #$i: Runtime Error""$DEFAULT"
    echo "Sample Input #$i"
    cat ${input}
    echo
  elif diff --brief -B --ignore-trailing-space ${myoutput} ${output}; then
    echo -e ${GREEN}"Sample test #$i: Accepted"${DEFAULT}
  else
    echo -e ${RED}"Sample test #$i: Wrong Answer"${DEFAULT}
    echo "========================================"
    echo "Sample Input #$i"
    cat ${input}
    echo
    echo "Sample Output #$i"
    cat ${output}
    echo
    echo "My Output #$i"
    cat ${myoutput}
    echo
  fi
  cat time.out
  echo "========================================"
  i=$[$i+1]
done
