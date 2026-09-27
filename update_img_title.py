import re

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = content.replace('<title>Giải Mã Giai Cấp Và Dân Tộc</title>', '<title>Giải Mã Nhà Nước Và Cách Mạng Xã Hội</title>')
content = content.replace('GIẢI MÃ GIAI CẤP VÀ DÂN TỘC', 'GIẢI MÃ NHÀ NƯỚC VÀ CÁCH MẠNG XÃ HỘI')

# Replace SVG with image
svg_start = content.find('<svg viewBox="0 0 1600 900">')
if svg_start != -1:
    svg_end = content.find('</svg>', svg_start) + 6
    if svg_end > 5:
        img_tag = '<img src="background.png" alt="Bức tranh lịch sử" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; z-index: 0;" />'
        content = content[:svg_start] + img_tag + content[svg_end:]

# Update completion text
content = content.replace('Giai cấp, dân tộc và nhân loại có quan hệ biện chứng với nhau.', 'Bạn đã khám phá thành công bức tranh lịch sử!')

with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated")
