#!/bin/bash

# Loop through all files in the current directory
for file in *info.txt; do
    echo "Processing file: $file"
    # Use sed to delete lines starting with 'path   :'
    sed -i '/^path   :/d' "$file"
    # Verify the changes
    echo "Updated file: $file"
    echo "Content after update:"
    cat "$file"
done

echo "Lines starting with 'path   :' have been removed from all .info.txt files."
