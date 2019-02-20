#!/bin/bash

RED="\e[31m"
DEFAULT="\e[39m"
GREEN="\e[32m"

INPUT_NAME="$1.in."
OUTPUT_NAME="$1.out."
MY_NAME="$1.my."
EXECMD="$1"

mkdir -p TEST
file="$1".cpp
if [ ! -f "$file" ]; then
    echo "$file not found."
    exit
fi

if ! clang++ -o "$1" $file -std=gnu++11 -O2 -g -Wall -Wcomma
then
    exit
fi

rm -R $MY_NAME* &>/dev/null

i=0
while [ -f "$INPUT_NAME$i" ] && [ -f "$OUTPUT_NAME$i" ]
do
  input="$INPUT_NAME$i"
  output="$OUTPUT_NAME$i"
  myoutput="$MY_NAME$i"

  if ! `which time` -o time.out -f "(%es)" ./"$EXECMD" < $input > $myoutput; then
    echo -e $RED"Sample test #$i: Runtime Error""$DEFAULT"
    cat time.out
    echo "========================================"
    echo "Sample Input #$i"
    cat $input
  elif diff --brief -B --ignore-trailing-space $myoutput $output; then
    echo -e $GREEN"Sample test #$i: Accepted"$DEFAULT
    cat time.out
  else
    echo -e $RED"Sample test #$i: Wrong Answer"$DEFAULT
    cat time.out
    echo "========================================"
    echo "Sample Input #$i"
    cat $input
    echo "========================================"
    echo "Sample Output #$i"
    cat $output
    echo "========================================"
    echo "My Output #$i"
    cat $myoutput
    echo "========================================"
  fi
  i=$[$i+1]
done
