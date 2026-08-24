import json
import os
import uuid
import streamlit as st
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# مسارات الملفات الدائمة
DATA_FILE = "platform_data.json"
UPLOADS_DIR = "uploaded_files"

if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR, exist_ok=True)

# هيكل البيانات الافتراضي الشامل (يحتوي على البرامج الثلاثة الأساسية)
DEFAULT_DATA = {
    "settings": {
        "platform_name": "المنصة البيداغوجية للتكوين المهني (APC)",
        "admin_password": "admin",
        "supervisor_name": "إشراف الأستاذة: فرحي حورية"
    },
    "programs": [
        {
            "id": "prog_tamheen",
            "name": "برنامج التكوين بالتمهين",
            "description": "البرنامج البيداغوجي الخاص بالمتربصين في صيغة التمهين المهني.",
            "units": [
                {
                    "id": "unit_t_1",
                    "name": "الوحدة الأساسية للتمهين والورشات التطبيقية",
                    "lessons": [
                        {
                            "id": "les_t_1",
                            "name": "قواعد العمل داخل ورشات الحلويات المهنية",
                            "content": "التعرف على تنظيم الورشة، احترام قواعد الأمن والسلامة المهنية.",
                            "objectives": "فهم محيط العمل المهني.",
                            "competencies": "الانضباط والتنظيم في الورشة.",
                            "pedagogy": "التكوين الميداني والتطبيقي.",
                            "steps": "1. تحضير الهندام المهني. 2. تعقيم وتجهيز طاولات العمل.",
                            "evaluation": "تقييم ميداني لسلوك المتربص.",
                            "technical_sheets": [],
                            "recipes": []
                        }
                    ]
                }
            ]
        },
        {
            "id": "prog_houdouri",
            "name": "برنامج التكوين الحضوري",
            "description": "البرنامج الموجه للأفواج الحضورية داخل المؤسسة التكوينية.",
            "units": [
                {
                    "id": "unit_h_1",
                    "name": "وحدة الدروس النظرية والتطبيقية الحضورية",
                    "lessons": [
                        {
                            "id": "les_h_1",
                            "name": "دراسة المواد الأولية في صناعة الحلويات",
                            "content": "الخصائص الفيزيائية والكيميائية للدقيق، السكريات، والمواد الدسمة.",
                            "objectives": "معرفة دور كل مكون أساسي في الوصفة.",
                            "competencies": "القدرة على اختيار المواد الأولية بدقة.",
                            "pedagogy": "المحاضرة التطبيقية والتجارب المخبرية المصغرة.",
                            "steps": "1. تصنيف المواد. 2. دراسة تأثير الحرارة عليها.",
                            "evaluation": "اختبار كتابي وتقييم تفاعلي.",
                            "technical_sheets": [],
                            "recipes": []
                        }
                    ]
                }
            ]
        },
        {
            "id": "prog_makatha",
            "name": "برنامج المرأة الماكثة بالبيت",
            "description": "برنامج تأهيلي مهني متكامل يضم تخصصات الحلويات المختلفة.",
            "units": [
                {
                    "id": "unit_m_trad",
                    "name": "حلويات تقليدية",
                    "lessons": [
                        {
                            "id": "les_m_trad",
                            "name": "ورشة الحلويات التقليدية الجزائرية العتيقة",
                            "content": "صناعة المقروط، كعب الغزال، والحلويات المعسلة بأصولها الفنية.",
                            "objectives": "الحفاظ على التراث الاصيل واحتراف صنعه.",
                            "competencies": "إتقان النقش، العجن، والتعسيل الصحيح.",
                            "pedagogy": "التعلم بالممارسة والمحاكاة المباشرة.",
                            "steps": "1. تحضير الغرس والعجينة. 2. التشكيل والنقش. 3. الطهي والتعسيل.",
                            "evaluation": "تقييم شكلي وتذوقي للحلويات.",
                            "technical_sheets": [
                                {
                                    "id": "ts_makrood",
                                    "title": "البطاقة التقنية: مقروط اللوز التقليدي",
                                    "category": "حلويات تقليدية",
                                    "ingredients_list": "لوز مطحون، سكر عادي، عطور، ماء زهر",
                                    "quantities": "1كغ لوز، 300غ سكر، ماء زهر",
                                    "steps": "مزج اللوز والسكر، البلل بماء الزهر، التشكيل.",
                                    "temperature": "160°C",
                                    "bake_time": "15 دقيقة",
                                    "prep_time": "60 دقيقة",
                                    "equipment": "طابع، منقاش، صواني خبز",
                                    "success_criteria": "بقاء اللون أبيض طرياً ومنقوشاً بوضوح",
                                    "common_errors": "الإكثار من الطهي مما يفقده طراوته",
                                    "hygiene_rules": "نظافة الأسطح واستخدام أدوات معقمة",
                                    "notes": "يقدم في المناسبات والأفراح."
                                }
                            ],
                            "recipes": [
                                {
                                    "id": "rec_makrood",
                                    "name": "وصفة مقروط اللوز الأصيل",
                                    "ingredients": "لوز، سكر، ماء زهر، قشور الليمون",
                                    "quantities": "حسب البطاقة التقنية",
                                    "steps": "تشكيل حربوش، تقطيع مقروضات، الطهي والتغليس.",
                                    "prep_time": "50 دقيقة",
                                    "bake_time": "15 دقيقة",
                                    "temperature": "160°C",
                                    "servings": "30 حبة",
                                    "notes": "يغمس في ماء زهر وماء ورد ثم يغبر بسكر رطب فائق الجودة."
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "unit_m_west",
                    "name": "حلويات غربية",
                    "lessons": [
                        {
                            "id": "les_m_west",
                            "name": "فن صناعة الحلويات الغربية والباتيسري",
                            "content": "تحضير الكيك الفاخر، التارتليت، والتشيز كيك بمعايير عالمية.",
                            "objectives": "التمكن من تقنيات الباتيسري الحديثة.",
                            "competencies": "الدقة في القياسات والتزيين الاحترافي.",
                            "pedagogy": "العرض المرئي والتطبيق الورشاتي الموجه.",
                            "steps": "1. خفق البسكويت. 2. إعداد الكريمة. 3. التجميع.",
                            "evaluation": "تقييم المظهر الخارجي والتذوق.",
                            "technical_sheets": [],
                            "recipes": []
                        }
                    ]
                },
                {
                    "id": "unit_m_east",
                    "name": "حلويات شرقية",
                    "lessons": [
                        {
                            "id": "les_m_east",
                            "name": "صناعة الحلويات الشرقية الفاخرة",
                            "content": "تحضير البقلاوة، الكنافة، والقطايف بأسسها الصحيحة.",
                            "objectives": "إتقان العجائن المورقة والشرقية.",
                            "competencies": "التحكم في درجات حرارة القطر والخبز.",
                            "pedagogy": "التطبيق العملي المتسلسل.",
                            "steps": "1. فرد طبقات العجين. 2. حشو المكسرات. 3. السقي بالقطر الساخن.",
                            "evaluation": "تقييم القرمشة والتشرب المتوازن للقطر.",
                            "technical_sheets": [],
                            "recipes": []
                        }
                    ]
                }
            ]
        }
    ],
    "exams": [
        {
            "id": "exam_default_1",
            "title": "الامتحان الشامل في التقنيات والوصفات",
            "program_id": "prog_makatha",
            "unit_id": "unit_m_trad",
            "lesson_id": "les_m_trad",
            "questions": [
                {
                    "id": "q_1",
                    "text": "ما هي درجة الحرارة المناسبة لخبز مقروط اللوز دون أن يتغير لونه؟",
                    "type": "mcq",
                    "options": ["160°C", "220°C", "100°C"],
                    "answer": 0,
                    "points": 5
                }
            ]
        }
    ],
    "results": [],
    "documents": []
}

def load_data():
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return DEFAULT_DATA
            for key in DEFAULT_DATA:
                if key not in data:
                    data[key] = DEFAULT_DATA[key]
            if "settings" not in data or not isinstance(data["settings"], dict):
                data["settings"] = DEFAULT_DATA["settings"]
            else:
                for skey in DEFAULT_DATA["settings"]:
                    if skey not in data["settings"]:
                        data["settings"][skey] = DEFAULT_DATA["settings"][skey]
            return data
    except Exception:
        return DEFAULT_DATA

def save_data(data):
    temp_file = DATA_FILE + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        if os.path.exists(DATA_FILE):
            os.replace(temp_file, DATA_FILE)
        else:
            os.rename(temp_file, DATA_FILE)
    except Exception as e:
        st.error(f"حدث خطأ أثناء حفظ البيانات: {e}")

if "db" not in st.session_state:
    st.session_state.db = load_data()

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

if "current_view" not in st.session_state:
    st.session_state.current_view = "home"

if "selected_program_id" not in st.session_state:
    st.session_state.selected_program_id = None

if "selected_unit_id" not in st.session_state:
    st.session_state.selected_unit_id = None

if "selected_lesson_id" not in st.session_state:
    st.session_state.selected_lesson_id = None

if "active_exam_id" not in st.session_state:
    st.session_state.active_exam_id = None

db = st.session_state.db

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .card-custom {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .supervisor-badge {
        background: #f1f5f9;
        padding: 8px 15px;
        border-radius: 8px;
        color: #1e293b;
        font-weight: 600;
        margin-bottom: 20px;
        border-right: 4px solid #2563eb;
    }
</style>
""", unsafe_allow_html=True)

col_title, col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([2, 1, 1, 1, 1])
with col_title:
    platform_title = db.get("settings", {}).get("platform_name", "المنصة البيداغوجية للتكوين المهني (APC)")
    st.markdown(f"### 🥐 {platform_title}")
with col_nav1:
    if st.button("🏠 الرئيسية", key="top_nav_home"):
        st.session_state.current_view = "home"
        st.rerun()
with col_nav2:
    if st.button("🔍 البحث الشامل", key="top_nav_search"):
        st.session_state.current_view = "search"
        st.rerun()
with col_nav3:
    if st.button("📝 الامتحانات", key="top_nav_exams"):
        st.session_state.current_view = "exams"
        st.rerun()
with col_nav4:
    if st.session_state.is_admin:
        if st.button("🚪 خروج المدير", key="top_nav_logout"):
            st.session_state.is_admin = False
            st.session_state.current_view = "home"
            st.rerun()
    else:
        if st.button("🔐 دخول الإدارة", key="top_nav_login"):
            st.session_state.current_view = "admin_login"
            st.rerun()

supervisor_text = db.get("settings", {}).get("supervisor_name", "إشراف الأستاذة: فرحي حورية")
st.markdown(f'<div class="supervisor-badge">✨ {supervisor_text}</div>', unsafe_allow_html=True)
st.markdown("---")

if st.session_state.current_view == "admin_login":
    st.subheader("تسجيل دخول المشرف (الإدارة)")
    pwd = st.text_input("كلمة المرور", type="password", key="admin_pwd_input")
    if st.button("دخول", key="admin_login_submit"):
        admin_pass = db.get("settings", {}).get("admin_password", "admin")
        if pwd == admin_pass:
            st.session_state.is_admin = True
            st.session_state.current_view = "admin_dashboard"
            st.success("تم تسجيل الدخول بنجاح!")
            st.rerun()
        else:
            st.error("كلمة المرور غير صحيحة.")

elif st.session_state.current_view == "admin_dashboard":
    if not st.session_state.is_admin:
        st.warning("يرجى تسجيل الدخول أولاً.")
        st.session_state.current_view = "home"
        st.rerun()
    
    st.header("⚙️ لوحة التحكم والإدارة الشاملة للمنصة")
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "البرامج والوحدات", "الدروس", "البطاقات التقنية", "الوصفات", "الامتحانات والأسئلة", "الوثائق والنتائج", "الإعدادات"
    ])
    
    with tab1:
        st.subheader("إدارة البرامج والوحدات")
        with st.form("add_prog_form"):
            p_name = st.text_input("اسم البرنامج الجديد")
            p_desc = st.text_area("وصف البرنامج")
            if st.form_submit_button("إضافة البرنامج") and p_name:
                db["programs"].append({
                    "id": f"prog_{uuid.uuid4().hex[:8]}",
                    "name": p_name,
                    "description": p_desc,
                    "units": []
                })
                save_data(db)
                st.success("تم إضافة البرنامج بنجاح!")
                st.rerun()
        
        st.markdown("---")
        if db["programs"]:
            p_sel = st.selectbox("اختر البرنامج لإدارة وحداته", [p["id"] for p in db["programs"]], format_func=lambda x: next((p["name"] for p in db["programs"] if p["id"] == x), x), key="admin_prog_select")
            prog_obj = next((p for p in db["programs"] if p["id"] == p_sel), None)
            
            if prog_obj:
                with st.form("add_unit_form"):
                    u_name = st.text_input("اسم الوحدة أو التخصص الجديد")
                    if st.form_submit_button("إضافة الوحدة") and u_name:
                        prog_obj["units"].append({
                            "id": f"unit_{uuid.uuid4().hex[:8]}",
                            "name": u_name,
                            "lessons": []
                        })
                        save_data(db)
                        st.success("تم إضافة الوحدة بنجاح!")
                        st.rerun()
                
                st.markdown("### الوحدات الحالية وتعديلها:")
                for idx, u in enumerate(list(prog_obj["units"])):
                    col_u1, col_u2 = st.columns([3, 1])
                    with col_u1:
                        new_u_name = st.text_input(f"تعديل اسم الوحدة {idx+1}", value=u["name"], key=f"edit_u_{u['id']}")
                        if new_u_name != u["name"]:
                            u["name"] = new_u_name
                            save_data(db)
                    with col_u2:
                        if st.button("حذف الوحدة", key=f"del_u_{u['id']}"):
                            prog_obj["units"].remove(u)
                            save_data(db)
                            st.rerun()

    with tab2:
        st.subheader("إدارة الدروس بالتفصيل البيداغوجي")
        if db["programs"]:
            p_choice = st.selectbox("اختر البرنامج للدرس", db["programs"], format_func=lambda x: x["name"], key="l_p_admin")
            if p_choice.get("units"):
                u_choice = st.selectbox("اختر الوحدة أو النظير", p_choice["units"], format_func=lambda x: x["name"], key="l_u_admin")
                
                with st.form("add_lesson_full"):
                    l_name = st.text_input("عنوان الدرس")
                    l_content = st.text_area("المحتوى المفصل للدرس")
                    l_obj = st.text_area("أهداف الدرس")
                    l_comp = st.text_area("الكفاءات المستهدفة")
                    l_ped = st.text_area("المقاربة البيداغوجية")
                    l_steps = st.text_area("خطوات الإنجاز")
                    l_eval = st.text_area("طريقة التقييم")
                    
                    if st.form_submit_button("حفظ وإضافة الدرس") and l_name:
                        u_choice["lessons"].append({
                            "id": f"lesson_{uuid.uuid4().hex[:8]}",
                            "name": l_name,
                            "content": l_content,
                            "objectives": l_obj,
                            "competencies": l_comp,
                            "pedagogy": l_ped,
                            "steps": l_steps,
                            "evaluation": l_eval,
                            "technical_sheets": [],
                            "recipes": []
                        })
                        save_data(db)
                        st.success("تم إضافة الدرس بنجاح!")
                        st.rerun()
            else:
                st.info("الرجاء إضافة وحدة لهذا البرنامج أولاً.")
        else:
            st.info("الرجاء إضافة برنامج أولاً.")

    with tab3:
        st.subheader("إدارة البطاقات التقنية الكاملة")
        all_lessons = []
        for p in db["programs"]:
            for u in p.get("units", []):
                for l in u.get("lessons", []):
                    all_lessons.append((f"{p['name']} > {u['name']} > {l['name']}", p, u, l))
        
        if all_lessons:
            les_sel = st.selectbox("اختر الدرس المرتبط بالبطاقة التقنية", all_lessons, format_func=lambda x: x[0], key="ts_les_select")
            p_obj, u_obj, l_obj = les_sel[1], les_sel[2], les_sel[3]
            
            with st.form("add_tech_sheet_form"):
                ts_title = st.text_input("اسم البطاقة التقنية")
                ts_cat = st.text_input("الصنف (مثال: حلويات تقليدية، غربية، شرقية)")
                ts_ing = st.text_area("المكونات")
                ts_qty = st.text_area("الكميات والوحدات")
                ts_steps = st.text_area("خطوات التحضير")
                ts_temp = st.text_input("درجة الحرارة (مثال: 160°C)")
                ts_bake = st.text_input("وقت الطهي")
                ts_prep = st.text_input("وقت التحضير")
                ts_eq = st.text_area("المعدات المطلوبة")
                ts_succ = st.text_area("معايير النجاح")
                ts_err = st.text_area("الأخطاء الشائعة")
                ts_hyg = st.text_area("قواعد النظافة والسلامة")
                ts_notes = st.text_area("ملاحظات إضافية")
                
                if st.form_submit_button("حفظ البطاقة التقنية") and ts_title:
                    if "technical_sheets" not in l_obj:
                        l_obj["technical_sheets"] = []
                    l_obj["technical_sheets"].append({
                        "id": f"ts_{uuid.uuid4().hex[:8]}",
                        "title": ts_title,
                        "category": ts_cat,
                        "ingredients_list": ts_ing,
                        "quantities": ts_qty,
                        "steps": ts_steps,
                        "temperature": ts_temp,
                        "bake_time": ts_bake,
                        "prep_time": ts_prep,
                        "equipment": ts_eq,
                        "success_criteria": ts_succ,
                        "common_errors": ts_err,
                        "hygiene_rules": ts_hyg,
                        "notes": ts_notes
                    })
                    save_data(db)
                    st.success("تم إضافة البطاقة التقنية بنجاح!")
                    st.rerun()
        else:
            st.info("يجب إضافة درس واحد على الأقل أولاً.")

    with tab4:
        st.subheader("إدارة الوصفات الفنية الكاملة")
        if all_lessons:
            les_sel_r = st.selectbox("اختر الدرس المرتبط بالوصفة", all_lessons, format_func=lambda x: x[0], key="rec_les_select")
            p_o, u_o, l_o = les_sel_r[1], les_sel_r[2], les_sel_r[3]
            
            with st.form("add_recipe_form"):
                rec_name = st.text_input("اسم الوصفة")
                rec_ing = st.text_area("المكونات الأساسية")
                rec_qty = st.text_area("الكميات الدقيقة")
                rec_steps = st.text_area("طريقة التحضير")
                rec_prep = st.text_input("مدة التحضير")
                rec_bake = st.text_input("مدة الطهي")
                rec_temp = st.text_input("درجة الحرارة")
                rec_serv = st.text_input("عدد الحصص")
                rec_notes = st.text_area("نصائح وملاحظات")
                
                if st.form_submit_button("حفظ الوصفة") and rec_name:
                    if "recipes" not in l_o:
                        l_o["recipes"] = []
                    l_o["recipes"].append({
                        "id": f"rec_{uuid.uuid4().hex[:8]}",
                        "name": rec_name,
                        "ingredients": rec_ing,
                        "quantities": rec_qty,
                        "steps": rec_steps,
                        "prep_time": rec_prep,
                        "bake_time": rec_bake,
                        "temperature": rec_temp,
                        "servings": rec_serv,
                        "notes": rec_notes
                    })
                    save_data(db)
                    st.success("تم إضافة الوصفة بنجاح!")
                    st.rerun()
        else:
            st.info("يجب إضافة درس واحد على الأقل أولاً.")

    with tab5:
        st.subheader("إدارة الامتحانات والأسئلة الشاملة")
        with st.form("create_exam_admin"):
            ex_title = st.text_input("عنوان الامتحان")
            if all_lessons:
                ex_les = st.selectbox("ربط الامتحان بالدرس", all_lessons, format_func=lambda x: x[0], key="ex_les_select")
                if st.form_submit_button("إنشاء الامتحان") and ex_title:
                    db["exams"].append({
                        "id": f"exam_{uuid.uuid4().hex[:8]}",
                        "title": ex_title,
                        "program_id": ex_les[1]["id"],
                        "unit_id": ex_les[2]["id"],
                        "lesson_id": ex_les[3]["id"],
                        "questions": []
                    })
                    save_data(db)
                    st.success("تم إنشاء الامتحان بنجاح!")
                    st.rerun()
            else:
                st.warning("أضف دروساً أولاً.")

        st.markdown("---")
        if db["exams"]:
            sel_ex_q = st.selectbox("اختر الامتحان لإضافة الأسئلة إليه", db["exams"], format_func=lambda x: x["title"], key="ex_q_select")
            with st.form("add_q_form"):
                q_txt = st.text_input("نص السؤال")
                q_type = st.selectbox("نوع السؤال", ["mcq", "true_false"], format_func=lambda x: "اختيار من متعدد" if x=="mcq" else "صح / خطأ")
                if q_type == "mcq":
                    opt1 = st.text_input("الخيار 1", "الخيار أ")
                    opt2 = st.text_input("الخيار 2", "الخيار ب")
                    opt3 = st.text_input("الخيار 3", "الخيار ج")
                    options = [opt1, opt2, opt3]
                    corr = st.number_input("رقم الإجابة الصحيحة (0، 1، 2)", min_value=0, max_value=2, value=0)
                else:
                    options = ["خطأ", "صحيح"]
                    corr = st.selectbox("الإجابة الصحيحة", [0, 1], format_func=lambda x: options[x], key="tf_corr_select")
                
                pts = st.number_input("النقاط", min_value=1, value=5)
                if st.form_submit_button("إضافة السؤال") and q_txt:
                    if "questions" not in sel_ex_q:
                        sel_ex_q["questions"] = []
                    sel_ex_q["questions"].append({
                        "id": f"q_{uuid.uuid4().hex[:8]}",
                        "text": q_txt,
                        "type": q_type,
                        "options": options,
                        "answer": int(corr),
                        "points": int(pts)
                    })
                    save_data(db)
                    st.success("تم إضافة السؤال بنجاح!")
                    st.rerun()

    with tab6:
        st.subheader("إدارة الوثائق والملفات ونتائج المتربصين")
        uploaded_file = st.file_uploader("رفع ملف جديد", type=["pdf", "docx", "xlsx", "pptx", "png", "jpg", "jpeg"])
        if uploaded_file is not None:
            file_ext = os.path.splitext(uploaded_file.name)[1]
            safe_filename = f"{uuid.uuid4().hex[:8]}{file_ext}"
            file_path = os.path.join(UPLOADS_DIR, safe_filename)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            if "documents" not in db:
                db["documents"] = []
            db["documents"].append({
                "id": f"doc_{uuid.uuid4().hex[:8]}",
                "title": uploaded_file.name,
                "name": safe_filename,
                "path": file_path,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            save_data(db)
            st.success("تم رفع الملف بنجاح!")
            st.rerun()
        
        st.markdown("### الملفات المرفوعة:")
        for doc in list(db.get("documents", [])):
            col_d1, col_d2 = st.columns([3, 1])
            with col_d1:
                st.write(f"📄 {doc.get('title', 'ملف بدون عنوان')}")
            with col_d2:
                if st.button("حذف الملف", key=f"del_doc_{doc['id']}"):
                    path_to_rm = doc.get("path")
                    if path_to_rm and os.path.exists(path_to_rm):
                        try:
                            os.remove(path_to_rm)
                        except Exception:
                            pass
                    db["documents"].remove(doc)
                    save_data(db)
                    st.rerun()
        
        st.markdown("---")
        st.subheader("📊 نتائج الامتحانات المسجلة للمتربصين:")
        if db.get("results"):
            for res in db["results"]:
                st.markdown(f"""
                <div class="card-custom">
                    <b>المتربص:</b> {res.get('student_name', '')} | <b>الامتحان:</b> {res.get('exam_title', '')} | <b>التاريخ:</b> {res.get('date', '')}<br>
                    <b>النقطة:</b> {res.get('score', 0)} / {res.get('total', 0)} ({res.get('percentage', 0)}%) - <b>الحالة:</b> {res.get('status', '')}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("لا توجد نتائج مسجلة حتى الآن.")

    with tab7:
        st.subheader("إعدادات المنصة")
        p_name_new = st.text_input("اسم المنصة", value=db.get("settings", {}).get("platform_name", ""))
        sup_name_new = st.text_input("نص الإشراف", value=db.get("settings", {}).get("supervisor_name", ""))
        pwd_new = st.text_input("كلمة مرور الإدارة الجديدة", type="password", key="settings_new_pwd")
        if st.button("حفظ التغييرات", key="save_settings_btn"):
            if "settings" not in db:
                db["settings"] = {}
            db["settings"]["platform_name"] = p_name_new
            db["settings"]["supervisor_name"] = sup_name_new
            if pwd_new:
                db["settings"]["admin_password"] = pwd_new
            save_data(db)
            st.success("تم حفظ الإعدادات بنجاح!")
            st.rerun()

elif st.session_state.current_view == "search":
    st.header("🔍 البحث الشامل في محتوى المنصة")
    query = st.text_input("أدخل كلمة البحث", key="global_search_input").strip().lower()
    
    if query:
        found = False
        for p in db.get("programs", []):
            if query in p.get("name", "").lower() or query in p.get("description", "").lower():
                found = True
                st.info(f"📁 برنامج: {p.get('name', '')}")
                if st.button("انتقل للبرنامج", key=f"s_p_{p['id']}"):
                    st.session_state.selected_program_id = p["id"]
                    st.session_state.current_view = "program_view"
                    st.rerun()
            
            for u in p.get("units", []):
                if query in u.get("name", "").lower():
                    found = True
                    st.success(f"📂 وحدة/تخصص: {u.get('name', '')} (تابعة لـ {p.get('name', '')})")
                    if st.button(f"عرض تفاصيل {u.get('name', '')}", key=f"s_u_{u['id']}"):
                        st.session_state.selected_program_id = p["id"]
                        st.session_state.selected_unit_id = u["id"]
                        st.session_state.current_view = "unit_view"
                        st.rerun()
                
                for l in u.get("lessons", []):
                    if query in l.get("name", "").lower() or query in l.get("content", "").lower():
                        found = True
                        st.warning(f"📖 درس: {l.get('name', '')}")
                        if st.button("فتح الدرس مباشرة", key=f"s_l_{l['id']}"):
                            st.session_state.selected_program_id = p["id"]
                            st.session_state.selected_unit_id = u["id"]
                            st.session_state.selected_lesson_id = l["id"]
                            st.session_state.current_view = "lesson_view"
                            st.rerun()

        if not found:
            st.warning("لم يتم العثور على نتائج تطابق بحثك.")

elif st.session_state.current_view == "exams":
    st.header("📝 الامتحانات المتاحة للمتربصين")
    if not db.get("exams"):
        st.info("لا توجد امتحانات متاحة حالياً.")
    else:
        for ex in db["exams"]:
            q_count = len(ex.get("questions", []))
            st.markdown(f"""
            <div class="card-custom">
                <h4>{ex.get('title', 'امتحان بدون عنوان')}</h4>
                <p>عدد الأسئلة: {q_count}</p>
            </div>
            """, unsafe_allow_html=True)
            if q_count > 0:
                if st.button(f"ابدأ الامتحان: {ex.get('title', '')}", key=f"start_ex_{ex['id']}"):
                    st.session_state.active_exam_id = ex["id"]
                    st.session_state.current_view = "exam_session"
                    st.rerun()

elif st.session_state.current_view == "exam_session":
    ex_obj = next((e for e in db.get("exams", []) if e["id"] == st.session_state.active_exam_id), None)
    if not ex_obj or not ex_obj.get("questions"):
        st.error("الامتحان غير موجود.")
        st.session_state.current_view = "exams"
        st.rerun()
    
    st.header(f"📝 امتحان: {ex_obj.get('title', '')}")
    student_name = st.text_input("اسم المتربص الثلاثي:", key="exam_student_name_input")
    
    with st.form("exam_form_sub"):
        answers = {}
        for idx, q in enumerate(ex_obj.get("questions", [])):
            st.markdown(f"**السؤال {idx+1}: {q.get('text', '')}** (النقاط: {q.get('points', 5)})")
            options = q.get("options", ["خطأ", "صحيح"])
            ans = st.radio("اختر الإجابة:", list(range(len(options))), format_func=lambda x: options[x], key=f"ans_{q.get('id', idx)}")
            answers[q.get('id', idx)] = ans
            st.markdown("---")
            
        if st.form_submit_button("إرسال الإجابات والحصول على النتيجة"):
            if not student_name.strip():
                st.error("يرجى إدخال اسم المتربص أولاً.")
            else:
                score = 0
                questions_list = ex_obj.get("questions", [])
                total = sum(q.get("points", 5) for q in questions_list)
                for q in questions_list:
                    if answers.get(q.get("id")) == q.get("answer"):
                        score += q.get("points", 5)
                
                percentage = round((score / total) * 100, 2) if total > 0 else 0
                status = "ناجح ✨" if percentage >= 50 else "راسب (يحتاج لإعادة المحاولة)"
                
                if "results" not in db:
                    db["results"] = []
                db["results"].append({
                    "id": f"res_{uuid.uuid4().hex[:8]}",
                    "student_name": student_name,
                    "exam_title": ex_obj.get("title", ""),
                    "score": score,
                    "total": total,
                    "percentage": percentage,
                    "status": status,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                save_data(db)
                
                st.success(f"🎉 النتيجة النهائية للمتربص {student_name}: {score} / {total} ({percentage}%) - {status}")

elif st.session_state.current_view == "home":
    st.header("🌟 برامج التكوين المهني في فنون الطهي وصناعة الحلويات")
    st.markdown("اختر البرنامج الأساسي المناسب للتصفح الهرمي:")
    
    if not db.get("programs"):
        st.info("لا توجد برامج متاحة حالياً.")
    else:
        for p in db["programs"]:
            st.markdown(f"""
            <div class="card-custom">
                <h3>📁 {p.get('name', '')}</h3>
                <p>{p.get('description', '')}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"استعراض أقسام وتخصصات: {p.get('name', '')}", key=f"p_btn_{p['id']}"):
                st.session_state.selected_program_id = p["id"]
                st.session_state.current_view = "program_view"
                st.rerun()

elif st.session_state.current_view == "program_view":
    prog = next((p for p in db.get("programs", []) if p["id"] == st.session_state.selected_program_id), None)
    if prog:
        st.header(f"📁 البرنامج: {prog.get('name', '')}")
        if st.button("← العودة للبرامج الرئيسية", key="back_home_btn"):
            st.session_state.current_view = "home"
            st.rerun()
            
        st.markdown("---")
        st.markdown("### الفروع والنوافذ المتاحة ضمن هذا البرنامج:")
        if not prog.get("units"):
            st.info("لا توجد وحدات أو فروع مضافة في هذا البرنامج.")
        else:
            for u in prog["units"]:
                st.markdown(f"""
                <div class="card-custom">
                    <h4>📂 {u.get('name', '')}</h4>
                </div>
                """, unsafe_allow_html=True)
                col_u1, col_u2 = st.columns([3, 1])
                with col_u2:
                    if st.button(f"فتح النافذة", key=f"open_u_{u['id']}"):
                        st.session_state.selected_unit_id = u["id"]
                        st.session_state.current_view = "unit_view"
                        st.rerun()

elif st.session_state.current_view == "unit_view":
    prog = next((p for p in db.get("programs", []) if p["id"] == st.session_state.selected_program_id), None)
    unit = next((u for u in prog.get("units", []) if u["id"] == st.session_state.selected_unit_id), None) if prog else None
    
    if unit:
        st.header(f"📂 النافذة / الفرع: {unit.get('name', '')}")
        if st.button("← العودة للبرنامج السابق", key="back_prog_from_unit"):
            st.session_state.current_view = "program_view"
            st.rerun()
            
        st.markdown("---")
        st.markdown("### الدروس والمحتويات البيداغوجية المتوفرة:")
        if not unit.get("lessons"):
            st.info("لا توجد دروس مضافة في هذه النافذة حالياً.")
        else:
            for l in unit["lessons"]:
                col_l1, col_l2 = st.columns([3, 1])
                with col_l1:
                    st.write(f"📖 درس: **{l.get('name', '')}**")
                with col_l2:
                    if st.button("فتح الدرس والبطاقات", key=f"open_l_{l['id']}"):
                        st.session_state.selected_lesson_id = l["id"]
                        st.session_state.current_view = "lesson_view"
                        st.rerun()

elif st.session_state.current_view == "lesson_view":
    prog = next((p for p in db.get("programs", []) if p["id"] == st.session_state.selected_program_id), None)
    unit = next((u for u in prog.get("units", []) if u["id"] == st.session_state.selected_unit_id), None) if prog else None
    lesson = next((l for l in unit.get("lessons", []) if l["id"] == st.session_state.selected_lesson_id), None) if unit else None
    
    if lesson:
        st.header(f"📖 الدرس: {lesson.get('name', '')}")
        if st.button("← العودة للنافذة السابقة", key="back_unit_btn"):
            st.session_state.current_view = "unit_view"
            st.rerun()
            
        st.markdown(f"""
        <div class="card-custom">
            <h4>🎯 الأهداف البيداغوجية</h4>
            <p>{lesson.get('objectives', 'غير محدد')}</p>
            <h4>🧠 الكفاءات المستهدفة</h4>
            <p>{lesson.get('competencies', 'غير محدد')}</p>
            <h4>📐 المقاربة البيداغوجية</h4>
            <p>{lesson.get('pedagogy', 'غير محدد')}</p>
            <h4>📝 محتوى الشرح المفصل</h4>
            <p>{lesson.get('content', 'غير محدد')}</p>
            <h4>⚡ خطوات الإنجاز</h4>
            <p>{lesson.get('steps', 'غير محدد')}</p>
            <h4>📋 طريقة التقييم</h4>
            <p>{lesson.get('evaluation', 'غير محدد')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("📋 البطاقات التقنية المرتبطة بالدرس")
        if lesson.get("technical_sheets"):
            for ts in lesson["technical_sheets"]:
                st.markdown(f"""
                <div class="card-custom">
                    <h4>{ts.get('title', '')} ({ts.get('category', '')})</h4>
                    <p><b>المكونات:</b> {ts.get('ingredients_list', '')}</p>
                    <p><b>الكميات:</b> {ts.get('quantities', '')}</p>
                    <p><b>خطوات التحضير:</b> {ts.get('steps', '')}</p>
                    <p><b>درجة الحرارة:</b> {ts.get('temperature', '')} | <b>وقت الطهي:</b> {ts.get('bake_time', '')} | <b>وقت التحضير:</b> {ts.get('prep_time', '')}</p>
                    <p><b>المعدات:</b> {ts.get('equipment', '')}</p>
                    <p><b>معايير النجاح:</b> {ts.get('success_criteria', '')}</p>
                    <p><b>الأخطاء الشائعة:</b> {ts.get('common_errors', '')}</p>
                    <p><b>قواعد النظافة والسلامة:</b> {ts.get('hygiene_rules', '')}</p>
                    <p><b>ملاحظات:</b> {ts.get('notes', '')}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("لا توجد بطاقات تقنية مرتبطة بهذا الدرس.")
            
        st.subheader("🧁 الوصفات الفنية المرتبطة بالدرس")
        if lesson.get("recipes"):
            for rec in lesson["recipes"]:
                st.markdown(f"""
                <div class="card-custom">
                    <h4>{rec.get('name', '')}</h4>
                    <p><b>المكونات:</b> {rec.get('ingredients', '')}</p>
                    <p><b>الكميات:</b> {rec.get('quantities', '')}</p>
                    <p><b>طريقة التحضير:</b> {rec.get('steps', '')}</p>
                    <p><b>مدة التحضير:</b> {rec.get('prep_time', '')} | <b>مدة الطهي:</b> {rec.get('bake_time', '')} | <b>الحرارة:</b> {rec.get('temperature', '')} | <b>الحصص:</b> {rec.get('servings', '')}</p>
                    <p><b>نصائح وملاحظات:</b> {rec.get('notes', '')}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("لا توجد وصفات مرتبطة بهذا الدرس.")
