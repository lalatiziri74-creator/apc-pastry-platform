import streamlit as st

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
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎓 المنصة البيداغوجية للتكوين المهني (APC)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">إشراف وتصميم بيداغوجي: الأستاذة فرحي حورية</div>', unsafe_allow_html=True)
st.markdown('<div class="watermark">إعداد الأستاذة فرحي حورية ©</div>', unsafe_allow_html=True)

st.success("تم تحديث الواجهة بنجاح وبدون أي أخطاء!")
