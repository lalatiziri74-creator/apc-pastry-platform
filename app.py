
import streamlit as st
from data import PLATFORM_DATA

# ==========================================
# 1. إعدادات الصفحة والتصميم العربي (RTL)
# ==========================================
st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني - APC",
    page_icon="🎓",
    layout="wide"
)

# تطبيق تنسيق المحاذاة العربية والنمط البصري
st.markdown("""
    <style>
    /* محاذاة من اليمين إلى اليسار */
    html, body, [class*="css"]  {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-header { font-size: 26px; font-weight: bold; color: #1E3A8A; text-align: center; margin-bottom: 5px; }
    .sub-header { font-size: 15px; color: #4B5563; text-align: center; margin-bottom: 20px; }
    .watermark { position: fixed; bottom: 10px; left: 10px; opacity: 0.2; font-size: 13px; font-weight: bold; z-index: 1000; }
    .breadcrumb { font-size: 14px; color: #2563EB; background-color: #EFF6FF; padding: 10px 14px; border-radius: 8px; margin-bottom: 20px; border-right: 5px solid #2563EB; }
    .stButton>button { width: 100%; border-radius: 6px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. إدارة الجلسة والتنقل (Session State)
# ==========================================
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_prog_id' not in st.session_state:
    st.session_state.selected_prog_id = None
if 'selected_spec_id' not in st.session_state:
    st.session_state.selected_spec_id = None
if 'selected_mod_id' not in st.session_state:
    st.session_state.selected_mod_id = None
if 'selected_subj_id' not in st.session_state:
    st.session_state.selected_subj_id = None
if 'selected_les_id' not in st.session_state:
    st.session_state.selected_les_id = None
if 'user_role' not in st.session_state:
    st.session_state.user_role = 'trainee'

# ==========================================
# 3. الهيدر والعلامة المائية
# ==========================================
st.markdown('<div class="main-header">🎓 المنصة البيداغوجية للتكوين المهني (APC)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">إشراف وتصميم بيداغوجي: الأستاذة فرحي حورية</div>', unsafe_allow_html=True)
st.markdown('<div class="watermark">إعداد الأستاذة فرحي حورية ©</div>', unsafe_allow_html=True)

# ==========================================
# 4. الشريط الجانبي (الأدوار والأدوات)
# ==========================================
with st.sidebar:
    st.header("⚙️ لوحة المعاينة والصلاحيات")
    role_choice = st.radio(
        "نوع المستخدم (معاينة الواجهة):",
        ["👨‍🎓 متربص (Trainee)", "👨‍🏫 أستاذ (Teacher)"]
    )
    st.session_state.user_role = 'teacher' if "أستاذ" in role_choice else 'trainee'
    
    st.divider()
    st.subheader("🛠️ أدوات بيداغوجية مستقلة")
    tool_choice = st.selectbox("اختر الأداة:", ["-- اختر أداة --", "📜 مولد البطاقات التقنية", "📊 شبكة تقييم المهارات"])
    if tool_choice == "📜 مولد البطاقات التقنية":
        st.info("أداة البطاقات التقنية جاهزة للهيكلة لاحقاً.")
    elif tool_choice == "📊 شبكة تقييم المهارات":
        st.info("أداة تقييم المهارات جاهزة للهيكلة لاحقاً.")
        
    st.divider()
    st.caption("جميع الحقوق محفوظة للأستاذة فرحي حورية ©")

# ==========================================
# 5. شريط البحث وإعطاء زر الرئيسية
# ==========================================
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

# ==========================================
# 6. بناء مسار التنقل (Breadcrumbs)
# ==========================================
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
                                        if les:
                                            path.append(les["title"])
                                            
    st.markdown(f'<div class="breadcrumb">{" ➔ ".join(path)}</div>', unsafe_allow_html=True)

render_breadcrumbs()

# ==========================================
# 7. التحكم في الواجهات الهرمية
# ==========================================

# المستوى 1: الرئيسية (عرض البرامج)
if st.session_state.current_page == 'home':
    st.subheader("📌 اختر برنامج التكوين")
    cols = st.columns(len(PLATFORM_DATA["programs"]))
    
    for idx, prog in enumerate(PLATFORM_DATA["programs"]):
        with cols[idx]:
            st.markdown(f"### {prog['title']}")
            st.write(prog['description'])
            if st.button(f"دخول {prog['title']}", key=prog['id'], use_container_width=True):
                st.session_state.selected_prog_id = prog['id']
                st.session_state.current_page = 'specialties'
                st.rerun()

# المستوى 2: التخصصات
elif st.session_state.current_page == 'specialties':
    if st.button("⬅️ العودة للرئيسية"):
        st.session_state.current_page = 'home'
        st.session_state.selected_prog_id = None
        st.rerun()
        
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    st.subheader(f"📂 التخصصات المتاحة - {curr_prog['title']}")
    
    for spec in curr_prog["specialties"]:
        if st.button(f"🎓 تخصص: {spec['title']} ({spec['code']})", key=spec['id'], use_container_width=True):
            st.session_state.selected_spec_id = spec['id']
            st.session_state.current_page = 'modules'
            st.rerun()

# المستوى 3: الوحدات
elif st.session_state.current_page == 'modules':
    if st.button("⬅️ العودة للتخصصات"):
        st.session_state.current_page = 'specialties'
        st.session_state.selected_spec_id = None
        st.rerun()
        
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    curr_spec = next(s for s in curr_prog["specialties"] if s["id"] == st.session_state.selected_spec_id)
    
    st.subheader(f"📦 الوحدات التكوينية - {curr_spec['title']}")
    for mod in curr_spec["modules"]:
        if st.button(f"📘 {mod['title']}", key=mod['id'], use_container_width=True):
            st.session_state.selected_mod_id = mod['id']
            st.session_state.current_page = 'subjects'
            st.rerun()

# المستوى 4: المقاييس ومخطط المقياس
elif st.session_state.current_page == 'subjects':
    if st.button("⬅️ العودة للوحدات"):
        st.session_state.current_page = 'modules'
        st.session_state.selected_mod_id = None
        st.rerun()
        
    curr_prog = next(p for p in PLATFORM_DATA["programs"] if p["id"] == st.session_state.selected_prog_id)
    curr_spec = next(s for s in curr_prog["specialties"] if s["id"] == st.session_state.selected_spec_id)
    curr_mod = next(m for m in curr_spec["modules"] if m["id"] == st.session_state.selected_mod_id)
    
    st.subheader(f"📐 المقاييس - {curr_mod['title']}")
    for subj in curr_mod["subjects"]:
        st.write(f"**📑 مخطط المقياس:** {subj['syllabus']}")
        if st.button(f"دخول {subj['title']}", key=subj['id'], use_container_width=True):
            st.session_state.selected_subj_id = subj['id']
            st.session_state.current_page = 'lessons'
            st.rerun()

# المستوى 5: الدروس (عرض قسم المتربص وقسم الأستاذ)
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
    
    st.subheader(f"📖 الدروس والبطاقات - {curr_subj['title']}")
    
    les_options = {les['title']: les['id'] for les in curr_subj["lessons"]}
    selected_les_title = st.selectbox("اختر الدرس للعرض:", list(les_options.keys()))
    selected_les_id = les_options[selected_les_title]
    st.session_state.selected_les_id = selected_les_id
    
    curr_les = next(l for l in curr_subj["lessons"] if l["id"] == selected_les_id)
    
    st.divider()
    
    if curr_les["is_premium"]:
        st.warning("⭐ هذا الدرس ينتمي للمحتوى المتقدم (Premium).")
    else:
        st.info("🟢 هذا الدرس متاح مجاناً (Free Access).")
        
    st.markdown(f"### 📝 {curr_les['title']}")
    
    # 1. محتوى المتربص
    st.markdown("#### 👨‍🎓 قسم المتربص:")
    st.write(f"**الشرح:** {curr_les['trainee_content']['description']}")
    st.write(f"**الأنشطة والتمارين:** {curr_les['trainee_content']['activities']}")
    st.write(f"**التقييم الذاتي:** {curr_les['trainee_content']['quiz']}")
    
    # 2. محتوى الأستاذ
    if st.session_state.user_role == 'teacher':
        st.markdown("---")
        st.markdown("#### 👨‍🏫 قسم الأستاذ (خاص ومحمي):")
        st.write(f"**مخطط الدرس (APC):** {curr_les['teacher_content']['apc_plan']}")
        st.write(f"**الأهداف التعليمية:** {curr_les['teacher_content']['objectives']}")
        st.write(f"**شبكة التقييم والمعايير:** {curr_les['teacher_content']['evaluation_grid']}")
        st.write(f"**التصحيح والإجابة النموذجية:** {curr_les['teacher_content']['model_answers']}")
        st.write(f"**البطاقة التقنية:** {curr_les['teacher_content']['technical_card']}")
    else:
        st.warning("🔒 تنبيه أمان: محتوى الأستاذ محجوب عن المتربص.")
