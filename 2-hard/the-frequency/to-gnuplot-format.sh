#!/bin/bash
set -eu

OUTPUT_DIR=$(pwd)/gnuplot

if [ $# -ne 1 ]
then
    echo "Usage: $0 <input-text-file>"
    exit 1
fi

input_text_file=$1
IFS='
'
counter=0
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

for line in $(cat $input_text_file)
do
    IFS=' '
    for point in $line
    do
        echo $point >> "$OUTPUT_DIR/$counter.txt"
    done

    echo "plot \"$OUTPUT_DIR/$counter.txt\"" > "$OUTPUT_DIR/$counter.p"
    echo "gnuplot -persist $OUTPUT_DIR/$counter.p" > "$OUTPUT_DIR/$counter.sh"

    chmod a+x "$OUTPUT_DIR/$counter.sh"

    counter=$(($counter+1))
done

echo "Done (output in $OUTPUT_DIR)."
