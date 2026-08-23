import streamlit as st

st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني - APC",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.main-header {
    background: linear-gradient(135deg, #2c3e50, #4ca1af);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}
.stButton>button {
    background-color: #4ca1af;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background-color: #2c3e50;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🎓 المنصة البيداغوجية للتكوين المهني (APC)</h1>
    <p>إشراف الأستاذة: فرحي حورية | التخصص: فنون الحلويات والتبويب المهني</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📚 البرامج البيداغوجية", "🛠️ البطاقات التقنية", "🧮 حاسبة المقادير", "📝 الامتحانات والتقييم"])

with tab1:
    st.header("البرامج البيداغوجية الرسمية (HRT)")
    st.write("مرحباً بكِ في قسم البرامج التكوينية المصنفة حسب المعايير الرسمية:")
    
    program_type = st.selectbox("اختر نمط التكوين:", ["برنامج المرأة الماكثة بالبيت", "برنامج التمهين", "برنامج الحضوري"])
    
    if program_type == "برنامج المرأة الماكثة بالبيت":
        st.success("تم اختيار: مسار المرأة الماكثة بالبيت - يركز على التطبيق الميداني والمشاريع المصغرة للحلويات التقليدية والعصرية.")
    elif program_type == "برنامج التمهين":
        st.info("تم اختيار: مسار التمهين - يجمع بين التربص التطبيقي في الورشات والدروس النظرية.")
    else:
        st.warning("تم اختيار: مسار التكوين الحضوري النظامي.")

with tab2:
    st.header("البطاقات التقنية للحلويات")
    st.write("دليل تقني مفصل لأهم العجين والكريمات الأساسية:")
    
    recipe = st.selectbox("اختر الوصفة التقنية:", ["Pâte Sucrée (العجين الحلو)", "Pâte Feuilletée (العجين المورق)", "Crème Pâtissière (كريمة الحلواني)", "Poire en Trompe-l'œil (تْرومب لُوي - إجاصة عصرية)"])
    
    if "Sucrée" in recipe:
        st.markdown("""
        ### وصفة Pâte Sucrée الأساسية:
        * **المكونات:** 250غ زبدة، 150غ سكر رطب، 50غ بيض، 400غ فرينة، رشة ملح.
        * **درجة الحرارة:** التبريد الجيد للعجين قبل الخبز على حرارة 165°م.
        """)
    elif "Feuilletée" in recipe:
        st.markdown("""
        ### وصفة Pâte Feuilletée العجين المورق:
        * **المكونات:** 500غ فرينة، 10غ ملح، 250مل ماء، 400غ زبدة التوراق.
        * **التقنية:** التورق الكلاسيكي (تطبيق الدورات المتتالية مع احترام أوقات الراحة في البرودة).
        """)
    elif "Pâtissière" in recipe:
        st.markdown("""
        ### وصفة Crème Pâtissière:
        * **المكونات:** 500مل حليب، 120غ سكر، 4 صفار بيض، 40غ نشاء الذرة، فانيليا.
        * **طريقة التحضير:** غلي الحليب مع نصف كمية السكر، خفق الصفار مع الباقي والنشاء، المزج ثم الإرجاع للنار حتى الثخانة.
        """)
    else:
        st.markdown("""
        ### تقنية Trompe-l'œil (الإجاصة العصرية):
        * **المفهوم:** تصميم عصري يحاكي شكل الفاكهة الطبيعية بدقة عالية يعتمد على قالب سيليكون، قلب من الفواكه، وغلاف شمعي أو قطيفة شوكولاتة.
        """)

with tab3:
    st.header("حاسبة المقادير الدقيقة للورشات")
    st.write("اعتمدي على الوزن بالغرام للحصول على دقة احترافية متناهية:")
    
    base_flour = st.number_input("أدخل كمية الفرينة (بالغرام):", min_value=100, max_value=5000, value=1000, step=100)
    st.write(f"--- حساب النسب للكمية المدخلة ({base_flour} غ فرينة) ---")
    st.info(f"الزبدة المقترحة (بنسبة 50%): {base_flour * 0.5} غ")
    st.info(f"السكر المقترح (بنسبة 30%): {base_flour * 0.3} غ")
    st.info(f"البيض المقترح (بنسبة 20%): {base_flour * 0.2} غ")

with tab4:
    st.header("الامتحانات والتقييم البيداغوجي")
    st.write("نماذج لجان الامتحانات وتوزيع التنقيط حسب معايير الكفاءة المهنية:")
    st.markdown("""
    * **التنظيم والنظافة:** 5 نقاط
    * **احترام التقنية المتبعة:** 5 نقاط
    * **الذوق والنكهة:** 5 نقاط
    * **المظهر الجمالي والتقديم:** 5 نقاط
    """)
