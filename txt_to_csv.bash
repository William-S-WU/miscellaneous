#!/bin/bash

if [ -z "$1" ]; then # Accepts input file name
  echo "Usage: $0 input_file"
  exit 1
fi

input_file="$1" 
output_file="${input_file%.*}.csv" #create output file name
sed -i 's/,//g' "$input_file"
awk 'BEGIN {FS=": "; OFS=","} {print $1, $2}' "$input_file" > "$output_file"
echo "Conversion complete: $input_file -> $output_file"
