import sys

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_tag = '<svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" role="img">'
end_tag = '</svg>'

start_idx = content.find(start_tag)
if start_idx != -1:
    end_idx = content.find(end_tag, start_idx) + len(end_tag)
    img_tag = '<img src="background.png" alt="Bức tranh lịch sử" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; display: block; z-index: 0;" />'
    
    new_content = content[:start_idx] + img_tag + content[end_idx:]
    with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced SVG with img tag.")
else:
    print("Start tag not found.")
