from yt_dlp.extractor.beacon import parse_vtt_chapters
with open('7NVsYA5c.vtt', encoding='utf-8') as f:
    vtt = f.read()
chapters = parse_vtt_chapters(vtt)
import json
print(json.dumps(chapters, indent=2))
