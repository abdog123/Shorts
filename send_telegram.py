import json, os, sys
import requests

cid = sys.argv[1]
ch = next(c for c in json.load(open("channels.json", encoding="utf-8")) if c["id"] == cid)
d = json.load(open(f"out/{cid}.json", encoding="utf-8"))
token, chat = os.environ["TG_TOKEN"], os.environ["TG_CHAT"]

tags = " ".join("#" + t.replace(" ", "_") for t in d.get("tags", []))
caption = f"📺 {ch['name']}\n\n{d['title']}\n\n{d['description']}\n\n{tags}\n#Shorts"[:1000]

with open(f"out/{cid}.mp4", "rb") as f:
    r = requests.post(f"https://api.telegram.org/bot{token}/sendVideo",
                      data={"chat_id": chat, "caption": caption, "supports_streaming": "true"},
                      files={"video": f}, timeout=600)
print(r.status_code, r.text[:200])
r.raise_for_status()
