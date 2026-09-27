import re

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "hỗ trợ người dân. Theo quan điểm chủ nghĩa Mác – Lênin, hoạt động này thể hiện vai trò nào của Nhà nước?",
        "hỗ trợ người dân.<br><br><strong>Hỏi:</strong> Theo quan điểm chủ nghĩa Mác – Lênin, hoạt động này thể hiện vai trò nào của Nhà nước?"
    ),
    (
        "phúc lợi xã hội. Theo quan điểm Mác – Lênin, điều gì phản ánh bản chất của Nhà nước?",
        "phúc lợi xã hội.<br><br><strong>Hỏi:</strong> Theo quan điểm Mác – Lênin, điều gì phản ánh bản chất của Nhà nước?"
    ),
    (
        "duy trì trật tự xã hội. Theo chủ nghĩa Mác – Lênin, Nhà nước ra đời do nguyên nhân nào?",
        "duy trì trật tự xã hội.<br><br><strong>Hỏi:</strong> Theo chủ nghĩa Mác – Lênin, Nhà nước ra đời do nguyên nhân nào?"
    ),
    (
        "môi trường. Tình huống này thể hiện điều gì?",
        "môi trường.<br><br><strong>Hỏi:</strong> Tình huống này thể hiện điều gì?"
    ),
    (
        "kinh tế và xã hội. Theo chủ nghĩa Mác – Lênin, cách mạng xã hội có vai trò gì?",
        "kinh tế và xã hội.<br><br><strong>Hỏi:</strong> Theo chủ nghĩa Mác – Lênin, cách mạng xã hội có vai trò gì?"
    ),
    (
        "cách mạng xã hội. Theo quan điểm Mác – Lênin, yếu tố nào có ý nghĩa quan trọng để cách mạng xã hội diễn ra?",
        "cách mạng xã hội.<br><br><strong>Hỏi:</strong> Theo quan điểm Mác – Lênin, yếu tố nào có ý nghĩa quan trọng để cách mạng xã hội diễn ra?"
    )
]

for search_text, replace_text in replacements:
    escaped = re.escape(search_text)
    pattern = escaped.replace(r'\ ', r'\s+')
    content = re.sub(pattern, replace_text, content)

with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated question formatting.")
