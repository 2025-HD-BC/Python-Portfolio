# Smart File Organizer

An intelligent file organization tool that automatically sorts files by type, date, and custom rules.

## Overview

This automation script demonstrates:
- File system operations with pathlib
- Automatic file categorization
- Safe file operations with backup
- Comprehensive logging
- Configuration management
- Duplicate detection

## Features

- **Automatic Organization**: Sorts files by type (documents, images, videos, etc.)
- **Date-based Organization**: Groups files by date if desired
- **Duplicate Detection**: Identifies duplicate files using hash comparison
- **Safe Operations**: Creates backups before moving files
- **Dry Run Mode**: Preview changes without making them
- **Customizable Rules**: Configure file type categories and rules
- **Detailed Logging**: Track all operations with timestamps

## Usage

### Basic Organization
```bash
# Organize downloads folder
python file_organizer.py --source "C:\Users\YourName\Downloads"

# Dry run (preview without changes)
python file_organizer.py --source "C:\Users\YourName\Downloads" --dry-run

# Organize by date
python file_organizer.py --source "C:\path\to\folder" --by-date

# Find duplicates
python file_organizer.py --source "C:\path\to\folder" --find-duplicates
```

### Configuration

Edit `config.json` to customize:
- File type categories
- Destination folders
- Ignored file extensions
- Naming conventions

## File Categories

Default categories:
- **Documents**: .pdf, .doc, .docx, .txt, .xlsx, .pptx
- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .svg
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv
- **Audio**: .mp3, .wav, .flac, .aac
- **Archives**: .zip, .rar, .7z, .tar, .gz
- **Code**: .py, .js, .java, .cpp, .html, .css

## Safety Features

- Creates backup before operations
- Validates file integrity after moves
- Handles file naming conflicts
- Comprehensive error handling
- Rollback capability
