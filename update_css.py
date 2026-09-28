import sys

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_head = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giải Mã Giai Cấp Và Dân Tộc</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-main: #f8fafc;
            --panel-bg: rgba(255, 255, 255, 0.85);
            --primary: #1e3a8a;
            --primary-hover: #1e40af;
            --accent: #3b82f6;
            --accent-light: #eff6ff;
            --text: #0f172a;
            --text-muted: #64748b;
            --border: rgba(226, 232, 240, 0.8);
            --success: #10b981;
            --error: #ef4444;
            --vh: 1vh;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        html, body { width: 100%; height: 100%; overflow: hidden; }
        
        body {
            font-family: 'Inter', system-ui, sans-serif;
            color: var(--text);
            /* Premium soft mesh gradient background */
            background: radial-gradient(circle at 15% 50%, rgba(224, 242, 254, 0.6), transparent 25%),
                        radial-gradient(circle at 85% 30%, rgba(219, 234, 254, 0.8), transparent 25%),
                        #f1f5f9;
            height: calc(100 * var(--vh));
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .app-wrapper {
            position: relative;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            padding: clamp(16px, 2vh, 32px) clamp(20px, 3vw, 40px);
            gap: clamp(16px, 2.5vh, 24px);
            max-width: 1600px;
            margin: 0 auto;
            z-index: 1;
        }

        /* Glassmorphism Header */
        header.header-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex: 0 0 auto;
            background: var(--panel-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            padding: 20px 32px;
            border-radius: 24px;
            box-shadow: 0 10px 30px -10px rgba(30, 58, 138, 0.1), inset 0 1px 0 rgba(255,255,255,0.6);
            border: 1px solid rgba(255,255,255,0.4);
        }

        .title-block { min-width: 0; }
        
        #game-title {
            font-family: 'Playfair Display', serif;
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: clamp(26px, 3.5vw, 36px);
            font-weight: 900;
            line-height: 1.2;
            letter-spacing: 0.01em;
            text-shadow: 0 4px 15px rgba(59, 130, 246, 0.1);
        }
        
        #game-subtitle {
            color: var(--text-muted);
            font-size: clamp(14px, 1.5vw, 16px);
            margin-top: 6px;
            font-weight: 500;
            letter-spacing: 0.02em;
        }

        .controls { display: flex; align-items: center; gap: 16px; flex: 0 0 auto; }
        
        .progress-box {
            display: flex; align-items: baseline; gap: 8px;
            padding: 10px 24px;
            border-radius: 99px;
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(59, 130, 246, 0.2);
            color: var(--primary);
            font-weight: 600;
            box-shadow: inset 0 2px 4px rgba(255,255,255,0.5);
        }
        
        #progress-count {
            font-size: clamp(20px, 2.5vw, 24px);
            font-weight: 800;
            color: var(--accent);
            font-variant-numeric: tabular-nums;
        }

        .btn {
            cursor: pointer;
            background: #ffffff;
            border: 1px solid var(--border);
            color: var(--primary);
            border-radius: 99px; /* Pill shape */
            padding: 12px 28px;
            font-weight: 700;
            font-size: 15px;
            font-family: inherit;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 4px 10px rgba(0,0,0,0.04), inset 0 1px 0 rgba(255,255,255,1);
        }
        
        .btn:hover {
            background: var(--accent-light);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.15);
            border-color: rgba(59, 130, 246, 0.3);
            color: var(--accent);
        }
        
        .btn:active { transform: translateY(1px); }
        
        .btn-primary {
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
            border: none;
            color: white;
            box-shadow: 0 6px 15px rgba(30, 58, 138, 0.25), inset 0 1px 0 rgba(255,255,255,0.2);
        }
        
        .btn-primary:hover {
            background: linear-gradient(135deg, #1e40af 0%, #1d4ed8 100%);
            color: white;
            box-shadow: 0 10px 25px rgba(30, 58, 138, 0.35);
        }

        main.stage-area {
            flex: 1 1 auto; min-height: 0; display: flex; align-items: center; justify-content: center;
        }

        .stage {
            position: relative; height: 100%; max-width: 100%; aspect-ratio: 16/9;
            border-radius: 28px; overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(30, 58, 138, 0.2), 0 0 0 1px rgba(255,255,255,0.6) inset;
            background: #ffffff;
        }

        .stage svg {
            position: absolute; inset: 0; width: 100%; height: 100%; display: block;
        }

        .pieces {
            position: absolute; inset: 0; display: grid;
            grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(2, 1fr);
            gap: 12px;
            padding: 12px;
        }

        .piece {
            position: relative; cursor: pointer; border: none;
            display: flex; align-items: center; justify-content: center;
            border-radius: 20px;
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 10px 20px rgba(0,0,0,0.15), inset 0 2px 4px rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.1);
            overflow: hidden;
        }
        
        /* Subtle diagonal shimmer effect on tiles */
        .piece::before {
            content: '';
            position: absolute; inset: 0;
            background: linear-gradient(105deg, transparent 20%, rgba(255,255,255,0.1) 25%, transparent 30%);
            background-size: 200% 200%;
            transition: all 0.5s ease;
        }

        .piece:nth-child(odd) { background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); }
        .piece:nth-child(even) { background: linear-gradient(135deg, #334155 0%, #475569 100%); }

        .piece:hover {
            transform: scale(1.03) translateY(-4px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.25), inset 0 2px 4px rgba(255,255,255,0.3);
            z-index: 10;
        }
        .piece:hover::before {
            background-position: 100% 100%;
        }

        .piece-num {
            font-family: 'Playfair Display', serif; font-weight: 800; font-size: clamp(48px, 6vw, 72px);
            color: white; 
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            text-shadow: 0 4px 20px rgba(0,0,0,0.3);
            z-index: 2;
        }

        .piece:hover .piece-num { transform: scale(1.15); text-shadow: 0 8px 30px rgba(0,0,0,0.4); }
        .piece.opened { opacity: 0; transform: scale(0.8) translateY(20px); pointer-events: none; }
        .piece.gone { visibility: hidden; }
        .piece.shake { animation: shake 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97) both; }

        /* Modal */
        .overlay {
            position: fixed; inset: 0; background: rgba(15, 23, 42, 0.4);
            display: flex; align-items: center; justify-content: center;
            padding: 2vh 2vw; z-index: 20; 
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            opacity: 1; transition: opacity 0.3s ease;
        }
        
        .hidden { display: none !important; }

        .modal {
            width: min(900px, 94vw); max-height: 92vh; display: flex; flex-direction: column;
            background: rgba(255,255,255,0.98); 
            border-radius: 32px; position: relative; overflow-y: auto; overflow-x: hidden;
            box-shadow: 0 40px 80px -20px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255,255,255,1);
            padding: clamp(32px, 5vh, 48px);
            border: 1px solid rgba(255,255,255,0.5);
            transform: translateY(0) scale(1);
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .modal.shake { animation: shake 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97) both; }
        
        @keyframes shake {
            10%, 90% { transform: translate3d(-2px, 0, 0); }
            20%, 80% { transform: translate3d(4px, 0, 0); }
            30%, 50%, 70% { transform: translate3d(-8px, 0, 0); }
            40%, 60% { transform: translate3d(8px, 0, 0); }
        }

        .modal-head {
            display: flex; align-items: center; gap: 12px; margin-bottom: 32px;
        }

        #modal-kicker { 
            color: var(--text-muted); font-weight: 700; text-transform: uppercase; 
            letter-spacing: 0.15em; font-size: 14px; 
            background: #f1f5f9; padding: 6px 14px; border-radius: 99px;
        }
        #modal-num { font-weight: 800; color: var(--accent); font-size: 20px; }
        
        .close-x {
            margin-left: auto; background: #f8fafc; border: 1px solid var(--border); 
            width: 44px; height: 44px; border-radius: 50%; font-size: 18px; 
            cursor: pointer; color: var(--text-muted);
            display: grid; place-items: center; transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }
        
        .close-x:hover { 
            background: #fee2e2; color: var(--error); border-color: #fca5a5;
            transform: rotate(90deg); 
        }

        .q-text {
            line-height: 1.4; margin-bottom: 40px; font-family: 'Playfair Display', serif;
            font-size: clamp(28px, 3.5vw, 40px); font-weight: 800; color: var(--primary);
            text-align: center; letter-spacing: -0.01em;
        }

        .answers { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }

        .ans {
            display: flex; align-items: center; gap: 20px; text-align: left; cursor: pointer;
            border: 2px solid transparent; border-radius: 24px; padding: 20px 24px;
            background: var(--bg-main); color: var(--text); font-family: inherit;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); min-height: 80px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        }

        .ans:hover { 
            background: #ffffff; border-color: var(--accent); 
            box-shadow: 0 10px 25px rgba(59, 130, 246, 0.15);
            transform: translateY(-3px);
        }
        
        .ans .badge {
            flex: 0 0 auto; width: 48px; height: 48px; border-radius: 50%; display: grid; place-items: center;
            background: #ffffff; color: var(--primary); font-weight: 800; font-size: 20px;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            border: 1px solid var(--border);
        }

        .ans:hover .badge { 
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
            color: white; border-color: transparent;
            box-shadow: 0 8px 20px rgba(30, 58, 138, 0.3);
        }

        .ans-text { font-size: 17px; font-weight: 600; line-height: 1.5; }

        .ans.wrong { 
            background: #fef2f2; border-color: var(--error); color: #991b1b; 
            animation: shake 0.5s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
        }
        .ans.wrong .badge { background: var(--error); color: white; border-color: transparent; }
        
        .ans.right { 
            background: #f0fdf4; border-color: var(--success); color: #166534; 
        }
        .ans.right .badge { background: var(--success); color: white; border-color: transparent; }
        .answers.locked .ans { pointer-events: none; }

        .feedback {
            margin-top: 32px; min-height: 28px; font-weight: 700; text-align: center; font-size: 20px;
        }
        #fb-wrong { color: var(--error); }
        #fb-right { color: var(--success); }

        /* Complete */
        .complete {
            position: fixed; inset: 0; z-index: 30; display: flex; align-items: center; justify-content: center;
            background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(16px); padding: 24px;
        }
        
        .complete-card {
            position: relative; z-index: 2; max-width: 650px; text-align: center;
            background: rgba(255,255,255,0.95); border-radius: 36px; padding: 56px 40px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255,255,255,1);
            animation: pop 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
            border: 1px solid rgba(255,255,255,0.6);
        }

        #complete-text {
            line-height: 1.5; margin-bottom: 40px; font-family: 'Playfair Display', serif;
            font-size: 32px; font-weight: 800; color: var(--primary);
            text-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .confetti { position: absolute; top: -20px; width: 12px; height: 16px; z-index: 1; animation: fall linear forwards; }
        @keyframes fall { to { transform: translateY(110vh) rotate(720deg); } }

        @media (max-width: 768px) {
            header.header-bar { flex-wrap: wrap; gap: 16px; padding: 16px 24px; border-radius: 20px; }
            .answers { grid-template-columns: 1fr; }
            .pieces { grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(3, 1fr); padding: 8px;}
            #game-title { font-size: 22px; }
            .piece-num { font-size: 48px; }
            .modal { padding: 24px; border-radius: 24px; }
            .q-text { font-size: 24px; margin-bottom: 24px; }
            .ans { padding: 16px; border-radius: 16px; }
        }
    </style>
</head>
"""

start_index = 0
for i, line in enumerate(lines):
    if line.strip() == "<body>":
        start_index = i
        break

final_html = new_head + "".join(lines[start_index:])
with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("CSS updated successfully.")
