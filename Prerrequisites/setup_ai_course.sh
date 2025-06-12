#!/bin/bash

ROOT="ai_python_course"
FOLDERS=("notebooks" "data" "src" "results")

mkdir -p $ROOT
for FOLDER in "${FOLDERS[@]}"; do
    mkdir -p "$ROOT/$FOLDER"
done

touch "$ROOT/README.md"
touch "$ROOT/requirements.txt"
touch "$ROOT/Makefile"

echo "Directory structure created successfully!"
