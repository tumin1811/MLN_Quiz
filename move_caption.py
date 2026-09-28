import re

with open(r'd:\Code\MLN\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract #image-caption
caption_match = re.search(r'(<div id="image-caption".*?</div>)', content, flags=re.DOTALL)
if not caption_match:
    print("Could not find image-caption")
    exit()

caption_html = caption_match.group(1)
content = content.replace(caption_html, '') # Remove it from current location

# 2. Insert it right after closing of .stage
# We know the closing of .stage is before </main>
stage_close_match = re.search(r'(\s*</div>\s*</main>)', content)
if not stage_close_match:
    print("Could not find closing of stage")
    exit()

content = content.replace(
    stage_close_match.group(1),
    f'\n                </div>\n{caption_html}\n        </main>'
)

# 3. Update mobile CSS for image-caption
old_mobile_caption = """            #image-caption {
                bottom: 10px !important;
                right: 10px !important;
                left: 10px !important;
                max-width: none !important;
                padding: 12px 16px !important;
                font-size: 13px !important;
                border-radius: 12px !important;
            }"""

new_mobile_caption = """            #image-caption {
                position: relative !important;
                bottom: auto !important;
                right: auto !important;
                left: auto !important;
                margin-top: 16px !important;
                width: 100% !important;
                max-width: none !important;
                padding: 12px 16px !important;
                font-size: 13px !important;
                border-radius: 12px !important;
                box-sizing: border-box !important;
            }"""

if old_mobile_caption in content:
    content = content.replace(old_mobile_caption, new_mobile_caption)
else:
    print("Warning: Could not find old mobile caption CSS to replace.")

with open(r'd:\Code\MLN\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully moved image caption outside stage and updated CSS.")
