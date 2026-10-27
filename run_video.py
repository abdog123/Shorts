import json, sys, time, requests

BASE = "http://127.0.0.1:8080/api/v1"
cid = sys.argv[1]
ch = next(c for c in json.load(open("channels.json", encoding="utf-8")) if c["id"] == cid)
d = json.load(open(f"out/{cid}.json", encoding="utf-8"))

payload = {
    "video_subject": d["title"],
    "video_script": d["script"],
    "video_terms": d["terms"],
    "video_aspect": "9:16",
    "video_source": "pixabay",
    "video_language": "ar-EG",
    "voice_name": ch["voice"],
    "voice_rate": 1.0,
    "subtitle_enabled": True,
    "font_name": "Arabic.ttf",
    "font_size": 60,
    "video_count": 1,
    "bgm_type": "random",
    "bgm_volume": 0.15,
}
r = requests.post(f"{BASE}/videos", json=payload, timeout=60)
r.raise_for_status()
tid = r.json()["data"]["task_id"]
print("task", tid)

for _ in range(120):  # حتى 20 دقيقة
    time.sleep(10)
    t = requests.get(f"{BASE}/tasks/{tid}", timeout=60).json()["data"]
    print("progress", t.get("progress"), "state", t.get("state"))
    if t.get("state") == 1:
        url = t["videos"][0]
        with open(f"out/{cid}.mp4", "wb") as f:
            f.write(requests.get(url, timeout=300).content)
        print("saved")
        sys.exit(0)
    if t.get("state") == -1:
        sys.exit("video generation failed")
sys.exit("timeout")
