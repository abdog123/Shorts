import json, os, re, sys
import anthropic

cid = sys.argv[1]
ch = next(c for c in json.load(open("channels.json", encoding="utf-8")) if c["id"] == cid)
os.makedirs("history", exist_ok=True)
os.makedirs("out", exist_ok=True)
hp = f"history/{cid}.json"
hist = json.load(open(hp, encoding="utf-8")) if os.path.exists(hp) else []

prompt = f"""أنت كاتب محتوى لقناة يوتيوب Shorts اسمها: {ch['name']}.
الأسلوب المطلوب: {ch['style']}
اللهجة: عامية مصرية سهلة وطبيعية.
الطول: حوالي {ch['words']} كلمة.
ممنوع تكرار أي موضوع من دول: {hist[-60:]}
قواعد: ابدأ بجملة تشد المشاهد في أول 3 ثواني. من غير رموز أو إيموجي أو عناوين. اكتب الأرقام بالحروف عشان النطق يطلع صح.
رجّع JSON فقط بالشكل ده:
{{"title": "عنوان جذاب أقل من 70 حرف", "script": "النص كله", "terms": "خمس كلمات بحث إنجليزية للقطات فيديو مفصولة بفواصل", "description": "وصف قصير", "tags": ["كلمة1", "كلمة2"]}}"""

client = anthropic.Anthropic()
r = client.messages.create(model="claude-haiku-5-5", max_tokens=1500,
                           messages=[{"role": "user", "content": prompt}])
m = re.search(r"\{.*\}", r.content[0].text, re.S)
data = json.loads(m.group(0))
json.dump(data, open(f"out/{cid}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
hist.append(data["title"])
json.dump(hist, open(hp, "w", encoding="utf-8"), ensure_ascii=False)
print("OK:", data["title"])
