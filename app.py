import streamlit as st
from datetime import datetime
import copy
import html
import re
from typing import List, Dict, Any

# ============================================================
# 1) إعداد الصفحة
# ============================================================

st.set_page_config(
    page_title="المنصة البيداغوجية للتكوين المهني APC",
    page_icon="🍰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2) التصميم (CSS)
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Tajawal', sans-serif !important;
}
.stApp { background: #fbf9f5; }
.block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-bottom: 4rem;
}
h1, h2, h3, h4, p, label, div {
    font-family: 'Tajawal', sans-serif !important;
}
.main-title {
    background: linear-gradient(135deg, #fff7e6, #ffffff);
    border-right: 7px solid #d97706;
    border-bottom: 4px solid #d97706;
    border-radius: 20px;
    padding: 35px 25px;
    margin-bottom: 25px;
    text-align: center;
    box-shadow: 0 5px 25px rgba(0,0,0,0.06);
}
.main-title h1 {
    color: #1e293b;
    font-size: 2.4rem;
    font-weight: 800;
    margin: 0;
}
.main-title .orange { color: #d97706; }
.main-title p {
    color: #64748b;
    font-size: 1.05rem;
    margin-top: 12px;
}
.owner {
    color: #92400e !important;
    font-weight: 700;
}
.card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.04);
}
.card:hover { border-color: #d97706; }
.program-box {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 25px;
    min-height: 220px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
}
.program-box h3 {
    color: #1e293b;
    font-size: 1.25rem;
}
.program-box p {
    color: #64748b;
    line-height: 1.8;
}
.badge {
    display: inline-block;
    background: #fef3c7;
    color: #92400e;
    padding: 5px 12px;
    border-radius: 30px;
    font-size: 0.82rem;
    font-weight: 700;
    margin: 3px;
}
.info-box {
    background: #fff7ed;
    border-right: 5px solid #f97316;
    border-radius: 12px;
    padding: 16px;
    margin: 12px 0;
}
.success-box {
    background: #f0fdf4;
    border-right: 5px solid #16a34a;
    border-radius: 12px;
    padding: 16px;
    margin: 12px 0;
}
.lesson-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-right: 5px solid #d97706;
    border-radius: 12px;
    padding: 18px;
    margin: 10px 0;
}
.recipe-box {
    background: #fffdf8;
    border: 1px solid #f1e4c8;
    border-radius: 14px;
    padding: 20px;
    margin: 10px 0;
}
.stat {
    background: white;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    padding: 20px;
    text-align: center;
}
.stat-number {
    color: #d97706;
    font-size: 2rem;
    font-weight: 800;
}
.stat-label {
    color: #64748b;
    font-size: 0.9rem;
}
.breadcrumb {
    background: #f8fafc;
    padding: 10px 15px;
    border-radius: 10px;
    color: #64748b;
    margin-bottom: 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
}
.breadcrumb-sep { color: #94a3b8; margin: 0 4px; }
.footer {
    text-align: center;
    padding: 30px 10px;
    margin-top: 50px;
    border-top: 1px solid #e2e8f0;
    color: #64748b;
}
.sidebar-title {
    text-align: center;
    color: #d97706;
    font-weight: 800;
}
.stButton button {
    border-radius: 10px !important;
    font-family: 'Tajawal', sans-serif !important;
    font-weight: 700 !important;
}
.recipe-section {
    background: #fefcf5;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 18px;
}
.recipe-section h4 {
    color: #d97706;
    margin-bottom: 10px;
}
.recipe-detail {
    padding: 10px 0;
    border-bottom: 1px dashed #e2e8f0;
}
.recipe-detail:last-child { border-bottom: none; }
.recipe-label {
    font-weight: 700;
    color: #1e293b;
    display: inline-block;
    min-width: 120px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 3) دوال بناء البيانات (مع حقول إضافية)
# ============================================================

def recipe(
    rid: str,
    title: str,
    category: str,
    definition: str = "",
    ingredients: List[tuple] = None,
    filling: str = "",
    topping: str = "",
    preparation: str = "",
    cooking: str = "",
    secrets: str = "",
    common_mistakes: str = "",
    storage: str = "",
    shelf_life: str = "",
    objective: str = "",
    steps: List[str] = None,
    equipment: List[str] = None,
    safety: List[str] = None,
    evaluation: List[str] = None
):
    return {
        "id": rid,
        "title": title,
        "category": category,
        "definition": definition,
        "ingredients": ingredients or [],
        "filling": filling,
        "topping": topping,
        "preparation": preparation,
        "cooking": cooking,
        "secrets": secrets,
        "common_mistakes": common_mistakes,
        "storage": storage,
        "shelf_life": shelf_life,
        "objective": objective,
        "steps": steps or [],
        "equipment": equipment or [],
        "safety": safety or [],
        "evaluation": evaluation or []
    }


def lesson(lid, title, objective, content, activities):
    return {
        "id": lid,
        "title": title,
        "objective": objective,
        "content": content,
        "activities": activities
    }


def module(mid, title, objective, lessons, recipes=None):
    return {
        "id": mid,
        "title": title,
        "objective": objective,
        "lessons": lessons,
        "recipes": recipes or []
    }


def make_id(prefix: str) -> str:
    return prefix + "_" + datetime.now().strftime("%Y%m%d%H%M%S%f")


# ============================================================
# 4) بطاقات حلويات اللوز (8 بطاقات كاملة)
# ============================================================

RECIPES_ALMOND = [

    # 1. البقلاوة
    recipe(
        "r_baklawa",
        "البقلاوة الجزائرية",
        "حلويات اللوز",
        definition="حلوى فاخرة تُحضَّر بعجينة رقيقة جدًا وحشو من اللوز، تُسقى بالعسيلة بعد الطهي.",
        ingredients=[("فرينة", "4 كيلات"), ("سمن", "1 كيلة"), ("ملح", "قرصة"), ("فانيليا", "حسب الرغبة"), ("ماء + ماء زهر", "حسب الحاجة")],
        filling="3 كيلات لوز، نصف كيلة سكر، ماء زهر.",
        topping="العسيلة: 3 كيلات سكر، 2 ماء، نصف ليمونة، ماء زهر.",
        preparation="فرد العجينة، ترتيب الطبقات، إضافة الحشو، تقطيع قبل الطهي، خبز على 180°، تسقية بالعسيلة الباردة.",
        cooking="خبز على 180° حتى يصبح لونها ذهبياً.",
        secrets="العجينة رقيقة جدًا، العسيلة باردة، التقطيع قبل الطهي.",
        common_mistakes="العجينة سميكة، العسيلة ساخنة، الحشو معجن.",
        storage="في علبة محكمة بعيدًا عن الرطوبة.",
        shelf_life="7–10 أيام."
    ),

    # 2. الكفتة
    recipe(
        "r_kfta",
        "حلوة الكفتة",
        "حلويات اللوز",
        definition="تُحضَّر بعجينة اللوز وتُشكل على شكل حربوش يُقطع إلى قطع صغيرة وتُزيَّن بالملون.",
        ingredients=[("لوز مرحي", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة")],
        filling="بسكويت مرحي، مكسرات، زبدة، غليكوز أو شوكولاتة طلي.",
        topping="ملونات غذائية، لمّاع.",
        preparation="فرد العجينة، وضع الحشو، لفه وتقطيعه، تزيين بالملون واللمّاع.",
        cooking="لا يحتاج طهي (تُشكل يدوياً).",
        secrets="العجينة ناعمة، الحشو متماسك، التزيين خفيف.",
        common_mistakes="الحشو جاف جدًا، الملون زائد.",
        storage="في علبة محكمة مع ورق زبدة.",
        shelf_life="5–7 أيام."
    ),

    # 3. العرايش
    recipe(
        "r_arayech",
        "حلوة العرايش",
        "حلويات اللوز",
        definition="حلوى راقية تُغطى بطليّة بيضاء وتُزيَّن بالورود السكرية.",
        ingredients=[("فرينة", "حسب الحاجة"), ("سمن", "حسب الحاجة"), ("زيت", "حسب الحاجة"), ("حليب", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("ملح", "قليل")],
        filling="لوز أو كاوكاو، سكر، قرفة، سمن، ماء زهر.",
        topping="بياض بيضة، زيت، حليب، ليمون، ماء زهر، سكر ناعم.",
        preparation="تشكيل كرات، حشوها، خبز على 160–170°، تغطية بالطلية، تزيين.",
        cooking="خبز في فرن 160–170° حتى ينضج.",
        secrets="العجينة ترتاح، الطلية ثقيلة، التزيين بالورود.",
        common_mistakes="الطلية خفيفة، العجينة غير مرتاحة.",
        storage="في مكان بارد وجاف.",
        shelf_life="5–6 أيام."
    ),

    # 4. التشاراك
    recipe(
        "r_charak",
        "التشاراك",
        "حلويات اللوز",
        definition="حلوى على شكل هلال محشو باللوز أو الكاوكاو.",
        ingredients=[("فرينة", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("ماء زهر", "حسب الحاجة")],
        filling="لوز أو كاوكاو، سكر، قرفة، ماء زهر.",
        topping="سكر ناعم للتغطية.",
        preparation="تشكيل دوائر، حشوها، إغلاقها على شكل هلال، خبز، تغطية بالسكر الناعم.",
        cooking="خبز في فرن 160–170° حتى ينضج.",
        secrets="العجينة طرية، التغطية بعد أن تبرد.",
        common_mistakes="تغطية ساخنة، العجينة جافة.",
        storage="في علبة محكمة.",
        shelf_life="5–7 أيام."
    ),

    # 5. الهريسة باللوز
    recipe(
        "r_harissa_almond",
        "الهريسة باللوز",
        "حلويات اللوز",
        definition="نسخة فاخرة من الهريسة تُحضَّر باللوز.",
        ingredients=[("لوز", "حسب الحاجة"), ("سكر", "حسب الحاجة"), ("بيض", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("ماء زهر", "حسب الحاجة"), ("خميرة", "قليل")],
        filling="",
        topping="العسيلة: مثل الهريسة بالسميد.",
        preparation="خفق البيض والسكر، إضافة اللوز والزبدة، خبز، تسقية بالعسيلة.",
        cooking="خبز في فرن 170–180° حتى ينضج.",
        secrets="اللوز محمص، خفق جيد.",
        common_mistakes="اللوز غير محمص، العسيلة ساخنة.",
        storage="في علبة محكمة.",
        shelf_life="4–5 أيام."
    ),

    # 6. المشقوق
    recipe(
        "r_mashkouk",
        "حلوة المشقوق",
        "حلويات اللوز",
        definition="حلوى تُشقق أثناء الطهي لتعطي شكل مميز.",
        ingredients=[("فرينة", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("بيض", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("خميرة", "قليل"), ("ماء زهر", "حسب الحاجة")],
        filling="لوز، سكر، قرفة، ماء زهر.",
        topping="سكر ناعم أو طلية حسب الرغبة.",
        preparation="تشكيل كرات محشوة، شقها بسكين، خبز، تغطية بالسكر أو الطلية.",
        cooking="خبز في فرن 160–170° حتى ينضج.",
        secrets="العجينة طرية، الشق واضح.",
        common_mistakes="العجينة قاسية، الشق سطحي.",
        storage="في علبة محكمة.",
        shelf_life="5–6 أيام."
    ),

    # 7. الفاكهة
    recipe(
        "r_fruit",
        "حلوة الفاكهة",
        "حلويات اللوز",
        definition="تُشكل على هيئة فواكه صغيرة وتُلوَّن بالملونات.",
        ingredients=[("لوز", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة")],
        filling="بسكويت، مكسرات، زبدة، ماء زهر (اختياري).",
        topping="ملونات غذائية، لمّاع، أعواد صغيرة.",
        preparation="تشكيل كرات بأشكال فواكه، تلوينها، تزيينها.",
        cooking="لا يحتاج طهي (تُشكل يدوياً).",
        secrets="العجينة ناعمة، التلوين خفيف.",
        common_mistakes="الملون زائد، العجينة خشنة.",
        storage="في علبة محكمة بعيدًا عن الضوء.",
        shelf_life="7–10 أيام."
    ),

    # 8. الثومية
    recipe(
        "r_thoumia",
        "حلوة الثومية",
        "حلويات اللوز",
        definition="تُشكل على شكل فصوص الثوم الصغيرة وتُلوَّن بالأبيض مع لمسة بنفسجي أو وردي، وتُعتبر من الحلويات الفاخرة.",
        ingredients=[("لوز", "3 كيلات"), ("سكر ناعم", "2 كيلات"), ("زبدة", "50غ"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة")],
        filling="بسكويت، مكسرات، زبدة، ماء زهر (اختياري).",
        topping="ملون أبيض، بنفسجي أو وردي، لمّاع، أعواد صغيرة.",
        preparation="تشكيل كرات صغيرة على شكل فصوص ثوم، تلوينها، تزيينها، تقديمها في ورق فضي أو ذهبي.",
        cooking="لا يحتاج طهي (تُشكل يدوياً).",
        secrets="تشكيل دقيق، التلوين طبيعي، التزيين باللمّاع.",
        common_mistakes="العجينة جافة، التلوين قوي جدًا.",
        storage="في علبة محكمة.",
        shelf_life="7–8 أيام."
    )
]

# ============================================================
# 5) بطاقات حلويات السميد (7 بطاقات + أنواع العسيلة)
# ============================================================

RECIPES_SEMOLINA = [

    # 1. المبرجة
    recipe(
        "r_mbradja",
        "المبرجة (البراج)",
        "حلويات السميد",
        definition="حلوى تقليدية تُحضّر في فصل الربيع، تعتمد على السميد المحشو بالغرس (التمر) المعطر بالقرفة والقرنفل.",
        ingredients=[("سميد متوسط", "3 كيلات"), ("سمن", "½ كيلة"), ("زيت", "½ كيلة"), ("ملح", "قليل"), ("ماء", "لجمع العجينة")],
        filling="تمر معجون + قرفة + جلجلان محمص.",
        topping="",
        preparation="يُعجن السميد بالسمن والزيت والملح والماء، يُفرد ويحشى بالتمر، يُقطع مربعات ويُطهى على الطاجين حتى يصبح ذهبيًا.",
        cooking="طهي على الطاجين لمدة 20 دقيقة حتى الذهبية.",
        secrets="",
        common_mistakes="العجينة جافة → أضيفي ماء. الحشو يخرج → اضغطي جيدًا على الأطراف.",
        storage="في علبة محكمة.",
        shelf_life="5 أيام."
    ),

    # 2. مقروط الفرن
    recipe(
        "r_makroud_oven",
        "مقروط الفرن",
        "حلويات السميد",
        definition="حلوى رمزية في الأعراس، يُخبز في الفرن ويُسقى بالعسل.",
        ingredients=[("سميد متوسط", "1 كلغ"), ("زيت", "1 كأس"), ("سمن", "1 كأس"), ("ماء زهر", "1 كأس"), ("فرينة", "2 كأس"), ("خميرة كيميائية", "قليل")],
        filling="تمر معجون + جلجلان + ماء زهر.",
        topping="عسل للتسقية.",
        preparation="يُعجن السميد بالسمن والزيت وماء الزهر، يُشكل معينات محشوة، يُخبز في فرن 180°، ثم يُسقى بالعسل.",
        cooking="خبز في فرن 180° لمدة 25 دقيقة.",
        secrets="",
        common_mistakes="قاسٍ → أضيفي سمن. لا يتشرب العسل → استعملي عسل دافئ.",
        storage="في علبة محكمة.",
        shelf_life="أسبوع."
    ),

    # 3. المقروط المقلي
    recipe(
        "r_makroud_fried",
        "المقروط المقلي",
        "حلويات السميد",
        definition="نسخة مقرمشة من المقروط، يُقلى في الزيت ويُسقى بالعسل.",
        ingredients=[("سميد متوسط", "3 كوب"), ("فرينة", "1 كوب"), ("خليط سمن وزيت", "1 كوب"), ("ماء", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة")],
        filling="تمر معجون بالزبدة والقرفة.",
        topping="عسل للتسقية.",
        preparation="تُعجن العجينة، تُشكل معينات محشوة، تُقلى في زيت متوسط الحرارة، ثم تُغمس في العسل.",
        cooking="قلي في زيت متوسط الحرارة لمدة 15 دقيقة.",
        secrets="",
        common_mistakes="يتشرب زيت → استعملي زيت متوسط الحرارة. يتفتت → اجعلي العجينة متماسكة.",
        storage="في علبة محكمة.",
        shelf_life="4 أيام."
    ),

    # 4. البسبوسة
    recipe(
        "r_basbousa",
        "البسبوسة الجزائرية",
        "حلويات السميد",
        definition="حلوى طرية تُحضّر من السميد والبيض وتُسقى بالعسل.",
        ingredients=[("بيض", "4 حبات"), ("سكر", "1 كأس"), ("حليب", "1 كأس"), ("سميد متوسط", "2 كأس"), ("فرينة", "1 مغرف"), ("خميرة", "2 كيس"), ("فانيليا", "حسب الرغبة")],
        filling="",
        topping="عسل للتسقية.",
        preparation="يُخفق البيض مع السكر والحليب والفانيليا، يُضاف السميد والفرينة والخميرة، يُخبز في فرن 180°، ثم يُسقى بالعسل.",
        cooking="خبز في فرن 180° لمدة 30 دقيقة.",
        secrets="",
        common_mistakes="جافة → أضيفي حليب. لا تتشرب العسل → استعملي عسل دافئ.",
        storage="في الثلاجة.",
        shelf_life="3 أيام."
    ),

    # 5. هريسة السميد
    recipe(
        "r_harissa_semolina",
        "هريسة السميد",
        "حلويات السميد",
        definition="حلوى شعبية تُحضّر من السميد والسكر وتُسقى بالعسل.",
        ingredients=[("سميد خشن", "2 كوب"), ("سكر", "1 كوب"), ("لبن زبادي", "1 كوب"), ("سمن", "½ كوب"), ("بيكنج باودر", "قليل"), ("فانيليا", "حسب الرغبة")],
        filling="",
        topping="لوز للتزيين، عسل للتسقية.",
        preparation="يُخلط السميد مع السكر واللبن والسمن، يُسكب في صينية ويُزين باللوز، يُخبز في فرن 180°، ثم يُسقى بالعسل.",
        cooking="خبز في فرن 180° لمدة 25 دقيقة.",
        secrets="",
        common_mistakes="العجينة سميكة → أضيفي لبن. الوجه لا يتشقق → اضبطي حرارة الفرن.",
        storage="في علبة محكمة.",
        shelf_life="4 أيام."
    ),

    # 6. المعمول
    recipe(
        "r_maamoul",
        "المعمول الجزائري",
        "حلويات السميد",
        definition="حلوى محشوة بالتمر أو المكسرات، تُشكل في قوالب خاصة.",
        ingredients=[("سميد خشن", "3 كوب"), ("سميد ناعم", "2 كوب"), ("دقيق", "1 كوب"), ("زبدة", "1½ كوب"), ("حليب دافئ", "1 كوب"), ("ماء زهر", "حسب الحاجة")],
        filling="تمر أو مكسرات.",
        topping="",
        preparation="يُعجن السميد والدقيق بالزبدة والحليب وماء الزهر، تُشكل كرات وتحشى، تُضغط في قوالب، تُخبز في فرن 180°.",
        cooking="خبز في فرن 180° لمدة 20 دقيقة.",
        secrets="",
        common_mistakes="يتفتت → أضيفي زبدة. الحشو يخرج → أغلقِ جيدًا.",
        storage="في علبة محكمة.",
        shelf_life="أسبوع."
    ),

    # 7. الرفيس القسنطيني
    recipe(
        "r_rafis_constantine",
        "الرفيس القسنطيني",
        "حلويات السميد",
        definition="طبق حلو من قسنطينة، يُحضّر في المولد النبوي الشريف، يعتمد على السميد المحمّص مع الزبدة والعسل.",
        ingredients=[("سميد متوسط", "1 كلغ"), ("زبدة", "250غ"), ("عسل", "250غ"), ("قرفة", "حسب الرغبة"), ("قرنفل", "حسب الرغبة")],
        filling="",
        topping="لوز أو تمر للتزيين.",
        preparation="يُحمّص السميد، يُضاف الزبدة، يُسكب العسل تدريجيًا، يُعطر بالقرفة والقرنفل، يُزين بالمكسرات.",
        cooking="تحميص على نار هادئة لمدة 30 دقيقة.",
        secrets="",
        common_mistakes="السميد يحترق → حمّصي على نار هادئة. الخليط جاف → أضيفي عسل. الطعم مرّ → لا تبالغي في التحميص.",
        storage="في علبة محكمة.",
        shelf_life="4–5 أيام."
    )
]

# ============================================================
# 6) بطاقات العسيلة (5 أنواع + مكان للسادس)
# ============================================================

RECIPES_SYRUP = [

    {
        "id": "syrup_classic",
        "title": "العسيلة الكلاسيكية",
        "category": "العسيلة والقطر",
        "ingredients": [("سكر", "2 كوب"), ("ماء", "1 كوب"), ("عصير نصف ليمونة", "حسب الرغبة")],
        "common_mistakes": "خفيفة → زيدي وقت الغلي. يتبلور → أضيفي الليمون.",
        "storage": "قارورة زجاجية.",
        "shelf_life": "2–3 أسابيع."
    },
    {
        "id": "syrup_flower",
        "title": "العسيلة بماء الزهر",
        "category": "العسيلة والقطر",
        "ingredients": [("سكر", "2 كوب"), ("ماء", "1 كوب"), ("ماء زهر", "حسب الرغبة"), ("قطرات ليمون", "قليل")],
        "common_mistakes": "الطعم مرّ → قللي ماء الزهر.",
        "storage": "قارورة زجاجية.",
        "shelf_life": "أسبوعين."
    },
    {
        "id": "syrup_rose",
        "title": "العسيلة بماء الورد والزهر",
        "category": "العسيلة والقطر",
        "ingredients": [("سكر", "3 كوب"), ("ماء", "1 كوب"), ("ماء ورد", "حسب الرغبة"), ("ماء زهر", "حسب الرغبة"), ("ليمون", "قليل")],
        "common_mistakes": "رائحة قوية → قللي ماء الورد.",
        "storage": "قارورة داكنة.",
        "shelf_life": "10 أيام."
    },
    {
        "id": "syrup_spice",
        "title": "العسيلة بالقرفة أو القرنفل",
        "category": "العسيلة والقطر",
        "ingredients": [("سكر", "2 كوب"), ("ماء", "1 كوب"), ("قرفة أو قرنفل", "حسب الرغبة"), ("ليمون", "قليل")],
        "common_mistakes": "الطعم مرّ → أزيلي التوابل بعد الغلي.",
        "storage": "قارورة زجاجية.",
        "shelf_life": "أسبوع."
    },
    {
        "id": "syrup_honey",
        "title": "العسيلة بالعسل",
        "category": "العسيلة والقطر",
        "ingredients": [("سكر", "1 كوب"), ("ماء", "1 كوب"), ("عسل", "2 ملعقة"), ("ليمون", "قليل")],
        "common_mistakes": "ثقيلة → أضيفي ماء.",
        "storage": "قارورة زجاجية.",
        "shelf_life": "أسبوعين."
    }
    # المكان للسادس: يمكن إضافة نوع جديد مستقبلاً
]

# ============================================================
# 7) البيانات الرئيسية (مع دمج جميع البطاقات)
# ============================================================

DEFAULT_DATA = {
    "platform": {
        "name": "المنصة البيداغوجية للتكوين المهني (APC)",
        "subtitle": "منصة تعليمية وتنظيمية لدروس وبرامج التكوين المهني في صناعة الحلويات",
        "owner": "إعداد الأستاذة: فرحي حورية © 2026"
    },
    "programs": [
        # ================= برنامج التمهين =================
        {
            "id": "apprenticeship",
            "title": "برنامج التمهين",
            "icon": "👩‍🍳",
            "type": "main",
            "hours": 0,
            "status": "قيد التحديد",
            "description": "برنامج التكوين المهني عن طريق التمهين في تخصص صناعة الحلويات، يجمع بين التكوين التطبيقي بالمؤسسة والتكوين النظري والبيداغوجي.",
            "objectives": [
                "اكتساب الكفاءات المهنية الأساسية في صناعة الحلويات.",
                "التعرف على المواد الأولية وخصائصها.",
                "تطبيق قواعد النظافة والأمن والسلامة.",
                "إتقان استعمال الأدوات والتجهيزات المهنية.",
                "تنفيذ الوصفات وفق بطاقة تقنية.",
                "احترام معايير الجودة والتقديم."
            ],
            "modules": [
                module(
                    "app_m1",
                    "الوحدة 01: النظافة والأمن والسلامة المهنية",
                    "تمكين المتربص من تطبيق قواعد النظافة الشخصية ونظافة الورشة واستعمال التجهيزات بأمان.",
                    [
                        lesson("app_l1", "النظافة الشخصية والمهنية", "التعرف على قواعد النظافة الواجب احترامها قبل وأثناء العمل.",
                               "تشمل النظافة الشخصية غسل اليدين بطريقة صحيحة، ارتداء اللباس المهني، تغطية الشعر، المحافظة على نظافة الأظافر، وعدم استعمال الحلي أثناء العمل.",
                               ["مناقشة أخطار عدم احترام النظافة.", "تطبيق عملي لغسل اليدين.", "فحص اللباس المهني."]),
                        lesson("app_l2", "تنظيم منصب العمل", "تعلم تنظيم الأدوات والمواد قبل بداية العمل.",
                               "يتم تنظيم منصب العمل حسب طبيعة الإنتاج، ووضع الأدوات الضرورية في أماكن يسهل الوصول إليها، مع المحافظة على حركة آمنة داخل الورشة.",
                               ["تحديد الأدوات الضرورية.", "ترتيب منصب العمل.", "تنظيف المنصب بعد الانتهاء."])
                    ]
                ),
                module(
                    "app_m2",
                    "الوحدة 02: المواد الأولية",
                    "التعرف على خصائص المواد الأساسية المستعملة في صناعة الحلويات.",
                    [
                        lesson("app_l3", "الدقيق والسميد", "التمييز بين أنواع الدقيق والسميد واختيار المناسب لكل تحضير.",
                               "الدقيق مصدر أساسي للنشاء والبروتين، بينما يختلف السميد حسب درجة الطحن والاستعمال. يجب اختيار المادة وفق طبيعة المنتج النهائي.",
                               ["مقارنة أنواع الدقيق.", "التعرف على السميد.", "ربط المادة بالمنتج المناسب."]),
                        lesson("app_l4", "السكر والدهون", "معرفة وظائف السكر والدهون في المنتجات.",
                               "يساهم السكر في الحلاوة واللون والقوام، بينما تؤثر الدهون في الطراوة والهشاشة والطعم.",
                               ["مقارنة الزبدة والسمن.", "دراسة تأثير السكر.", "تطبيق على وصفة بسيطة."])
                    ]
                )
            ]
        },
        # ================= البرنامج الحضوري =================
        {
            "id": "fulltime",
            "title": "البرنامج الحضوري",
            "icon": "🏫",
            "type": "main",
            "hours": 0,
            "status": "قيد التحديد",
            "description": "برنامج التكوين الحضوري في صناعة الحلويات، مبني وفق المقاربة بالكفاءات APC ويجمع بين المعارف النظرية والتطبيقات المهنية.",
            "objectives": [
                "تطوير الكفاءة المهنية في صناعة الحلويات.",
                "إتقان قراءة البطاقة التقنية.",
                "تنفيذ المنتجات وفق معايير الجودة.",
                "تنظيم العمل داخل الورشة.",
                "احترام قواعد الصحة والسلامة.",
                "الاستعداد للتقييمات المهنية."
            ],
            "modules": [
                module(
                    "ft_m1",
                    "الوحدة 01: التكنولوجيا الغذائية",
                    "دراسة المواد الأولية وخصائصها وتفاعلاتها أثناء التحضير والطهي.",
                    [
                        lesson("ft_l1", "خصائص الدقيق", "فهم دور الدقيق في تكوين العجائن.",
                               "تختلف خصائص الدقيق حسب نسبة البروتين ودرجة الطحن والرطوبة. اختيار الدقيق يؤثر مباشرة على بنية المنتج النهائي.",
                               ["ملاحظة أنواع الدقيق.", "تحديد الاستعمال المناسب.", "تحليل نتيجة التحضير."]),
                        lesson("ft_l2", "البيض في صناعة الحلويات", "معرفة الوظائف التقنية للبيض.",
                               "يستعمل البيض للربط والاستحلاب والرغوة وإضافة اللون والقيمة الغذائية.",
                               ["فصل مكونات البيض.", "تحضير رغوة البياض.", "دراسة تأثير الحرارة."])
                    ]
                ),
                module(
                    "ft_m2",
                    "الوحدة 02: العجائن الأساسية",
                    "إتقان تحضير أهم العجائن المستخدمة في صناعة الحلويات.",
                    [
                        lesson("ft_l3", "العجينة المكسرة", "تحضير عجينة مكسرة متجانسة وهشة.",
                               "تخلط الدهون مع الدقيق بطريقة مناسبة ثم تضاف السوائل حسب الوصفة، مع تجنب الإفراط في العجن.",
                               ["وزن المواد.", "تحضير العجينة.", "الراحة.", "التوريق والتشكيل."]),
                        lesson("ft_l4", "العجينة المورقة", "فهم مبدأ التوريق والطبقات.",
                               "تعتمد العجينة المورقة على تكوين طبقات متناوبة من العجين والدهون، وتحتاج إلى التحكم في درجة الحرارة وعدد الطيات.",
                               ["تحضير العجين.", "إدخال الدهون.", "إنجاز الطيات.", "الطهي."])
                    ]
                )
            ]
        },
        # ================= برنامج المرأة الماكثة بالبيت =================
        {
            "id": "home_woman",
            "title": "برنامج المرأة الماكثة بالبيت",
            "icon": "🏠",
            "type": "parent",
            "hours": 84,
            "status": "جاهز",
            "description": "برنامج تكويني تطبيقي يهدف إلى تمكين المرأة الماكثة بالبيت من اكتساب مهارات صناعة الحلويات وتحويلها إلى نشاط منتج.",
            "objectives": [
                "اكتساب مهارات عملية في صناعة الحلويات.",
                "التعرف على المواد والأدوات.",
                "إتقان الوصفات التقليدية.",
                "تنظيم العمل والإنتاج.",
                "حساب تكلفة المنتجات.",
                "اكتساب مبادئ التسويق والنشاط الحرفي."
            ],
            "subPrograms": [
                # =========== الحلويات التقليدية ===========
                {
                    "id": "traditional",
                    "title": "الحلويات التقليدية",
                    "icon": "🥮",
                    "hours": 84,
                    "status": "جاهز",
                    "description": "برنامج تطبيقي في صناعة الحلويات التقليدية الجزائرية، مع التركيز على حلويات اللوز والسميد والمعسلات.",
                    "modules": [
                        module(
                            "tr_m1",
                            "المقياس 01: حلويات اللوز (8 حلويات)",
                            "إتقان تحضير وتشكيل 8 حلويات تقليدية معتمدة على اللوز.",
                            [
                                lesson("tr_l1", "تحضير عجينة اللوز", "تعلم تحضير عجينة اللوز بقوام مناسب للتشكيل.",
                                       "تمزج مكونات عجينة اللوز تدريجياً مع التحكم في كمية السائل حتى الحصول على قوام متماسك قابل للتشكيل.",
                                       ["وزن اللوز والسكر.", "إضافة السائل تدريجياً.", "اختبار القوام.", "تلوين العجينة عند الحاجة."]),
                                lesson("tr_l2", "التشكيل والتزيين", "تطوير الدقة في تشكيل الحلويات.",
                                       "يعتمد نجاح التشكيل على تجانس العجينة ودقة الوزن واستعمال الأدوات المناسبة.",
                                       ["تقسيم العجينة.", "التشكيل اليدوي.", "التزيين.", "تنظيم المنتجات."])
                            ],
                            RECIPES_ALMOND
                        ),
                        module(
                            "tr_m2",
                            "المقياس 02: حلويات السميد (7 حلويات)",
                            "إتقان تحضير 7 حلويات تقليدية معتمدة على السميد والمعسلات.",
                            [
                                lesson("tr_l3", "تقنيات تبسيس السميد", "تعلم التعامل الصحيح مع السميد والدهون والسائل.",
                                       "تحتاج عجائن السميد إلى عملية تبسيس جيدة حتى تتوزع الدهون داخل حبيبات السميد، ثم تتم إضافة السائل تدريجياً دون إفراط في العجن.",
                                       ["وزن السميد.", "إضافة الدهون.", "عملية التبسيس.", "إضافة السائل.", "الراحة."]),
                                lesson("tr_l4", "تقنيات القلي والسقي", "التحكم في عملية القلي والسقي.",
                                       "يجب التحكم في درجة حرارة الزيت وتوقيت السقي للحصول على منتج متماسك ومتشرب بطريقة متوازنة.",
                                       ["تسخين الزيت.", "اختبار الحرارة.", "القلي.", "التصفية.", "السقي."])
                            ],
                            RECIPES_SEMOLINA + RECIPES_SYRUP
                        ),
                        module(
                            "tr_m3",
                            "المقياس 03: التقييم والتطبيق الشامل",
                            "دمج الكفاءات المكتسبة في إنجاز منتج كامل وفق بطاقة تقنية.",
                            [
                                lesson("tr_l5", "النشاط التطبيقي الشامل", "إنجاز منتج من اختيار المتربص تحت إشراف الأستاذ.",
                                       "يختار المتربص منتجاً مناسباً لمستواه ويقوم بإنجاز جميع مراحل العمل من تحضير المواد إلى التشطيب والتقديم.",
                                       ["قراءة البطاقة التقنية.", "تجهيز المواد.", "تنظيم منصب العمل.", "الإنتاج.", "التشطيب.", "التقييم الذاتي."])
                            ]
                        )
                    ]
                },
                # =========== الحلويات الشرقية ===========
                {
                    "id": "oriental",
                    "title": "الحلويات الشرقية",
                    "icon": "🍯",
                    "hours": 0,
                    "status": "قيد التطوير",
                    "description": "برنامج تخصصي في مجموعة من الحلويات الشرقية وتقنيات العجائن والحشوات والشرابات.",
                    "modules": [
                        module(
                            "or_m1",
                            "المقياس 01: البقلاوة والحلويات المشرقية",
                            "التعرف على تقنيات تحضير المنتجات الشرقية.",
                            [
                                lesson("or_l1", "تقنيات تحضير الشربات", "تحضير شربات متجانس واستعماله بالشكل الصحيح.",
                                       "يعتمد نجاح الشربات على احترام نسب السكر والسائل والتحكم في مدة الطهي والتبريد.",
                                       ["وزن السكر.", "إضافة الماء.", "الغليان.", "التحكم في القوام.", "التبريد."]),
                                lesson("or_l2", "تقنيات الكنافة", "التعرف على المبادئ الأساسية لتحضير الكنافة.",
                                       "تشمل مراحل تحضير الكنافة تجهيز الخيوط أو العجينة، إضافة الدهون والحشوة، الطهي، ثم السقي والتقديم.",
                                       ["تجهيز الكنافة.", "إضافة الدهون.", "إضافة الحشوة.", "الطهي.", "السقي."])
                            ]
                        )
                    ]
                },
                # =========== الحلويات الغربية ===========
                {
                    "id": "western",
                    "title": "الحلويات الغربية",
                    "icon": "🍰",
                    "hours": 0,
                    "status": "قيد التطوير",
                    "description": "برنامج تطبيقي في مجموعة من تقنيات الحلويات الغربية والكريمة والتزيين والكيك.",
                    "modules": [
                        module(
                            "we_m1",
                            "المقياس 01: الكيك والكريمات",
                            "اكتساب المهارات الأساسية في تحضير الكيك والكريمات.",
                            [
                                lesson("we_l1", "الكيك الإسفنجي", "تحضير قاعدة كيك إسفنجي متجانسة.",
                                       "تعتمد جودة الكيك الإسفنجي على إدخال الهواء والمحافظة على الرغوة وعدم الإفراط في الخلط بعد إضافة الدقيق.",
                                       ["خفق البيض.", "إضافة السكر.", "إدخال الدقيق.", "وضع الخليط في القالب.", "الخبز."]),
                                lesson("we_l2", "الكريمة الأساسية", "التعرف على أنواع الكريمات واستعمالاتها.",
                                       "تختلف الكريمات حسب طريقة التحضير والاستخدام، ومنها الكريمات المطبوخة والكريمة المخفوقة والغاناش.",
                                       ["تحضير كريمة.", "تبريدها.", "تجهيزها للتزيين.", "تطبيق زخارف بسيطة."])
                            ]
                        )
                    ]
                }
            ]
        }
    ]
}


# ============================================================
# 8) إدارة الحالة (State Management)
# ============================================================

def initialize():
    if "data" not in st.session_state:
        st.session_state.data = copy.deepcopy(DEFAULT_DATA)

    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "program_id" not in st.session_state:
        st.session_state.program_id = None
    if "subprogram_id" not in st.session_state:
        st.session_state.subprogram_id = None
    if "module_id" not in st.session_state:
        st.session_state.module_id = None
    if "lesson_id" not in st.session_state:
        st.session_state.lesson_id = None
    if "recipe_id" not in st.session_state:
        st.session_state.recipe_id = None

    if "role" not in st.session_state:
        st.session_state.role = "متربص"
    if "admin" not in st.session_state:
        st.session_state.admin = False
    if "admin_password" not in st.session_state:
        st.session_state.admin_password = "123"

    if "search" not in st.session_state:
        st.session_state.search = ""
    if "search_result" not in st.session_state:
        st.session_state.search_result = None


initialize()


# ============================================================
# 9) دوال المساعدة (الوصول إلى البيانات)
# ============================================================

def get_program(program_id: str):
    for p in st.session_state.data["programs"]:
        if p["id"] == program_id:
            return p
    return None


def get_subprogram(program_id: str, subprogram_id: str):
    program = get_program(program_id)
    if not program:
        return None
    for sub in program.get("subPrograms", []):
        if sub["id"] == subprogram_id:
            return sub
    return None


def find_module(parent, module_id: str):
    for mod in parent.get("modules", []):
        if mod["id"] == module_id:
            return mod
    return None


def find_lesson(module_obj, lesson_id: str):
    for les in module_obj.get("lessons", []):
        if les["id"] == lesson_id:
            return les
    return None


def find_recipe(module_obj, recipe_id: str):
    for rec in module_obj.get("recipes", []):
        if rec["id"] == recipe_id:
            return rec
    return None


def clear_navigation_state():
    st.session_state.subprogram_id = None
    st.session_state.module_id = None
    st.session_state.lesson_id = None
    st.session_state.recipe_id = None


def navigate_to_home():
    st.session_state.page = "home"
    st.session_state.program_id = None
    clear_navigation_state()
    st.rerun()


def navigate_to_program(program_id: str):
    st.session_state.program_id = program_id
    clear_navigation_state()
    prog = get_program(program_id)
    if prog and prog.get("type") == "parent":
        st.session_state.page = "subprograms"
    else:
        st.session_state.page = "program"
    st.rerun()


def navigate_to_subprogram(subprogram_id: str):
    st.session_state.subprogram_id = subprogram_id
    st.session_state.module_id = None
    st.session_state.lesson_id = None
    st.session_state.recipe_id = None
    st.session_state.page = "program"
    st.rerun()


def navigate_to_module(module_id: str):
    st.session_state.module_id = module_id
    st.session_state.lesson_id = None
    st.session_state.recipe_id = None
    st.session_state.page = "program"
    st.rerun()


def navigate_to_lesson(lesson_id: str):
    st.session_state.lesson_id = lesson_id
    st.session_state.recipe_id = None
    st.session_state.page = "program"
    st.rerun()


def navigate_to_recipe(recipe_id: str):
    st.session_state.recipe_id = recipe_id
    st.session_state.lesson_id = None
    st.session_state.page = "program"
    st.rerun()


def render_breadcrumb():
    if st.session_state.page == "home":
        return

    crumbs = []
    crumbs.append(("🏠 الرئيسية", "home", None))

    prog = get_program(st.session_state.program_id) if st.session_state.program_id else None
    if prog:
        crumbs.append((prog.get("icon", "📚") + " " + prog["title"], "program", st.session_state.program_id))

    sub = None
    if st.session_state.subprogram_id:
        sub = get_subprogram(st.session_state.program_id, st.session_state.subprogram_id)
        if sub:
            crumbs.append((sub.get("icon", "📂") + " " + sub["title"], "subprogram", st.session_state.subprogram_id))

    parent = sub if sub else prog
    mod = None
    if st.session_state.module_id and parent:
        mod = find_module(parent, st.session_state.module_id)
        if mod:
            crumbs.append(("📘 " + mod["title"], "module", st.session_state.module_id))

    html = '<div class="breadcrumb">'
    for i, (label, key, value) in enumerate(crumbs):
        if i > 0:
            html += '<span class="breadcrumb-sep"> ← </span>'
        if i == len(crumbs) - 1:
            html += f'<span style="font-weight:bold;color:#1e293b;">{label}</span>'
        else:
            btn_id = f"breadcrumb_{i}_{key}"
            html += f'<span style="cursor:pointer;color:#d97706;text-decoration:underline;" onclick="document.getElementById(\'{btn_id}\').click();">{label}</span>'
            html += f'<button id="{btn_id}" style="display:none;" onclick="window.location.reload();">nav</button>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

    for i, (label, key, value) in enumerate(crumbs):
        if i < len(crumbs) - 1:
            btn_key = f"crumb_{i}_{key}"
            if st.button(label, key=btn_key, use_container_width=False, help="الانتقال إلى هذا المستوى"):
                if key == "home":
                    navigate_to_home()
                elif key == "program":
                    navigate_to_program(value)
                elif key == "subprogram":
                    navigate_to_subprogram(value)
                elif key == "module":
                    navigate_to_module(value)
                break


# ============================================================
# 10) نظام البحث المتقدم
# ============================================================

def build_search_index():
    index = []
    data = st.session_state.data
    for prog in data["programs"]:
        index.append({
            "type": "برنامج",
            "title": prog["title"],
            "description": prog.get("description", ""),
            "program_id": prog["id"],
            "subprogram_id": None,
            "module_id": None,
            "lesson_id": None,
            "recipe_id": None
        })
        for mod in prog.get("modules", []):
            index.append({
                "type": "وحدة",
                "title": mod["title"],
                "description": mod.get("objective", ""),
                "program_id": prog["id"],
                "subprogram_id": None,
                "module_id": mod["id"],
                "lesson_id": None,
                "recipe_id": None
            })
            for les in mod.get("lessons", []):
                index.append({
                    "type": "درس",
                    "title": les["title"],
                    "description": les.get("objective", ""),
                    "program_id": prog["id"],
                    "subprogram_id": None,
                    "module_id": mod["id"],
                    "lesson_id": les["id"],
                    "recipe_id": None
                })
            for rec in mod.get("recipes", []):
                index.append({
                    "type": "بطاقة تقنية",
                    "title": rec["title"],
                    "description": rec.get("definition", rec.get("objective", "")),
                    "program_id": prog["id"],
                    "subprogram_id": None,
                    "module_id": mod["id"],
                    "lesson_id": None,
                    "recipe_id": rec["id"]
                })
        for sub in prog.get("subPrograms", []):
            index.append({
                "type": "برنامج فرعي",
                "title": sub["title"],
                "description": sub.get("description", ""),
                "program_id": prog["id"],
                "subprogram_id": sub["id"],
                "module_id": None,
                "lesson_id": None,
                "recipe_id": None
            })
            for mod in sub.get("modules", []):
                index.append({
                    "type": "وحدة",
                    "title": mod["title"],
                    "description": mod.get("objective", ""),
                    "program_id": prog["id"],
                    "subprogram_id": sub["id"],
                    "module_id": mod["id"],
                    "lesson_id": None,
                    "recipe_id": None
                })
                for les in mod.get("lessons", []):
                    index.append({
                        "type": "درس",
                        "title": les["title"],
                        "description": les.get("objective", ""),
                        "program_id": prog["id"],
                        "subprogram_id": sub["id"],
                        "module_id": mod["id"],
                        "lesson_id": les["id"],
                        "recipe_id": None
                    })
                for rec in mod.get("recipes", []):
                    index.append({
                        "type": "بطاقة تقنية",
                        "title": rec["title"],
                        "description": rec.get("definition", rec.get("objective", "")),
                        "program_id": prog["id"],
                        "subprogram_id": sub["id"],
                        "module_id": mod["id"],
                        "lesson_id": None,
                        "recipe_id": rec["id"]
                    })
    return index


def perform_search(query: str):
    if not query.strip():
        return []
    query = query.lower().strip()
    results = []
    for item in build_search_index():
        text = (item["title"] + " " + item["description"]).lower()
        if query in text:
            results.append(item)
    return results


def render_search_results():
    query = st.session_state.search.strip()
    if not query:
        return
    results = perform_search(query)
    if not results:
        st.warning("🔍 لم يتم العثور على نتائج.")
        return
    st.markdown("### 🔎 نتائج البحث")
    for idx, item in enumerate(results):
        with st.expander(f"{item['type']} — {item['title']}"):
            st.write(item["description"])
            btn_key = f"search_open_{idx}_{item.get('recipe_id', '')}_{item.get('lesson_id', '')}"
            if st.button("📂 فتح", key=btn_key):
                st.session_state.program_id = item["program_id"]
                st.session_state.subprogram_id = item.get("subprogram_id")
                st.session_state.module_id = item.get("module_id")
                st.session_state.lesson_id = item.get("lesson_id")
                st.session_state.recipe_id = item.get("recipe_id")
                prog = get_program(item["program_id"])
                if prog and prog.get("type") == "parent":
                    st.session_state.page = "subprograms"
                else:
                    st.session_state.page = "program"
                st.rerun()


# ============================================================
# 11) دوال العرض الأساسية
# ============================================================

def render_header():
    st.markdown("""
    <div class="main-title">
        <h1>🍰 منصة <span class="orange">التكوين المهني (APC)</span></h1>
        <p>المنصة البيداغوجية للتكوين المهني في صناعة الحلويات</p>
        <p class="owner">إعداد وإشراف الأستاذة: فرحي حورية © 2026</p>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-title">🎛️ لوحة المنصة</div>', unsafe_allow_html=True)
        st.markdown("---")

        role = st.radio(
            "اختر طريقة الدخول",
            ["متربص", "أستاذ"],
            index=0 if st.session_state.role == "متربص" else 1
        )
        st.session_state.role = role

        if role == "أستاذ":
            password = st.text_input("رمز الأستاذ", type="password", placeholder="أدخل الرمز")
            if password == st.session_state.admin_password:
                st.session_state.admin = True
                st.success("✅ تم الدخول إلى مساحة الأستاذ")
            elif password:
                st.session_state.admin = False
                st.error("❌ رمز الدخول غير صحيح")
        else:
            st.session_state.admin = False

        st.markdown("---")
        if st.button("🏠 الرئيسية", use_container_width=True):
            navigate_to_home()

        st.markdown("---")
        st.text_input("🔎 البحث داخل المنصة", key="search", on_change=st.rerun)

        st.markdown("---")
        st.markdown("""
        <div style="text-align:center;color:#64748b;font-size:0.8rem;">
        المنصة البيداغوجية للتكوين المهني<br>
        صناعة الحلويات<br><br>
        إعداد الأستاذة: فرحي حورية<br>
        © 2026
        </div>
        """, unsafe_allow_html=True)


def render_stats():
    data = st.session_state.data
    programs = data["programs"]
    prog_count = len(programs)
    module_count = 0
    lesson_count = 0
    recipe_count = 0

    def count_in_parent(parent):
        nonlocal module_count, lesson_count, recipe_count
        for mod in parent.get("modules", []):
            module_count += 1
            lesson_count += len(mod.get("lessons", []))
            recipe_count += len(mod.get("recipes", []))
        for sub in parent.get("subPrograms", []):
            for mod in sub.get("modules", []):
                module_count += 1
                lesson_count += len(mod.get("lessons", []))
                recipe_count += len(mod.get("recipes", []))

    for prog in programs:
        count_in_parent(prog)

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown(f'<div class="stat"><div style="font-size:1.5rem;">📚</div><div class="stat-number">{prog_count}</div><div class="stat-label">البرامج</div></div>', unsafe_allow_html=True)
    with col2: st.markdown(f'<div class="stat"><div style="font-size:1.5rem;">📘</div><div class="stat-number">{module_count}</div><div class="stat-label">الوحدات</div></div>', unsafe_allow_html=True)
    with col3: st.markdown(f'<div class="stat"><div style="font-size:1.5rem;">📝</div><div class="stat-number">{lesson_count}</div><div class="stat-label">الدروس</div></div>', unsafe_allow_html=True)
    with col4: st.markdown(f'<div class="stat"><div style="font-size:1.5rem;">🥮</div><div class="stat-number">{recipe_count}</div><div class="stat-label">البطاقات التقنية</div></div>', unsafe_allow_html=True)


def render_resources():
    st.markdown("## 📚 الموارد البيداغوجية")
    resources = [
        ("📖", "البطاقة التقنية", "وثيقة تنظيمية لتحديد المواد والمراحل والعتاد ومعايير الإنجاز."),
        ("🎯", "المقاربة بالكفاءات APC", "تنظيم التعلم انطلاقاً من الكفاءة المستهدفة والوضعيات المهنية."),
        ("🧼", "النظافة والسلامة", "مرجع أساسي لاحترام شروط الصحة والنظافة والأمن داخل الورشة."),
        ("⚖️", "الوزن والقياس", "أهمية الدقة في وزن المواد واحترام النسب."),
        ("📊", "التقييم", "شبكات تساعد الأستاذ على متابعة اكتساب الكفاءات.")
    ]
    cols = st.columns(2)
    for idx, (icon, title, desc) in enumerate(resources):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card">
                <h3>{icon} {title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
# 12) عرض الدروس والبطاقات (مع الحقول الجديدة)
# ============================================================

def render_lesson_detail(les, is_selected=False):
    st.markdown(f"""
    <div class="lesson-box" style="{'border-right-color: #16a34a; background: #f0fdf4;' if is_selected else ''}">
        <h4>📝 {html.escape(les['title'])}</h4>
        <p><strong>الهدف:</strong> {html.escape(les['objective'])}</p>
        <p><strong>المحتوى:</strong> {html.escape(les['content'])}</p>
    </div>
    """, unsafe_allow_html=True)
    activities = les.get("activities", [])
    if activities:
        st.markdown("**🔧 النشاطات التطبيقية:**")
        for act in activities:
            st.write("• " + act)


def render_recipe_detail(rec, is_selected=False):
    st.markdown(f"""
    <div class="recipe-box" style="{'border: 2px solid #16a34a;' if is_selected else ''}">
        <h3>🥮 {html.escape(rec['title'])}</h3>
        <span class="badge">{html.escape(rec['category'])}</span>
        <p><strong>🎯 التعريف:</strong> {html.escape(rec.get('definition', ''))}</p>
    </div>
    """, unsafe_allow_html=True)

    # المقادير
    if rec.get("ingredients"):
        st.markdown("#### 🧺 المقادير")
        for name, qty in rec["ingredients"]:
            st.write(f"• **{name}** — {qty}")

    # الحشو
    if rec.get("filling"):
        st.markdown("#### 🥜 الحشو")
        st.write(rec["filling"])

    # الطلاء/التزيين
    if rec.get("topping"):
        st.markdown("#### 🎨 الطلاء/التزيين")
        st.write(rec["topping"])

    # طريقة التحضير
    if rec.get("preparation"):
        st.markdown("#### 👩‍🍳 طريقة التحضير")
        st.write(rec["preparation"])

    # الطهي
    if rec.get("cooking"):
        st.markdown("#### 🔥 الطهي")
        st.write(rec["cooking"])

    # أسرار النجاح
    if rec.get("secrets"):
        st.markdown("#### ⭐ أسرار النجاح")
        st.write(rec["secrets"])

    # الأخطاء الشائعة
    if rec.get("common_mistakes"):
        st.markdown("#### ⚠️ الأخطاء الشائعة")
        st.write(rec["common_mistakes"])

    # الحفظ
    if rec.get("storage"):
        st.markdown("#### 📦 الحفظ")
        st.write(rec["storage"])

    # مدة الصلاحية
    if rec.get("shelf_life"):
        st.markdown("#### ⏱️ مدة الصلاحية")
        st.write(rec["shelf_life"])

    # الأقسام القديمة (للتوافق)
    if rec.get("steps"):
        st.markdown("#### 👩‍🍳 مراحل الإنجاز (خطوات)")
        for i, step in enumerate(rec["steps"], 1):
            st.markdown(f"**{i}.** {step}")

    if rec.get("equipment"):
        st.markdown("#### 🛠️ العتاد")
        for item in rec["equipment"]:
            st.write("• " + item)

    if rec.get("safety"):
        st.markdown("#### 🧼 قواعد النظافة والسلامة")
        for rule in rec["safety"]:
            st.write("• " + rule)

    if rec.get("evaluation"):
        st.markdown("#### 📊 معايير التقييم")
        for criterion in rec["evaluation"]:
            st.write("• " + criterion)


# ============================================================
# 13) نماذج الإضافة والتعديل والحذف للأستاذ
# ============================================================

def admin_add_lesson_form(module_obj):
    if not st.session_state.admin:
        return
    with st.expander("➕ إضافة درس جديد", expanded=False):
        with st.form(f"add_lesson_{module_obj['id']}"):
            title = st.text_input("عنوان الدرس")
            objective = st.text_area("الهدف")
            content = st.text_area("المحتوى")
            activities_text = st.text_area("النشاطات (كل نشاط في سطر)")
            submitted = st.form_submit_button("حفظ الدرس")
            if submitted:
                if not title.strip():
                    st.error("أدخل عنوان الدرس.")
                else:
                    activities = [a.strip() for a in activities_text.split("\n") if a.strip()]
                    module_obj.setdefault("lessons", []).append(
                        lesson(make_id("lesson"), title, objective, content, activities)
                    )
                    st.success("تمت إضافة الدرس.")
                    st.rerun()


def admin_add_recipe_form(module_obj):
    if not st.session_state.admin:
        return
    with st.expander("➕ إضافة بطاقة تقنية جديدة", expanded=False):
        with st.form(f"add_recipe_{module_obj['id']}"):
            title = st.text_input("اسم الوصفة")
            category = st.text_input("التصنيف")
            definition = st.text_area("التعريف")
            ingredients_text = st.text_area("المقادير (كل سطر: اسم | كمية)")
            filling = st.text_area("الحشو")
            topping = st.text_area("الطلاء/التزيين")
            preparation = st.text_area("طريقة التحضير")
            cooking = st.text_area("الطهي")
            secrets = st.text_area("أسرار النجاح")
            mistakes = st.text_area("الأخطاء الشائعة")
            storage = st.text_area("الحفظ")
            shelf_life = st.text_area("مدة الصلاحية")
            submitted = st.form_submit_button("حفظ البطاقة")
            if submitted:
                if not title.strip():
                    st.error("أدخل اسم الوصفة.")
                else:
                    ingredients = []
                    for line in ingredients_text.split("\n"):
                        if "|" in line:
                            parts = [p.strip() for p in line.split("|")]
                            if len(parts) >= 2:
                                ingredients.append((parts[0], parts[1]))
                    module_obj.setdefault("recipes", []).append(
                        recipe(
                            make_id("recipe"), title, category,
                            definition=definition,
                            ingredients=ingredients,
                            filling=filling,
                            topping=topping,
                            preparation=preparation,
                            cooking=cooking,
                            secrets=secrets,
                            common_mistakes=mistakes,
                            storage=storage,
                            shelf_life=shelf_life
                        )
                    )
                    st.success("تم حفظ البطاقة التقنية.")
                    st.rerun()


def admin_edit_lesson(module_obj, lesson_obj):
    if not st.session_state.admin:
        return
    with st.expander(f"✏️ تعديل الدرس: {lesson_obj['title']}", expanded=False):
        with st.form(f"edit_lesson_{lesson_obj['id']}"):
            new_title = st.text_input("العنوان", value=lesson_obj["title"])
            new_objective = st.text_area("الهدف", value=lesson_obj["objective"])
            new_content = st.text_area("المحتوى", value=lesson_obj["content"])
            new_activities = st.text_area("النشاطات (كل نشاط في سطر)", value="\n".join(lesson_obj.get("activities", [])))
            submitted = st.form_submit_button("💾 حفظ التعديلات")
            if submitted:
                lesson_obj["title"] = new_title
                lesson_obj["objective"] = new_objective
                lesson_obj["content"] = new_content
                lesson_obj["activities"] = [a.strip() for a in new_activities.split("\n") if a.strip()]
                st.success("تم تحديث الدرس.")
                st.rerun()
        if st.button(f"🗑️ حذف الدرس", key=f"del_lesson_{lesson_obj['id']}"):
            if st.checkbox(f"تأكيد حذف الدرس '{lesson_obj['title']}'", key=f"confirm_del_lesson_{lesson_obj['id']}"):
                module_obj["lessons"] = [l for l in module_obj["lessons"] if l["id"] != lesson_obj["id"]]
                st.success("تم حذف الدرس.")
                st.rerun()


def admin_edit_recipe(module_obj, recipe_obj):
    if not st.session_state.admin:
        return
    with st.expander(f"✏️ تعديل البطاقة: {recipe_obj['title']}", expanded=False):
        with st.form(f"edit_recipe_{recipe_obj['id']}"):
            new_title = st.text_input("اسم الوصفة", value=recipe_obj["title"])
            new_category = st.text_input("التصنيف", value=recipe_obj["category"])
            new_definition = st.text_area("التعريف", value=recipe_obj.get("definition", ""))
            ing_text = "\n".join([f"{n} | {q}" for n, q in recipe_obj.get("ingredients", [])])
            new_ing = st.text_area("المقادير (اسم | كمية)", value=ing_text)
            new_filling = st.text_area("الحشو", value=recipe_obj.get("filling", ""))
            new_topping = st.text_area("الطلاء/التزيين", value=recipe_obj.get("topping", ""))
            new_preparation = st.text_area("طريقة التحضير", value=recipe_obj.get("preparation", ""))
            new_cooking = st.text_area("الطهي", value=recipe_obj.get("cooking", ""))
            new_secrets = st.text_area("أسرار النجاح", value=recipe_obj.get("secrets", ""))
            new_mistakes = st.text_area("الأخطاء الشائعة", value=recipe_obj.get("common_mistakes", ""))
            new_storage = st.text_area("الحفظ", value=recipe_obj.get("storage", ""))
            new_shelf = st.text_area("مدة الصلاحية", value=recipe_obj.get("shelf_life", ""))
            submitted = st.form_submit_button("💾 حفظ التعديلات")
            if submitted:
                ingredients = []
                for line in new_ing.split("\n"):
                    if "|" in line:
                        parts = [p.strip() for p in line.split("|")]
                        if len(parts) >= 2:
                            ingredients.append((parts[0], parts[1]))
                recipe_obj["title"] = new_title
                recipe_obj["category"] = new_category
                recipe_obj["definition"] = new_definition
                recipe_obj["ingredients"] = ingredients
                recipe_obj["filling"] = new_filling
                recipe_obj["topping"] = new_topping
                recipe_obj["preparation"] = new_preparation
                recipe_obj["cooking"] = new_cooking
                recipe_obj["secrets"] = new_secrets
                recipe_obj["common_mistakes"] = new_mistakes
                recipe_obj["storage"] = new_storage
                recipe_obj["shelf_life"] = new_shelf
                st.success("تم تحديث البطاقة.")
                st.rerun()
        if st.button(f"🗑️ حذف البطاقة", key=f"del_recipe_{recipe_obj['id']}"):
            if st.checkbox(f"تأكيد حذف البطاقة '{recipe_obj['title']}'", key=f"confirm_del_recipe_{recipe_obj['id']}"):
                module_obj["recipes"] = [r for r in module_obj["recipes"] if r["id"] != recipe_obj["id"]]
                st.success("تم حذف البطاقة.")
                st.rerun()


# ============================================================
# 14) عرض محتوى البرنامج (صفحة تفاصيل)
# ============================================================

def render_program_content(container):
    program = get_program(st.session_state.program_id)
    subprogram_id = st.session_state.subprogram_id

    if subprogram_id:
        current_parent = get_subprogram(st.session_state.program_id, subprogram_id)
        if not current_parent:
            st.error("البرنامج الفرعي غير موجود.")
            return
        is_sub = True
    else:
        current_parent = program
        if not current_parent:
            st.error("البرنامج غير موجود.")
            return
        is_sub = False

    # عرض مقدمة البرنامج
    objectives = current_parent.get("objectives", [])
    obj_html = "".join([f"<li>{html.escape(o)}</li>" for o in objectives])
    st.markdown(f"""
    <div class="card">
        <h2>{current_parent.get('icon', '📚')} {html.escape(current_parent['title'])}</h2>
        <p>{html.escape(current_parent.get('description', ''))}</p>
        <span class="badge">⏱️ {current_parent.get('hours', 0)} ساعة</span>
        <span class="badge">{html.escape(current_parent.get('status', ''))}</span>
        <hr>
        <h4>🎯 الكفاءات والأهداف العامة</h4>
        <ul>{obj_html}</ul>
    </div>
    """, unsafe_allow_html=True)

    # أزرار العودة
    col_back, _ = st.columns([1, 5])
    with col_back:
        if is_sub:
            if st.button("← العودة إلى البرامج الفرعية"):
                st.session_state.subprogram_id = None
                st.session_state.module_id = None
                st.session_state.lesson_id = None
                st.session_state.recipe_id = None
                st.rerun()
        else:
            if st.button("← العودة إلى الرئيسية"):
                navigate_to_home()

    # عرض الوحدات
    modules = current_parent.get("modules", [])
    if not modules:
        st.info("لا توجد وحدات مسجلة في هذا البرنامج.")
        if st.session_state.admin:
            admin_add_module_form(current_parent)
        return

    target_module_id = st.session_state.module_id
    for mod in modules:
        if target_module_id and mod["id"] != target_module_id:
            continue

        expander_label = f"📘 {mod['title']}"
        if target_module_id and mod["id"] == target_module_id:
            expander_label += " (مفتوحة)"
        with st.expander(expander_label, expanded=(target_module_id == mod["id"])):
            st.write(mod["objective"])

            # الدروس
            if mod.get("lessons"):
                st.markdown("#### 📝 الدروس")
                for les in mod["lessons"]:
                    is_selected = (st.session_state.lesson_id == les["id"])
                    render_lesson_detail(les, is_selected)
                    if st.session_state.admin:
                        admin_edit_lesson(mod, les)
            else:
                st.info("لا توجد دروس مسجلة.")

            # البطاقات التقنية
            if mod.get("recipes"):
                st.markdown("#### 🥮 البطاقات التقنية")
                for rec in mod["recipes"]:
                    is_selected = (st.session_state.recipe_id == rec["id"])
                    render_recipe_detail(rec, is_selected)
                    if st.session_state.admin:
                        admin_edit_recipe(mod, rec)
            else:
                st.info("لا توجد بطاقات تقنية مسجلة.")

            # حذف الوحدة
            if st.session_state.admin:
                if st.button(f"🗑️ حذف هذه الوحدة", key=f"del_mod_{mod['id']}"):
                    if st.checkbox(f"تأكيد حذف الوحدة '{mod['title']}'", key=f"confirm_del_mod_{mod['id']}"):
                        current_parent["modules"] = [m for m in current_parent["modules"] if m["id"] != mod["id"]]
                        st.success("تم حذف الوحدة.")
                        st.rerun()

            # نماذج الإضافة للأستاذ
            if st.session_state.admin:
                admin_add_lesson_form(mod)
                admin_add_recipe_form(mod)

    # إضافة وحدة جديدة
    if st.session_state.admin:
        admin_add_module_form(current_parent)


def admin_add_module_form(parent):
    with st.expander("➕ إضافة وحدة جديدة", expanded=False):
        with st.form(f"add_module_{parent['id']}"):
            title = st.text_input("عنوان الوحدة")
            objective = st.text_area("الهدف والكفاءة المستهدفة")
            submitted = st.form_submit_button("حفظ الوحدة")
            if submitted:
                if not title.strip():
                    st.error("يجب إدخال عنوان الوحدة.")
                else:
                    parent.setdefault("modules", []).append(
                        module(make_id("module"), title, objective, [], [])
                    )
                    st.success("تمت إضافة الوحدة.")
                    st.rerun()


# ============================================================
# 15) التقييم البيداغوجي المرتبط بالبرنامج
# ============================================================

def render_evaluation():
    program_id = st.session_state.program_id
    if not program_id:
        return

    program = get_program(program_id)
    if not program:
        return

    st.markdown("## 📊 التقييم البيداغوجي")

    sub_id = st.session_state.subprogram_id
    if sub_id:
        sub = get_subprogram(program_id, sub_id)
        prog_name = sub["title"] if sub else program["title"]
    else:
        prog_name = program["title"]

    st.markdown(f"""
    <div class="info-box">
    تقييم خاص بـ: <strong>{prog_name}</strong>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.admin:
        st.info("🔒 التقييم متاح للأستاذ فقط.")
        return

    criteria = [
        {"id": "c1", "name": "تنظيم منصب العمل"},
        {"id": "c2", "name": "احترام قواعد النظافة والسلامة"},
        {"id": "c3", "name": "اختيار المواد الأولية"},
        {"id": "c4", "name": "استعمال الأدوات والتجهيزات"},
        {"id": "c5", "name": "احترام البطاقة التقنية"},
        {"i
