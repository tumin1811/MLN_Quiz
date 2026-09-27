import sys

with open(r'd:\Code\MLN\quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

split_marker = r'<!-- Modal cho câu hỏi -->'
parts = content.split(split_marker)

new_modal_and_js = """<!-- Modal cho câu hỏi -->
    <div class="overlay hidden" id="overlay">
        <section class="modal" id="modal" role="dialog" aria-modal="true" aria-labelledby="modal-kicker">
            <div class="modal-head">
                <div style="display: flex; align-items: baseline; gap: 8px;">
                    <span id="modal-kicker">MẢNH GHÉP</span>
                    <span id="modal-num"></span>
                </div>
                <button type="button" class="close-x" id="close-btn" aria-label="Đóng">✕</button>
            </div>
            
            <div class="question hidden" data-q="0">
                <p class="q-text" style="margin-bottom: 24px;">Câu 1: Vai trò của Nhà nước<br><span style="font-size: 0.55em; font-weight: 500; font-family: 'Inter', sans-serif; color: var(--text-muted); display: block; margin-top: 16px; line-height: 1.6;">Tình huống: Khi xảy ra thiên tai, Nhà nước huy động ngân sách, lực lượng cứu hộ và các nguồn lực xã hội để hỗ trợ người dân. Theo quan điểm chủ nghĩa Mác – Lênin, hoạt động này thể hiện vai trò nào của Nhà nước?</span></p>
                <div class="answers">
                    <button type="button" class="ans" data-k="0"><span class="badge">A</span><span class="ans-text">Chỉ bảo vệ lợi ích của một cá nhân trong xã hội.</span></button>
                    <button type="button" class="ans" data-k="1"><span class="badge">B</span><span class="ans-text">Thực hiện chức năng quản lý xã hội và bảo đảm trật tự.</span></button>
                    <button type="button" class="ans" data-k="2"><span class="badge">C</span><span class="ans-text">Xóa bỏ hoàn toàn sự khác biệt giữa các giai cấp.</span></button>
                    <button type="button" class="ans" data-k="3"><span class="badge">D</span><span class="ans-text">Thay thế mọi hoạt động của người dân.</span></button>
                </div>
            </div>

            <div class="question hidden" data-q="1">
                <p class="q-text" style="margin-bottom: 24px;">Câu 2: Bản chất của Nhà nước<br><span style="font-size: 0.55em; font-weight: 500; font-family: 'Inter', sans-serif; color: var(--text-muted); display: block; margin-top: 16px; line-height: 1.6;">Tình huống: Trong xã hội hiện đại, Nhà nước ban hành các chính sách về thuế, tiền lương và phúc lợi xã hội. Theo quan điểm Mác – Lênin, điều gì phản ánh bản chất của Nhà nước?</span></p>
                <div class="answers">
                    <button type="button" class="ans" data-k="0"><span class="badge">A</span><span class="ans-text">Nhà nước luôn đứng ngoài mọi quan hệ giai cấp.</span></button>
                    <button type="button" class="ans" data-k="1"><span class="badge">B</span><span class="ans-text">Nhà nước chỉ tồn tại để phục vụ lợi ích kinh tế.</span></button>
                    <button type="button" class="ans" data-k="2"><span class="badge">C</span><span class="ans-text">Nhà nước mang bản chất giai cấp, đồng thời thực hiện chức năng xã hội.</span></button>
                    <button type="button" class="ans" data-k="3"><span class="badge">D</span><span class="ans-text">Nhà nước được hình thành hoàn toàn từ ý chí cá nhân.</span></button>
                </div>
            </div>

            <div class="question hidden" data-q="2">
                <p class="q-text" style="margin-bottom: 24px;">Câu 3: Nguồn gốc ra đời của Nhà nước<br><span style="font-size: 0.55em; font-weight: 500; font-family: 'Inter', sans-serif; color: var(--text-muted); display: block; margin-top: 16px; line-height: 1.6;">Tình huống: Trong lịch sử, khi xã hội xuất hiện chế độ tư hữu, phân hóa giàu nghèo và mâu thuẫn giai cấp ngày càng gay gắt, một tổ chức quyền lực đặc biệt dần hình thành để duy trì trật tự xã hội. Theo chủ nghĩa Mác – Lênin, Nhà nước ra đời do nguyên nhân nào?</span></p>
                <div class="answers">
                    <button type="button" class="ans" data-k="0"><span class="badge">A</span><span class="ans-text">Nhu cầu tự nhiên của con người muốn có người lãnh đạo.</span></button>
                    <button type="button" class="ans" data-k="1"><span class="badge">B</span><span class="ans-text">Sự phát triển của lực lượng sản xuất và những mâu thuẫn giai cấp không thể điều hòa.</span></button>
                    <button type="button" class="ans" data-k="2"><span class="badge">C</span><span class="ans-text">Mong muốn của một cá nhân muốn nắm quyền lực.</span></button>
                    <button type="button" class="ans" data-k="3"><span class="badge">D</span><span class="ans-text">Sự phát triển của khoa học và công nghệ.</span></button>
                </div>
            </div>

            <div class="question hidden" data-q="3">
                <p class="q-text" style="margin-bottom: 24px;">Câu 4: Chức năng của Nhà nước<br><span style="font-size: 0.55em; font-weight: 500; font-family: 'Inter', sans-serif; color: var(--text-muted); display: block; margin-top: 16px; line-height: 1.6;">Tình huống: Trước tình trạng ô nhiễm môi trường, Nhà nước ban hành quy định xử phạt doanh nghiệp xả thải trái phép, đồng thời triển khai các chương trình bảo vệ môi trường. Tình huống này thể hiện điều gì?</span></p>
                <div class="answers">
                    <button type="button" class="ans" data-k="0"><span class="badge">A</span><span class="ans-text">Nhà nước chỉ thực hiện chức năng trấn áp.</span></button>
                    <button type="button" class="ans" data-k="1"><span class="badge">B</span><span class="ans-text">Nhà nước không có vai trò trong các vấn đề xã hội.</span></button>
                    <button type="button" class="ans" data-k="2"><span class="badge">C</span><span class="ans-text">Nhà nước thực hiện chức năng đối nội và quản lý xã hội.</span></button>
                    <button type="button" class="ans" data-k="3"><span class="badge">D</span><span class="ans-text">Nhà nước chỉ bảo vệ lợi ích của doanh nghiệp.</span></button>
                </div>
            </div>

            <div class="question hidden" data-q="4">
                <p class="q-text" style="margin-bottom: 24px;">Câu 5: Vai trò của cách mạng xã hội<br><span style="font-size: 0.55em; font-weight: 500; font-family: 'Inter', sans-serif; color: var(--text-muted); display: block; margin-top: 16px; line-height: 1.6;">Tình huống: Khi mâu thuẫn giữa lực lượng sản xuất và quan hệ sản xuất trở nên gay gắt, xã hội có thể xuất hiện những biến đổi sâu sắc về chính trị, kinh tế và xã hội. Theo chủ nghĩa Mác – Lênin, cách mạng xã hội có vai trò gì?</span></p>
                <div class="answers">
                    <button type="button" class="ans" data-k="0"><span class="badge">A</span><span class="ans-text">Duy trì nguyên trạng mọi quan hệ xã hội.</span></button>
                    <button type="button" class="ans" data-k="1"><span class="badge">B</span><span class="ans-text">Thay thế hình thái KT-XH cũ bằng hình thái KT-XH mới tiến bộ hơn.</span></button>
                    <button type="button" class="ans" data-k="2"><span class="badge">C</span><span class="ans-text">Chỉ thay đổi người đứng đầu Nhà nước.</span></button>
                    <button type="button" class="ans" data-k="3"><span class="badge">D</span><span class="ans-text">Chỉ cải thiện đời sống kinh tế mà không làm thay đổi xã hội.</span></button>
                </div>
            </div>

            <div class="question hidden" data-q="5">
                <p class="q-text" style="margin-bottom: 24px;">Câu 6: Điều kiện của cách mạng xã hội<br><span style="font-size: 0.55em; font-weight: 500; font-family: 'Inter', sans-serif; color: var(--text-muted); display: block; margin-top: 16px; line-height: 1.6;">Tình huống: Trong thực tế, một xã hội có thể xuất hiện nhiều bất bình đẳng và mâu thuẫn. Tuy nhiên, không phải mọi mâu thuẫn đều dẫn đến cách mạng xã hội. Theo quan điểm Mác – Lênin, yếu tố nào có ý nghĩa quan trọng để cách mạng xã hội diễn ra?</span></p>
                <div class="answers">
                    <button type="button" class="ans" data-k="0"><span class="badge">A</span><span class="ans-text">Chỉ cần người dân không hài lòng với một chính sách.</span></button>
                    <button type="button" class="ans" data-k="1"><span class="badge">B</span><span class="ans-text">Chỉ cần nền kinh tế phát triển nhanh chóng.</span></button>
                    <button type="button" class="ans" data-k="2"><span class="badge">C</span><span class="ans-text">Mâu thuẫn gay gắt, cùng với sự trưởng thành của lực lượng cách mạng.</span></button>
                    <button type="button" class="ans" data-k="3"><span class="badge">D</span><span class="ans-text">Chỉ cần thay đổi một vài quy định pháp luật.</span></button>
                </div>
            </div>
            
            <div class="feedback" aria-live="assertive">
                <p id="fb-wrong" class="hidden" style="margin: 0;">Chưa đúng, hãy thử lại!</p>
                <p id="fb-right" class="hidden" style="margin: 0;">Chính xác!</p>
            </div>

            <!-- Khung giải thích lý thuyết -->
            <div id="explanation-box" class="hidden" style="margin-top: 24px; padding: 24px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; text-align: left; animation: slideUp 0.4s ease; box-shadow: inset 0 2px 5px rgba(255,255,255,1), 0 10px 20px rgba(59,130,246,0.1);">
                <p id="explanation-text" style="font-size: 16px; line-height: 1.6; color: #1e3a8a; margin: 0;"></p>
                <div style="text-align: center; margin-top: 24px;">
                    <button type="button" class="btn btn-primary" id="btn-continue">Tiếp tục mở mảnh ghép ➔</button>
                </div>
            </div>
            <style>
                @keyframes slideUp {
                    from { transform: translateY(10px); opacity: 0; }
                    to { transform: translateY(0); opacity: 1; }
                }
            </style>
        </section>
    </div>

    <!-- Hoàn thành -->
    <div class="complete hidden" id="complete">
        <div id="confetti-layer"></div>
        <section class="complete-card" role="status">
            <p id="complete-text">HOÀN THÀNH!<br>Giai cấp, dân tộc và nhân loại có quan hệ biện chứng với nhau.</p>
            <button type="button" class="btn btn-primary" id="complete-replay">↻ Chơi lại</button>
        </section>
    </div>

    <script>
        (function(){
            // Đáp án đúng cho từng câu (A=0, B=1, C=2, D=3)
            const KEY = [1, 2, 1, 2, 1, 2];
            
            const EXPLANATIONS = [
                "Nhà nước không chỉ quản lý xã hội mà còn giải quyết các vấn đề chung như thiên tai, giáo dục và y tế, nhằm bảo vệ lợi ích cộng đồng.",
                "Nhà nước mang bản chất giai cấp, bảo vệ lợi ích của giai cấp thống trị, đồng thời thực hiện các chức năng phục vụ xã hội.",
                "Nhà nước ra đời khi xã hội xuất hiện tư hữu, phân chia giai cấp và mâu thuẫn giữa các giai cấp trở nên không thể điều hòa.",
                "Việc ban hành luật và xử phạt doanh nghiệp gây ô nhiễm là hoạt động quản lý các vấn đề bên trong đất nước, thuộc chức năng đối nội của Nhà nước.",
                "Cách mạng xã hội giúp thay thế xã hội cũ bằng một xã hội mới tiến bộ hơn, làm thay đổi căn bản các quan hệ xã hội.",
                "Cách mạng xã hội diễn ra khi mâu thuẫn xã hội trở nên gay gắt và lực lượng cách mạng đã đủ trưởng thành để thực hiện sự thay đổi."
            ];

            const pieces = [...document.querySelectorAll('.piece')];
            const questions = [...document.querySelectorAll('.question')];
            const overlay = document.getElementById('overlay');
            const modal = document.getElementById('modal');
            const fbW = document.getElementById('fb-wrong');
            const fbR = document.getElementById('fb-right');
            const expBox = document.getElementById('explanation-box');
            const expText = document.getElementById('explanation-text');
            const btnContinue = document.getElementById('btn-continue');
            const countEl = document.getElementById('progress-count');
            const completeEl = document.getElementById('complete');
            const confettiLayer = document.getElementById('confetti-layer');
            let opened = new Set();
            let current = null;
            let busy = false;

            function clearState(q) {
                q.querySelectorAll('.ans').forEach(a => a.classList.remove('wrong', 'right'));
                q.querySelector('.answers').classList.remove('locked');
            }

            function openQ(i) {
                if (current !== null || busy || opened.has(i)) return;
                current = i;
                questions.forEach(q => q.classList.add('hidden'));
                const q = questions[i]; 
                clearState(q); 
                q.classList.remove('hidden');
                fbW.classList.add('hidden'); 
                fbR.classList.add('hidden');
                expBox.classList.add('hidden');
                document.getElementById('modal-num').textContent = String(i + 1).padStart(2, '0');
                overlay.classList.remove('hidden');
            }

            function closeModal() {
                overlay.classList.add('hidden');
                if (current !== null) clearState(questions[current]);
                current = null; 
                busy = false;
            }

            function shake(el) {
                el.classList.remove('shake');
                void el.offsetWidth;
                el.classList.add('shake');
            }

            function answer(btn) {
                if (current === null || busy) return;
                const q = questions[current];
                const k = +btn.dataset.k;
                q.querySelectorAll('.ans').forEach(a => a.classList.remove('wrong'));
                
                if (k === KEY[current]) {
                    busy = true;
                    q.querySelector('.answers').classList.add('locked');
                    btn.classList.add('right');
                    fbW.classList.add('hidden'); 
                    fbR.classList.remove('hidden');
                    
                    // Show explanation instead of auto-closing
                    expText.innerHTML = "<strong>Ý nghĩa:</strong> " + EXPLANATIONS[current];
                    expBox.classList.remove('hidden');
                    
                } else {
                    btn.classList.add('wrong');
                    fbR.classList.add('hidden'); 
                    fbW.classList.remove('hidden');
                    shake(modal); 
                }
            }
            
            // Handle Continue button
            btnContinue.addEventListener('click', () => {
                if (current === null) return;
                const idx = current;
                opened.add(idx);
                const p = pieces[idx];
                p.classList.add('opened'); 
                p.disabled = true;
                
                setTimeout(() => p.classList.add('gone'), 500);
                countEl.textContent = opened.size;
                closeModal();
                
                if (opened.size === 6) { 
                    pieces.forEach(p => p.disabled = true); 
                    finish(); 
                }
            });

            function finish() {
                confettiLayer.innerHTML = '';
                const colors = ['#1e3a8a', '#3b82f6', '#93c5fd', '#f8fafc', '#38bdf8', '#2563eb'];
                for (let n = 0; n < 100; n++) {
                    const c = document.createElement('span');
                    c.className = 'confetti';
                    c.style.left = Math.random() * 100 + '%';
                    c.style.background = colors[n % colors.length];
                    c.style.borderRadius = n % 3 === 0 ? '50%' : '4px';
                    c.style.animationDuration = (2.5 + Math.random() * 2) + 's';
                    c.style.animationDelay = (Math.random() * 0.5) + 's';
                    confettiLayer.appendChild(c);
                }
                
                setTimeout(() => {
                    completeEl.classList.remove('hidden');
                }, 500);
            }

            function reset() {
                overlay.classList.add('hidden');
                questions.forEach(q => {
                    clearState(q);
                    q.classList.add('hidden');
                });
                fbW.classList.add('hidden'); 
                fbR.classList.add('hidden');
                expBox.classList.add('hidden');
                current = null; 
                busy = false; 
                opened = new Set();
                
                pieces.forEach(p => {
                    p.classList.remove('opened', 'gone', 'shake');
                    p.disabled = false;
                });
                
                countEl.textContent = '0';
                completeEl.classList.add('hidden'); 
                confettiLayer.innerHTML = '';
            }

            // Gán sự kiện
            pieces.forEach(p => p.addEventListener('click', () => openQ(+p.dataset.i)));
            
            document.querySelectorAll('.ans').forEach(a => {
                a.addEventListener('click', () => answer(a));
            });
            
            document.getElementById('close-btn').addEventListener('click', () => {
                if (!busy) closeModal();
            });
            
            overlay.addEventListener('click', e => {
                // If busy (explanation showing), don't close on overlay click
                if (e.target === overlay && !busy) closeModal();
            });
            
            document.addEventListener('keydown', e => {
                if (e.key === 'Escape' && current !== null && !busy) closeModal();
            });
            
            document.getElementById('reset-btn').addEventListener('click', reset);
            
            document.getElementById('show-answers').addEventListener('click', () => {
                pieces.forEach(p => {
                    p.classList.add('opened', 'gone');
                    p.disabled = true;
                });
            });
            
            document.getElementById('complete-replay').addEventListener('click', reset);
        })();
    </script>
</body>
</html>
"""

final_html = parts[0] + new_modal_and_js
with open(r'd:\Code\MLN\quiz.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Questions updated successfully.")
