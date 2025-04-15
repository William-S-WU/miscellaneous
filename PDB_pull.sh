#!/bin/bash
ACCESSION_FILE="accession_numbers.txt"
# Base URL for downloading files from PDB
BASE_URL="https://files.rcsb.org/download"
# Read accession numbers from the file and download each file
# Read the file into an array
mapfile -t ACCESSION_ARRAY < "$ACCESSION_FILE"
for ACCESSION in "${ACCESSION_ARRAY[@]}"; do
  ACCESSION=$(echo "$ACCESSION" | tr -d '\r')
  echo "Downloading file for accession number: $ACCESSION"
  echo "$ACCESSION.pdb"
  curl "$BASE_URL/$ACCESSION.pdb" -o "$ACCESSION.pdb"
  echo "Download complete for: $ACCESSION"
done < "$ACCESSION_FILE"
echo "All downloads complete!"
