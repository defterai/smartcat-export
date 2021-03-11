#! /bin/sh

# Export document or exit if scripr fails
set -eu

printf "\nExport document %s:%s to %s...\n" "$3" "$4" "$5"

python3 export-smartcat.py $1 $2 $3 $4 $5 || { printf "\nUnable to export %s document.\n" "$5"; exit 1; }

printf "\nSuccessfully exported %s file.\n" "$5"