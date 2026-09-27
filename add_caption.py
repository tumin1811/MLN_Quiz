import sys

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add caption HTML right after the background img
caption_html = """
                <div id="image-caption" class="hidden" style="position: absolute; bottom: 20px; right: 20px; background: rgba(15, 23, 42, 0.85); color: #fff; padding: 16px 20px; border-radius: 12px; font-family: 'Inter', sans-serif; font-size: 14.5px; text-align: left; z-index: 5; backdrop-filter: blur(8px); box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 320px; line-height: 1.6; border: 1px solid rgba(255,255,255,0.15); transition: opacity 0.5s ease;">
                    <strong style="color: #60a5fa; display: block; margin-bottom: 4px;">Bối cảnh bức tranh:</strong> "Lênin và các chiến sĩ Hồng quân trên đường ra mặt trận Ba Lan năm 1920"
                </div>
"""
img_tag = '<img src="background.png" alt="Bức tranh lịch sử" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; image-rendering: high-quality; filter: contrast(1.08) saturate(1.1) brightness(1.02); display: block; z-index: 0;" />'
if img_tag in content:
    content = content.replace(img_tag, img_tag + caption_html)

# Update finish()
finish_old = "completeEl.classList.remove('hidden');"
finish_new = "completeEl.classList.remove('hidden');\n                    const caption = document.getElementById('image-caption');\n                    if (caption) caption.classList.remove('hidden');"
if finish_old in content:
    content = content.replace(finish_old, finish_new)

# Update reset()
reset_old = "completeEl.classList.add('hidden');"
reset_new = "completeEl.classList.add('hidden'); \n                const caption = document.getElementById('image-caption');\n                if (caption) caption.classList.add('hidden');"
if reset_old in content:
    content = content.replace(reset_old, reset_new)

# Update 'Hiện đáp án' button
show_answers_old = "document.getElementById('show-answers').addEventListener('click', () => {"
show_answers_new = "document.getElementById('show-answers').addEventListener('click', () => {\n                const caption = document.getElementById('image-caption');\n                if (caption) caption.classList.remove('hidden');"
if show_answers_old in content:
    content = content.replace(show_answers_old, show_answers_new)

with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added caption and logic")
