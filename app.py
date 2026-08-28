import streamlit as st

st.set_page_config(
    page_title="الشيف البيداغوجي - منصة التكوين المهني",
    page_icon="👩‍🍳",
    layout="wide"
)

# ترويسة المنصة مع توقيعك المهني
st.markdown("<h1 style='text-align: right;'>👩‍🍳 الشيف البيداغوجي - منصة التكوين المهني والابتكار الفندقي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; color: gray;'>إشراف وتعداد الخبيرة: <b>فرحي حورية</b></p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: right;'>📋 الوحدات البيداغوجية الأساسية</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'>• تنظيم البرامج والمقررات التكوينية للحلويات الفندقية.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'>• البطاقات التقنية ومعايير الدقة في الوزن والحرارة.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'>• إعداد الامتحانات التطبيقية وتقييم المتربصين.</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='text-align: right;'>🎯 أهداف المنصة</h3>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'>• مرافقة الأساتذة والمتربصين بأحدث المعايير المهنية.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'>• توفير أدوات التخطيط السنوي والساعات البيداغوجية.</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: right;'>• تنظيم المحتوى التقني والعلمي بدقة واحترافية.</div>", unsafe_allow_html=True)

st.markdown("---")
st.success("منصتكِ الآن جاهزة لاستقبال ونشر محتواكِ التدريبي خطوة بخطوة بكل أمان واستقرار!")
