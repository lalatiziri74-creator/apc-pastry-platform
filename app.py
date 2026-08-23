import streamlit as st

# إعدادات الصفحة والتصميم العربي (RTL) وتصميم عصري زاهي
st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني - APC",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #F8FAFC;
    }
    .main-header { 
        font-size: 30px; 
        font-weight: 800; 
        color: #1E3A8A; 
        text-align: center; 
        margin-bottom: 5px; 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .sub-header { 
        font-size: 16px; 
        color: #0D9488; 
        text-align: center; 
        margin-bottom: 25px; 
        font-weight: 600;
    }
    .watermark { 
        position: fixed; 
        bottom: 10px; 
        left: 10px; 
        opacity: 0.3; 
        font-size: 12px; 
        font-weight: bold; 
        z-index: 1000; 
        color: #1E3A8A;
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
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    /* تصميم البطاقات الملونة الواضحة */
    .card-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# قاعدة البيانات الشاملة (تشمل البرامج الثلاثة: المرأة الماكثة، التكوين الحضوري، و CAP)
PLATFORM_DATA = {
    "programs": [
        {
            "id": "prog_woman_home",
            "title": "برنامج المرأة الماكثة بالبيت",
            "description": "التكوين التأهيلي الموجه للمرأة الماكثة بالبيت لتطوير حرف الإنتاج المصغر.",
            "specialties": [
                {
                    "id": "spec_trad",
                    "title": "تخصص الحلويات التقليدية المنزلية",
                    "code": "PAT_HW_01",
                    "modules": [
                        {
                            "id": "mod_trad_1",
                            "title": "وحدة تقنيات صناعة الحلويات التقليدية",
                            "subjects": [
                                {
                                    "id": "subj_trad_1",
                                    "title": "مقياس العجائن والمعسلات التقليدية",
                                    "syllabus": "مخطط المقياس: دراسة عجائن المقروط والدزريات والمعسلات.",
                                    "lessons": [
                                        {
                                            "id": "les_dziriette",
                                            "title": "درس تحضير الدزريات الأصلية",
                                            "trainee_content": {
                                                "description": "تعلم كيفية تحضير العينة، التشكيل، والعسل الخاص بالدزريات.",
                                                "activities": "تطبيق عملية تزيين ووزن العجين والحشو.",
                                                "quiz": "ماهي درجات العسل المناسبة لسقي الدزريات؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط درس وفق المقاربة بالكفاءات (APC).",
                                                "objectives": "أن تتمكن المتربصة من إتقان قالب الدزريات بنسبة نجاح تامة.",
                                                "evaluation_grid": "شبكة التقييم: اللون، اللمعان، وطراوة الحشو.",
                                                "model_answers": "الإجابة النموذجية وطريقة تفادي جفاف الحشو.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: الدزريات",
                                                    "base_portions": 20,
                                                    "ingredients": [
                                                        {"item": "فرينة (طحين)", "qty": 500, "unit": "غرام"},
                                                        {"item": "سمن معطر", "qty": 125, "unit": "غرام"},
                                                        {"item": "لوز مطحون (الحشو)", "qty": 300, "unit": "غرام"},
                                                        {"item": "سكر عادي", "qty": 100, "unit": "غرام"},
                                                        {"item": "عسل", "qty": 250, "unit": "غرام"}
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "spec_oriental",
                    "title": "تخصص الحلويات الشرقية والمعاصرة",
                    "code": "PAT_HW_02",
                    "modules": [
                        {
                            "id": "mod_oriental_1",
                            "title": "وحدة الحلويات الشرقية",
                            "subjects": [
                                {
                                    "id": "subj_oriental_1",
                                    "title": "مقياس المعجنات الشرقية الدقيقة",
                                    "syllabus": "مخطط المقياس: تقنيات الطهي والتشكيل الشرقي.",
                                    "lessons": [
                                        {
                                            "id": "les_baklawa",
                                            "title": "درس البقلاوة الجزائرية التقليدية",
                                            "trainee_content": {
                                                "description": "حساب الطبقات، تورق العجين، وتوزيع الحشو.",
                                                "activities": "ترتيب 7 طبقات سفلية و 7 علوية.",
                                                "quiz": "كيف يتم تجنب انتفاخ طبقات البقلاوة أثناء الخبز؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط بيداغوجي لدرس البقلاوة.",
                                                "objectives": "التحكم في تقطيع ووزن الصينية.",
                                                "evaluation_grid": "التناسق، القرمشة، وتشرب العسل.",
                                                "model_answers": "الحل النموذجي لالتصاق الطبقات.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: البقلاوة الصينية القياسية",
                                                    "base_portions": 30,
                                                    "ingredients": [
                                                        {"item": "فرينة", "qty": 1000, "unit": "غرام"},
                                                        {"item": "سمن", "qty": 300, "unit": "غرام"},
                                                        {"item": "لوز مرحي", "qty": 3000, "unit": "غرام"},
                                                        {"item": "سكر", "qty": 1000, "unit": "غرام"}
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "spec_western",
                    "title": "تخصص الحلويات الغربية (Patisserie Fine)",
                    "code": "PAT_HW_03",
                    "modules": [
                        {
                            "id": "mod_western_1",
                            "title": "وحدة الترتلات والكريمة",
                            "subjects": [
                                {
                                    "id": "subj_western_1",
                                    "title": "مقياس العجائن الهشة والفاخرة",
                                    "syllabus": "مخطط المقياس: Pâte Sablée et Crèmes.",
                                    "lessons": [
                                        {
                                            "id": "les_tarts",
                                            "title": "درس تارتليت الفواكه الموسمية",
                                            "trainee_content": {
                                                "description": "إعداد العجينة الهشة، الخبز الأعمى، وترتيب الفواكه.",
                                                "activities": "تلبيس القوالب الصغرى بدقة.",
                                                "quiz": "لماذا نقوم بثقب العجينة الهشة قبل الخبز؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط بيداغوجي لدرس الترتليت.",
                                                "objectives": "إتقان الطهي المتساوي لقواعد العجين.",
                                                "evaluation_grid": "لون الحواف، ثبات الكريمة، واللمعان.",
                                                "model_answers": "التعامل مع انكماش العجينة في الفرن.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: تارتليت الفواكه",
                                                    "base_portions": 10,
                                                    "ingredients": [
                                                        {"item": "فرينة", "qty": 250, "unit": "غرام"},
                                                        {"item": "زبدة باردة", "qty": 125, "unit": "غرام"},
                                                        {"item": "سكر رطب", "qty": 75, "unit": "غرام"},
                                                        {"item": "بيضة", "qty": 1, "unit": "حبة"}
                                                    ]
                                                }
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
            "id": "prog_present",
            "title": "برنامج التكوين الحضوري",
            "description": "التكوين النظامي الحضوري الموجه للمتمهنين والمتربصين بالمؤسسات.",
            "specialties": [
                {
                    "id": "spec_present_general",
                    "title": "تخصص فنون الطهي والحلويات النظامية",
                    "code": "PRES_01",
                    "modules": [
                        {
                            "id": "mod_pres_1",
                            "title": "وحدة أساسيات المخبر والامن المهني",
                            "subjects": [
                                {
                                    "id": "subj_pres_1",
                                    "title": "مقياس نظافة وتطهير محيط العمل",
                                    "syllabus": "مخطط المقياس: قواعد النظافة الصحية في مخبر الحلويات (HACCP).",
                                    "lessons": [
                                        {
                                            "id": "les_hygiene",
                                            "title": "درس تطبيق قواعد النظافة والأمن بالمخبر",
                                            "trainee_content": {
                                                "description": "التعرف على معايير نظافة الأسطح، المعدات، والنظافة الشخصية.",
                                                "activities": "تطبيق عملية تعقيم طاولات العمل.",
                                                "quiz": "ما هي درجات الحرارة المناسبة لغسل أدوات الحلويات الدهنية؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط درس الأمن الصناعي.",
                                                "objectives": "ترسيخ ثقافة السلامة المهنية للمتربص.",
                                                "evaluation_grid": "الالتزام بلباس المخبر والنظافة العامة.",
                                                "model_answers": "الإجابة النموذجية لمعايير الاعتماد الصحي.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: محلول التعقيم القياسي",
                                                    "base_portions": 1,
                                                    "ingredients": [
                                                        {"item": "ماء دافئ", "qty": 1000, "unit": "ملليتر"},
                                                        {"item": "مطهير معتمد (جافيل مخفف)", "qty": 10, "unit": "ملليتر"}
                                                    ]
                                                }
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
            "id": "prog_cap",
            "title": "شهادة الكفاءة المهنية (CAP)",
            "description": "برنامج التكوين المهني الأساسي للحصول على شهادة الكفاءة المهنية.",
            "specialties": [
                {
                    "id": "spec_cap_pat",
                    "title": "تخصص صانع حلويات محترف (CAP Patissier)",
                    "code": "CAP_01",
                    "modules": [
                        {
                            "id": "mod_cap_1",
                            "title": "وحدة الحلويات الأساسية لشهادة الكفاءة",
                            "subjects": [
                                {
                                    "id": "subj_cap_1",
                                    "title": "مقياس العجائن المخمرة والمنفوخة",
                                    "syllabus": "مخطط المقياس: تحضير الكرواسون والبريوش.",
                                    "lessons": [
                                        {
                                            "id": "les_croissant",
                                            "title": "درس تحضير الكرواسون الفرنسي بالتفصيل",
                                            "trainee_content": {
                                                "description": "عجن العجينة الابتدائية، التوريق، والتشكيل الهلالي.",
                                                "activities": "حساب طبقات التوريق والتحكم في زبدة التبريد.",
                                                "quiz": "لماذا يجب تبريد العجين بين طيات التوريق؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط بيداغوجي لدرس الكرواسون الرسمي.",
                                                "objectives": "إتقان تقنية التوريق الفردي والمزدوج.",
                                                "evaluation_grid": "وضوح الطبقات من الداخل، اللون الذهبي، والقرمشة.",
                                                "model_answers": "طريقة معالجة ذوبان الزبدة أثناء التوريق.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: عجين الكرواسون الأساسي",
                                                    "base_portions": 15,
                                                    "ingredients": [
                                                        {"item": "فرينة الخبز", "qty": 500, "unit": "غرام"},
                                                        {"item": "زبدة التوريق", "qty": 250, "unit": "غرام"},
                                                        {"item": "حليب دافئ", "qty": 250, "unit": "ملليتر"},
                                                        {"item": "سكر", "qty": 50, "unit": "غرام"},
                                                        {"item": "خميرة الخباز", "qty": 10, "unit": "غرام"}
                                                    ]
                                                }
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
}

# إدارة حالة التنقل
if 'current_page' not in st.session_state: st.session_state.current_page = 'home'
if 'selected_prog_id' not in st.session_state: st.session_state.selected_prog_id = None
if 'selected_spec_id' not in st.session_state: st.session_state.selected_spec_id = None
if 'selected_mod_id' not in st.session_state: st.session_state.selected_mod_id = None
if 'selected_subj_id' not in st.session_state: st.session_state.selected_subj_id = None
if 'selected_les_id' not in st.session_state: st.session_state.selected_les_id = None
if 'user_role' not in st.session_state: st.session_state.user_role = 'trainee'

# ترويسة المنصة
st.markdown('<div class="main-header">🎓 المنصة البيداغوجية للتكوين المهني (APC)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">إشراف وتصميم بيداغوجي: الأستاذة فرحي حورية</div>', unsafe_allow_html=True)
st.markdown('<div class="watermark">إعداد الأستاذة فرحي حورية ©</div>', unsafe_allow_html=True)

# شريط التحكم بالصلاحيات الجانبي
with st.sidebar:
    st.header("⚙️ لوحة المعاينة والصلاحيات")
    role_choice = st.radio("نوع المستخدم (معاينة الواجهة):", ["👨‍🎓 متربص (Trainee)", "👨‍🏫 أستاذ (Teacher)"])
    st.session_state.user_role = 'teacher' if "أستاذ" in role_choice else 'trainee'
    st.divider()
    st.info("💡 هذه اللوحة تمكنكِ من المعاينة برؤية المتربص أو الأستاذ المحمي.")
    st.caption("جميع الحقوق محفوظة للأستاذة فرحي حورية ©")

# شريط البحث والعودة للرئيسية
col_nav1, col_nav2 = st.columns([3, 1])
with col_nav1:
    search_q = st.text_input("🔍 بحث في المناهج والدروس...", placeholder="ابحث عن درس أو وحدة...")
with col_nav2:
    if st.button("🏠 الرئيسية", use_container_width=True):
        st.session_state.current_page = 'home'
        st.session_state.selected_prog_id = None
        st.session_state.selected_spec_id = None
        st.session_state.selected_mod_id = None
        st.session_state.selected_subj_id = None
        st.session_state.selected_les_id = None
        st.rerun()

def render_breadcrumbs():
    path = ["🏠 الرئيسية"]
    if st.session_state.selected_prog_id:
        p = next((x for x in PLATFORM_DATA["programs"] if x["id"] == st.session_state.selected_prog_id), None)
        if p:
            path.append(p["title"])
            if st.session_state.selected_spec_id:
                sp = next((x for x in p["specialties"] if x["id"] == st.session_state.selected_spec_id), None)
                if sp:
                    path.append(sp["title"])
                    if st.session_state.selected_mod_id:
                        m = next((x for x in sp["modules"] if x["id"] == st.session_state.selected_mod_id), None)
                        if m:
                            path.append(m["title"])
                            if st.session_state.selected_subj_id:
                                sb = next((x for x in m["subjects"] if x["id"] == st.session_state.selected_subj_id), None)
                                if sb:
                                    path.append(sb["title"])
                                    if st.session_state.selected_les_id:
                                        les = next((x for x in sb["lessons"] if x["id"] == st.session_state.selected_les_id), None)
                                        if les: path.append(les["title"])
    st.markdown(f'<div class="breadcrumb">{" ➔ ".join(path)}</div>', unsafe_allow_html=True)

render_breadcrumbs()

# الصفحة الرئيسية بتصميم زاهي ومنظم في بطاقات
if st.session_state.current_page == 'home':
    st.markdown("### 📌 اختر برنامج التكوين المهني:")
    cols = st.columns(len(PLATFORM_DATA["programs"]))
    for idx, prog in enumerate(PLATFORM_DATA["programs"]):
        with cols[idx]:
            st.markdown(f"""
                <div class="card-box" style="border-top: 5px solid #2563EB;">
                    <h3 style="color: #1E3A8A; font-size: 20px;">{prog['title']}</h3>
                    <p style="color: #4B5563; font-size: 14px; min-height: 50px;">{prog['description']}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"📂 دخول {prog['title']}", key=prog['id'], use_container_width=True):
                st.session_state.selected_prog_id = prog['id']
                st.session_state.current_page = 'specialties'
                st.rerun()

elif st.session_state.current_page == 'specialties':
    if st.button("⬅️ العودة للرئيسية"):
        st.session_state.current_page = 'home'
        st.session_state.selected_prog_id = None
        st.rerun()
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    st.subheader(f"📂 التخصصات المتاحة - {curr_prog['title']}")
    for spec in curr_prog["specialties"]:
        st.markdown(f"""
            <div class="card-box" style="border-right: 5px solid #0D9488;">
                <h4 style="color: #0F766E;">🎓 تخصص: {spec['title']}</h4>
                <p style="color: #64748B; margin: 0;">رمز التخصص: <b>{spec['code']}</b></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"اختيار هذا التخصص", key=spec['id'], use_container_width=True):
            st.session_state.selected_spec_id = spec['id']
            st.session_state.current_page = 'modules'
            st.rerun()

elif st.session_state.current_page == 'modules':
    if st.button("⬅️ العودة للتخصصات"):
        st.session_state.current_page = 'specialties'
        st.session_state.selected_spec_id = None
        st.rerun()
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    curr_spec = next(s for s in curr_prog["specialties"] if s["id"] == st.session_state.selected_spec_id)
    st.subheader(f"📦 الوحدات التكوينية - {curr_spec['title']}")
    for mod in curr_spec["modules"]:
        st.markdown(f"""
            <div class="card-box" style="border-right: 5px solid #7C3AED;">
                <h4 style="color: #6D28D9;">📘 {mod['title']}</h4>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"استعراض الوحدة", key=mod['id'], use_container_width=True):
            st.session_state.selected_mod_id = mod['id']
            st.session_state.current_page = 'subjects'
            st.rerun()

elif st.session_state.current_page == 'subjects':
    if st.button("⬅️ العودة للوحدات"):
        st.session_state.current_page = 'modules'
        st.session_state.selected_mod_id = None
        st.rerun()
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    curr_spec = next(s for s in curr_prog["specialties"] if s["id"] == st.session_state.selected_spec_id)
    curr_mod = next(m for m in curr_spec["modules"] if m["id"] == st.session_state.selected_mod_id)
    st.subheader(f"📐 المقاييس البيداغوجية - {curr_mod['title']}")
    for subj in curr_mod["subjects"]:
        st.markdown(f"""
            <div class="card-box">
                <h4 style="color: #1E3A8A;">📑 {subj['title']}</h4>
                <p style="color: #4B5563;"><b>مخطط المقياس:</b> {subj['syllabus']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"دخول المقياس", key=subj['id'], use_container_width=True):
            st.session_state.selected_subj_id = subj['id']
            st.session_state.current_page = 'lessons'
            st.rerun()

elif st.session_state.current_page == 'lessons':
    if st.button("⬅️ العودة للمقاييس"):
        st.session_state.current_page = 'subjects'
        st.session_state.selected_subj_id = None
        st.session_state.selected_les_id = None
        st.rerun()
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    curr_spec = next(s for s in curr_prog["specialties"] if s["id"] == st.session_state.selected_spec_id)
    curr_mod = next(m for m in curr_spec["modules"] if m["id"] == st.session_state.selected_mod_id)
    curr_subj = next(sb for sb in curr_mod["subjects"] if sb["id"] == st.session_state.selected_subj_id)
    
    st.subheader(f"📖 الدروس والبطاقات التقنية - {curr_subj['title']}")
    les_options = {les['title']: les['id'] for les in curr_subj["lessons"]}
    selected_les_title = st.selectbox("اختر الدرس للعرض:", list(les_options.keys()))
    selected_les_id = les_options[selected_les_title]
    st.session_state.selected_les_id = selected_les_id
    curr_les = next(l for l in curr_subj["lessons"] if l["id"] == selected_les_id)
    st.divider()
    
    st.markdown(f"""
        <div class="card-box" style="background-color: #EFF6FF; border-right: 6px solid #2563EB;">
            <h3 style="color: #1E40AF;">📝 {curr_les['title']}</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # قسم المتربص في نافذة واضحة
    st.markdown("#### 👨‍🎓 قسم المتربص:")
    st.markdown(f"""
        <div class="card-box">
            <p><b>📌 الشرح:</b> {curr_les['trainee_content']['description']}</p>
            <p><b>🛠️ الأنشطة التطبيقية:</b> {curr_les['trainee_content']['activities']}</p>
            <p><b>❓ التقييم الذاتي:</b> {curr_les['trainee_content']['quiz']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # حاسبة المقادير والبطاقة التقنية
    st.markdown("#### 🧮 البطاقة التقنية وحاسبة المقادير التفاعلية:")
    t_card = curr_les['teacher_content']['technical_card']
    
    st.markdown(f"""
        <div class="card-box" style="background-color: #F0FDF4; border-right: 6px solid #10B981;">
            <h4 style="color: #047857;">📌 {t_card['title']}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    base_p = t_card['base_portions']
    target_p = st.number_input("حدد عدد القطع المطلوب تحضيرها:", min_value=1, value=base_p, key=f"calc_{curr_les['id']}")
    ratio = target_p / base_p
    
    st.write(f"**المقادير المعدلة لـ {target_p} قطعة (النسبة الأصلية لـ {base_p} قطعة):**")
    for ing in t_card['ingredients']:
        new_q = ing['qty'] * ratio
        st.markdown(f"- **{ing['item']}**: `{new_q:.1f}` {ing['unit']}")

    # قسم الأستاذ المحمي
    if st.session_state.user_role == 'teacher':
        st.markdown("---")
        st.markdown("#### 👨‍🏫 قسم الأستاذ (خاص ومحمي):")
        st.markdown(f"""
            <div class="card-box" style="background-color: #FEF2F2; border-right: 6px solid #DC2626;">
                <p><b>📐 مخطط الدرس (APC):</b> {curr_les['teacher_content']['apc_plan']}</p>
                <p><b>🎯 الأهداف التعليمية:</b> {curr_les['teacher_content']['objectives']}</p>
                <p><b>📊 شبكة التقييم والمعايير:</b> {curr_les['teacher_content']['evaluation_grid']}</p>
                <p><b>💡 الإجابات النموذجية:</b> {curr_les['teacher_content']['model_answers']}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("🔒 محتوى التوجيه البيداغوجي الخاص بالأستاذ محجوب في وضع معاينة المتربص.")
