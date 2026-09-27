import re

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace aspect-ratio
content = re.sub(
    r'aspect-ratio:\s*16/9;',
    r'aspect-ratio: 706 / 474;',
    content
)

# Replace img tags
img_pattern = r'<img src="background.png" alt="Bức tranh lịch sử nền".*?z-index: 0;" />'
content = re.sub(img_pattern, '', content, flags=re.DOTALL)

img_pattern2 = r'<img src="background.png" alt="Bức tranh lịch sử".*?z-index: 0;" />'
replacement_img = '<img src="background.png" alt="Bức tranh lịch sử" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; image-rendering: high-quality; filter: contrast(1.08) saturate(1.1) brightness(1.02); display: block; z-index: 0;" />'
content = re.sub(img_pattern2, replacement_img, content, flags=re.DOTALL)

# Clean up empty lines where first img was
content = content.replace('<!-- Hình nền kết quả: Vẽ bằng SVG thay vì ảnh ngoài -->\n                \n                <img', '<!-- Hình nền kết quả -->\n                <img')

with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated aspect ratio and images")
