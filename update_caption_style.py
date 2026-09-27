import sys

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_caption = """                <div id="image-caption" class="hidden" style="position: absolute; bottom: 20px; right: 20px; background: rgba(15, 23, 42, 0.85); color: #fff; padding: 16px 20px; border-radius: 12px; font-family: 'Inter', sans-serif; font-size: 14.5px; text-align: left; z-index: 5; backdrop-filter: blur(8px); box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 320px; line-height: 1.6; border: 1px solid rgba(255,255,255,0.15); transition: opacity 0.5s ease;">
                    <strong style="color: #60a5fa; display: block; margin-bottom: 4px;">Bối cảnh bức tranh:</strong> "Lênin và các chiến sĩ Hồng quân trên đường ra mặt trận Ba Lan năm 1920"
                </div>"""

new_caption = """                <div id="image-caption" class="hidden" style="position: absolute; bottom: 24px; right: 24px; background: linear-gradient(135deg, rgba(220, 38, 38, 0.95), rgba(153, 27, 27, 0.95)); color: #fff; padding: 18px 24px; border-radius: 16px; font-family: 'Inter', sans-serif; font-size: 15px; text-align: left; z-index: 5; backdrop-filter: blur(12px); box-shadow: 0 15px 35px rgba(153, 27, 27, 0.4), inset 0 2px 4px rgba(255,255,255,0.3); max-width: 360px; line-height: 1.6; border: 1px solid rgba(255, 180, 180, 0.4); transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);">
                    <strong style="color: #fde047; font-size: 16px; text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px; text-shadow: 0 2px 4px rgba(0,0,0,0.4);">Bối cảnh lịch sử:</strong> "Lênin và các chiến sĩ Hồng quân trên đường ra mặt trận Ba Lan năm 1920"
                </div>"""

if old_caption in content:
    content = content.replace(old_caption, new_caption)
    with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Caption style updated to vibrant red.")
else:
    print("Old caption not found. Check exact spacing.")
