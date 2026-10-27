# نظام الـ Shorts اليومي (4 قنوات) → تليجرام

الفيديوهات بتتبعت على تليجرام جاهزة، وإنت بترفعها يدوي على يوتيوب (ملف upload_youtube.py موجود لو عايز تفعّل الرفع التلقائي بعدين).

## الإعداد
1. ارفع المجلد على ريبو GitHub **خاص (Private)**.
2. Settings → Secrets and variables → Actions، وضيف:
   - `ANTHROPIC_API_KEY`
   - `PIXABAY_KEY` (مجاني من pixabay.com/api/docs)
   - `TG_TOKEN` (توكن البوت من @BotFather)
   - `TG_CHAT` (رقم الشات بتاعك)
3. افتح البوت في تليجرام واضغط **Start** مرة، وإلا مش هيقدر يبعتلك.
4. Actions → daily-shorts → Run workflow للتجربة.

## ملاحظات
- لا تكتب أي مفتاح أو توكن داخل الملفات، حطه في Secrets بس.
- عدّل `channels.json` لتغيير النيش أو الصوت أو الطول.
