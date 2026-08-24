import streamlit as st
import json
import time
from datetime import datetime

# ========================================================================
# 1. إعدادات الصفحة والبيانات الافتراضية
# ========================================================================
st.set_page_config(page_title="الشيف البيداغوجي", layout="wide", initial_sidebar_state="collapsed")

# CSS مخصص للواجهة العربية والمظهر الاحترافي
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, .stApp, div, p, h1, h2, h3, h4, span, label {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    .stButton button {
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        transition: all 0.3s;
        background-color: #f3f4f6;
        color: #1f2937;
        border: 1px solid #e5e7eb;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        border-color: #b8860b;
    }
    .main-header {
        background: linear-gradient(to left, #fffbeb, #ffffff);
        padding: 1.5rem;
        border-radius: 20px;
        border-bottom: 3px solid #f59e0b;
        margin-bottom: 2rem;
        text-align: center;
    }
    .program-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
        cursor: pointer;
        transition: 0.3s;
        height: 100%;
    }
    .program-card:hover {
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border-color: #b8860b;
    }
    .module-card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        border-right: 6px solid #b8860b;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .badge-pending { background: #fef3c7; color: #92400e; padding: 0.1rem 0.6rem; border-radius: 999px; font-size: 0.7rem; }
    .badge-reviewed { background: #d1fae5; color: #065f46; padding: 0.1rem 0.6rem; border-radius: 999px; font-size: 0.7rem; }
    .admin-box { background: #f9f7f4; padding: 1.5rem; border-radius: 16px; border: 1px dashed #d1d5db; }
    hr { margin: 2rem 0; }
    .stExpander { border: 1px solid #e5e7eb !important; border-radius: 12px !important; }
    .stExpander .st-emotion-cache-1h9usn1 { background: #faf8f5; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------
# البيانات الافتراضية الكاملة (نفس الهيكل الهرمي القديم)
# ------------------------------------------------------------------------
DEFAULT_DATA = {
    "programs": [
        {
            "id": "p1",
            "title": "برنامج المرأة الماكثة بالبيت",
            "desc": "برنامج شامل لتكوين المرأة الماكثة بالبيت في صناعة الحلويات",
            "hours": 84,
            "status": "قيد التدقيق",
            "timeDistribution": [
                {"stage": "المقدمة", "duration": "1 ساعة", "notes": "عرض شفهي"},
                {"stage": "تحضير الحشوة", "duration": "10 ساعات", "notes": "تطبيقي"},
                {"stage": "إنجاز حلويات اللوز", "duration": "29 ساعة", "notes": "8 حلويات"},
                {"stage": "الطهي", "duration": "13 ساعة", "notes": "فرن وقلي"},
                {"stage": "التشطيب", "duration": "21 ساعة", "notes": "تطبيقي"},
                {"stage": "النشاط الشامل", "duration": "5 ساعات", "notes": "إنتاج متكامل"},
                {"stage": "التقييم", "duration": "5 ساعات", "notes": "نظري وعملي"}
            ],
            "evaluationCriteria": [
                {"criterion": "احترام الوصفة", "indicator": "احترام المقادير والمراحل"},
                {"criterion": "التنظيم", "indicator": "ترتيب العمل واستغلال الوقت"},
                {"criterion": "التشكيل", "indicator": "انتظام ودقة الأشكال"},
                {"criterion": "الطهي", "indicator": "لون وقوام مناسب"},
                {"criterion": "التشطيب", "indicator": "نظافة ودقة التزيين"},
                {"criterion": "الطعم", "indicator": "توازن النكهات"},
                {"criterion": "القوام", "indicator": "مناسب لنوع الحلوى"},
                {"criterion": "النظافة", "indicator": "احترام قواعد النظافة والسلامة"},
                {"criterion": "التقديم", "indicator": "مظهر مهني جذاب"}
            ],
            "theoryQuestions": [
                "ما أهمية وزن المواد الأولية بدقة؟",
                "ما دور راحة العجينة؟",
                "ما العوامل التي تؤثر في جودة الطهي؟",
                "كيف نميز الحلوى المطهية جيدًا؟",
                "ما شروط نجاح عجينة اللوز؟",
                "ما أهمية التحكم في قوام الحشوة؟",
                "ما قواعد النظافة الواجب احترامها أثناء العمل؟"
            ],
            "modules": [
                {
                    "id": "m1",
                    "title": "MQ1 – إعداد حلويات اللوز",
                    "desc": "إنجاز الحلويات التقليدية الجزائرية المصنوعة من اللوز (84 ساعة)",
                    "cards": [
                        {"id": "c1", "title": "البقلاوة الجزائرية التقليدية", "content": "المقادير: لوز، عسل، عجين...\nالخطوات: التحضير، الطهي، التشطيب.", "status": "قيد التدقيق"},
                        {"id": "c2", "title": "الكفتة الجزائرية", "content": "المقادير: لوز، سكر، زبدة...\nالخطوات: العجن، التشكيل، التزيين.", "status": "قيد التدقيق"},
                        {"id": "c3", "title": "حلوة الفاكهة", "content": "المقادير: عجينة اللوز، ألوان غذائية...\nالخطوات: التلوين، التشكيل.", "status": "قيد التدقيق"},
                        {"id": "c4", "title": "الثومية", "content": "المقادير: لوز، سكر، ماء زهر...\nالخطوات: التشكيل، التلوين.", "status": "قيد التدقيق"},
                        {"id": "c5", "title": "حلوة المشكلة", "content": "المقادير: لوز، سكر، مكسرات...\nالخطوات: تحضير العجينة، الحشو، التشكيل.", "status": "قيد التدقيق"},
                        {"id": "c6", "title": "العرايش الجزائرية", "content": "المقادير: فرينة، سمن، لوز...\nالخطوات: العجن، الحشو، الخبز.", "status": "قيد التدقيق"},
                        {"id": "c7", "title": "التشاراك التقليدي", "content": "المقادير: فرينة، زبدة، سكر...\nالخطوات: العجن، التشكيل، الخبز.", "status": "قيد التدقيق"},
                        {"id": "c8", "title": "الهريسية باللوز", "content": "المقادير: لوز، سكر، بيض...\nالخطوات: الخلط، الطهي، التسقية.", "status": "قيد التدقيق"}
                    ]
                },
                {
                    "id": "m2",
                    "title": "MQ2 – تحضير الحشوات والكريمات",
                    "desc": "تحضير الحشوات المختلفة المستخدمة في الحلويات",
                    "cards": [
                        {"id": "c9", "title": "كريمة اللوز", "content": "مقادير وطريقة تحضير كريمة اللوز التقليدية.", "status": "قيد التدقيق"},
                        {"id": "c10", "title": "الحشوة بالتمر", "content": "مقادير وطريقة تحضير حشوة التمر.", "status": "قيد التدقيق"}
                    ]
                }
            ]
        }
    ]
}

# ========================================================================
# 2. إدارة الجلسة (Session State) وحفظ البيانات
# ========================================================================
def init_session():
    if "app_data" not in st.session_state:
        st.session_state.app_data = json.loads(json.dumps(DEFAULT_DATA))  # نسخ عميق
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "current_program_id" not in st.session_state:
        st.session_state.current_program_id = None
    if "admin_auth" not in st.session_state:
        st.session_state.admin_auth = False
    if "modal_type" not in st.session_state:
        st.session_state.modal_type = None

def save_data():
    # البيانات محفوظة تلقائياً في session_state
    pass

# دوال مساعدة للبحث
def get_program(pid):
    for p in st.session_state.app_data["programs"]:
        if p["id"] == pid:
            return p
    return None

def get_unit(pid, uid):
    p = get_program(pid)
    if not p: return None
    for u in p["modules"]:
        if u["id"] == uid:
            return u
    return None

def generate_id():
    return str(int(time.time() * 1000)) + "_" + str(datetime.now().microsecond)

# ========================================================================
# 3. عرض الصفحات (الرئيسية، التفاصيل، الإدارة)
# ========================================================================
def render_home():
    st.markdown('<div class="main-header"><h1 style="font-size:2.2rem;">🍰 منصة <span style="color:#b8860b;">الشيف البيداغوجي</span></h1><p style="color:#6b7280;">منصة تكوين مهني جزائرية في صناعة الحلويات التقليدية</p><p style="font-size:0.8rem;color:#9ca3af;">إعداد الأستاذة: <strong style="color:#92400e;">حورية فرحي</strong> © 2026</p></div>', unsafe_allow_html=True)

    st.subheader("📚 برامج التكوين")
    programs = st.session_state.app_data["programs"]
    
    if not programs:
        st.info("لا توجد برامج مسجلة. أضف برنامجاً جديداً من لوحة الإدارة.")
        return

    cols = st.columns(3)
    for idx, p in enumerate(programs):
        with cols[idx % 3]:
            status_badge = f'<span class="badge-pending">{p["status"]}</span>' if p["status"] == "قيد التدقيق" else f'<span class="badge-reviewed">{p["status"]}</span>'
            st.markdown(f"""
            <div class="program-card" onclick="window.location.href='?program={p["id"]}'">
                <h3 style="margin:0;font-size:1.2rem;">{p["title"]}</h3>
                <p style="color:#6b7280;font-size:0.9rem;margin:0.3rem 0;">{p["desc"]}</p>
                <span style="background:#fef3c7;padding:0.2rem 0.8rem;border-radius:999px;font-size:0.8rem;">{p["hours"]} ساعة</span>
                {status_badge}
            </div>
            """, unsafe_allow_html=True)
            # معالجة النقر (طريقة Streamlit الصحيحة)
            if st.button(f"📂 فتح {p['title']}", key=f"btn_{p['id']}"):
                st.session_state.current_program_id = p["id"]
                st.session_state.page = "program"
                st.rerun()

def render_program_detail():
    pid = st.session_state.current_program_id
    p = get_program(pid)
    if not p:
        st.error("البرنامج غير موجود")
        if st.button("← العودة للرئيسية"):
            st.session_state.page = "home"
            st.rerun()
        return

    # زر العودة
    if st.button("← العودة للرئيسية", key="back_home"):
        st.session_state.page = "home"
        st.rerun()

    # عنوان البرنامج
    st.markdown(f"""
    <div style="background:white;padding:1.5rem;border-radius:16px;border:1px solid #e5e7eb;margin-bottom:1.5rem;">
        <h2 style="margin:0;font-size:1.8rem;">{p["title"]}</h2>
        <p style="color:#6b7280;">{p["desc"]}</p>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;">
            <span style="background:#fef3c7;padding:0.2rem 1rem;border-radius:999px;">{p["hours"]} ساعة</span>
            <span class="badge-pending">{p["status"]}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # التوزيع الزمني
    if p.get("timeDistribution"):
        with st.expander("⏱️ التوزيع الزمني", expanded=True):
            data = [{"المرحلة": row["stage"], "المدة": row["duration"], "ملاحظات": row.get("notes", "")} for row in p["timeDistribution"]]
            st.table(data)

    # معايير التقييم
    if p.get("evaluationCriteria"):
        with st.expander("⭐ معايير تقييم المنتوج النهائي", expanded=True):
            data = [{"المعيار": row["criterion"], "مؤشر النجاح": row["indicator"]} for row in p["evaluationCriteria"]]
            st.table(data)

    # الأسئلة النظرية
    if p.get("theoryQuestions"):
        with st.expander("📝 أسئلة نظرية", expanded=True):
            for q in p["theoryQuestions"]:
                st.markdown(f"- {q}")

    # النظافة والسلامة
    with st.expander("🧼 النظافة والسلامة المهنية", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - غسل اليدين جيدًا
            - تنظيف وتعقيم سطح العمل
            - استعمال أدوات نظيفة
            - احترام شروط حفظ المواد الأولية
            """)
        with col2:
            st.markdown("""
            - التأكد من صلاحية المواد
            - استعمال الفرن والمعدات بطريقة آمنة
            - ارتداء اللباس المهني المناسب
            """)

    # النشاط الشامل
    with st.expander("🏆 النشاط الشامل", expanded=True):
        st.markdown("""
        في نهاية المقياس، ينجز المتكوّن منتوجًا متكاملًا باستعمال المهارات المكتسبة في الدروس السابقة.
        """)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- اختيار الوصفة\n- قراءة بطاقة الوصفة\n- تحضير المواد")
        with col2:
            st.markdown("- تنظيم مكان العمل\n- تنفيذ المراحل\n- التشطيب والتزيين")
        st.markdown("**📜 الكفاءة النهائية:** ينجز المتكوّن حلوى تقليدية جزائرية قائمة على اللوز وفق الوصفة والتقنيات المهنية، مع احترام الجودة والنظافة والسلامة.")

    # الوحدات والبطاقات
    st.subheader(f"📚 الوحدات ({len(p['modules'])})")
    
    # أزرار إدارة سريعة للبرنامج الحالي
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ إضافة وحدة", key="add_unit_btn"):
            st.session_state.modal_type = "unit"
            st.rerun()
    with col2:
        if st.button("✏️ تعديل البرنامج", key="edit_prog_btn"):
            st.session_state.modal_type = "edit_program"
            st.rerun()
    with col3:
        if st.button("🗑️ حذف البرنامج", key="del_prog_btn"):
            if st.session_state.app_data["programs"]:
                st.session_state.app_data["programs"] = [pr for pr in st.session_state.app_data["programs"] if pr["id"] != pid]
                st.session_state.page = "home"
                st.rerun()

    # عرض الوحدات
    for unit in p["modules"]:
        with st.expander(f"📘 {unit['title']} (عدد البطاقات: {len(unit['cards'])})", expanded=True):
            st.caption(unit["desc"])
            # إدارة الوحدة
            c1, c2, c3 = st.columns([1,1,4])
            with c1:
                if st.button("✏️ تعديل", key=f"edit_unit_{unit['id']}"):
                    st.session_state.modal_type = "edit_unit"
                    st.session_state._edit_unit_id = unit["id"]
                    st.rerun()
            with c2:
                if st.button("🗑️ حذف", key=f"del_unit_{unit['id']}"):
                    p["modules"] = [u for u in p["modules"] if u["id"] != unit["id"]]
                    st.rerun()
            with c3:
                if st.button("➕ إضافة بطاقة", key=f"add_card_{unit['id']}"):
                    st.session_state.modal_type = "card"
                    st.session_state._target_unit_id = unit["id"]
                    st.rerun()
            st.divider()
            
            # عرض البطاقات
            if not unit["cards"]:
                st.info("لا توجد بطاقات في هذه الوحدة")
            else:
                for card in unit["cards"]:
                    with st.expander(f"📄 {card['title']} - {card.get('status', 'قيد التدقيق')}", expanded=True):
                        st.text_area("المحتوى", value=card["content"], height=150, key=f"card_{card['id']}_content", on_change=None)
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("💾 حفظ التعديل", key=f"save_card_{card['id']}"):
                                # تحديث المحتوى من الـ text_area
                                new_content = st.session_state.get(f"card_{card['id']}_content", card["content"])
                                for c in unit["cards"]:
                                    if c["id"] == card["id"]:
                                        c["content"] = new_content
                                        break
                                st.success("تم الحفظ!")
                                time.sleep(0.5)
                                st.rerun()
                        with col2:
                            if st.button("🗑️ حذف البطاقة", key=f"del_card_{card['id']}"):
                                unit["cards"] = [c for c in unit["cards"] if c["id"] != card["id"]]
                                st.rerun()

def render_admin():
    st.markdown('<div class="admin-box">', unsafe_allow_html=True)
    st.subheader("🔐 لوحة الإدارة المتقدمة")
    
    # التحقق من كلمة المرور
    if not st.session_state.admin_auth:
        password = st.text_input("أدخل كلمة مرور الإدارة", type="password")
        if st.button("تسجيل الدخول"):
            if password == "admin123":
                st.session_state.admin_auth = True
                st.success("تم تسجيل الدخول بنجاح!")
                st.rerun()
            else:
                st.error("كلمة مرور خاطئة")
        st.stop()
    
    # عرض البيانات الخام مع خيار التصدير
    st.json(st.session_state.app_data)
    
    # أزرار الإدارة العامة
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("➕ برنامج جديد"):
            st.session_state.modal_type = "program"
            st.rerun()
    with col2:
        if st.button("📥 تصدير JSON"):
            json_str = json.dumps(st.session_state.app_data, ensure_ascii=False, indent=2)
            st.download_button("تحميل الملف", data=json_str, file_name="backup_data.json", mime="application/json")
    with col3:
        if st.button("📤 استيراد JSON"):
            uploaded = st.file_uploader("اختر ملف JSON", type=["json"])
            if uploaded:
                try:
                    new_data = json.load(uploaded)
                    st.session_state.app_data = new_data
                    st.success("تم الاستيراد بنجاح!")
                    st.rerun()
                except:
                    st.error("ملف غير صالح")
    with col4:
        if st.button("🗑️ حذف كل البيانات"):
            if st.checkbox("أنا متأكد، احذف كل شيء"):
                st.session_state.app_data = {"programs": []}
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# ========================================================================
# 4. المودالات (النوافذ المنبثقة) لإضافة وتعديل البيانات
# ========================================================================
def render_modal():
    modal_type = st.session_state.get("modal_type")
    if not modal_type:
        return

    with st.form(key="modal_form", clear_on_submit=True):
        st.markdown(f"### { '➕ إضافة برنامج جديد' if modal_type == 'program' else '➕ إضافة وحدة جديدة' if modal_type == 'unit' else '➕ إضافة بطاقة جديدة' if modal_type == 'card' else '✏️ تعديل' }")
        
        title = ""
        desc = ""
        hours = 0
        status = "قيد التدقيق"
        target_id = None

        if modal_type == "program":
            title = st.text_input("عنوان البرنامج")
            desc = st.text_area("الوصف")
            hours = st.number_input("المدة (ساعات)", min_value=0, step=1)
            status = st.selectbox("الحالة", ["قيد التدقيق", "تمت المراجعة", "قيد التطوير"])
        
        elif modal_type == "unit":
            title = st.text_input("عنوان الوحدة")
            desc = st.text_area("الوصف")
            st.caption("ستتم إضافة الوحدة إلى البرنامج الحالي المفتوح")
        
        elif modal_type == "card":
            title = st.text_input("عنوان البطاقة")
            desc = st.text_area("المحتوى (مقادير، خطوات، ملاحظات)", height=200)
            st.caption("ستتم إضافة البطاقة إلى أول وحدة في البرنامج الحالي")

        elif modal_type == "edit_program":
            pid = st.session_state.current_program_id
            p = get_program(pid)
            if p:
                new_title = st.text_input("العنوان الجديد", value=p["title"])
                new_desc = st.text_area("الوصف الجديد", value=p["desc"])
                new_hours = st.number_input("المدة الجديدة", value=p["hours"])
                if st.form_submit_button("💾 حفظ التعديلات"):
                    p["title"] = new_title
                    p["desc"] = new_desc
                    p["hours"] = new_hours
                    st.session_state.modal_type = None
                    st.rerun()
                if st.form_submit_button("إلغاء"):
                    st.session_state.modal_type = None
                    st.rerun()
                return

        elif modal_type == "edit_unit":
            uid = st.session_state.get("_edit_unit_id")
            pid = st.session_state.current_program_id
            u = get_unit(pid, uid)
            if u:
                new_title = st.text_input("العنوان الجديد", value=u["title"])
                new_desc = st.text_area("الوصف الجديد", value=u["desc"])
                if st.form_submit_button("💾 حفظ التعديلات"):
                    u["title"] = new_title
                    u["desc"] = new_desc
                    st.session_state.modal_type = None
                    st.rerun()
                if st.form_submit_button("إلغاء"):
                    st.session_state.modal_type = None
                    st.rerun()
                return

        # أزرار الحفظ والإلغاء للأنواع الأساسية
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("✅ حفظ")
        with col2:
            cancel = st.form_submit_button("❌ إلغاء")

        if cancel:
            st.session_state.modal_type = None
            st.rerun()

        if submit:
            if not title:
                st.error("الرجاء إدخال العنوان")
                return
            
            if modal_type == "program":
                new_prog = {
                    "id": generate_id(),
                    "title": title,
                    "desc": desc,
                    "hours": hours,
                    "status": status,
                    "timeDistribution": [],
                    "evaluationCriteria": [],
                    "theoryQuestions": [],
                    "modules": []
                }
                st.session_state.app_data["programs"].append(new_prog)
                st.success("تم إضافة البرنامج!")
                
            elif modal_type == "unit":
                pid = st.session_state.current_program_id
                p = get_program(pid)
                if p:
                    p["modules"].append({
                        "id": generate_id(),
                        "title": title,
                        "desc": desc,
                        "cards": []
                    })
                    st.success("تم إضافة الوحدة!")
                else:
                    st.error("البرنامج غير موجود")
            
            elif modal_type == "card":
                pid = st.session_state.current_program_id
                p = get_program(pid)
                if p and p["modules"]:
                    p["modules"][0]["cards"].append({
                        "id": generate_id(),
                        "title": title,
                        "content": desc,
                        "status": "قيد التدقيق"
                    })
                    st.success("تم إضافة البطاقة!")
                else:
                    st.error("البرنامج أو الوحدة غير موجودة")
            
            st.session_state.modal_type = None
            time.sleep(0.5)
            st.rerun()

# ========================================================================
# 5. التشغيل الرئيسي (معالج التنقل والمودال)
# ========================================================================
def main():
    init_session()
    
    # عرض المودال أولاً إذا كان موجوداً
    if st.session_state.get("modal_type"):
        render_modal()
        return  # نمنع عرض الصفحات أثناء ظهور المودال

    # معالجة التنقل
    page = st.session_state.page

    if page == "home":
        render_home()
    elif page == "program":
        render_program_detail()
    else:
        # صفحة الإدارة
        render_admin()

    # شريط جانبي للتنقل السريع
    with st.sidebar:
        st.markdown("---")
        if st.button("🏠 الرئيسية"):
            st.session_state.page = "home"
            st.rerun()
        if st.button("⚙️ لوحة الإدارة"):
            st.session_state.page = "admin"
            st.rerun()
        st.markdown("---")
        st.caption("© 2026 الشيف البيداغوجي - حورية فرحي")

if __name__ == "__main__":
    main()
