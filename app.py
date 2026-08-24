<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الشيف البيداغوجي – النسخة المتقدمة</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        * { box-sizing: border-box; }
        body { font-family: 'Tajawal', 'Segoe UI', system-ui, sans-serif; background: #faf8f5; }
        .shadow-soft { box-shadow: 0 4px 20px rgba(0,0,0,0.06); }
        .program-card { border: 1px solid #e5e7eb; border-radius: 16px; padding: 1.5rem; background: white; cursor: pointer; transition: all 0.3s ease; }
        .program-card:hover { box-shadow: 0 8px 30px rgba(0,0,0,0.08); }
        .page-section { display: none; }
        .page-section.active { display: block; }
        .badge-pending { background: #fef3c7; color: #92400e; font-size: 0.65rem; padding: 0.15rem 0.5rem; border-radius: 999px; }
        .badge-reviewed { background: #d1fae5; color: #065f46; font-size: 0.65rem; padding: 0.15rem 0.5rem; border-radius: 999px; }
        .badge-draft { background: #e5e7eb; color: #4b5563; font-size: 0.65rem; padding: 0.15rem 0.5rem; border-radius: 999px; }
        .module-card { border-right: 4px solid #b8860b; background: white; border-radius: 12px; padding: 1rem; margin-bottom: 1rem; }
        .card-item { border: 1px solid #e5e7eb; border-radius: 8px; padding: 0.75rem; margin-top: 0.5rem; background: #fefcf9; cursor: pointer; }
        .card-item:hover { background: #fdf6ed; }
        .btn-admin { padding: 0.3rem 0.8rem; border-radius: 6px; font-size: 0.8rem; border: none; cursor: pointer; transition: 0.2s; background: #f3f4f6; }
        .btn-admin:hover { opacity: 0.8; }
        .modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); display: none; align-items: center; justify-content: center; z-index: 999; }
        .modal-overlay.active { display: flex; }
        .modal-box { background: white; border-radius: 20px; padding: 2rem; max-width: 500px; width: 90%; max-height: 90vh; overflow-y: auto; }
        .accordion-content { padding: 0.5rem 0 1rem; }
        .accordion-btn { background: #f9f7f4; border: 1px solid #e5e7eb; border-radius: 8px; padding: 0.6rem 1rem; width: 100%; text-align: right; font-weight: 600; display: flex; align-items: center; gap: 0.5rem; transition: all 0.2s ease; cursor: pointer; }
        .accordion-btn:hover { background: #f3f0ea; }
        .accordion-btn .arrow { transition: transform 0.2s ease; }
        .accordion-btn .arrow.open { transform: rotate(180deg); }
        .eval-grid td, .eval-grid th { text-align: center; vertical-align: middle; font-size: 0.85rem; padding: 0.25rem 0.2rem; }
        .video-placeholder { background: #f1f3f5; border: 1px dashed #ced4da; border-radius: 6px; padding: 0.4rem 0.8rem; text-align: center; color: #6c757d; font-size: 0.85rem; }
        .ingredient-list { display: flex; flex-wrap: wrap; gap: 0.5rem; }
        .ingredient-item { background: #f9f7f4; padding: 0.2rem 0.6rem; border-radius: 6px; border: 1px solid #e5e7eb; }
        @media print { .no-print { display: none !important; } .accordion-content { display: block !important; } .accordion-btn { border: none; background: none; } .accordion-btn .arrow { display: none; } }
    </style>
</head>
<body>

<nav class="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50 no-print">
    <div class="max-w-7xl mx-auto px-4 flex justify-between items-center h-16">
        <span class="font-bold text-lg text-gray-800">🍰 الشيف البيداغوجي</span>
        <div>
            <button onclick="navigateTo('home')" class="text-sm text-gray-600 hover:text-amber-700 px-2">🏠 الرئيسية</button>
            <button onclick="navigateTo('admin')" class="text-sm text-gray-600 hover:text-amber-700 px-2">⚙️ إدارة</button>
        </div>
    </div>
</nav>

<header class="bg-gradient-to-l from-amber-50 to-white border-b border-amber-100 py-6 text-center">
    <h1 class="text-2xl sm:text-3xl font-bold text-gray-800">🍰 منصة <span class="text-amber-700">الشيف البيداغوجي</span></h1>
    <p class="text-gray-600 mt-1 text-sm">منصة تكوين مهني جزائرية في صناعة الحلويات التقليدية</p>
    <p class="text-xs text-gray-500 mt-2">إعداد الأستاذة: <strong class="text-amber-800">حورية فرحي</strong> © 2026</p>
</header>

<main class="max-w-7xl mx-auto px-4 py-6">

    <section id="page-home" class="page-section active">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">📚 برامج التكوين</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4" id="programList"></div>
    </section>

    <section id="page-program" class="page-section">
        <button onclick="navigateTo('home')" class="text-sm text-amber-700 hover:text-amber-900 no-print">← العودة</button>
        <div id="programDetailContainer" class="mt-4"></div>
        <button onclick="window.print()" class="mt-4 bg-amber-700 text-white px-4 py-2 rounded-lg no-print">🖨️ طباعة</button>
    </section>

    <section id="page-admin" class="page-section">
        <button onclick="navigateTo('home')" class="text-sm text-amber-700 hover:text-amber-900 no-print">← العودة</button>
        <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mt-4">
            <h3 class="text-xl font-bold text-gray-800">🔐 إدارة المنصة</h3>
            <p class="text-sm text-gray-500 mb-4">إضافة وتعديل وحذف البرامج والوحدات والبطاقات. التغييرات تحفظ تلقائياً.</p>
            <div class="flex flex-wrap gap-3 mb-4">
                <button onclick="openModal('program')" class="btn-admin bg-green-100 text-green-700 px-3 py-1 rounded">➕ برنامج جديد</button>
                <button onclick="openModal('unit')" class="btn-admin bg-blue-100 text-blue-700 px-3 py-1 rounded">➕ وحدة جديدة</button>
                <button onclick="openModal('card')" class="btn-admin bg-purple-100 text-purple-700 px-3 py-1 rounded">➕ بطاقة جديدة</button>
                <button onclick="resetAllData()" class="btn-admin bg-red-100 text-red-700 px-3 py-1 rounded">🗑️ حذف الكل</button>
            </div>
            <pre id="adminOutput" class="mt-4 text-xs bg-gray-100 p-2 rounded max-h-60 overflow-auto"></pre>
        </div>
    </section>

</main>

<div id="modalOverlay" class="modal-overlay" onclick="if(event.target===this) closeModal()">
    <div class="modal-box">
        <h4 id="modalTitle" class="text-xl font-bold text-gray-800 mb-4">إضافة جديد</h4>
        <form id="modalForm" onsubmit="saveModalItem(event)">
            <div id="modalFields"></div>
            <div class="flex gap-3 mt-6">
                <button type="submit" class="bg-amber-700 text-white px-4 py-2 rounded-lg hover:bg-amber-800 transition">حفظ</button>
                <button type="button" onclick="closeModal()" class="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-300 transition">إلغاء</button>
            </div>
        </form>
    </div>
</div>

<footer class="bg-white border-t border-gray-200 py-4 mt-6 text-center text-sm text-gray-500 no-print">
    © 2026 الشيف البيداغوجي – إعداد الأستاذة: حورية فرحي
</footer>

<script>
    // ========================================================================
    // 1. البيانات الافتراضية مع كل تفاصيل المقياس
    // ========================================================================
    const DEFAULT_DATA = {
        programs: [
            {
                id: 'p1',
                title: 'برنامج المرأة الماكثة بالبيت',
                desc: 'برنامج شامل لتكوين المرأة الماكثة بالبيت في صناعة الحلويات',
                hours: 84,
                status: 'قيد التدقيق',
                timeDistribution: [
                    { stage: 'المقدمة', duration: '1 ساعة', notes: 'عرض شفهي' },
                    { stage: 'تحضير الحشوة', duration: '10 ساعات', notes: 'تطبيقي' },
                    { stage: 'إنجاز حلويات اللوز', duration: '29 ساعة', notes: '8 حلويات' },
                    { stage: 'الطهي', duration: '13 ساعة', notes: 'فرن وقلي' },
                    { stage: 'التشطيب', duration: '21 ساعة', notes: 'تطبيقي' },
                    { stage: 'النشاط الشامل', duration: '5 ساعات', notes: 'إنتاج متكامل' },
                    { stage: 'التقييم', duration: '5 ساعات', notes: 'نظري وعملي' }
                ],
                evaluationCriteria: [
                    { criterion: 'احترام الوصفة', indicator: 'احترام المقادير والمراحل' },
                    { criterion: 'التنظيم', indicator: 'ترتيب العمل واستغلال الوقت' },
                    { criterion: 'التشكيل', indicator: 'انتظام ودقة الأشكال' },
                    { criterion: 'الطهي', indicator: 'لون وقوام مناسب' },
                    { criterion: 'التشطيب', indicator: 'نظافة ودقة التزيين' },
                    { criterion: 'الطعم', indicator: 'توازن النكهات' },
                    { criterion: 'القوام', indicator: 'مناسب لنوع الحلوى' },
                    { criterion: 'النظافة', indicator: 'احترام قواعد النظافة والسلامة' },
                    { criterion: 'التقديم', indicator: 'مظهر مهني جذاب' }
                ],
                theoryQuestions: [
                    'ما أهمية وزن المواد الأولية بدقة؟',
                    'ما دور راحة العجينة؟',
                    'ما العوامل التي تؤثر في جودة الطهي؟',
                    'كيف نميز الحلوى المطهية جيدًا؟',
                    'ما شروط نجاح عجينة اللوز؟',
                    'ما أهمية التحكم في قوام الحشوة؟',
                    'ما قواعد النظافة الواجب احترامها أثناء العمل؟'
                ],
                modules: [
                    {
                        id: 'm1',
                        title: 'MQ1 – إعداد حلويات اللوز',
                        desc: 'إنجاز الحلويات التقليدية الجزائرية المصنوعة من اللوز (84 ساعة)',
                        cards: [
                            { id: 'c1', title: 'البقلاوة الجزائرية التقليدية', content: 'المقادير: لوز، عسل، عجين...\nالخطوات: التحضير، الطهي، التشطيب.', status: 'قيد التدقيق' },
                            { id: 'c2', title: 'الكفتة الجزائرية', content: 'المقادير: لوز، سكر، زبدة...\nالخطوات: العجن، التشكيل، التزيين.', status: 'قيد التدقيق' },
                            { id: 'c3', title: 'حلوة الفاكهة', content: 'المقادير: عجينة اللوز، ألوان غذائية...\nالخطوات: التلوين، التشكيل.', status: 'قيد التدقيق' },
                            { id: 'c4', title: 'الثومية', content: 'المقادير: لوز، سكر، ماء زهر...\nالخطوات: التشكيل، التلوين.', status: 'قيد التدقيق' },
                            { id: 'c5', title: 'حلوة المشكلة', content: 'المقادير: لوز، سكر، مكسرات...\nالخطوات: تحضير العجينة، الحشو، التشكيل.', status: 'قيد التدقيق' },
                            { id: 'c6', title: 'العرايش الجزائرية', content: 'المقادير: فرينة، سمن، لوز...\nالخطوات: العجن، الحشو، الخبز.', status: 'قيد التدقيق' },
                            { id: 'c7', title: 'التشاراك التقليدي', content: 'المقادير: فرينة، زبدة، سكر...\nالخطوات: العجن، التشكيل، الخبز.', status: 'قيد التدقيق' },
                            { id: 'c8', title: 'الهريسية باللوز', content: 'المقادير: لوز، سكر، بيض...\nالخطوات: الخلط، الطهي، التسقية.', status: 'قيد التدقيق' }
                        ]
                    },
                    {
                        id: 'm2',
                        title: 'MQ2 – تحضير الحشوات والكريمات',
                        desc: 'تحضير الحشوات المختلفة المستخدمة في الحلويات',
                        cards: [
                            { id: 'c9', title: 'كريمة اللوز', content: 'مقادير وطريقة تحضير كريمة اللوز التقليدية.', status: 'قيد التدقيق' },
                            { id: 'c10', title: 'الحشوة بالتمر', content: 'مقادير وطريقة تحضير حشوة التمر.', status: 'قيد التدقيق' }
                        ]
                    }
                ]
            }
        ]
    };

    // ========================================================================
    // 2. تحميل البيانات وحالة البطاقات
    // ========================================================================
    let appData = null;
    let currentProgramId = null;
    let modalType = null;
    let editingId = null;
    let cardStates = {};

    function loadData() {
        const saved = localStorage.getItem('chef_advanced_data');
        if (saved) {
            try { appData = JSON.parse(saved); }
            catch(e) { appData = JSON.parse(JSON.stringify(DEFAULT_DATA)); }
        } else {
            appData = JSON.parse(JSON.stringify(DEFAULT_DATA));
        }
        appData.programs.forEach(p => {
            if (!p.modules) p.modules = [];
            p.modules.forEach(m => { if (!m.cards) m.cards = []; });
        });
        saveData();
        const states = localStorage.getItem('chef_advanced_states');
        if (states) {
            try { cardStates = JSON.parse(states); } catch(e) { cardStates = {}; }
        }
    }

    function saveData() {
        localStorage.setItem('chef_advanced_data', JSON.stringify(appData));
        renderAdmin();
    }

    function saveCardStates() {
        localStorage.setItem('chef_advanced_states', JSON.stringify(cardStates));
    }

    function generateId() { return Date.now().toString(36) + Math.random().toString(36).substr(2, 5); }

    // ========================================================================
    // 3. العرض مع البطاقات المفتوحة وجميع التفاصيل
    // ========================================================================
    function renderPrograms() {
        const container = document.getElementById('programList');
        container.innerHTML = '';
        appData.programs.forEach(p => {
            const div = document.createElement('div');
            div.className = 'program-card';
            div.onclick = () => { currentProgramId = p.id; navigateTo('program'); renderProgramDetail(p.id); };
            const badge = p.status === 'قيد التدقيق' ? 'badge-pending' : p.status === 'تمت المراجعة' ? 'badge-reviewed' : 'badge-draft';
            div.innerHTML = `
                <h3 class="font-bold text-lg text-gray-800">${p.title}</h3>
                <p class="text-sm text-gray-500">${p.desc}</p>
                <span class="bg-amber-100 text-amber-800 px-3 py-1 rounded-full text-xs font-semibold">${p.hours || 0} ساعة</span>
                <span class="${badge} block mt-2">${p.status}</span>
            `;
            container.appendChild(div);
        });
    }

    function renderProgramDetail(programId) {
        const container = document.getElementById('programDetailContainer');
        const p = appData.programs.find(pr => pr.id === programId);
        if (!p) { container.innerHTML = '<p class="text-gray-400">البرنامج غير موجود</p>'; return; }

        let html = `
            <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mb-6">
                <h2 class="text-2xl font-bold text-gray-800">${p.title}</h2>
                <p class="text-gray-500">${p.desc}</p>
                <div class="mt-2 flex flex-wrap gap-3">
                    <span class="bg-amber-100 text-amber-800 px-3 py-1 rounded-full text-xs font-semibold">${p.hours} ساعة</span>
                    <span class="badge-pending">${p.status}</span>
                </div>
            </div>
        `;

        // التوزيع الزمني
        if (p.timeDistribution && p.timeDistribution.length) {
            html += `
                <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mb-6">
                    <h4 class="font-bold text-gray-800 mb-4">⏱️ التوزيع الزمني</h4>
                    <div class="overflow-x-auto">
                        <table class="w-full text-sm text-right"><thead class="bg-gray-50"><tr><th class="p-2 border">المرحلة</th><th class="p-2 border">المدة</th><th class="p-2 border">ملاحظات</th></tr></thead><tbody>
                            ${p.timeDistribution.map(row => `<tr><td class="p-2 border">${row.stage}</td><td class="p-2 border">${row.duration}</td><td class="p-2 border">${row.notes || ''}</td></tr>`).join('')}
                        </tbody></table>
                    </div>
                </div>
            `;
        }

        // معايير التقييم
        if (p.evaluationCriteria && p.evaluationCriteria.length) {
            html += `
                <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mb-6">
                    <h4 class="font-bold text-gray-800 mb-4">⭐ معايير تقييم المنتوج النهائي</h4>
                    <div class="overflow-x-auto">
                        <table class="w-full text-sm text-right"><thead class="bg-gray-50"><tr><th class="p-2 border">المعيار</th><th class="p-2 border">مؤشر النجاح</th></tr></thead><tbody>
                            ${p.evaluationCriteria.map(item => `<tr><td class="p-2 border">${item.criterion}</td><td class="p-2 border">${item.indicator}</td></tr>`).join('')}
                        </tbody></table>
                    </div>
                </div>
            `;
        }

        // الأسئلة النظرية
        if (p.theoryQuestions && p.theoryQuestions.length) {
            html += `
                <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mb-6">
                    <h4 class="font-bold text-gray-800 mb-4">📝 أسئلة نظرية</h4>
                    <ul class="text-sm text-gray-600 list-disc list-inside space-y-1">
                        ${p.theoryQuestions.map(q => `<li>${q}</li>`).join('')}
                    </ul>
                </div>
            `;
        }

        // النظافة والسلامة
        html += `
            <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mb-6">
                <h4 class="font-bold text-gray-800 mb-4">🧼 النظافة والسلامة المهنية</h4>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
                    <ul class="list-disc list-inside space-y-1"><li>غسل اليدين جيدًا</li><li>تنظيف وتعقيم سطح العمل</li><li>استعمال أدوات نظيفة</li><li>احترام شروط حفظ المواد الأولية</li></ul>
                    <ul class="list-disc list-inside space-y-1"><li>التأكد من صلاحية المواد</li><li>استعمال الفرن والمعدات بطريقة آمنة</li><li>ارتداء اللباس المهني المناسب</li></ul>
                </div>
            </div>
        `;

        // النشاط الشامل
        html += `
            <div class="bg-white rounded-xl shadow-soft border border-gray-100 p-6 mb-6">
                <h4 class="font-bold text-gray-800 mb-4">🏆 النشاط الشامل</h4>
                <p class="text-sm text-gray-600">في نهاية المقياس، ينجز المتكوّن منتوجًا متكاملًا باستعمال المهارات المكتسبة في الدروس السابقة.</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-3 text-sm text-gray-600">
                    <ul class="list-disc list-inside space-y-1"><li>اختيار الوصفة</li><li>قراءة بطاقة الوصفة</li><li>تحضير المواد</li></ul>
                    <ul class="list-disc list-inside space-y-1"><li>تنظيم مكان العمل</li><li>تنفيذ المراحل</li><li>التشطيب والتزيين</li></ul>
                </div>
                <p class="text-sm text-gray-700 mt-3 font-medium">📜 الكفاءة النهائية: ينجز المتكوّن حلوى تقليدية جزائرية قائمة على اللوز وفق الوصفة والتقنيات المهنية، مع احترام الجودة والنظافة والسلامة.</p>
            </div>
        `;

        // الوحدات والبطاقات
        html += `<div class="mb-6"><h4 class="font-bold text-gray-800 mb-4">📚 الوحدات (${p.modules.length})</h4>`;
        if (p.modules.length === 0) {
            html += `<p class="text-gray-400 text-center py-6">لا توجد وحدات مسجلة لهذا البرنامج.</p>`;
        } else {
            p.modules.forEach(mod => {
                html += `<div class="module-card"><h4 class="font-bold text-gray-800">📘 ${mod.title}</h4><p class="text-sm text-gray-500">${mod.desc}</p>`;
                if (mod.cards && mod.cards.length > 0) {
                    mod.cards.forEach(card => {
                        const isOpen = cardStates[card.id] !== undefined ? cardStates[card.id] : true;
                        const arrowClass = isOpen ? 'open' : '';
                        const contentDisplay = isOpen ? 'block' : 'none';
                        html += `
                            <div class="card-item">
                                <button class="accordion-btn" onclick="toggleCard('${card.id}')">
                                    <span class="flex-1 text-right">📄 ${card.title}</span>
                                    <span class="arrow ${arrowClass}">▼</span>
                                </button>
                                <div id="card-content-${card.id}" class="accordion-content" style="display: ${contentDisplay};">
                                    <p class="text-sm text-gray-700 whitespace-pre-wrap">${card.content || 'لا يوجد محتوى'}</p>
                                    <div class="flex gap-2 mt-2 no-print">
                                        <button onclick="editCardContent('${card.id}')" class="btn-admin bg-blue-100 text-blue-700 px-2 py-1 rounded text-xs">✏️ تعديل</button>
                                        <button onclick="deleteCard('${card.id}')" class="btn-admin bg-red-100 text-red-700 px-2 py-1 rounded text-xs">🗑️ حذف</button>
                                    </div>
                                </div>
                            </div>
                        `;
                    });
                } else {
                    html += `<p class="text-sm text-gray-400">لا توجد بطاقات</p>`;
                }
                html += `
                    <div class="flex gap-2 mt-3 no-print">
                        <button onclick="editUnit('${mod.id}')" class="btn-admin bg-blue-100 text-blue-700 px-2 py-1 rounded text-xs">✏️ تعديل</button>
                        <button onclick="deleteUnit('${mod.id}')" class="btn-admin bg-red-100 text-red-700 px-2 py-1 rounded text-xs">🗑️ حذف</button>
                        <button onclick="addCardToUnit('${mod.id}')" class="btn-admin bg-green-100 text-green-700 px-2 py-1 rounded text-xs">➕ بطاقة</button>
                    </div>
                `;
                html += `</div>`;
            });
        }
        html += `</div>`;

        // أزرار إدارة البرنامج
        html += `
            <div class="flex gap-3 mt-4 no-print">
                <button onclick="editProgram('${p.id}')" class="btn-admin bg-blue-100 text-blue-700 px-3 py-1 rounded text-sm">✏️ تعديل البرنامج</button>
                <button onclick="deleteProgram('${p.id}')" class="btn-admin bg-red-100 text-red-700 px-3 py-1 rounded text-sm">🗑️ حذف البرنامج</button>
                <button onclick="addUnitToProgram('${p.id}')" class="btn-admin bg-green-100 text-green-700 px-3 py-1 rounded text-sm">➕ إضافة وحدة</button>
            </div>
        `;

        container.innerHTML = html;
    }

    // ========================================================================
    // 4. التحكم في فتح/طي البطاقات
    // ========================================================================
    function toggleCard(cardId) {
        const current = cardStates[cardId] !== undefined ? cardStates[cardId] : true;
        cardStates[cardId] = !current;
        saveCardStates();
        const content = document.getElementById(`card-content-${cardId}`);
        if (content) {
            content.style.display = cardStates[cardId] ? 'block' : 'none';
        }
        const btn = content?.closest('.card-item')?.querySelector('.accordion-btn .arrow');
        if (btn) {
            btn.classList.toggle('open', cardStates[cardId]);
        }
    }

    function toggleAllCards(programId, open) {
        const p = appData.programs.find(pr => pr.id === programId);
        if (!p) return;
        p.modules.forEach(mod => {
            mod.cards.forEach(card => {
                cardStates[card.id] = open;
            });
        });
        saveCardStates();
        renderProgramDetail(programId);
    }

    // ========================================================================
    // 5. التنقل
    // ========================================================================
    function navigateTo(page) {
        document.querySelectorAll('.page-section').forEach(el => el.classList.remove('active'));
        if (page === 'home') {
            document.getElementById('page-home').classList.add('active');
            renderPrograms();
        } else if (page === 'program') {
            document.getElementById('page-program').classList.add('active');
            if (currentProgramId) renderProgramDetail(currentProgramId);
        } else if (page === 'admin') {
            document.getElementById('page-admin').classList.add('active');
            renderAdmin();
        }
    }

    // ========================================================================
    // 6. الإدارة (عمليات CRUD)
    // ========================================================================
    function renderAdmin() {
        document.getElementById('adminOutput').textContent = JSON.stringify(appData, null, 2);
    }

    function editProgram(id) {
        const p = appData.programs.find(pr => pr.id === id);
        if (!p) return;
        const newTitle = prompt('تعديل اسم البرنامج:', p.title);
        if (newTitle !== null) p.title = newTitle;
        const newDesc = prompt('تعديل وصف البرنامج:', p.desc);
        if (newDesc !== null) p.desc = newDesc;
        const newHours = prompt('تعديل عدد الساعات:', p.hours);
        if (newHours !== null) p.hours = parseInt(newHours) || 0;
        saveData();
        renderProgramDetail(id);
    }

    function deleteProgram(id) {
        if (!confirm('هل أنت متأكد من حذف هذا البرنامج وجميع وحداته وبطاقاته؟')) return;
        appData.programs = appData.programs.filter(p => p.id !== id);
        saveData();
        navigateTo('home');
    }

    function addUnitToProgram(programId) {
        const p = appData.programs.find(pr => pr.id === programId);
        if (!p) return;
        const title = prompt('أدخل اسم الوحدة:');
        if (!title) return;
        const desc = prompt('أدخل وصف الوحدة:') || '';
        p.modules.push({ id: generateId(), title, desc, cards: [] });
        saveData();
        renderProgramDetail(programId);
    }

    function editUnit(unitId) {
        let found = null;
        let parentProg = null;
        for (const p of appData.programs) {
            const m = p.modules.find(mod => mod.id === unitId);
            if (m) { found = m; parentProg = p; break; }
        }
        if (!found) return;
        const newTitle = prompt('تعديل اسم الوحدة:', found.title);
        if (newTitle !== null) found.title = newTitle;
        const newDesc = prompt('تعديل وصف الوحدة:', found.desc);
        if (newDesc !== null) found.desc = newDesc;
        saveData();
        if (parentProg) renderProgramDetail(parentProg.id);
    }

    function deleteUnit(unitId) {
        if (!confirm('حذف هذه الوحدة وجميع بطاقاتها؟')) return;
        for (const p of appData.programs) {
            const idx = p.modules.findIndex(m => m.id === unitId);
            if (idx !== -1) {
                p.modules.splice(idx, 1);
                saveData();
                renderProgramDetail(p.id);
                return;
            }
        }
    }

    function addCardToUnit(unitId) {
        let parentProg = null;
        let unit = null;
        for (const p of appData.programs) {
            const m = p.modules.find(mod => mod.id === unitId);
            if (m) { unit = m; parentProg = p; break; }
        }
        if (!unit) return;
        const title = prompt('أدخل عنوان البطاقة:');
        if (!title) return;
        const content = prompt('أدخل محتوى البطاقة (وصف، مقادير، خطوات):') || '';
        const newCard = { id: generateId(), title, content, status: 'قيد التدقيق' };
        unit.cards.push(newCard);
        cardStates[newCard.id] = true;
        saveCardStates();
        saveData();
        if (parentProg) renderProgramDetail(parentProg.id);
    }

    function editCardContent(cardId) {
        let card = null;
        let parentProg = null;
        for (const p of appData.programs) {
            for (const m of p.modules) {
                const c = m.cards.find(crd => crd.id === cardId);
                if (c) { card = c; parentProg = p; break; }
            }
            if (card) break;
        }
        if (!card) return;
        const newContent = prompt('تعديل محتوى البطاقة:', card.content);
        if (newContent !== null) {
            card.content = newContent;
            saveData();
            if (parentProg) renderProgramDetail(parentProg.id);
        }
    }

    function deleteCard(cardId) {
        if (!confirm('حذف هذه البطاقة؟')) return;
        for (const p of appData.programs) {
            for (const m of p.modules) {
                const idx = m.cards.findIndex(c => c.id === cardId);
                if (idx !== -1) {
                    m.cards.splice(idx, 1);
                    delete cardStates[cardId];
                    saveCardStates();
                    saveData();
                    renderProgramDetail(p.id);
                    return;
                }
            }
        }
    }

    function resetAllData() {
        if (!confirm('تحذير: سيتم حذف جميع البيانات نهائياً. هل أنت متأكدة؟')) return;
        appData.programs = [];
        cardStates = {};
        saveCardStates();
        saveData();
        navigateTo('home');
        renderAdmin();
    }

    // ========================================================================
    // 7. المودال (إضافة برامج/وحدات/بطاقات)
    // ========================================================================
    function openModal(type, id = null) {
        modalType = type;
        editingId = id;
        const overlay = document.getElementById('modalOverlay');
        const title = document.getElementById('modalTitle');
        const fields = document.getElementById('modalFields');

        let html = '';
        if (type === 'program') {
            title.innerText = 'إضافة برنامج جديد';
            html = `
                <div class="mb-3"><label class="block text-sm font-bold">العنوان</label><input id="f_title" class="w-full border rounded p-2" required></div>
                <div class="mb-3"><label class="block text-sm font-bold">الوصف</label><input id="f_desc" class="w-full border rounded p-2"></div>
                <div class="mb-3"><label class="block text-sm font-bold">المدة (ساعات)</label><input id="f_hours" type="number" class="w-full border rounded p-2" value="0"></div>
                <div class="mb-3"><label class="block text-sm font-bold">الحالة</label>
                    <select id="f_status" class="w-full border rounded p-2">
                        <option value="قيد التدقيق">قيد التدقيق</option>
                        <option value="تمت المراجعة">تمت المراجعة</option>
                        <option value="قيد التطوير">قيد التطوير</option>
                    </select>
                </div>
            `;
        } else if (type === 'unit') {
            title.innerText = 'إضافة وحدة جديدة';
            html = `
                <div class="mb-3"><label class="block text-sm font-bold">عنوان الوحدة</label><input id="f_title" class="w-full border rounded p-2" required></div>
                <div class="mb-3"><label class="block text-sm font-bold">الوصف</label><input id="f_desc" class="w-full border rounded p-2"></div>
                <p class="text-xs text-gray-400">سيتم إضافة الوحدة إلى البرنامج الحالي المفتوح.</p>
            `;
        } else if (type === 'card') {
            title.innerText = 'إضافة بطاقة جديدة';
            html = `
                <div class="mb-3"><label class="block text-sm font-bold">عنوان البطاقة</label><input id="f_title" class="w-full border rounded p-2" required></div>
                <div class="mb-3"><label class="block text-sm font-bold">المحتوى</label><textarea id="f_content" class="w-full border rounded p-2" rows="4"></textarea></div>
                <p class="text-xs text-gray-400">ستتم إضافة البطاقة إلى أول وحدة في البرنامج الحالي.</p>
            `;
        }
        fields.innerHTML = html;
        overlay.classList.add('active');
    }

    function closeModal() {
        document.getElementById('modalOverlay').classList.remove('active');
        modalType = null;
        editingId = null;
    }

    function saveModalItem(e) {
        e.preventDefault();
        const title = document.getElementById('f_title')?.value.trim();
        if (!title) { alert('الرجاء إدخال العنوان'); return; }

        if (modalType === 'program') {
            const desc = document.getElementById('f_desc')?.value || '';
            const hours = parseInt(document.getElementById('f_hours')?.value) || 0;
            const status = document.getElementById('f_status')?.value || 'قيد التدقيق';
            appData.programs.push({
                id: generateId(),
                title,
                desc,
                hours,
                status,
                timeDistribution: [],
                evaluationCriteria: [],
                theoryQuestions: [],
                modules: []
            });
        } else if (modalType === 'unit') {
            const p = appData.programs.find(pr => pr.id === currentProgramId);
            if (!p) { alert('لا يوجد برنامج مفتوح لإضافة وحدة إليه.'); return; }
            const desc = document.getElementById('f_desc')?.value || '';
            p.modules.push({ id: generateId(), title, desc, cards: [] });
        } else if (modalType === 'card') {
            const p = appData.programs.find(pr => pr.id === currentProgramId);
            if (!p || p.modules.length === 0) { alert('البرنامج الحالي لا يحتوي على وحدات. أنشئ وحدة أولاً.'); return; }
            const content = document.getElementById('f_content')?.value || '';
            const newCard = { id: generateId(), title, content, status: 'قيد التدقيق' };
            p.modules[0].cards.push(newCard);
            cardStates[newCard.id] = true;
            saveCardStates();
        }

        saveData();
        closeModal();
        if (modalType === 'program') {
            navigateTo('home');
        } else {
            if (currentProgramId) renderProgramDetail(currentProgramId);
        }
        renderAdmin();
    }

    // ========================================================================
    // 8. بدء التشغيل
    // ========================================================================
    loadData();
    renderPrograms();
    renderAdmin();
    console.log('🍰 المنصة المتقدمة جاهزة (جميع البطاقات مفتوحة)');
</script>
</body>
</html>
