# نظام الـ Shorts اليومي (4 قنوات) → تليجرام

الفيديوهات بتتبعت على تليجرام جاهزة، وإنت بترفعها يدوي على يوتيوب (ملف upload_youtube.py موجود لو عايز تفعّل الرفع التلقائي بعدين).

## الإعداد
1. ارفع المجلد على ريبو GitHub **خاص (Private)**.
2. Settings → Secrets and variables → Actions، وضيف:
   - `sk_343900e3d2e5876749707e0c17bdf7df21c3a417054ff838`
   - `58178574-0e0faf961bc97f89d694f985d` (مجاني من pixabay.com/api/docs)
   - `8507652296:AAEczKvAmsPhmWzqUY2byVLS0nN5x6UCMuw` (توكن البوت من @BotFather)
   - `8055147774` (رقم الشات بتاعك)
3. افتح البوت في تليجرام واضغط **Start** مرة، وإلا مش هيقدر يبعتلك.
4. Actions → daily-shorts → Run workflow للتجربة.

## ملاحظات
- لا تكتب أي مفتاح أو توكن داخل الملفات، حطه في Secrets بس.
- عدّل `channels.json` لتغيير النيش أو الصوت أو الطول.
