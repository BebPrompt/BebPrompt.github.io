# Audio Library

A simple web-based audio library that organizes audio files by artist and category. This site allows users to browse, play, and download audio files along with their descriptions.

## Features

- Hierarchical organization by artist and category
- Audio playback with standard HTML5 audio controls
- Display of text descriptions for each audio file
- Dark mode UI for comfortable viewing
- Collapsible sidebar for maximizing content space
- Responsive design for desktop and mobile devices

## How It Works

1. The website loads a structure of artists and categories from the filesystem
2. When a category is selected, it loads all audio files and their corresponding text descriptions
3. Audio files and descriptions are paired based on matching filenames
4. Audio can be played directly in the browser

## File Structure

The expected file structure is:

```
/
├── index.html
├── 404.html
├── README.md
└── [Artist Name]/
    └── [Category Name]/
        ├── audio_file_1.mp3
        ├── audio_file_1.txt
        ├── audio_file_2.mp3
        ├── audio_file_2.txt
        └── ...
```

## Hosting on GitHub Pages

This site is designed to be hosted directly on GitHub Pages. After pushing to GitHub:

1. Go to your repository settings
2. Navigate to the "Pages" section
3. Select the branch you want to deploy (usually "main")
4. Save the settings and wait for the site to be published

## Local Development

To develop locally, you can use any simple HTTP server. For example:

With Python:
```
python -m http.server
```

With Node.js (after installing `http-server`):
```
npx http-server
```

## Technical Notes

- The site uses the GitHub API to fetch directory contents
- No external JavaScript libraries are required
- Audio playback uses the native HTML5 audio element
- The sidebar can be toggled to maximize screen space, particularly useful on mobile devices 