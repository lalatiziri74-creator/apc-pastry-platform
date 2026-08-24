import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الشاملة والمهنية
st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني (APC)",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# إخفاء عناصر غيت هاب وشريط ستريمليت العلوي لتوفير واجهة منصة مستقلة كلياً
st.markdown(
    """
    <style>
        .stAppHeader, .stSidebar, .st-emotion-cache-1r6slb0, footer {
            display: none !important;
        }
        .main > div {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>المنصة البيداغوجية للتكوين المهني (APC)</title>
    <style>
        :root {
            --primary-dark: #231915;      /* شوكولاتة داكنة وعميقة ومحترفة */
            --primary-coffee: #4a352d;    /* قهوة دافئة وأنيقة */
            --primary-accent: #6b4c3b;    /* تدرج قهوة راقي للأزرار */
            --gold-accent: #a88544;       /* ذهبي هادئ وراقي */
            --gold-light: #dfc89d;        /* ذهبي خفيف للحدود المميزة */
            --bg-page: #f6f3ee;           /* خلفية كريمية ناعمة ومريحة للعين */
            --card-bg: #ffffff;           /* أبيض ناصع للبطاقات */
            --text-main: #251e1b;         /* لون النصوص الرئيسية واضح */
            --text-muted: #665750;        /* لون النصوص الثانوية */
            --border-color: #dfd4c8;      /* حدود دافئة متناسقة */
            --border-radius: 16px;
        }
        
        * { 
            box-sizing: border-box; 
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-page);
            color: var(--text-main);
            direction: rtl;
            text-align: right;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }

        /* رأس المنصة البيداغوجية الفاخر والأكاديمي */
        header {
            background: linear-gradient(135deg, var(--primary-dark), var(--primary-coffee));
            color: white;
            padding: 50px 20px;
            text-align: center;
            box-shadow: 0 6px 25px rgba(35, 25, 21, 0.2);
            border-bottom: 4px solid var(--gold-accent);
            position: relative;
        }

        header::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--gold-accent), transparent);
        }

        .header-content {
            max-width: 900px;
            margin: 0 auto;
        }

        header h1 {
            margin: 0 0 12px 0;
            font-size: 28px;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.3px;
        }

        header h2 {
            margin: 0 0 10px 0;
            font-size: 18px;
            font-weight: 500;
            color: var(--gold-light);
        }

        header p {
            margin: 0;
            font-size: 14px;
            color: #d1c2b4;
            font-weight: 400;
        }

        /* حاوية المحتوى الرئيسية */
        .container {
            max-width: 1100px;
            width: 100%;
            margin: 40px auto;
            padding: 0 20px;
            flex: 1;
        }

        /* العوالم والصفحات الديناميكية */
        .view-section {
            display: none;
            background: var(--card-bg);
            padding: 40px 35px;
            border-radius: var(--border-radius);
            box-shadow: 0 12px 35px rgba(35, 25, 21, 0.05);
            margin-bottom: 30px;
            border: 1px solid var(--border-color);
            animation: fadeIn 0.3s ease-in-out;
        }

        .view-section.active { display: block; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .section-title {
            text-align: center;
            margin-bottom: 35px;
        }

        .section-title h2 {
            color: var(--primary-dark);
            font-size: 24px;
            margin-bottom: 8px;
            font-weight: 600;
        }

        .section-title p {
            color: var(--text-muted);
            font-size: 14px;
            margin: 0;
        }

        /* شبكة البطاقات المهنية الأنيقة */
        .grid-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 20px;
        }

        .card {
            background: var(--card-bg);
            border: 2px solid var(--border-color);
            border-radius: var(--border-radius);
            padding: 35px 25px;
            text-align: center;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
            display: flex;
            flex-direction: column;
            align-items: center;
            outline: none;
            position: relative;
            -webkit-tap-highlight-color: transparent;
        }

        .card:focus-visible { 
            outline: 3px solid var(--gold-accent); 
            outline-offset: 3px;
        }

        .card:hover, .card:active {
            border-color: var(--gold-accent);
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(168, 133, 68, 0.12);
            background: #fffefd;
        }

        .card.apprenticeship { border-top: 5px solid #6b4c3b; }
        .card.presence { border-top: 5px solid #4a6b5d; }
        .card.homemaker { border-top: 5px solid #8c6d48; }

        .card-icon {
            font-size: 40px;
            margin-bottom: 18px;
            background: #f4efe9;
            width: 75px;
            height: 75px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            border: 1px solid var(--border-color);
            transition: transform 0.25s ease;
        }

        .card:hover .card-icon { transform: scale(1.08); }

        .card h3 {
            color: var(--primary-dark);
            margin: 0 0 12px 0;
            font-size: 19px;
            font-weight: 600;
        }

        .card p {
            color: var(--text-muted);
            font-size: 13.5px;
            margin: 0 0 25px 0;
            line-height: 1.6;
            flex-grow: 1;
        }

        .btn-entry {
            background-color: var(--primary-accent);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 13.5px;
            pointer-events: none;
            transition: background 0.2s ease;
        }

        .card:hover .btn-entry {
            background-color: var(--primary-dark);
        }

        /* شريط مسار التنقل (Breadcrumb) وأزرار التحكم العلوية */
        .nav-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
            flex-wrap: wrap;
            gap: 12px;
        }

        .breadcrumb {
            font-size: 13.5px;
            color: var(--text-muted);
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #f4efe9;
            padding: 9px 16px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
        }

        .nav-buttons-group {
            display: flex;
            gap: 10px;
        }

        .btn-action {
            background-color: var(--primary-coffee);
            padding: 9px 18px;
            font-size: 13.5px;
            border-radius: 8px;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: background 0.2s ease;
            -webkit-tap-highlight-color: transparent;
        }

        .btn-action:hover {
            background-color: var(--primary-dark);
        }

        .btn-home {
            background-color: var(--gold-accent);
        }
        .btn-home:hover {
            background-color: #8e6f36;
        }

        /* فضاء الحاويات المعيارية (Modular Containers) لاستقبال المحتوى مستقبلاً بدون إعادة بناء */
        .modular-space {
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .empty-placeholder {
            text-align: center;
            padding: 50px 20px;
            background: #faf7f2;
            border-radius: var(--border-radius);
            border: 1px dashed var(--gold-accent);
            color: var(--text-muted);
            font-size: 14px;
        }

        /* Footer احترافي وأنيق */
        footer {
            background-color: var(--primary-dark);
            color: #ab9a8c;
            text-align: center;
            padding: 25px 20px;
            font-size: 13.5px;
            border-top: 2px solid var(--gold-accent);
            margin-top: auto;
        }

        footer p {
            margin: 0;
            letter-spacing: 0.3px;
        }

        /* التوافق التام والتام مع الهواتف الذكية بنسبة 100% */
        @media (max-width: 768px) {
            header { padding: 35px 15px; }
            header h1 { font-size: 21px; }
            header h2 { font-size: 15px; }
            header p { font-size: 12.5px; }
            .container { margin: 20px auto; padding: 0 12px; }
            .view-section { padding: 25px 18px; }
            .grid-cards { grid-template-columns: 1fr; gap: 18px; }
            .card { padding: 28px 20px; }
            .nav-controls { flex-direction: column; align-items: stretch; }
            .breadcrumb { width: 100%; justify-content: center; }
            .nav-buttons-group { justify-content: space-between; }
            .btn-action { flex: 1; justify-content: center; }
        }
    </style>
</head>
<body>

    <header>
        <div class="header-content">
            <h1>المنصة البيداغوجية للتكوين المهني (APC)</h1>
            <h2>تحت إشراف الأستاذة فرحي حورية</h2>
            <p>التكوين المهني في صناعة الحلويات</p>
        </div>
    </header>

    <div class="container" id="app-container"></div>

    <footer>
        <p>© فرحي حورية - جميع الحقوق محفوظة للمنصة البيداغوجية للتكوين المهني (APC)</p>
    </footer>

    <script>
        /**
         * =========================================================================
         * معمارية البيانات المجدولة وقابلة للتوسع (Modular Data Architecture)
         * =========================================================================
         * تم فصل محتوى المسارات بالكامل هنا. عند إرسال المحتوى لاحقاً، يتم ملء 
         * هذه الحاويات (Units, Lessons, Technical Cards, Assessments) ديناميكياً.
         */
        const platformData = {
            main: {
                id: 'main-view',
                title: 'اختر مسارك التكويني',
                subtitle: 'بوابة الوصول إلى العوالم البيداغوجية المتخصصة',
                isMain: true,
                children: [
                    { id: 'apprenticeship-view', icon: '📘', title: 'برنامج التمهين', desc: 'المسار المخصص للجمع بين التكوين التطبيقي والدروس النظرية.', className: 'apprenticeship' },
                    { id: 'presence-view', icon: '🏫', title: 'البرنامج الحضوري', desc: 'المسار المخصص للتكوين النظامي داخل الهياكل البيداغوجية.', className: 'presence' },
                    { id: 'homemaker-view', icon: '👩‍🍳', title: 'برنامج المرأة الماكثة بالبيت', desc: 'المسار المخصص لتطوير المهارات وإنشاء المشاريع المهنية.', className: 'homemaker' }
                ]
            },
            pages: {
                'apprenticeship-view': {
                    title: 'عالم برنامج التمهين',
                    subtitle: 'الفضاء البيداغوجي الخاص بمسار التمهين',
                    breadcrumb: '🏠 الرئيسية ← برنامج التمهين',
                    backTo: 'main-view',
                    // حاويات معيارية مستقبلية (Modular Containers)
                    units: [],
                    lessons: [],
                    technicalCards: [],
                    assessments: [],
                    tools: []
                },
                'presence-view': {
                    title: 'عالم البرنامج الحضوري',
                    subtitle: 'الفضاء البيداغوجي الخاص بالتكوين الحضوري النظامي',
                    breadcrumb: '🏠 الرئيسية ← البرنامج الحضوري',
                    backTo: 'main-view',
                    units: [],
                    lessons: [],
                    technicalCards: [],
                    assessments: [],
                    tools: []
                },
                'homemaker-view': {
                    title: 'برنامج المرأة الماكثة بالبيت',
                    subtitle: 'التخصصات الفرعية المعتمدة للمسار',
                    breadcrumb: '🏠 الرئيسية ← برنامج المرأة الماكثة بالبيت',
                    backTo: 'main-view',
                    isParent: true,
                    children: [
                        { id: 'traditional-view', icon: '🍰', title: 'الحلويات التقليدية', desc: 'الفضاء المتخصص في تراث الحلويات التقليدية وأصالتها.', className: 'homemaker' },
                        { id: 'eastern-view', icon: '🧁', title: 'الحلويات الشرقية', desc: 'الفضاء المتخصص في الحلويات الشرقية وتقنياتها.', className: 'homemaker' },
                        { id: 'western-view', icon: '🥐', title: 'الحلويات الغربية', desc: 'الفضاء المتخصص في الحلويات الغربية وتقنيات العجين الفاخر.', className: 'homemaker' }
                    ]
                },
                'traditional-view': {
                    title: 'عالم الحلويات التقليدية',
                    subtitle: 'التخصص البيداغوجي للحلويات التقليدية',
                    breadcrumb: '🏠 الرئيسية ← برنامج المرأة الماكثة بالبيت ← الحلويات التقليدية',
                    backTo: 'homemaker-view',
                    lessons: [],
                    technicalCards: [],
                    assessments: []
                },
                'eastern-view': {
                    title: 'عالم الحلويات الشرقية',
                    subtitle: 'التخصص البيداغوجي للحلويات الشرقية',
                    breadcrumb: '🏠 الرئيسية ← برنامج المرأة الماكثة بالبيت ← الحلويات الشرقية',
                    backTo: 'homemaker-view',
                    lessons: [],
                    technicalCards: [],
                    assessments: []
                },
                'western-view': {
                    title: 'عالم الحلويات الغربية',
                    subtitle: 'التخصص البيداغوجي للحلويات الغربية',
                    breadcrumb: '🏠 الرئيسية ← برنامج المرأة الماكثة بالبيت ← الحلويات الغربية',
                    backTo: 'homemaker-view',
                    lessons: [],
                    technicalCards: [],
                    assessments: []
                }
            }
        };

        /**
         * =========================================================================
         * محرك العرض الديناميكي (Dynamic Rendering Engine)
         * =========================================================================
         */
        function buildCard(item) {
            return `
                <div class="card ${item.className || ''}" tabindex="0" role="button" 
                     onclick="switchView('${item.id}')" 
                     onkeydown="if(event.key==='Enter') switchView('${item.id}')">
                    <div class="card-icon">${item.icon}</div>
                    <h3>${item.title}</h3>
                    <p>${item.desc}</p>
                    <button class="btn-entry">دخول العالم</button>
                </div>
            `;
        }

        function renderMainView() {
            const main = platformData.main;
            let cardsHtml = main.children.map(child => buildCard(child)).join('');
            return `
                <div id="main-view" class="view-section active">
                    <div class="section-title">
                        <h2>${main.title}</h2>
                        <p>${main.subtitle}</p>
                    </div>
                    <div class="grid-cards">${cardsHtml}</div>
                </div>
            `;
        }

        function renderPageView(pageId) {
            const page = platformData.pages[pageId];
            if (!page) return '';

            let innerHtml = '';
            if (page.isParent && page.children) {
                let cardsHtml = page.children.map(child => buildCard(child)).join('');
                innerHtml = `<div class="grid-cards">${cardsHtml}</div>`;
            } else {
                // عرض الحاويات المعيارية الفارغة بانتظار المحتوى مستقبلاً دون تدمير الواجهة
                innerHtml = `
                    <div class="modular-space">
                        <div class="empty-placeholder">
                            هذا الفضاء جاهز هندسياً لاستقبال الوحدات، الدروس، والبطاقات التقنية فور إضافتها.
                        </div>
                    </div>
                `;
            }

            let backButtonText = "⬅ العودة السابقة";
            if (page.backTo === 'homemaker-view') {
                backButtonText = "⬅ العودة لبرنامج المرأة الماكثة بالبيت";
            } else if (page.backTo === 'main-view') {
                backButtonText = "⬅ العودة للرئيسية";
            }

            return `
                <div id="${pageId}" class="view-section">
                    <div class="nav-controls">
                        <div class="breadcrumb">${page.breadcrumb}</div>
                        <div class="nav-buttons-group">
                            <button class="btn-action" onclick="switchView('${page.backTo}')">${backButtonText}</button>
                            <button class="btn-action btn-home" onclick="switchView('main-view')">🏠 الرئيسية</button>
                        </div>
                    </div>
                    <div class="section-title">
                        <h2>${page.title}</h2>
                        <p>${page.subtitle}</p>
                    </div>
                    ${innerHtml}
                </div>
            `;
        }

        function renderAllViews() {
            let html = renderMainView();
            for (const pageId in platformData.pages) {
                html += renderPageView(pageId);
            }
            document.getElementById('app-container').innerHTML = html;
        }

        function switchView(viewId) {
            const sections = document.querySelectorAll('.view-section');
            sections.forEach(section => section.classList.remove('active'));
            const target = document.getElementById(viewId);
            if (target) {
                target.classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        window.onload = function() {
            renderAllViews();
        };
    </script>

</body>
</html>
"""

components.html(html_code, height=750, scrolling=True)
