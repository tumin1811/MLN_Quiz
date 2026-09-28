import re

with open(r'd:\Code\MLN\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the old media query
media_query_pattern = r'        @media \(max-width: 768px\) \{.*?\n        \}\n'
old_mq_match = re.search(media_query_pattern, content, flags=re.DOTALL)
if old_mq_match:
    old_mq = old_mq_match.group(0)
    # Remove it from the current position
    content = content.replace(old_mq, '')
else:
    print("Could not find the old media query!")

# 2. Build the new media query
new_mq = """        @media (max-width: 768px) {
            .app-wrapper {
                padding: 10px;
                gap: 12px;
            }
            header.header-bar {
                flex-direction: column;
                align-items: stretch;
                gap: 12px;
                padding: 16px;
            }
            .title-block {
                text-align: center;
            }
            .controls {
                justify-content: space-between;
                width: 100%;
                gap: 8px;
            }
            .btn {
                padding: 10px 14px;
                font-size: 14px;
                white-space: nowrap;
            }
            .progress-box {
                padding: 8px 16px;
            }
            #progress-count {
                font-size: 18px;
            }
            .answers {
                grid-template-columns: 1fr;
            }
            .pieces {
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(2, 1fr);
                padding: 0;
            }
            #game-title {
                font-size: 20px;
            }
            #game-subtitle {
                font-size: 13px;
            }
            .piece-num {
                font-size: clamp(24px, 8vw, 36px);
            }
            .modal {
                padding: 20px;
                border-radius: 20px;
            }
            .q-title {
                font-size: 22px;
                margin-bottom: 16px;
            }
            .q-situation {
                font-size: 15px;
                padding: 16px;
                margin-bottom: 20px;
                border-left-width: 4px;
            }
            .ans {
                padding: 14px;
                border-radius: 16px;
                gap: 12px;
                min-height: 60px;
            }
            .ans .badge {
                width: 36px;
                height: 36px;
                font-size: 16px;
            }
            .ans-text {
                font-size: 15px;
            }
            #image-caption {
                bottom: 10px !important;
                right: 10px !important;
                left: 10px !important;
                max-width: none !important;
                padding: 12px 16px !important;
                font-size: 13px !important;
                border-radius: 12px !important;
            }
            #image-caption strong {
                font-size: 14px !important;
                margin-bottom: 4px !important;
            }
            .complete-card {
                padding: 40px 24px;
            }
            #complete-text {
                font-size: 24px;
                margin-bottom: 24px;
            }
        }
"""

# 3. Insert the new media query right before </style>
if '</style>' in content:
    content = content.replace('</style>', new_mq + '    </style>')
else:
    print("Could not find </style> tag!")

with open(r'd:\Code\MLN\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile styles updated successfully.")
