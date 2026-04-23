import requests

YOUTUBE_API_KEY = "AIzaSyAgTKAF7pxJ8mrgN2rTm3pm6Z8XpXHL4ds"

def get_youtube_videos(topic, max_results=3):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": topic + " tutorial explained",
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY,
        "relevanceLanguage": "en"
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    videos = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        videos.append({
            "title": title,
            "url": f"https://www.youtube.com/watch?v={video_id}"
        })
    return videos
