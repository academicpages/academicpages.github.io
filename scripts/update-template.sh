#!/bin/bash

# Update your site from the latest template
# Original template repository URL: https://github.com/pm25/showlit

set -e

TEMPLATE_REPO="https://github.com/pm25/showlit.git"
TMP_DIR="$(mktemp -d)"
BACKUP_DIR="./backup/$(date +%Y%m%d%H%M%S)"

echo "💡 Creating backup of current template-related files in $BACKUP_DIR..."
mkdir -p "$BACKUP_DIR"

# List of directories/files to update from template
FILES_TO_UPDATE=(
  # "config"
  "src"
  "scripts"
  "package.json"
  "package-lock.json"
  "README.md"
  "CHANGELOG.md"
  ".gitignore"
)

# Backup current files
for f in "${FILES_TO_UPDATE[@]}"; do
  if [ -e "$f" ]; then
    cp -r "$f" "$BACKUP_DIR/"
  fi
done

echo "💡 Downloading latest template into temporary directory..."
git clone --depth 1 "$TEMPLATE_REPO" "$TMP_DIR"

echo "💡 Checking for updates..."
for f in "${FILES_TO_UPDATE[@]}"; do
  SRC="$TMP_DIR/$f"
  DEST="./$f"

  if [ ! -e "$SRC" ]; then
    continue
  fi

  if [ -e "$DEST" ]; then
    diff_output=$(diff -qr "$SRC" "$DEST" || true)
    if [ -z "$diff_output" ]; then
      echo "✅ $f is up-to-date, skipping."
      continue
    fi

    echo "------"
    echo "⚠️  Changes detected in $f:"
    echo "$diff_output"
    read -p "Do you want to overwrite $f? (y/N): " choice
    if [[ "$choice" =~ ^[Yy]$ ]]; then
      cp -r "$SRC" "$DEST"
      echo "✅ $f updated."
    else
      echo "⏩ $f skipped."
    fi
  else
    cp -r "$SRC" "$DEST"
    echo "✅ $f added."
  fi
done

# Clean up
rm -rf "$TMP_DIR"

echo "🎉 Template update complete! Your previous files are backed up in $BACKUP_DIR."
