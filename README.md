# BebPrompt Audio Library

This repository contains an audio library website for BebPrompt, organized with a JSON-based dynamic loading system.

## Project Structure

The project follows this directory structure:

```
BebPrompt.github.io/
├── index.html           # The main website
├── artists.json         # List of all artists with metadata links
├── update_json.py       # Script to update all JSON files
├── README.md            # This file
├── [Artist1]/           # Artist directory (e.g., Penelope)
│   ├── metadata.json    # Artist metadata with categories
│   ├── [Category1]/     # Category directory (e.g., Original)
│   │   ├── category.json # Category data with file listings
│   │   ├── file1.mp3    # Audio files
│   │   ├── file1.txt    # Description files (matching audio filenames)
│   │   └── ...
│   ├── [Category2]/
│   │   └── ...
│   └── ...
└── [Artist2]/
    └── ...
```

## How It Works

1. The website loads `artists.json` to get a list of all artists
2. For each artist, it loads their `metadata.json` to get categories
3. When a category is selected, it loads the corresponding `category.json`
4. Audio files and their descriptions are displayed based on the category data

## Updating the Library

### Adding New Content

To add new content to the library:

1. Place audio files in the appropriate artist/category directory
2. Create matching `.txt` files with the same name for descriptions
3. Run the update script to regenerate all JSON files

### Using the Update Script

The `update_json.py` script automatically scans the directory structure and updates all JSON files with the correct content and URLs.

To run the script:

```bash
python update_json.py
```

This will:
1. Scan all artist directories
2. For each artist, scan all category directories
3. For each category, find all audio files and their matching description files
4. Generate or update the appropriate JSON files with proper GitHub raw URLs
5. Sort all entries alphabetically for consistency

## Supported File Types

- Audio files: `.mp3`, `.wav`, `.m4a`, `.ogg`
- Description files: `.txt`

## Important Notes

- Audio files must have matching description text files with the same base name
- The script assumes the site is hosted on GitHub Pages from the main branch
- File and directory names shouldn't start with `.` or `_` to be recognized
- Add only the files you want to include in the library; the script processes all matching files

## Development

### Local Testing

For local testing, you can:

1. Run the `update_json.py` script to generate all JSON files
2. Use a local server to test the website (e.g., `python -m http.server`)
3. Open `http://localhost:8000` in your browser 