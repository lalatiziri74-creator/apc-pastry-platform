import streamlit as st

# إعدادات الصفحة وتصميم عصري زاهي (RTL)
st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني - APC",
    page_icon="🎓",
    layout="wide"
)

# تصميم الواجهة والألوان الزاهية والنوافذ التفاعلية
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #F8FAFC;
    }
    .main-header { 
        font-size: 32px; 
        font-weight: 900; 
        color: #1E3A8A; 
        text-align: center; 
        margin-bottom: 5px; 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .sub-header { 
        font-size: 17px; 
        color: #0D9488; 
        text-align: center; 
        margin-bottom: 25px; 
        font-weight: 700;
    }
    .watermark { 
        position: fixed; 
        bottom: 10px; 
        left: 10px; 
        opacity: 0.35; 
        font-size: 13px; 
        font-weight: bold; 
        z-index: 1000; 
        color: #1E3A8A;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 5px 10px;
        border-radius: 6px;
    }
    .breadcrumb { 
        font-size: 15px; 
        color: #1E40AF; 
        background-color: #DBEAFE; 
        padding: 12px 18px; 
        border-radius: 10px; 
        margin-bottom: 20px; 
        border-right: 6px solid #2563EB; 
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .card-box {
        background-color: #FFFFFF;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
        margin-bottom: 18px;
        transition: transform 0.2s ease;
    }
    .card-box:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.12);
    }
    </style>
""", unsafe_allow_html=True)

# قاعدة بيانات المنصة الشاملة (مرنة وقابلة للتعديل والإضافة)
PLATFORM_DATABASE = {
    "programs": [
        {
            "id": "prog_apprentice",
            "title": "برنامج التكوين عن طريق التمهين",
            "icon": "🎓",
            "desc": "البرنامج الرسمي المعتمد للمتربصين عبر المؤسسات وتجمعات العمل.",
            "sub_categories": [
                {
                    "sub_id": "sub_patisserie_app",
                    "title": "تخصص خبازة وحلويات (CAP Pâtisserie)",
                    "specialties": [
                        {
                            "spec_id": "spec_west_app",
                            "title": "الحلويات الغربية والأساسيات",
                            "modules": [
                                {
                                    "mod_title": "وحدة أساسيات الحلويات والتمهين",
                                    "syllabus": "دراسة العجائن الكبرى، الكريمات، والتقنيات الأساسية.",
                                    "lessons": [
                                        {
                                            "les_title": "درس تطبيق تقنيات الحلويات المخادعة (Trompe-l'œil)",
                                            "apc_plan": "مخطط بيداغوجي وفق المقاربة بالكفاءات (APC) لإعداد فواكه تروما لوي.",
                                            "objectives": "التحكم في المظهر الخارجي، القوام، ودرجات حرارة التغلاص.",
                                            "evaluation": "شبكة التقييم: الدقة الهندسية، اللمعان، التوازن السكري.",
                                            "tech_card": {
                                                "title": "البطاقة التقنية: فواكه تروما لوي",
                                                "portions": 10,
                                                "ingredients": [
                                                    {"item": "بيوريه الفواكه الجاهز", "qty": 250, "unit": "غرام"},
                                                    {"item": "شوكولاتة بيضاء بيور", "qty": 300, "unit": "غرام"},
                                                    {"item": "قواعد بيسكويت جاهزة", "qty": 10, "unit": "قطع"}
                                                ]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "id": "prog_resident",
            "title": "برنامج التكوين الحضوري",
            "icon": "🏫",
            "desc": "البرامج النظامية داخل ورشات معاهد التكوين المهني.",
            "sub_categories": [
                {
                    "sub_id": "sub_resident_general",
                    "title": "تخصصات الفندقة والتحضير المهني",
                    "specialties": [
                        {
                            "spec_id": "spec_res_1",
                            "title": "مقياس صناعة الحلويات الفندقية",
                            "modules": [
                                {
                                    "mod_title": "وحدة التزيين والتركيب الفندقي",
                                    "syllabus": "تقنيات الإنتاج الكمي والنوعي للحلويات الكبرى.",
                                    "lessons": [
                                        {
                                            "les_title": "درس تحضير وتشكيل التارتلت الفندقي",
                                            "apc_plan": "مخطط بيداغوجي حضوري لتنظيم خط الإنتاج اليومي.",
                                            "objectives": "السرعة، نظافة المحيط، واحترام معايير النظافة الصحية HACCP.",
                                            "evaluation": "معايير التقييم: توحيد الأحجام، التجانس، والسرعة.",
                                            "tech_card": {
                                                "title": "البطاقة التقنية: تارتلت الفواكه",
                                                "portions": 20,
                                                "ingredients": [
                                                    {"item": "عجينة الصابلي الجاهزة", "qty": 500, "unit": "غرام"},
                                                    {"item": "كريم باتيسيير", "qty": 400, "unit": "غرام"},
                                                    {"item": "فواكه مشكلة مقطعة", "qty": 300, "unit": "غرام"}
                                                ]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "id": "prog_women",
            "title": "برنامج المرأة الماكثة بالبيت",
            "icon": "🏡",
            "desc": "برامج مخصصة لتطوير مهارات المرأة الماكثة بالبيت وتمكينها من إطلاق مشاريع مصغرة.",
            "sub_categories": [
                {
                    "sub_id": "sub_trad",
                    "title": "برنامج الحلويات التقليدية",
                    "specialties": [
                        {
                            "spec_id": "spec_dziriette",
                            "title": "مقياس المعسلات العسلية",
                            "modules": [
                                {
                                    "mod_title": "وحدة الحقيبة التقليدية الأصيلة",
                                    "syllabus": "صناعة وتزيين الحلويات العسلية التقليدية بمقاييس تجارية دقيقة.",
                                    "lessons": [
                                        {
                                            "les_title": "درس تحضير الدزريات التقليدية المفصلة",
                                            "apc_plan": "مخطط بيداغوجي لتمكين المتربصة من إتقان العجينة والحشو والتعسيل.",
                                            "objectives": "التحكم في نقش العجينة، ضبط حموضة وسمك العسل.",
                                            "evaluation": "شبكة التقييم: ثبات النقش، عدم انكماش الحشو، اللون الذهبي.",
                                            "tech_card": {
                                                "title": "البطاقة التقنية: الدزريات الورشة المنزلية",
                                                "portions": 25,
                                                "ingredients": [
                                                    {"item": "فرينة متعددة الاستعمالات", "qty": 500, "unit": "غرام"},
                                                    {"item": "لوز مرحي رقيق", "qty": 300, "unit": "غرام"},
                                                    {"item": "عسل حر مغذي", "qty": 400, "unit": "غرام"}
                                                ]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "sub_id": "sub_oriental",
                    "title": "برنامج الحلويات الشرقية",
                    "specialties": [
                        {
                            "spec_id": "spec_baklawa",
                            "title": "مقياس الحلويات المعاصرة والشرقية",
                            "modules": [
                                {
                                    "mod_title": "وحدة الفطائر الشرقية الفاخرة",
                                    "syllabus": "تقنيات التورق المكيال والطبقات المتعددة.",
                                    "lessons": [
                                        {
                                            "les_title": "درس البقلاوة الجزائرية المطورة للمشاريع",
                                            "apc_plan": "مخطط بيداغوجي لتخطيط الإنتاج التجاري المنزلي.",
                                            "objectives": "ضبط التورق، تقطيع متناسق، ودرجة حرارة الخبز المناسبة.",
                                            "evaluation": "معايير التقييم: عدد الطبقات، تجانس الحشو، التغليف والعرض.",
                                            "tech_card": {
                                                "title": "البطاقة التقنية: صينية بقلاوة قياسية",
                                                "portions": 40,
                                                "ingredients": [
                                                    {"item": "عجينة التورق الجاهزة", "qty": 1000, "unit": "غرام"},
                                                    {"item": "لوز خشن", "qty": 750, "unit": "غرام"},
                                                    {"item": "سمن عالي الجودة", "qty": 400, "unit": "غرام"}
                                                ]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "sub_id": "sub_western_women",
                    "title": "برنامج الحلويات الغربية للمشاريع المصغرة",
                    "specialties": [
                        {
                            "spec_id": "spec_cakes",
                            "title": "مقياس الكيك ديزاين والحلويات الباردة",
                            "modules": [
                                {
                                    "mod_title": "وحدة الحلويات الراقية للمناسبات",
                                    "syllabus": "صناعة التورطات العصرية والكيك الحديث.",
                                    "lessons": [
                                        {
                                            "les_title": "درس تحضير وتغليف قالب كيك المناسبات العصري",
                                            "apc_plan": "مخطط بيداغوجي لتحضير الكيك وقواعد التزيين الحديث.",
                                            "objectives": "استخدام الكريمة بانتظام، التمليس الحاد، والتنسيق الجمالي.",
                                            "evaluation": "معايير التقييم: استواء السطح، ثبات الحشو، والنظافة البصرية.",
                                            "tech_card": {
                                                "title": "البطاقة التقنية: قالب كيك قطرة 20 سم",
                                                "portions": 12,
                                                "ingredients": [
                                                    {"item": "بيسكويت جينواز جاهز", "qty": 1, "unit": "قالب"},
                                                    {"item": "كريمة زبدة مرنة", "qty": 500, "unit": "غرام"},
                                                    {"item": "مكسرات محمصة للتزيين", "qty": 100, "unit": "غرام"}
                                                ]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
]

# العلامة المائية الثابتة لحفظ حقوق الملكية الفكرية
st.markdown('<div class="watermark">إعداد وتصميم الأستاذة: فرحي حورية © 2026</div>', unsafe_allow_html=True)

# إدارة حالة التنقل بين النوافذ
if 'nav_path' not in st.session_state:
    st.session_state.nav_path = {"prog": None, "sub": None, "spec": None, "mod": None, "les": None}

# ترويسة المنصة
st.markdown('<div class="main-header">🎓 المنصة البيداغوجية الاحترافية للتكوين المهني (APC)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">إشراف وتصميم هندسي بيداغوجي: الأستاذة فرحي حورية</div>', unsafe_allow_html=True)

# نافذة البحث السريع في الواجهة الرئيسية
with st.container():
    search_query = st.text_input("🔍 البحث السريع في الدروس، المقاييس، أو البرامج:", placeholder="اكتب اسم الدرس أو المقياس هنا...")

# زر العودة للرئيسية
if st.session_state.nav_path["prog"] is not None:
    if st.button("🏠 العودة إلى القائمة الرئيسية للبرامج", use_container_width=True):
        st.session_state.nav_path = {"prog": None, "sub": None, "spec": None, "mod": None, "les": None}
        st.rerun()
    st.markdown("<br>", unsafe_allow_html=True)

# معالجة نظام البحث السريع
if search_query:
    st.markdown(f'<div class="breadcrumb">🔎 نتائج البحث عن: "{search_query}"</div>', unsafe_allow_html=True)
    found_any = False
    for p in PLATFORM_DATABASE["programs"]:
        for sc in p.get("sub_categories", []):
            for sp in sc.get("specialties", []):
                for m in sp.get("modules", []):
                    for l in m.get("lessons", []):
                        if search_query.lower() in l["les_title"].lower() or search_query.lower() in m["mod_title"].lower():
                            found_any = True
                            with st.container():
                                st.markdown(f"""
                                    <div class="card-box">
                                        <h4>📂 البرنامج: {p['title']} ➔ {sc['title']}</h4>
                                        <p><b>المقياس:</b> {m['mod_title']}</p>
                                        <p><b>الدرس:</b> {l['les_title']}</p>
                                    </div>
                                """, unsafe_allow_html=True)
    if not found_any:
        st.info("لم يتم العثور على نتائج تطابق بحثك. جرب كلمات أخرى.")
    st.divider()

# الهيكلة الرئيسية وتوزيع النوافذ
path = st.session_state.nav_path

if path["prog"] is None:
    # نافذة اختيار البرامج الكبرى
    st.subheader("📌 اختر البرنامج البيداغوجي المطلوب:")
    col1, col2, col3 = st.columns(3)
    
    programs = PLATFORM_DATABASE["programs"]
    for i, prog in enumerate(programs):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
                <div class="card-box" style="text-align: center;">
                    <h2>{prog['icon']}</h2>
                    <h3>{prog['title']}</h3>
                    <p>{prog['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"دخول {prog['title']}", key=f"btn_{prog['id']}", use_container_width=True):
                st.session_state.nav_path["prog"] = prog['id']
                st.rerun()

elif path["sub"] is None:
    # نافذة الفروع الداخلية للبرنامج المختار (مثل فروع المرأة الماكثة بالبيت)
    prog_obj = next((p for p in PLATFORM_DATABASE["programs"] if p['id'] == path["prog"]), None)
    if prog_obj:
        st.markdown(f'<div class="breadcrumb">📂 البرنامج الحالي: {prog_obj["title"]}</div>', unsafe_allow_html=True)
        st.subheader("📁 حدد التخصص أو البرنامج الفرعي:")
        
        for sub in prog_obj["sub_categories"]:
            with st.container():
                st.markdown(f"""
                    <div class="card-box">
                        <h3>📚 {sub['title']}</h3>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"استعراض محتوى: {sub['title']}", key=f"sub_{sub['sub_id']}", use_container_width=True):
                    st.session_state.nav_path["sub"] = sub['sub_id']
                    st.rerun()

elif path["spec"] is None:
    # نافذة المقاييس والتخصصات الدقيقة
    prog_obj = next((p for p in PLATFORM_DATABASE["programs"] if p['id'] == path["prog"]), None)
    sub_obj = next((s for s in prog_obj["sub_categories"] if s['sub_id'] == path["sub"]), None) if prog_obj else None
    
    if sub_obj:
        st.markdown(f'<div class="breadcrumb">📂 {prog_obj["title"]} ➔ {sub_obj["title"]}</div>', unsafe_allow_html=True)
        st.subheader("🎯 المقاييس البيداغوجية المتاحة:")
        
        for spec in sub_obj["specialties"]:
            for mod in spec["modules"]:
                with st.container():
                    st.markdown(f"""
                        <div class="card-box">
                            <h4>📖 المقياس: {spec['title']}</h4>
                            <p><b>الوحدة:</b> {mod['mod_title']}</p>
                            <p><i>المنهجية: {mod['syllabus']}</i></p>
                        </div>
                    """, unsafe_allow_html=True)
                    for idx, les in enumerate(mod["lessons"]):
                        if st.button(f"📖 فتح الدرس: {les['les_title']}", key=f"les_{sub['sub_id']}_{idx}", use_container_width=True):
                            st.session_state.nav_path["mod"] = mod['mod_title']
                            st.session_state.nav_path["les"] = les['les_title']
                            st.rerun()

else:
    # نافذة عرض الدرس الاحترافية (المخطط البيداغوجي APC + البطاقة التقنية)
    prog_obj = next((p for p in PLATFORM_DATABASE["programs"] if p['id'] == path["prog"]), None)
    sub_obj = next((s for s in prog_obj["sub_categories"] if s['sub_id'] == path["sub"]), None) if prog_obj else None
    
    found_lesson = None
    if sub_obj:
        for spec in sub_obj["specialties"]:
            for mod in spec["modules"]:
                for les in mod["lessons"]:
                    if les['les_title'] == path["les"]:
                        found_lesson = les

    if found_lesson:
        st.markdown(f'<div class="breadcrumb">📘 عرض الدرس التفصيلي وفق المقاربة بالكفاءات (APC)</div>', unsafe_allow_html=True)
        
        st.markdown(f"## 🌟 {found_lesson['les_title']}")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### 📋 التخطيط البيداغوجي")
            st.success(f"**المخطط البيداغوجي (APC):**\n\n{found_lesson['apc_plan']}")
            st.info(f"**الأهداف التعلمية:**\n\n{found_lesson['objectives']}")
        
        with col_b:
            st.markdown("### 📐 التقييم والبطاقة التقنية")
            st.warning(f"**معايير شبكة التقييم:**\n\n{found_lesson['evaluation']}")
            
            tc = found_lesson['tech_card']
            st.markdown(f"#### 🧾 {tc['title']} (لـ {tc['portions']} حصص)")
            for ing in tc['ingredients']:
                st.text(f"• {ing['item']}: {ing['qty']} {ing['unit']}")
