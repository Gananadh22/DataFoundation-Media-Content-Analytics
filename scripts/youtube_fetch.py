import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Step 1: Search videos (get multiple IDs)
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

search_params = {
    "part": "snippet",
    "q": "music",
    "type": "video",
    "maxResults": 10,
    "key": API_KEY
}

search_response = requests.get(SEARCH_URL, params=search_params)
search_data = search_response.json()

video_ids = [item["id"]["videoId"] for item in search_data["items"]]

print("Fetched video IDs:")
print(video_ids)

# Step 2: Fetch metrics for each video
VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"

rows = []

for video_id in video_ids:
    params = {
        "part": "snippet,statistics",
        "id": video_id,
        "key": API_KEY
    }

    response = requests.get(VIDEO_URL, params=params)
    data = response.json()

    if not data["items"]:
        continue

    video = data["items"][0]
    stats = video["statistics"]
    snippet = video["snippet"]

    rows.append({
        "video_id": video_id,
        "title": snippet["title"],
        "view_count": int(stats.get("viewCount", 0)),
        "like_count": int(stats.get("likeCount", 0)),
        "comment_count": int(stats.get("commentCount", 0)),
        "published_at": snippet["publishedAt"]
    })

# Step 3: Save to CSV
df = pd.DataFrame(rows)

output_path = "data/processed/youtube_metrics.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")
print(df.head())