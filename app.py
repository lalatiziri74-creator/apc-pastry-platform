import streamlit as st
import json
import time
from datetime import datetime

# ========================================================================
# 1. إعدادات الصفحة والواجهة
# ========================================================================
st.set_page_config(page_title="الشيف البيداغوجي", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, .stApp, div, p, h1, h2, h3, h4, span, label {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    .main > div { overflow-y: auto !important; height: 100vh !important; }
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; border-radius: 10px; }
    ::-webkit-scrollbar-thumb { background: #b8860b; border-radius: 10px; }
    .stButton button { width: 100%; border-radius: 12px; font-weight: bold; transition: 0.3s; background: #f3f4f6; border: 1px solid #e5e7eb; }
    .stButton button:hover { transform: translateY(-2px); border-color: #b8860b; }
    .main-header { background: linear-gradient(to left, #fffbeb, #ffffff); padding: 1.5rem; border-radius: 20px; border-bottom: 3px solid #f59e0b; margin-bottom: 2rem; text-align: center; }
    .program-card { background: white; padding: 1.5rem; border-radius: 16px; border: 1px solid #e5e7eb; box-shadow: 0 4px 6px rgba(0,0,0,0.03); transition: 0.3s; height: 100%; }
    .program-card:hover { box-shadow: 0 10px 25px rgba(0,0,0,0.08); border-color: #b8860b; }
    .sub-program-card { border-right: 4px solid #b8860b; background: #faf8f5; }
    .badge-pending { background: #fef3c7; color: #92400e; padding: 0.1rem 0.6rem; border-radius: 999px; font-size: 0.7rem; }
    .badge-dev { background: #e0f2fe; color: #0369a1; padding: 0.1rem 0.6rem; border-radius: 999px; font-size: 0.7rem; }
    .admin-box { background: #f9f7f4; padding: 1.5rem; border-radius: 16px; border: 1px dashed #d1d5db; }
    .stExpander { border: 1px solid #e5e7eb !important; border-radius: 12px !important; }
    .stExpander .st-emotion-cache-1h9usn1 { background: #faf8f5; }
    .ingredient-item { background: #f9f7f4; padding: 0.2rem 0.8rem; border-radius: 6px; border: 1px solid #e5e7eb; display: inline-block; margin: 0.2rem; }
    .ingredient-list { display: flex; flex-wrap: wrap; gap: 0.3rem; }
</style>
""", unsafe_allow_html=True)

# ========================================================================
# 2. البيانات الافتراضية
# ========================================================================
DEFAULT_DATA = {
    "programs": [
        {
            "id": "p_woman",
            "title": "برنامج المرأة الماكثة بالبيت",
            "desc": "برنامج شامل لتكوين المرأة الماكثة بالبيت في صناعة الحلويات",
            "hours": 84,
            "status": "قيد التدقيق",
            "type": "parent",
            "subPrograms": [
                {
                    "id": "p_traditional",
                    "title": "برنامج الحلويات التقليدية",
                    "desc": "مقياس مهني في صناعة الحلويات التقليدية الجزائرية",
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
                            "desc": "إنجاز الحلويات التقليدية الجزائرية المصنوعة من اللوز",
                            "cards": [
                                {"id": "c1", "title": "البقلاوة الجزائرية", "content": "المقادير: لوز، عسل، عجين...\nالخطوات: التحضير، الطهي، التشطيب.", "status": "قيد التدقيق", "ingredients": [{"name": "لوز", "amount": 3, "unit": "كيلات"}, {"name": "سكر", "amount": 2, "unit": "كيلتان"}]},
                                {"id": "c2", "title": "الكفتة الجزائرية", "content": "المقادير: لوز، سكر، زبدة...\nالخطوات: العجن، التشكيل، التزيين.", "status": "قيد التدقيق", "ingredients": [{"name": "لوز", "amount": 3, "unit": "كيلات"}, {"name": "سكر ناعم", "amount": 2, "unit": "كيلتان"}]},
                                {"id": "c3", "title": "حلوة الفاكهة", "content": "المقادير: عجينة اللوز، ألوان غذائية...\nالخطوات: التلوين، التشكيل.", "status": "قيد التدقيق"},
                                {"id": "c4", "title": "الثومية", "content": "المقادير: لوز، سكر، ماء زهر...\nالخطوات: التشكيل، التلوين.", "status": "قيد التدقيق"},
                                {"id": "c5", "title": "حلوة المشكلة", "content": "المقادير: لوز، سكر، مكسرات...\nالخطوات: تحضير العجينة، الحشو، التشكيل.", "status": "قيد التدقيق"},
                                {"id": "c6", "title": "العرايش الجزائرية", "content": "المقادير: فرينة، سمن، لوز...\nالخطوات: العجن، الحشو، الخبز.", "status": "قيد التدقيق"},
                                {"id": "c7", "title": "التشاراك التقليدي", "content": "المقادير: فرينة، زبدة، سكر...\nالخطوات: العجن، التشكيل، الخبز.", "status": "قيد التدقيق"},
                                {"id": "c8", "title": "الهريسية باللوز", "content": "المقادير: لوز، سكر، بيض...\nالخطوات: الخلط، الطهي، التسقية.", "status": "قيد التدقيق"}
                            ]
                        },
                        {"id": "m2", "title": "MQ2 – حلويات السميد", "desc": "ستضاف البطاقات لاحقاً", "cards": []},
                        {"id": "m3", "title": "MC1 – تكنولوجيا عامة", "desc": "ستضاف البطاقات لاحقاً", "cards": []},
                        {"id": "m4", "title": "MC2 – الأمن والسلامة", "desc": "ستضاف البطاقات لاحقاً", "cards": []}
                    ]
                },
                {"id": "p_oriental", "title": "برنامج الحلويات الشرقية", "desc": "قيد التطوير – سيتم الإعلان عن تفاصيله قريباً", "hours": 0, "status": "قيد التطوير", "modules": []},
                {"id": "p_western", "title": "برنامج الحلويات الغربية", "desc": "قيد التطوير – سيتم الإعلان عن تفاصيله قريباً", "hours": 0, "status": "قيد التطوير", "modules": []}
            ]
        },
        {
            "id": "p_apprenticeship",
            "title": "برنامج التمهين",
            "desc": "برنامج التكوين عن طريق التمهين في مجال صناعة الحلويات",
            "hours": 120,
            "status": "قيد التدقيق",
            "type": "simple",
            "modules": []
        },
        {
            "id": "p_fulltime",
            "title": "برنامج التكوين الحضوري",
            "desc": "برنامج تكوين حضوري متخصص في صناعة الحلويات التقليدية",
            "hours": 200,
            "status": "قيد التدقيق",
            "type": "simple",
            "modules": []
        }
    ]
}

# ========================================================================
# 3. إدارة الجلسة
# ========================================================================
def init_session():
    if "app_data" not in st.session_state:
        st.session_state.app_data = json.loads(json.dumps(DEFAULT_DATA))
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "current_program_id" not in st.session_state:
        st.session_state.current_program_id = None
    if "current_sub_program_id" not in st.session_state:
        st.session_state.current_sub_program_id = None
    if "admin_auth" not in st.session_state:
        st.session_state.admin_auth = False
    if "modal_type" not in st.session_state:
        st.session_state.modal_type = None
    if "view_mode" not in st.session_state:
        st.session_state.view_mode = "programs"
    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False
    if "locked" not in st.session_state:
        st.session_state.locked = False

def get_program(pid):
    for p in st.session_state.app_data["programs"]:
        if p["id"] == pid:
            return p
    return None

def get_sub_program(pid, spid):
    p = get_program(pid)
    if not p or "subPrograms" not in p:
        return None
    for sp in p["subPrograms"]:
        if sp["id"] == spid:
            return sp
    return None

def generate_id():
    return str(int(time.time() * 1000)) + "_" + str(datetime.now().microsecond)

def render_ingredients(ingredients, factor=1):
    if not ingredients:
        return "لا توجد مقادير مسجلة"
    html = '<div class="ingredient-list">'
    for item in ingredients:
        amount = item["amount"] * factor
        display = f"{amount:.2f}" if amount % 1 != 0 else str(int(amount))
        html += f'<span class="ingredient-item">{item["name"]}: <strong>{display}</strong> {item["unit"]}</span>'
    html += '</div>'
    return html

# ========================================================================
# 4. الصفحات
# ========================================================================
def render_home():
    st.markdown('<div class="main-header"><h1 style="font-size:2.2rem;">🍰 منصة <span style="color:#b8860b;">الشيف البيداغوجي</span></h1><p style="color:#6b7280;">منصة تكوين مهني جزائرية في صناعة الحلويات التقليدية</p><p style="font-size:0.8rem;color:#9ca3af;">إعداد الأستاذة: <strong style="color:#92400e;">حورية فرحي</strong> © 2026</p></div>', unsafe_allow_html=True)
    st.subheader("📚 برامج التكوين")
    programs = st.session_state.app_data["programs"]
    if not programs:
        st.info("لا توجد برامج مسجلة.")
        return
    cols = st.columns(3)
    for idx, p in enumerate(programs):
        with cols[idx % 3]:
            badge = f'<span class="badge-pending">{p["status"]}</span>' if p["status"] == "قيد التدقيق" else f'<span class="badge-dev">{p["status"]}</span>'
            icon = "📂" if p.get("type") == "parent" else "📄"
            st.markdown(f"""
            <div class="program-card">
                <div style="display:flex;justify-content:space-between;align-items:start;">
                    <div>
                        <h3 style="margin:0;font-size:1.2rem;">{icon} {p["title"]}</h3>
                        <p style="color:#6b7280;font-size:0.9rem;margin:0.3rem 0;">{p["desc"]}</p>
                    </div>
                </div>
                <div style="margin-top:0.5rem;">{badge}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"📂 فتح {p['title']}", key=f"btn_{p['id']}"):
                st.session_state.current_program_id = p["id"]
                st.session_state.current_sub_program_id = None
                if p.get("type") == "parent" and p.get("subPrograms"):
                    st.session_state.view_mode = "sub_programs"
                else:
                    st.session_state.view_mode = "detail"
                st.session_state.page = "program"
                st.rerun()

def render_sub_programs():
    pid = st.session_state.current_program_id
    p = get_program(pid)
    if not p:
        st.error("البرنامج غير موجود")
        st.session_state.page = "home"
        st.rerun()
        return
    if st.button("← العودة للرئيسية"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown(f"<h2 style='font-size:1.8rem;'>📂 {p['title']}</h2><p style='color:#6b7280;'>{p['desc']}</p><p style='color:#9ca3af;'>اختر المسار الذي ترغب في الالتحاق به</p>", unsafe_allow_html=True)
    st.subheader("📚 البرامج الفرعية")
    sub_programs = p.get("subPrograms", [])
    if not sub_programs:
        st.info("لا توجد برامج فرعية.")
        return
    cols = st.columns(3)
    for idx, sp in enumerate(sub_programs):
        with cols[idx % 3]:
            is_pending = sp["status"] == "قيد التطوير"
            icon = "🔜" if is_pending else "🍰"
            badge = f'<span class="badge-dev">{sp["status"]}</span>' if is_pending else f'<span class="badge-pending">{sp["status"]}</span>'
            st.markdown(f"""
            <div class="program-card sub-program-card">
                <div style="display:flex;justify-content:space-between;align-items:start;">
                    <div>
                        <h3 style="margin:0;font-size:1.2rem;">{icon} {sp["title"]}</h3>
                        <p style="color:#6b7280;font-size:0.9rem;margin:0.3rem 0;">{sp["desc"]}</p>
                    </div>
                </div>
                <div style="margin-top:0.5rem;">{badge}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"📂 فتح {sp['title']}", key=f"btn_sub_{sp['id']}"):
                if not is_pending:
                    st.session_state.current_sub_program_id = sp["id"]
                    st.session_state.view_mode = "detail"
                    st.rerun()
                else:
                    st.info("هذا البرنامج قيد التطوير، سيتم الإعلان عن تفاصيله قريباً.")

def render_program_detail():
    pid = st.session_state.current_program_id
    spid = st.session_state.current_sub_program_id
    if spid:
        p = get_sub_program(pid, spid)
        if not p:
            st.error("البرنامج الفرعي غير موجود")
            st.session_state.view_mode = "sub_programs"
            st.rerun()
            return
        is_sub = True
    else:
        p = get_program(pid)
        if not p:
            st.error("البرنامج غير موجود")
            st.session_state.page = "home"
            st.rerun()
            return
        is_sub = False

    col1, col2, col3 = st.columns([1,1,2])
    with col1:
        if st.session_state.locked:
            if st.button("🔓 فتح التعديل (كلمة مرور)", key="unlock_btn"):
                pw = st.text_input("أدخل كلمة المرور", type="password", key="unlock_pw")
                if pw == "farhi123":
                    st.session_state.locked = False
                    st.success("تم فتح التعديل!")
                    st.rerun()
                elif pw:
                    st.error("كلمة مرور خاطئة")
        else:
            if st.button("🔒 قفل المنصة (نشر)", key="lock_btn"):
                st.session_state.locked = True
                st.success("تم قفل المنصة! لن يتمكن أحد من التعديل.")
                st.rerun()
    with col2:
        if not st.session_state.locked:
            if st.button("✏️ تفعيل التعديل المباشر", key="toggle_edit_btn"):
                st.session_state.edit_mode = not st.session_state.edit_mode
                st.rerun()
    with col3:
        if is_sub:
            if st.button("← العودة للبرامج الفرعية"):
                st.session_state.view_mode = "sub_programs"
                st.session_state.current_sub_program_id = None
                st.rerun()
        else:
            if st.button("← العودة للرئيسية"):
                st.session_state.page = "home"
                st.rerun()

    if st.session_state.edit_mode and not st.session_state.locked:
        with st.form(key="edit_program_main"):
            new_title = st.text_input("العنوان", value=p["title"])
            new_desc = st.text_area("الوصف", value=p["desc"])
            new_hours = st.number_input("عدد الساعات", value=p["hours"], step=1)
            new_status = st.selectbox("الحالة", ["قيد التدقيق", "تمت المراجعة", "قيد التطوير"], index=["قيد التدقيق", "تمت المراجعة", "قيد التطوير"].index(p["status"]) if p["status"] in ["قيد التدقيق", "تمت المراجعة", "قيد التطوير"] else 0)
            if st.form_submit_button("💾 حفظ معلومات البرنامج"):
                p["title"] = new_title
                p["desc"] = new_desc
                p["hours"] = new_hours
                p["status"] = new_status
                st.success("تم حفظ التعديلات!")
                time.sleep(0.5)
                st.rerun()
        st.divider()
    else:
        st.markdown(f"<h2 style='font-size:1.8rem;'>{p['title']}</h2><p style='color:#6b7280;'>{p['desc']}</p><div style='display:flex;gap:0.5rem;flex-wrap:wrap;margin-top:0.5rem;'><span style='background:#fef3c7;padding:0.2rem 1rem;border-radius:999px;'>{p['hours']} ساعة</span><span class='badge-pending'>{p['status']}</span></div>", unsafe_allow_html=True)

    if p.get("timeDistribution") and len(p["timeDistribution"]) > 0:
        with st.expander("⏱️ التوزيع الزمني", expanded=True):
            st.table([{"المرحلة": row["stage"], "المدة": row["duration"], "ملاحظات": row.get("notes", "")} for row in p["timeDistribution"]])
    if p.get("evaluationCriteria") and len(p["evaluationCriteria"]) > 0:
        with st.expander("⭐ معايير تقييم المنتوج النهائي", expanded=True):
            st.table([{"المعيار": row["criterion"], "مؤشر النجاح": row["indicator"]} for row in p["evaluationCriteria"]])
    if p.get("theoryQuestions") and len(p["theoryQuestions"]) > 0:
        with st.expander("📝 أسئلة نظرية", expanded=True):
            for q in p["theoryQuestions"]:
                st.markdown(f"- {q}")
    with st.expander("🧼 النظافة والسلامة المهنية", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- غسل اليدين جيدًا\n- تنظيف وتعقيم سطح العمل\n- استعمال أدوات نظيفة\n- احترام شروط حفظ المواد الأولية")
        with col2:
            st.markdown("- التأكد من صلاحية المواد\n- استعمال الفرن والمعدات بطريقة آمنة\n- ارتداء اللباس المهني المناسب")
    with st.expander("🏆 النشاط الشامل", expanded=True):
        st.markdown("في نهاية المقياس، ينجز المتكوّن منتوجًا متكاملًا باستعمال المهارات المكتسبة في الدروس السابقة.")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- اختيار الوصفة\n- قراءة بطاقة الوصفة\n- تحضير المواد")
        with col2:
            st.markdown("- تنظيم مكان العمل\n- تنفيذ المراحل\n- التشطيب والتزيين")
        st.markdown("**📜 الكفاءة النهائية:** ينجز المتكوّن حلوى تقليدية جزائرية قائمة على اللوز وفق الوصفة والتقنيات المهنية، مع احترام الجودة والنظافة والسلامة.")

    modules = p.get("modules", [])
    st.subheader(f"📚 الوحدات ({len(modules)})")

    if not st.session_state.locked:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("➕ إضافة وحدة"):
                st.session_state.modal_type = "unit"
                st.rerun()
        with col2:
            if st.button("✏️ تعديل البرنامج"):
                st.session_state.modal_type = "edit_program"
                st.rerun()
        with col3:
            if st.button("🗑️ حذف البرنامج"):
                if is_sub:
                    parent = get_program(pid)
                    if parent and "subPrograms" in parent:
                        parent["subPrograms"] = [sp for sp in parent["subPrograms"] if sp["id"] != spid]
                        st.session_state.view_mode = "sub_programs"
                        st.session_state.current_sub_program_id = None
                        st.rerun()
                else:
                    st.session_state.app_data["programs"] = [pr for pr in st.session_state.app_data["programs"] if pr["id"] != pid]
                    st.session_state.page = "home"
                    st.rerun()

    if not modules:
        st.info("لا توجد وحدات مسجلة في هذا البرنامج.")
    else:
        for unit in modules:
            with st.expander(f"📘 {unit['title']} (عدد البطاقات: {len(unit['cards'])})", expanded=True):
                st.caption(unit["desc"])
                if not st.session_state.locked:
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

                if not unit["cards"]:
                    st.info("لا توجد بطاقات في هذه الوحدة")
                else:
                    for card in unit["cards"]:
                        if st.session_state.edit_mode and not st.session_state.locked:
                            with st.expander(f"📄 {card['title']} - {card.get('status', 'قيد التدقيق')}", expanded=True):
                                new_title = st.text_input("عنوان البطاقة", value=card["title"], key=f"title_{card['id']}")
                                new_content = st.text_area("المحتوى", value=card["content"], height=200, key=f"content_{card['id']}")
                                new_status = st.selectbox("الحالة", ["قيد التدقيق", "تمت المراجعة", "قيد التطوير"], index=["قيد التدقيق", "تمت المراجعة", "قيد التطوير"].index(card.get("status", "قيد التدقيق")), key=f"status_{card['id']}")
                                if st.button("💾 حفظ البطاقة", key=f"save_card_{card['id']}"):
                                    card["title"] = new_title
                                    card["content"] = new_content
                                    card["status"] = new_status
                                    st.success("تم حفظ البطاقة!")
                                    time.sleep(0.5)
                                    st.rerun()
                                if st.button("🗑️ حذف البطاقة", key=f"del_card_{card['id']}"):
                                    unit["cards"] = [c for c in unit["cards"] if c["id"] != card["id"]]
                                    st.rerun()
                        else:
                            with st.expander(f"📄 {card['title']} - {card.get('status', 'قيد التدقيق')}", expanded=True):
                                st.text_area("المحتوى", value=card["content"], height=150, key=f"view_{card['id']}", disabled=True)
                                if "ingredients" in card and card["ingredients"]:
                                    st.markdown("**⚖️ المقادير:**")
                                    st.markdown(render_ingredients(card["ingredients"]), unsafe_allow_html=True)

# ========================================================================
# 5. الإدارة
# ========================================================================
def render_admin():
    st.markdown('<div class="admin-box">', unsafe_allow_html=True)
    st.subheader("🔐 لوحة الإدارة")
    if not st.session_state.admin_auth:
        password = st.text_input("أدخل كلمة مرور الإدارة", type="password")
        if st.button("تسجيل الدخول"):
            if password == "farhi123":
                st.session_state.admin_auth = True
                st.success("تم تسجيل الدخول بنجاح!")
                st.rerun()
            else:
                st.error("كلمة مرور خاطئة")
        st.stop()
    programs = st.session_state.app_data["programs"]
    total_programs = len(programs)
    total_modules = sum(len(p.get("modules", [])) for p in programs)
    total_cards = sum(len(card) for p in programs for m in p.get("modules", []) for card in m.get("cards", []))
    st.metric("📊 إحصائيات المنصة", f"{total_programs} برامج | {total_modules} وحدة | {total_cards} بطاقة")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("➕ برنامج جديد"):
            st.session_state.modal_type = "program"
            st.rerun()
    with col2:
        if st.button("📥 تصدير البيانات"):
            json_str = json.dumps(st.session_state.app_data, ensure_ascii=False, indent=2)
            st.download_button("تحميل الملف", data=json_str, file_name="backup_data.json", mime="application/json")
    with col3:
        if st.button("📤 استيراد بيانات"):
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
        if st.button("🗑️ حذف الكل"):
            if st.checkbox("أنا متأكد، احذف كل شيء"):
                st.session_state.app_data = {"programs": []}
                st.rerun()
    st.subheader("📋 قائمة البرامج")
    for p in programs:
        with st.expander(f"📂 {p['title']} ({p['hours']} ساعة)", expanded=False):
            st.markdown(f"**الوصف:** {p['desc']}")
            st.markdown(f"**الحالة:** {p['status']}")
            if p.get("type") == "parent" and p.get("subPrograms"):
                st.markdown("**البرامج الفرعية:**")
                for sp in p["subPrograms"]:
                    st.markdown(f"- {sp['title']} ({sp['hours']} ساعة) – {sp['status']}")
            elif p.get("modules"):
                st.markdown(f"**عدد الوحدات:** {len(p['modules'])}")
                for m in p["modules"]:
                    st.markdown(f"- {m['title']} ({len(m['cards'])} بطاقة)")
    st.markdown('</div>', unsafe_allow_html=True)

# ========================================================================
# 6. المودالات
# ========================================================================
def render_modal():
    modal_type = st.session_state.get("modal_type")
    if not modal_type:
        return
    with st.form(key="modal_form", clear_on_submit=True):
        st.markdown(f"### { '➕ إضافة برنامج جديد' if modal_type == 'program' else '➕ إضافة وحدة جديدة' if modal_type == 'unit' else '➕ إضافة بطاقة جديدة' if modal_type == 'card' else '✏️ تعديل' }")
        if modal_type == "program":
            title = st.text_input("عنوان البرنامج")
            desc = st.text_area("الوصف")
            hours = st.number_input("المدة (ساعات)", min_value=0, step=1)
            status = st.selectbox("الحالة", ["قيد التدقيق", "تمت المراجعة", "قيد التطوير"])
            prog_type = st.selectbox("نوع البرنامج", ["simple", "parent"], format_func=lambda x: "برنامج عادي" if x == "simple" else "برنامج رئيسي (له برامج فرعية)")
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
                new_prog = {"id": generate_id(), "title": title, "desc": desc, "hours": hours, "status": status, "type": prog_type, "subPrograms": [] if prog_type == "parent" else None, "modules": [] if prog_type == "simple" else None}
                st.session_state.app_data["programs"].append(new_prog)
                st.success("تم إضافة البرنامج!")
                st.session_state.modal_type = None
                time.sleep(0.5)
                st.rerun()
        elif modal_type == "unit":
            title = st.text_input("عنوان الوحدة")
            desc = st.text_area("الوصف")
            st.caption("ستتم إضافة الوحدة إلى البرنامج الحالي المفتوح")
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
                pid = st.session_state.current_program_id
                spid = st.session_state.current_sub_program_id
                target = get_sub_program(pid, spid) if spid else get_program(pid)
                if target:
                    if "modules" not in target:
                        target["modules"] = []
                    target["modules"].append({"id": generate_id(), "title": title, "desc": desc, "cards": []})
                    st.success("تم إضافة الوحدة!")
                else:
                    st.error("البرنامج غير موجود")
                st.session_state.modal_type = None
                time.sleep(0.5)
                st.rerun()
        elif modal_type == "card":
            title = st.text_input("عنوان البطاقة")
            desc = st.text_area("المحتوى (مقادير، خطوات، ملاحظات)", height=200)
            st.caption("ستتم إضافة البطاقة إلى أول وحدة في البرنامج الحالي")
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
                pid = st.session_state.current_program_id
                spid = st.session_state.current_sub_program_id
                target = get_sub_program(pid, spid) if spid else get_program(pid)
                if target and target.get("modules") and len(target["modules"]) > 0:
                    target["modules"][0]["cards"].append({"id": generate_id(), "title": title, "content": desc, "status": "قيد التدقيق", "ingredients": []})
                    st.success("تم إضافة البطاقة!")
                else:
                    st.error("البرنامج أو الوحدة غير موجودة")
                st.session_state.modal_type = None
                time.sleep(0.5)
                st.rerun()
        elif modal_type == "edit_program":
            pid = st.session_state.current_program_id
            spid = st.session_state.current_sub_program_id
            target = get_sub_program(pid, spid) if spid else get_program(pid)
            if target:
                new_title = st.text_input("العنوان الجديد", value=target["title"])
                new_desc = st.text_area("الوصف الجديد", value=target["desc"])
                new_hours = st.number_input("المدة الجديدة", value=target["hours"])
                col1, col2 = st.columns(2)
                with col1:
                    if st.form_submit_button("💾 حفظ التعديلات"):
                        target["title"] = new_title
                        target["desc"] = new_desc
                        target["hours"] = new_hours
                        st.session_state.modal_type = None
                        st.rerun()
                with col2:
                    if st.form_submit_button("إلغاء"):
                        st.session_state.modal_type = None
                        st.rerun()
            return
        elif modal_type == "edit_unit":
            uid = st.session_state.get("_edit_unit_id")
            pid = st.session_state.current_program_id
            spid = st.session_state.current_sub_program_id
            target = get_sub_program(pid, spid) if spid else get_program(pid)
            if target:
                unit = next((u for u in target.get("modules", []) if u["id"] == uid), None)
                if unit:
                    new_title = st.text_input("العنوان الجديد", value=unit["title"])
                    new_desc = st.text_area("الوصف الجديد", value=unit["desc"])
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.form_submit_button("💾 حفظ التعديلات"):
                            unit["title"] = new_title
                            unit["desc"] = new_desc
                            st.session_state.modal_type = None
                            st.rerun()
                    with col2:
                        if st.form_submit_button("إلغاء"):
                            st.session_state.modal_type = None
                            st.rerun()
            return

# ========================================================================
# 7. التشغيل الرئيسي
# ========================================================================
def main():
    init_session()
    if st.session_state.get("modal_type"):
        render_modal()
        return
    page = st.session_state.page
    view_mode = st.session_state.get("view_mode", "programs")
    if page == "home":
        render_home()
    elif page == "program":
        if view_mode == "sub_programs":
            render_sub_programs()
        else:
            render_program_detail()
    else:
        render_admin()
    with st.sidebar:
        st.markdown("---")
        if st.button("🏠 الرئيسية"):
            st.session_state.page = "home"
            st.session_state.view_mode = "programs"
            st.session_state.current_sub_program_id = None
            st.rerun()
        if st.button("⚙️ لوحة الإدارة"):
            st.session_state.page = "admin"
            st.rerun()
        st.markdown("---")
        if st.session_state.locked:
            st.warning("🔒 المنصة مقفلة (وضع النشر)")
        else:
            st.success("🔓 المنصة مفتوحة للتعديل")
        st.caption("© 2026 الشيف البيداغوجي - حورية فرحي")

if __name__ == "__main__":
    main()
