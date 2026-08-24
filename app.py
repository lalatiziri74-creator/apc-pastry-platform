import streamlit as st
import json
import os
import uuid
from datetime import datetime

# =========================================================
# 1. إعداد المنصة
# =========================================================

st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني - فرحي حورية",
    page_icon="🥐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

DATA_FILE = "platform_data.json"
UPLOADS_DIR = "uploaded_files"

os.makedirs(UPLOADS_DIR, exist_ok=True)


# =========================================================
# 2. البيانات الافتراضية
# =========================================================

def uid(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def default_lesson(name, description=""):
    return {
        "id": uid("lesson"),
        "name": name,
        "content": description,
        "objectives": "",
        "competencies": "",
        "pedagogy": "",
        "steps": "",
        "evaluation": "",
        "technical_sheets": [],
        "recipes": []
    }


def default_unit(name, lessons=None):
    return {
        "id": uid("unit"),
        "name": name,
        "description": "",
        "lessons": lessons or []
    }


def default_window(name, description="", units=None):
    return {
        "id": uid("window"),
        "name": name,
        "description": description,
        "units": units or []
    }


def default_program(program_id, name, description, windows):
    return {
        "id": program_id,
        "name": name,
        "description": description,
        "windows": windows
    }


DEFAULT_DATA = {

    "settings": {
        "platform_name": "المنصة البيداغوجية للتكوين المهني (APC)",
        "supervisor_name": "إشراف الأستاذة: فرحي حورية",
        "admin_password": "admin"
    },

    "programs": [

        # =================================================
        # البرنامج الأول: التمهين
        # =================================================

        default_program(
            "apprenticeship",
            "📖 برنامج التكوين بالتمهين",
            "التكوين عن طريق التمهين داخل المؤسسات والورشات المهنية.",
            [

                default_window(
                    "🏢 التكوين النظري",
                    "المعارف النظرية والمهنية الأساسية.",
                    [
                        default_unit(
                            "المعارف المهنية الأساسية",
                            [
                                default_lesson(
                                    "التعريف بالمهنة ومحيط العمل"
                                ),
                                default_lesson(
                                    "الأمن والسلامة المهنية"
                                ),
                                default_lesson(
                                    "النظافة المهنية"
                                )
                            ]
                        )
                    ]
                ),

                default_window(
                    "👩‍🍳 التكوين التطبيقي",
                    "التطبيق العملي للمهارات المهنية.",
                    [
                        default_unit(
                            "تقنيات صناعة الحلويات",
                            [
                                default_lesson(
                                    "تحضير العجائن الأساسية"
                                ),
                                default_lesson(
                                    "تحضير الكريمات"
                                ),
                                default_lesson(
                                    "تقنيات التزيين"
                                )
                            ]
                        )
                    ]
                ),

                default_window(
                    "🏭 التكوين داخل المؤسسة المستقبلة",
                    "تطبيق الكفاءات داخل المحيط المهني الحقيقي.",
                    [
                        default_unit(
                            "الممارسة المهنية",
                            [
                                default_lesson(
                                    "تنظيم العمل داخل الورشة"
                                ),
                                default_lesson(
                                    "استعمال التجهيزات المهنية"
                                ),
                                default_lesson(
                                    "احترام قواعد الجودة"
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # =================================================
        # البرنامج الثاني: الحضوري
        # =================================================

        default_program(
            "presential",
            "🏫 برنامج التكوين الحضوري",
            "برنامج التكوين الحضوري داخل مؤسسة التكوين المهني.",
            [

                default_window(
                    "📚 الجانب النظري",
                    "المعارف والمفاهيم النظرية.",
                    [
                        default_unit(
                            "المواد الأولية",
                            [
                                default_lesson(
                                    "الدقيق والسكريات والمواد الدسمة"
                                ),
                                default_lesson(
                                    "البيض والمواد المضافة"
                                )
                            ]
                        )
                    ]
                ),

                default_window(
                    "👩‍🍳 الجانب التطبيقي",
                    "تطبيق التقنيات المهنية داخل الورشة.",
                    [
                        default_unit(
                            "العجائن",
                            [
                                default_lesson(
                                    "العجائن الأساسية"
                                ),
                                default_lesson(
                                    "العجائن المورقة"
                                ),
                                default_lesson(
                                    "عجينة الشو"
                                )
                            ]
                        ),
                        default_unit(
                            "الكريمات والحشوات",
                            [
                                default_lesson(
                                    "الكريمة الأساسية"
                                ),
                                default_lesson(
                                    "الغاناش"
                                ),
                                default_lesson(
                                    "الموس"
                                )
                            ]
                        )
                    ]
                ),

                default_window(
                    "📝 التقييم والامتحانات",
                    "التقييم المستمر والاختبارات المهنية.",
                    [
                        default_unit(
                            "التقييم",
                            [
                                default_lesson(
                                    "التقييم النظري"
                                ),
                                default_lesson(
                                    "التقييم التطبيقي"
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # =================================================
        # البرنامج الثالث: المرأة الماكثة بالبيت
        # =================================================

        default_program(
            "home_women",
            "👩‍🍳 برنامج المرأة الماكثة بالبيت",
            "برنامج تأهيلي مهني في فنون الطبخ وصناعة الحلويات.",
            [

                default_window(
                    "🍰 الحلويات التقليدية الجزائرية",
                    "التعرف على تقنيات الحلويات الجزائرية الأصيلة.",
                    [
                        default_unit(
                            "حلويات تقليدية",
                            [
                                default_lesson(
                                    "المقروط"
                                ),
                                default_lesson(
                                    "كعب الغزال"
                                ),
                                default_lesson(
                                    "البقلاوة الجزائرية"
                                ),
                                default_lesson(
                                    "قلب اللوز"
                                )
                            ]
                        )
                    ]
                ),

                default_window(
                    "🧁 الحلويات الغربية",
                    "تقنيات الباتيسري الحديثة.",
                    [
                        default_unit(
                            "الحلويات الغربية",
                            [
                                default_lesson(
                                    "الكيك"
                                ),
                                default_lesson(
                                    "التارت"
                                ),
                                default_lesson(
                                    "التشيز كيك"
                                )
                            ]
                        )
                    ]
                ),

                default_window(
                    "🍫 الحلويات الشرقية والشوكولاتة",
                    "تقنيات الحلويات الشرقية والشوكولاتة.",
                    [
                        default_unit(
                            "الحلويات الشرقية",
                            [
                                default_lesson(
                                    "الكنافة"
                                ),
                                default_lesson(
                                    "القطايف"
                                )
                            ]
                        ),
                        default_unit(
                            "الشوكولاتة",
                            [
                                default_lesson(
                                    "أساسيات الشوكولاتة"
                                ),
                                default_lesson(
                                    "تقنيات التزيين بالشوكولاتة"
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ],

    "exams": [],
    "results": [],
    "documents": []
}


# =========================================================
# 3. الحفظ والتحميل
# =========================================================

def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )
        return True
    except Exception as e:
        st.error(f"حدث خطأ أثناء الحفظ: {e}")
        return False


def load_data():

    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        # توافق مع البيانات القديمة
        if "settings" not in data:
            data["settings"] = DEFAULT_DATA["settings"]

        if "programs" not in data:
            data["programs"] = DEFAULT_DATA["programs"]

        if "exams" not in data:
            data["exams"] = []

        if "results" not in data:
            data["results"] = []

        if "documents" not in data:
            data["documents"] = []

        return data

    except Exception:
        st.warning("تعذر قراءة ملف البيانات، سيتم إنشاء بيانات جديدة.")
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA


if "db" not in st.session_state:
    st.session_state.db = load_data()

db = st.session_state.db


# =========================================================
# 4. حالة التطبيق
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "admin" not in st.session_state:
    st.session_state.admin = False

if "program_id" not in st.session_state:
    st.session_state.program_id = None

if "window_id" not in st.session_state:
    st.session_state.window_id = None

if "unit_id" not in st.session_state:
    st.session_state.unit_id = None

if "lesson_id" not in st.session_state:
    st.session_state.lesson_id = None

if "exam_id" not in st.session_state:
    st.session_state.exam_id = None


# =========================================================
# 5. التصميم
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
}

.main-title {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 5px;
}

.supervisor {
    text-align: center;
    padding: 10px;
    border-radius: 10px;
    background: #f1f5f9;
    margin-bottom: 20px;
    font-weight: bold;
}

.card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    margin-bottom: 15px;
    background: white;
}

.window-card {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #cbd5e1;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 6. الرأس
# =========================================================

settings = db["settings"]

st.markdown(
    f"<div class='main-title'>🥐 {settings['platform_name']}</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"<div class='supervisor'>✨ {settings['supervisor_name']}</div>",
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("🏠 الرئيسية", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

with nav2:
    if st.button("🔍 البحث", use_container_width=True):
        st.session_state.page = "search"
        st.rerun()

with nav3:
    if st.button("📝 الامتحانات", use_container_width=True):
        st.session_state.page = "exams"
        st.rerun()

with nav4:
    if st.button("📊 النتائج", use_container_width=True):
        st.session_state.page = "results"
        st.rerun()

with nav5:
    if st.session_state.admin:
        if st.button("⚙️ الإدارة", use_container_width=True):
            st.session_state.page = "admin"
            st.rerun()
    else:
        if st.button("🔐 دخول الإدارة", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

st.divider()


# =========================================================
# 7. الرئيسية
# =========================================================

if st.session_state.page == "home":

    st.header("🌟 برامج التكوين المهني")

    st.write(
        "اختاري البرنامج المناسب للوصول إلى النوافذ والوحدات والدروس والبطاقات التقنية والوصفات."
    )

    for program in db["programs"]:

        st.markdown(
            f"""
            <div class="card">
                <h3>{program['name']}</h3>
                <p>{program['description']}</p>
                <b>عدد النوافذ: {len(program.get('windows', []))}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"فتح البرنامج ← {program['name']}",
            key=f"program_{program['id']}",
            use_container_width=True
        ):

            st.session_state.program_id = program["id"]
            st.session_state.page = "program"
            st.rerun()


# =========================================================
# 8. البرنامج
# =========================================================

elif st.session_state.page == "program":

    program = next(
        (
            p for p in db["programs"]
            if p["id"] == st.session_state.program_id
        ),
        None
    )

    if not program:
        st.error("البرنامج غير موجود.")
        st.stop()

    st.header(program["name"])
    st.write(program["description"])

    if st.button("← العودة إلى البرامج"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    st.subheader("🪟 النوافذ الرئيسية للبرنامج")

    windows = program.get("windows", [])

    if not windows:
        st.info("لا توجد نوافذ لهذا البرنامج.")
    else:

        for window in windows:

            st.markdown(
                f"""
                <div class="window-card">
                    <h3>{window['name']}</h3>
                    <p>{window.get('description', '')}</p>
                    <b>عدد الوحدات: {len(window.get('units', []))}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"فتح النافذة: {window['name']}",
                key=f"window_{window['id']}",
                use_container_width=True
            ):

                st.session_state.window_id = window["id"]
                st.session_state.page = "window"
                st.rerun()


# =========================================================
# 9. النافذة
# =========================================================

elif st.session_state.page == "window":

    program = next(
        (
            p for p in db["programs"]
            if p["id"] == st.session_state.program_id
        ),
        None
    )

    window = None

    if program:
        window = next(
            (
                w for w in program.get("windows", [])
                if w["id"] == st.session_state.window_id
            ),
            None
        )

    if not window:
        st.error("النافذة غير موجودة.")
        st.stop()

    st.header(window["name"])
    st.write(window.get("description", ""))

    if st.button("← العودة إلى البرنامج"):
        st.session_state.page = "program"
        st.rerun()

    st.divider()

    st.subheader("📚 الوحدات")

    for unit in window.get("units", []):

        st.markdown(
            f"""
            <div class="card">
                <h3>📂 {unit['name']}</h3>
                <p>{unit.get('description', '')}</p>
                <b>عدد الدروس: {len(unit.get('lessons', []))}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"فتح الوحدة: {unit['name']}",
            key=f"unit_{unit['id']}",
            use_container_width=True
        ):

            st.session_state.unit_id = unit["id"]
            st.session_state.page = "unit"
            st.rerun()


# =========================================================
# 10. الوحدة
# =========================================================

elif st.session_state.page == "unit":

    program = next(
        (
            p for p in db["programs"]
            if p["id"] == st.session_state.program_id
        ),
        None
    )

    window = None
    unit = None

    if program:

        window = next(
            (
                w for w in program.get("windows", [])
                if w["id"] == st.session_state.window_id
            ),
            None
        )

    if window:

        unit = next(
            (
                u for u in window.get("units", [])
                if u["id"] == st.session_state.unit_id
            ),
            None
        )

    if not unit:
        st.error("الوحدة غير موجودة.")
        st.stop()

    st.header(f"📂 {unit['name']}")

    if st.button("← العودة إلى النافذة"):
        st.session_state.page = "window"
        st.rerun()

    st.divider()

    st.subheader("📖 الدروس")

    for lesson in unit.get("lessons", []):

        st.markdown(
            f"""
            <div class="card">
                <h3>📖 {lesson['name']}</h3>
                <p>{lesson.get('content', '')}</p>
                <b>البطاقات التقنية: {len(lesson.get('technical_sheets', []))}</b>
                <br>
                <b>الوصفات: {len(lesson.get('recipes', []))}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"فتح الدرس: {lesson['name']}",
            key=f"lesson_{lesson['id']}",
            use_container_width=True
        ):

            st.session_state.lesson_id = lesson["id"]
            st.session_state.page = "lesson"
            st.rerun()


# =========================================================
# 11. الدرس
# =========================================================

elif st.session_state.page == "lesson":

    lesson = None

    for program in db["programs"]:

        for window in program.get("windows", []):

            for unit in window.get("units", []):

                for l in unit.get("lessons", []):

                    if l["id"] == st.session_state.lesson_id:
                        lesson = l

    if not lesson:
        st.error("الدرس غير موجود.")
        st.stop()

    st.header(f"📖 {lesson['name']}")

    if st.button("← العودة"):
        st.session_state.page = "unit"
        st.rerun()

    st.divider()

    st.subheader("🎯 الأهداف البيداغوجية")
    st.write(lesson.get("objectives") or "لم تتم إضافة الأهداف بعد.")

    st.subheader("🧠 الكفاءات المستهدفة")
    st.write(lesson.get("competencies") or "لم تتم إضافة الكفاءات بعد.")

    st.subheader("📐 المقاربة البيداغوجية")
    st.write(lesson.get("pedagogy") or "لم تتم إضافة المقاربة البيداغوجية بعد.")

    st.subheader("📚 المحتوى")
    st.write(lesson.get("content") or "لم تتم إضافة محتوى الدرس بعد.")

    st.subheader("⚙️ خطوات الإنجاز")
    st.write(lesson.get("steps") or "لم تتم إضافة خطوات الإنجاز بعد.")

    st.subheader("📋 التقييم")
    st.write(lesson.get("evaluation") or "لم تتم إضافة طريقة التقييم بعد.")

    st.divider()

    # البطاقات التقنية

    st.subheader("📋 البطاقات التقنية")

    if lesson.get("technical_sheets"):

        for sheet in lesson["technical_sheets"]:

            with st.expander(sheet["title"]):

                st.write("**الصنف:**", sheet.get("category", ""))
                st.write("**المكونات:**", sheet.get("ingredients_list", ""))
                st.write("**الكميات:**", sheet.get("quantities", ""))
                st.write("**خطوات التحضير:**", sheet.get("steps", ""))
                st.write("**درجة الحرارة:**", sheet.get("temperature", ""))
                st.write("**وقت الطهي:**", sheet.get("bake_time", ""))
                st.write("**وقت التحضير:**", sheet.get("prep_time", ""))
                st.write("**المعدات:**", sheet.get("equipment", ""))
                st.write("**معايير النجاح:**", sheet.get("success_criteria", ""))
                st.write("**الأخطاء الشائعة:**", sheet.get("common_errors", ""))
                st.write("**النظافة والسلامة:**", sheet.get("hygiene_rules", ""))
                st.write("**ملاحظات:**", sheet.get("notes", ""))

    else:
        st.info("لا توجد بطاقات تقنية لهذا الدرس حالياً.")

    # الوصفات

    st.subheader("🧁 الوصفات")

    if lesson.get("recipes"):

        for recipe in lesson["recipes"]:

            with st.expander(recipe["name"]):

                st.write("**المكونات:**", recipe.get("ingredients", ""))
                st.write("**الكميات:**", recipe.get("quantities", ""))
                st.write("**طريقة التحضير:**", recipe.get("steps", ""))
                st.write("**مدة التحضير:**", recipe.get("prep_time", ""))
                st.write("**مدة الطهي:**", recipe.get("bake_time", ""))
                st.write("**درجة الحرارة:**", recipe.get("temperature", ""))
                st.write("**عدد الحصص:**", recipe.get("servings", ""))
                st.write("**ملاحظات:**", recipe.get("notes", ""))

    else:
        st.info("لا توجد وصفات لهذا الدرس حالياً.")


# =========================================================
# 12. تسجيل الدخول
# =========================================================

elif st.session_state.page == "login":

    st.header("🔐 دخول الإدارة")

    password = st.text_input(
        "كلمة مرور الإدارة",
        type="password"
    )

    if st.button("دخول الإدارة", use_container_width=True):

        if password == db["settings"].get("admin_password", "admin"):

            st.session_state.admin = True
            st.session_state.page = "admin"

            st.success("تم تسجيل الدخول بنجاح.")
            st.rerun()

        else:
            st.error("كلمة المرور غير صحيحة.")


# =========================================================
# 13. لوحة الإدارة
# =========================================================

elif st.session_state.page == "admin":

    if not st.session_state.admin:

        st.warning("يجب تسجيل الدخول أولاً.")
        st.stop()

    st.header("⚙️ لوحة الإدارة")

    if st.button("🚪 تسجيل الخروج"):
        st.session_state.admin = False
        st.session_state.page = "home"
        st.rerun()

    tabs = st.tabs([
        "📚 البرامج والنوافذ",
        "📖 الدروس",
        "📋 البطاقات",
        "🧁 الوصفات",
        "📝 الامتحانات",
        "📁 الوثائق",
        "⚙️ الإعدادات"
    ])

    # -----------------------------------------------------
    # البرامج والنوافذ
    # -----------------------------------------------------

    with tabs[0]:

        st.subheader("📚 إدارة البرامج")

        for program in db["programs"]:

            st.markdown(f"### {program['name']}")

            st.write(program["description"])

            st.write(
                f"عدد النوافذ الحالية: {len(program.get('windows', []))}"
            )

            with st.expander("➕ إضافة نافذة جديدة"):

                window_name = st.text_input(
                    "اسم النافذة",
                    key=f"wn_{program['id']}"
                )

                window_desc = st.text_area(
                    "وصف النافذة",
                    key=f"wd_{program['id']}"
                )

                if st.button(
                    "إضافة النافذة",
                    key=f"addw_{program['id']}"
                ):

                    if window_name.strip():

                        program.setdefault("windows", []).append(
                            default_window(
                                window_name,
                                window_desc
                            )
                        )

                        save_data(db)

                        st.success("تمت إضافة النافذة.")
                        st.rerun()

            for window in program.get("windows", []):

                with st.expander(
                    f"🪟 {window['name']}"
                ):

                    new_name = st.text_input(
                        "تعديل اسم النافذة",
                        value=window["name"],
                        key=f"editw_{window['id']}"
                    )

                    if st.button(
                        "حفظ اسم النافذة",
                        key=f"savew_{window['id']}"
                    ):

                        window["name"] = new_name
                        save_data(db)
                        st.success("تم الحفظ.")
                        st.rerun()

                    st.write(
                        f"عدد الوحدات: {len(window.get('units', []))}"
                    )

                    unit_name = st.text_input(
                        "اسم وحدة جديدة",
                        key=f"newunit_{window['id']}"
                    )

                    if st.button(
                        "➕ إضافة وحدة",
                        key=f"addunit_{window['id']}"
                    ):

                        if unit_name.strip():

                            window.setdefault(
                                "units", []
                            ).append(
                                default_unit(unit_name)
                            )

                            save_data(db)

                            st.success("تمت إضافة الوحدة.")
                            st.rerun()

    # -----------------------------------------------------
    # الدروس
    # -----------------------------------------------------

    with tabs[1]:

        st.subheader("📖 إضافة درس كامل")

        for program in db["programs"]:

            for window in program.get("windows", []):

                for unit in window.get("units", []):

                    with st.expander(
                        f"{program['name']} ← {window['name']} ← {unit['name']}"
                    ):

                        lesson_name = st.text_input(
                            "عنوان الدرس",
                            key=f"ln_{unit['id']}"
                        )

                        content = st.text_area(
                            "المحتوى",
                            key=f"lc_{unit['id']}"
                        )

                        objectives = st.text_area(
                            "الأهداف",
                            key=f"lo_{unit['id']}"
                        )

                        competencies = st.text_area(
                            "الكفاءات",
                            key=f"lco_{unit['id']}"
                        )

                        pedagogy = st.text_area(
                            "المقاربة البيداغوجية",
                            key=f"lp_{unit['id']}"
                        )

                        steps = st.text_area(
                            "خطوات الإنجاز",
                            key=f"ls_{unit['id']}"
                        )

                        evaluation = st.text_area(
                            "التقييم",
                            key=f"le_{unit['id']}"
                        )

                        if st.button(
                            "💾 إضافة الدرس",
                            key=f"addlesson_{unit['id']}"
                        ):

                            if lesson_name.strip():

                                lesson = default_lesson(
                                    lesson_name,
                                    content
                                )

                                lesson["objectives"] = objectives
                                lesson["competencies"] = competencies
                                lesson["pedagogy"] = pedagogy
                                lesson["steps"] = steps
                                lesson["evaluation"] = evaluation

                                unit.setdefault(
                                    "lessons", []
                                ).append(lesson)

                                save_data(db)

                                st.success(
                                    "تمت إضافة الدرس بنجاح."
                                )

                                st.rerun()

    # -----------------------------------------------------
    # البطاقات التقنية
    # -----------------------------------------------------

    with tabs[2]:

        st.subheader("📋 إضافة بطاقة تقنية")

        lessons = []

        for program in db["programs"]:
            for window in program.get("windows", []):
                for unit in window.get("units", []):
                    for lesson in unit.get("lessons", []):

                        lessons.append(
                            (
                                f"{program['name']} / "
                                f"{window['name']} / "
                                f"{unit['name']} / "
                                f"{lesson['name']}",
                                lesson
                            )
                        )

        if lessons:

            selected = st.selectbox(
                "اختاري الدرس",
                lessons,
                format_func=lambda x: x[0]
            )

            lesson = selected[1]

            title = st.text_input("عنوان البطاقة")
            category = st.text_input("الصنف")

            ingredients = st.text_area("المكونات")
            quantities = st.text_area("الكميات")
            steps = st.text_area("خطوات التحضير")

            temperature = st.text_input("درجة الحرارة")
            bake_time = st.text_input("وقت الطهي")
            prep_time = st.text_input("وقت التحضير")

            equipment = st.text_area("المعدات")
            success = st.text_area("معايير النجاح")
            errors = st.text_area("الأخطاء الشائعة")
            hygiene = st.text_area("النظافة والسلامة")
            notes = st.text_area("ملاحظات")

            if st.button("💾 حفظ البطاقة التقنية"):

                if title.strip():

                    lesson.setdefault(
                        "technical_sheets",
                        []
                    ).append({
                        "id": uid("sheet"),
                        "title": title,
                        "category": category,
                        "ingredients_list": ingredients,
                        "quantities": quantities,
                        "steps": steps,
                        "temperature": temperature,
                        "bake_time": bake_time,
                        "prep_time": prep_time,
                        "equipment": equipment,
                        "success_criteria": success,
                        "common_errors": errors,
                        "hygiene_rules": hygiene,
                        "notes": notes
                    })

                    save_data(db)

                    st.success("تم حفظ البطاقة.")
                    st.rerun()

        else:
            st.info("أضيفي درساً أولاً.")


    # -----------------------------------------------------
    # الوصفات
    # -----------------------------------------------------

    with tabs[3]:

        st.subheader("🧁 إضافة وصفة")

        lessons = []

        for program in db["programs"]:
            for window in program.get("windows", []):
                for unit in window.get("units", []):
                    for lesson in unit.get("lessons", []):

                        lessons.append(
                            (
                                f"{program['name']} / "
                                f"{window['name']} / "
                                f"{unit['name']} / "
                                f"{lesson['name']}",
                                lesson
                            )
                        )

        if lessons:

            selected = st.selectbox(
                "الدرس المرتبط بالوصفة",
                lessons,
                format_func=lambda x: x[0],
                key="recipe_lesson"
            )

            lesson = selected[1]

            name = st.text_input("اسم الوصفة")
            ingredients = st.text_area("المكونات")
            quantities = st.text_area("الكميات")
            steps = st.text_area("طريقة التحضير")
            prep = st.text_input("مدة التحضير")
            bake = st.text_input("مدة الطهي")
            temperature = st.text_input("درجة الحرارة")
            servings = st.text_input("عدد الحصص")
            notes = st.text_area("نصائح وملاحظات")

            if st.button("💾 حفظ الوصفة"):

                if name.strip():

                    lesson.setdefault(
                        "recipes",
                        []
                    ).append({
                        "id": uid("recipe"),
                        "name": name,
                        "ingredients": ingredients,
                        "quantities": quantities,
                        "steps": steps,
                        "prep_time": prep,
                        "bake_time": bake,
                        "temperature": temperature,
                        "servings": servings,
                        "notes": notes
                    })

                    save_data(db)

                    st.success("تم حفظ الوصفة.")
                    st.rerun()

        else:
            st.info("أضيفي درساً أولاً.")


    # -----------------------------------------------------
    # الامتحانات
    # -----------------------------------------------------

    with tabs[4]:

        st.subheader("📝 إنشاء امتحان")

        exam_title = st.text_input(
            "عنوان الامتحان"
        )

        if st.button("➕ إنشاء الامتحان"):

            if exam_title.strip():

                db["exams"].append({
                    "id": uid("exam"),
                    "title": exam_title,
                    "questions": []
                })

                save_data(db)

                st.success("تم إنشاء الامتحان.")
                st.rerun()

        st.divider()

        for exam in db["exams"]:

            with st.expander(exam["title"]):

                question = st.text_input(
                    "نص السؤال",
                    key=f"qt_{exam['id']}"
                )

                opt1 = st.text_input(
                    "الخيار الأول",
                    key=f"o1_{exam['id']}"
                )

                opt2 = st.text_input(
                    "الخيار الثاني",
                    key=f"o2_{exam['id']}"
                )

                opt3 = st.text_input(
                    "الخيار الثالث",
                    key=f"o3_{exam['id']}"
                )

                answer = st.number_input(
                    "رقم الإجابة الصحيحة",
                    min_value=0,
                    max_value=2,
                    value=0,
                    key=f"ans_{exam['id']}"
                )

                points = st.number_input(
                    "النقاط",
                    min_value=1,
                    value=5,
                    key=f"pts_{exam['id']}"
                )

                if st.button(
                    "➕ إضافة السؤال",
                    key=f"addq_{exam['id']}"
                ):

                    if question.strip():

                        exam["questions"].append({
                            "id": uid("question"),
                            "text": question,
                            "options": [
                                opt1,
                                opt2,
                                opt3
                            ],
                            "answer": int(answer),
                            "points": int(points)
                        })

                        save_data(db)

                        st.success("تمت إضافة السؤال.")
                        st.rerun()


    # -----------------------------------------------------
    # الوثائق
    # -----------------------------------------------------

    with tabs[5]:

        st.subheader("📁 إدارة الوثائق")

        uploaded = st.file_uploader(
            "رفع وثيقة",
            type=[
                "pdf",
                "docx",
                "xlsx",
                "pptx",
                "png",
                "jpg",
                "jpeg"
            ]
        )

        if uploaded:

            filename = (
                uuid.uuid4().hex[:10]
                + "_"
                + uploaded.name
            )

            path = os.path.join(
                UPLOADS_DIR,
                filename
            )

            with open(path, "wb") as f:
                f.write(uploaded.getbuffer())

            db["documents"].append({
                "id": uid("document"),
                "title": uploaded.name,
                "filename": filename,
                "path": path,
                "date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M"
                )
            })

            save_data(db)

            st.success("تم رفع الوثيقة.")
            st.rerun()

        for doc in db["documents"]:

            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(
                    f"📄 {doc.get('title', '')}"
                )

            with col2:

                if st.button(
                    "🗑️ حذف",
                    key=f"del_{doc['id']}"
                ):

                    path = doc.get("path")

                    if path and os.path.exists(path):
                        os.remove(path)

                    db["documents"].remove(doc)

                    save_data(db)

                    st.success("تم حذف الوثيقة.")
                    st.rerun()


    # -----------------------------------------------------
    # الإعدادات
    # -----------------------------------------------------

    with tabs[6]:

        st.subheader("⚙️ إعدادات المنصة")

        platform_name = st.text_input(
            "اسم المنصة",
            value=db["settings"].get(
                "platform_name",
                ""
            )
        )

        supervisor = st.text_input(
            "اسم الإشراف",
            value=db["settings"].get(
                "supervisor_name",
                ""
            )
        )

        new_password = st.text_input(
            "كلمة مرور جديدة",
            type="password"
        )

        if st.button("💾 حفظ الإعدادات"):

            db["settings"]["platform_name"] = platform_name
            db["settings"]["supervisor_name"] = supervisor

            if new_password.strip():
                db["settings"]["admin_password"] = new_password

            save_data(db)

            st.success("تم حفظ الإعدادات.")
            st.rerun()


# =========================================================
# 14. الامتحانات للمتربصين
# =========================================================

elif st.session_state.page == "exams":

    st.header("📝 الامتحانات")

    if not db["exams"]:

        st.info("لا توجد امتحانات حالياً.")

    else:

        for exam in db["exams"]:

            st.markdown(
                f"""
                <div class="card">
                    <h3>{exam['title']}</h3>
                    <p>عدد الأسئلة: {len(exam.get('questions', []))}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"▶️ بدء الامتحان",
                key=f"start_{exam['id']}"
            ):

                st.session_state.exam_id = exam["id"]
                st.session_state.page = "exam_session"
                st.rerun()


# =========================================================
# 15. جلسة الامتحان
# =========================================================

elif st.session_state.page == "exam_session":

    exam = next(
        (
            e for e in db["exams"]
            if e["id"] == st.session_state.exam_id
        ),
        None
    )

    if not exam:
        st.error("الامتحان غير موجود.")
        st.stop()

    st.header(f"📝 {exam['title']}")

    student = st.text_input(
        "اسم المتربص الثلاثي"
    )

    answers = {}

    for index, question in enumerate(
        exam.get("questions", [])
    ):

        options = question.get(
            "options",
            []
        )

        answers[question["id"]] = st.radio(
            f"السؤال {index + 1}: {question['text']}",
            range(len(options)),
            format_func=lambda x, opts=options: opts[x],
            key=f"answer_{question['id']}"
        )

    if st.button(
        "📤 إرسال الإجابات والحصول على النتيجة"
    ):

        if not student.strip():

            st.error(
                "يرجى إدخال اسم المتربص."
            )

        else:

            score = 0
            total = 0

            for question in exam.get(
                "questions",
                []
            ):

                points = question.get(
                    "points",
                    5
                )

                total += points

                if answers.get(
                    question["id"]
                ) == question.get("answer"):

                    score += points

            percentage = (
                round(
                    score / total * 100,
                    2
                )
                if total
                else 0
            )

            status = (
                "ناجح ✨"
                if percentage >= 50
                else
                "يحتاج إلى إعادة المحاولة"
            )

            db["results"].append({
                "id": uid("result"),
                "student_name": student,
                "exam_title": exam["title"],
                "score": score,
                "total": total,
                "percentage": percentage,
                "status": status,
                "date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M"
                )
            })

            save_data(db)

            st.success(
                f"النتيجة: {score} / {total}"
            )

            st.metric(
                "النسبة",
                f"{percentage}%"
            )

            st.info(status)


# =========================================================
# 16. النتائج
# =========================================================

elif st.session_state.page == "results":

    st.header("📊 نتائج المتربصين")

    if not db["results"]:

        st.info("لا توجد نتائج مسجلة.")

    else:

        for result in reversed(
            db["results"]
        ):

            st.markdown(
                f"""
                <div class="card">
                    <b>المتربص:</b>
                    {result['student_name']}<br>

                    <b>الامتحان:</b>
                    {result['exam_title']}<br>

                    <b>النقطة:</b>
                    {result['score']} / {result['total']}<br>

                    <b>النسبة:</b>
                    {result['percentage']}%<br>

                    <b>الحالة:</b>
                    {result['status']}<br>

                    <b>التاريخ:</b>
                    {result['date']}
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# 17. البحث الشامل
# =========================================================

elif st.session_state.page == "search":

    st.header("🔍 البحث الشامل")

    query = st.text_input(
        "اكتبي كلمة البحث"
    ).strip().lower()

    if query:

        found = False

        for program in db["programs"]:

            if query in program["name"].lower():

                found = True

                st.success(
                    f"📚 برنامج: {program['name']}"
                )

            for window in program.get(
                "windows",
                []
            ):

                if query in window["name"].lower():

                    found = True

                    st.info(
                        f"🪟 نافذة: {window['name']}"
                    )

                for unit in window.get(
                    "units",
                    []
                ):

                    if query in unit["name"].lower():

                        found = True

                        st.warning(
                            f"📂 وحدة: {unit['name']}"
                        )

                    for lesson in unit.get(
                        "lessons",
                        []
                    ):

                        text = (
                            lesson["name"]
                            + " "
                            + lesson.get(
                                "content",
                                ""
                            )
                        ).lower()

                        if query in text:

                            found = True

                            st.write(
                                f"📖 درس: {lesson['name']}"
                            )

        if not found:

            st.warning(
                "لم يتم العثور على نتائج."
            )
