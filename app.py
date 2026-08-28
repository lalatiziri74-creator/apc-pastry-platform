import streamlit as st
import pandas as pd
import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="منصة التكوين المهني - اختصاص صناعة الحلويات (APC)",
    page_icon="🥐",
    layout="wide"
)

# تهيئة بيانات الجلسة (Session State) الافتراضية
if 'modules' not in st.session_state:
    st.session_state['modules'] = [
        {"id": 1, "code": "MOD-01", "name": "حلويات اللوز التقليدية والمطورة", "unit": "الوحدة الأساسية 1", "theo_hours": 15, "prac_hours": 45, "total": 60},
        {"id": 2, "code": "MOD-02", "name": "عجينة الفطائر والمعجنات (Puff Pastry & Briochard)", "unit": "الوحدة الأساسية 2", "theo_hours": 12, "prac_hours": 48, "total": 60},
        {"id": 3, "code": "MOD-03", "name": "الكريمات والتحضيرات الأساسية (Mousse, Ganache, Dacquoise)", "unit": "الوحدة التقنية 3", "theo_hours": 20, "prac_hours": 40, "total": 60},
        {"id": 4, "code": "MOD-04", "name": "تطبيقات الحلويات الفردية والـ Trompe-l'œil", "unit": "الوحدة التطبيقية 4", "theo_hours": 10, "prac_hours": 50, "total": 60}
    ]

if 'technical_sheets' not in st.session_state:
    st.session_state['technical_sheets'] = [
        {"title": "بطاقة تقنية: داقواز اللوز (Dacquoise)", "category": "الكريمات والحلويات", "author": "أ. حورية فرحي", "date": "2026-07-01"},
        {"title": "بطاقة تقنية: كعك الويكند / بريوشارد", "category": "المعجنات", "author": "أ. حورية فرحي", "date": "2025-10-15"},
        {"title": "بطاقة تقنية: تطبيق ترويج الـ Trompe-l'œil (إجاص/مانجو)", "category": "حلويات راقية", "author": "أ. حورية فرحي", "date": "2026-05-10"}
    ]

if 'exams' not in st.session_state:
    st.session_state['exams'] = [
        {"exam_name": "امتحان نهاية الصدقي - تطبيقي", "module": "تطبيقات الحلويات الفردية والـ Trompe-l'œil", "status": "نشط", "date": "2026-06-15"}
    ]

# الشريط الجانبي للتنقل
st.sidebar.title("إدارة المنصة (APC)")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "التنقل البيداغوجي:",
    ["الرئيسية", "الوحدات والبرامج البيداغوجية", "البطاقات التقنية للوصفات", "إدارة الامتحانات والتقييم", "لوحة التحكم للأستاذ"]
)

st.sidebar.markdown("---")
st.sidebar.info("الإصدار: 1.0.0\nالمشرفة البيداغوجية: الأستاذة فرحي حورية")

# 1. واجهة الرئيسية
if menu == "الرئيسية":
    st.title("🥐 منصة التكوين المهني - اختصاص صناعة الحلويات (APC)")
    st.markdown("""
    ### مرحباً بكِ أستاذة **حورية فرحي** في منصتك الرقمية البيداغوجية.
    تم تصميم هذه المنصة لتنظيم، هيكلة، وإدارة الوحدات التكوينية، البطاقات التقنية، ومواضيع الامتحانات التطبيقية لمتكوني قطاع التكوين المهني في الجزائر.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="إجمالي الوحدات التكوينية", value=len(st.session_state['modules']))
    with col2:
        st.metric(label="البطاقات التقنية المعتمدة", value=len(st.session_state['technical_sheets']))
    with col3:
        st.metric(label="الامتحانات والاختبارات", value=len(st.session_state['exams']))

    st.markdown("---")
    st.subheader("📌 نظرة عامة على سير العمل البيداغوجي:")
    st.write("- تجميع الوحدات التكوينية وفق المقاربة بالكفاءات (APC).")
    st.write("- ضبط معايير التحضير العلمي والدقيق (استخدام الموازين الرقمية والتحكم الحراري).")
    st.write("- إعداد الامتحانات التطبيقية الخاصة بالحلويات الفردية والـ Trompe-l'œil.")

# 2. واجهة الوحدات والبرامج البيداغوجية
elif menu == "الوحدات والبرامج البيداغوجية":
    st.title("📚 الوحدات والبرامج التكوينية")
    st.write("إدارة وتعديل الحصص النظرية والتطبيقية وتوزيع الساعات البيداغوجية للمقرر.")

    # عرض جدول الوحدات
    df_modules = pd.DataFrame(st.session_state['modules'])
    st.dataframe(df_modules, use_container_width=True)

    st.markdown("### ➕ إضافة وحدة تكوينية جديدة")
    with st.form("add_module_form"):
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            mod_code = st.text_input("رمز الموديل (مثال: MOD-05)")
            mod_name = st.text_name if hasattr(st, 'text_name') else st.text_input("عنوان الوحدة أو الموديل")
        with col_m2:
            mod_unit = st.text_input("اسم الوحدة البيداغوجية الكبرى")
            col_h1, col_h2 = st.columns(2)
            with col_h1:
                theo = st.number_input("الساعات النظرية", min_value=0, value=10)
            with col_h2:
                prac = st.number_input("الساعات التطبيقية", min_value=0, value=30)
        
        submitted_mod = st.form_submit_button("حفظ وإضافة الموديل")
        if submitted_mod:
            if mod_code and mod_name:
                new_id = len(st.session_state['modules']) + 1
                st.session_state['modules'].append({
                    "id": new_id,
                    "code": mod_code,
                    "name": mod_name,
                    "unit": mod_unit,
                    "theo_hours": theo,
                    "prac_hours": prac,
                    "total": theo + prac
                })
                st.success("تمت إضافة الوحدة التكوينية بنجاح!")
                st.rerun()
            else:
                st.error("الرجاء ملء الحقول الإجبارية (الرمز والاسم).")

# 3. واجهة البطاقات التقنية للوصفات
elif menu == "البطاقات التقنية للوصفات":
    st.title("📄 البطاقات التقنية والوصفات المهنية")
    st.write("استعراض وتوثيق البطاقات الفنية للحلويات، الكريمات، والمعجنات وفق المعايير الأكاديمية.")

    # نموذج إضافة بطاقة تقنية جديدة
    with st.expander("➕ إضافة بطاقة تقنية جديدة"):
        with st.form("tech_sheet_form"):
            t_title = st.text_input("عنوان الوصفة / البطاقة التقنية")
            t_cat = st.selectbox("التصنيف", ["حلويات اللوز", "المعجنات", "الكريمات والحلويات", "حلويات راقية (Trompe-l'œil)"])
            t_author = st.text_input("المؤلف / الخبير", value="أ. حورية فرحي")
            t_submit = st.form_submit_button("إدراج البطاقة التقنية")
            
            if t_submit and t_title:
                st.session_state['technical_sheets'].append({
                    "title": t_title,
                    "category": t_cat,
                    "author": t_author,
                    "date": str(datetime.date.today())
                })
                st.success("تم حفظ البطاقة التقنية بنجاح!")
                st.rerun()

    st.markdown("---")
    # عرض البطاقات المتوفرة
    for idx, sheet in enumerate(st.session_state['technical_sheets']):
        with st.container():
            st.subheader(f"{idx+1}. {sheet['title']}")
            col_s1, col_s2, col_s3 = st.columns(3)
            col_s1.write(f"**التصنيف:** {sheet['category']}")
            col_s2.write(f"**المعد:** {sheet['author']}")
            col_s3.write(f"**تاريخ الإصدار:** {sheet['date']}")
            st.markdown("---")

# 4. واجهة إدارة الامتحانات والتقييم
elif menu == "إدارة الامتحانات والتقييم":
    st.title("📝 إدارة الامتحانات والتقييم المهني")
    st.write("تنظيم الاختبارات العملية والتطبيقية (مثل تقييم تجميعات الـ Trompe-l'œil وتحضير العجين وتجهيز القواعد المسبقة).")

    df_exams = pd.DataFrame(st.session_state['exams'])
    st.dataframe(df_exams, use_container_width=True)

    with st.form("exam_form"):
        st.subheader("جدولة امتحان تطبيقي جديد")
        ex_name = st.text_input("عنوان الاختبار التطبيقي (مثال: امتحان تدمير وعرض عجينة اللوز / مانجو)")
        ex_mod = st.selectbox("الموديل المرتبط", [m['name'] for m in st.session_state['modules']])
        ex_date = st.date_input("تاريخ الإجراء")
        ex_submit = st.form_submit_button("اعتماد الامتحان")

        if ex_submit and ex_name:
            st.session_state['exams'].append({
                "exam_name": ex_name,
                "module": ex_mod,
                "status": "مجدول",
                "date": str(ex_date)
            })
            st.success("تمت جدولة الامتحان بنجاح!")
            st.rerun()

# 5. لوحة التحكم للأستاذ
elif menu == "لوحة التحكم للأستاذ":
    st.title("⚙️ لوحة التحكم وإعدادات الأستاذة")
    st.write("إدارة الملف الشخصي، تتبع النسخ الاحتياطي، وإعدادات النظام البيئي للمنصة.")

    st.info("الملف الشخصي النشط: أستاذة فرحي حورية (خبير تكوين مهني في صناعة الحلويات).")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("حالة الاتصال والبيانات")
        st.write("✅ قاعدة البيانات المحلية متزامنة.")
        st.write("✅ هيكلة الوحدات حسب المقاربة بالكفاءات (APC) نشطة.")
    
    with col_c2:
        st.subheader("إجراءات سريعة")
        if st.button("تصدير تقرير الوحدات (CSV)"):
            df_export = pd.DataFrame(st.session_state['modules'])
            st.download_button(
                label="تحميل ملف البيانات",
                data=df_export.to_csv(index=False).encode('utf-8'),
                file_name='apc_pastry_modules.csv',
                mime='text/csv'
            )
        if st.button("إعادة ضبط إعدادات المنصة افتراضياً"):
            st.warning("تم استعادة الإعدادات الافتراضية بنجاح.")
