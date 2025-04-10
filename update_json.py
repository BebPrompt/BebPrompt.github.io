import os
import json
import glob
from urllib.parse import quote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GITHUB_RAW_URL = "https://raw.githubusercontent.com/BebPrompt/BebPrompt.github.io/main"
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.m4a', '.ogg']
TEXT_EXTENSIONS = ['.txt']

def get_artist_directories():
    """Get all artist directories (immediate subdirectories of the base dir)"""
    return [d for d in os.listdir(BASE_DIR) 
            if os.path.isdir(os.path.join(BASE_DIR, d))
            and not d.startswith('.') and not d.startswith('_')]

def get_category_directories(artist):
    """Get all category directories for an artist"""
    artist_path = os.path.join(BASE_DIR, artist)
    return [d for d in os.listdir(artist_path) 
            if os.path.isdir(os.path.join(artist_path, d))
            and not d.startswith('.') and not d.startswith('_')]

def create_category_json(artist, category):
    """Create or update a category.json file"""
    category_path = os.path.join(BASE_DIR, artist, category)
    json_path = os.path.join(category_path, "category.json")
    
    # Find all audio files in the category directory
    audio_files = []
    for ext in AUDIO_EXTENSIONS:
        audio_files.extend(glob.glob(os.path.join(category_path, f"*{ext}")))
    
    files_data = []
    for audio_file in audio_files:
        filename = os.path.basename(audio_file)
        name, ext = os.path.splitext(filename)
        
        # Look for corresponding text file
        txt_file = None
        for text_ext in TEXT_EXTENSIONS:
            possible_txt = os.path.join(category_path, f"{name}{text_ext}")
            if os.path.exists(possible_txt):
                txt_file = possible_txt
                break
        
        if txt_file:
            # Create URL-safe paths for GitHub
            rel_audio_path = os.path.join(artist, category, filename).replace('\\', '/')
            rel_txt_path = os.path.join(artist, category, os.path.basename(txt_file)).replace('\\', '/')
            
            # Use URL quoting for spaces in filenames
            github_audio_url = f"{GITHUB_RAW_URL}/{quote(rel_audio_path)}"
            github_txt_url = f"{GITHUB_RAW_URL}/{quote(rel_txt_path)}"
            
            files_data.append({
                "name": name,
                "audioPath": github_audio_url,
                "descPath": github_txt_url
            })
    
    # Sort files by name
    files_data.sort(key=lambda x: x["name"])
    
    # Create or update the JSON file
    category_data = {
        "category": category,
        "files": files_data
    }
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(category_data, f, indent=2)
    
    print(f"Updated {json_path} with {len(files_data)} files")
    return len(files_data)

def create_artist_metadata(artist):
    """Create or update an artist's metadata.json file"""
    artist_path = os.path.join(BASE_DIR, artist)
    json_path = os.path.join(artist_path, "metadata.json")
    
    categories = get_category_directories(artist)
    categories_data = []
    
    for category in categories:
        category_json_path = os.path.join(artist, category, "category.json").replace('\\', '/')
        github_json_url = f"{GITHUB_RAW_URL}/{quote(category_json_path)}"
        
        categories_data.append({
            "name": category,
            "jsonPath": github_json_url
        })
    
    # Sort categories by name
    categories_data.sort(key=lambda x: x["name"])
    
    # Create or update the metadata file
    metadata = {
        "artist": artist,
        "categories": categories_data
    }
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Updated {json_path} with {len(categories_data)} categories")
    return len(categories_data)

def create_artists_json():
    """Create or update the main artists.json file"""
    json_path = os.path.join(BASE_DIR, "artists.json")
    
    artists = get_artist_directories()
    artists_data = []
    
    for artist in artists:
        metadata_path = os.path.join(artist, "metadata.json").replace('\\', '/')
        github_metadata_url = f"{GITHUB_RAW_URL}/{quote(metadata_path)}"
        
        artists_data.append({
            "name": artist,
            "metadataPath": github_metadata_url
        })
    
    # Sort artists by name
    artists_data.sort(key=lambda x: x["name"])
    
    # Create or update the artists file
    data = {
        "artists": artists_data
    }
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated {json_path} with {len(artists_data)} artists")
    return len(artists_data)

def main():
    print("Starting JSON update process...")
    
    # Get all artists
    artists = get_artist_directories()
    total_categories = 0
    total_files = 0
    
    # Process each artist
    for artist in artists:
        print(f"\nProcessing artist: {artist}")
        
        # Get all categories for this artist
        categories = get_category_directories(artist)
        
        # Process each category
        for category in categories:
            print(f"Processing category: {category}")
            files_count = create_category_json(artist, category)
            total_files += files_count
        
        # Create/update artist metadata
        categories_count = create_artist_metadata(artist)
        total_categories += categories_count
    
    # Create/update main artists.json
    artists_count = create_artists_json()
    
    print("\nUpdate complete!")
    print(f"Updated {artists_count} artists, {total_categories} categories, and {total_files} files")

if __name__ == "__main__":
    main() 