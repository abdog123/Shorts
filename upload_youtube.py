import datetime as dt, json, os, sys
from zoneinfo import ZoneInfo
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

cid = sys.argv[1]
ch = next(c for c in json.load(open("channels.json", encoding="utf-8")) if c["id"] == cid)
d = json.load(open(f"out/{cid}.json", encoding="utf-8"))
path = f"out/{cid}.mp4"


def tg(msg, video=None):
    t, c = os.environ.get("TG_TOKEN"), os.environ.get("TG_CHAT")
    if not t or not c:
        return
    if video:
        requests.post(f"https://api.telegram.org/bot{t}/sendVideo",
                      data={"chat_id": c, "caption": msg[:1000]},
                      files={"video": open(video, "rb")}, timeout=300)
    else:
        requests.post(f"https://api.telegram.org/bot{t}/sendMessage",
                      data={"chat_id": c, "text": msg}, timeout=60)


try:
    creds = Credentials(None, refresh_token=os.environ["YT_REFRESH"],
                        client_id=os.environ["YT_CLIENT_ID"],
                        client_secret=os.environ["YT_CLIENT_SECRET"],
                        token_uri="https://oauth2.googleapis.com/token")
    yt = build("youtube", "v3", credentials=creds)

    tz = ZoneInfo("Africa/Cairo")  # يتعامل مع التوقيت الصيفي تلقائياً
    now = dt.datetime.now(tz)
    pub = now.replace(hour=14, minute=0, second=0, microsecond=0)
    if pub <= now + dt.timedelta(minutes=15):
        pub += dt.timedelta(days=1)
    publish_at = pub.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

    body = {
        "snippet": {"title": d["title"][:95],
                    "description": d["description"] + "\n\n#Shorts",
                    "tags": d.get("tags", []), "categoryId": "24",
                    "defaultLanguage": "ar"},
        "status": {"privacyStatus": "private", "publishAt": publish_at,
                   "selfDeclaredMadeForKids": bool(ch["kids"])},
    }
    media = MediaFileUpload(path, mimetype="video/mp4", resumable=True)
    res = yt.videos().insert(part="snippet,status", body=body, media_body=media).execute()
    print("uploaded", res["id"], "publish at", publish_at)
except Exception as e:
    print("upload failed:", e)
    tg(f"[{ch['name']}] فشل الرفع: {e}\n{d['title']}", path)
    sys.exit(1)
