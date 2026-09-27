import re

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<p class="q-text" style="margin-bottom: 24px;">(.*?)<br><span[^>]*>Tình huống:\s*(.*?)</span></p>'
replacement = r'''<h3 class="q-title">\1</h3>
                <div class="q-situation"><strong>Tình huống:</strong> \2</div>'''

new_content = re.sub(pattern, replacement, content)

new_css = """
        .q-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(28px, 3.5vw, 40px);
            font-weight: 900;
            color: var(--primary);
            text-align: center;
            margin-bottom: 24px;
            letter-spacing: -0.01em;
        }
        .q-situation {
            font-family: 'Inter', sans-serif;
            font-size: 17px;
            font-weight: 500;
            line-height: 1.7;
            color: #334155;
            background: #f8fafc;
            border-left: 5px solid var(--accent);
            padding: 20px 24px;
            border-radius: 0 16px 16px 0;
            margin-bottom: 32px;
            text-align: justify;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
            border-top: 1px solid #e2e8f0;
            border-right: 1px solid #e2e8f0;
            border-bottom: 1px solid #e2e8f0;
        }
"""

if '.q-title {' not in content:
    new_content = new_content.replace('</style>', new_css + '    </style>')

with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Alignment script finished.")
