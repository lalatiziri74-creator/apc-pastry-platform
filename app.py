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
.recipe-detail {
    padding: 8px 0;
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
# 3) دوال مساعدة وبناء البيانات
# ============================================================

def make_id(prefix: str) -> str:
    return prefix + "_" + datetime.now().strftime("%Y%m%d%H%M%S%f")


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


# ============================================================
# 4) البيانات: بطاقات حلويات اللوز (8)
# ============================================================

RECIPES_ALMOND = [
    {
        "id": "r_baklawa",
        "title": "البقلاوة الجزائرية",
        "category": "حلويات اللوز",
        "definition": "حلوى فاخرة تُحضَّر بعجينة رقيقة جداً وحشو من اللوز، تُسقى بالعسيلة بعد الطهي.",
        "ingredients": [("فرينة", "4 كيلات"), ("سمن", "1 كيلة"), ("ملح", "قرصة"), ("فانيليا", "حسب الرغبة"), ("ماء + ماء زهر", "حسب الحاجة")],
        "filling": "3 كيلات لوز، نصف كيلة سكر، ماء زهر.",
        "topping": "العسيلة: 3 كيلات سكر، 2 ماء، نصف ليمونة، ماء زهر.",
        "preparation": "فرد العجينة، ترتيب الطبقات، إضافة الحشو، تقطيع قبل الطهي، خبز على 180°، تسقية بالعسيلة الباردة.",
        "cooking": "خبز على 180° حتى يصبح لونها ذهبياً.",
        "secrets": "العجينة رقيقة جداً، العسيلة باردة، التقطيع قبل الطهي.",
        "common_mistakes": "العجينة سميكة، العسيلة ساخنة، الحشو معجن.",
        "storage": "في علبة محكمة بعيداً عن الرطوبة.",
        "shelf_life": "7–10 أيام."
    },
    {
        "id": "r_kfta",
        "title": "حلوة الكفتة",
        "category": "حلويات اللوز",
        "definition": "تُحضَّر بعجينة اللوز وتُشكل على شكل حربوش يُقطع إلى قطع صغيرة وتُزيَّن بالملون.",
        "ingredients": [("لوز مرحي", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة")],
        "filling": "بسكويت مرحي، مكسرات، زبدة، غليكوز أو شوكولاتة طلي.",
        "topping": "ملونات غذائية، لمّاع.",
        "preparation": "فرد العجينة، وضع الحشو، لفه وتقطيعه، تزيين بالملون واللمّاع.",
        "cooking": "لا يحتاج طهي (تُشكل يدوياً).",
        "secrets": "العجينة ناعمة، الحشو متماسك، التزيين خفيف.",
        "common_mistakes": "الحشو جاف جداً، الملون زائد.",
        "storage": "في علبة محكمة مع ورق زبدة.",
        "shelf_life": "5–7 أيام."
    },
    {
        "id": "r_arayech",
        "title": "حلوة العرايش",
        "category": "حلويات اللوز",
        "definition": "حلوى راقية تُغطى بطليّة بيضاء وتُزيَّن بالورود السكرية.",
        "ingredients": [("فرينة", "حسب الحاجة"), ("سمن", "حسب الحاجة"), ("زيت", "حسب الحاجة"), ("حليب", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("ملح", "قليل")],
        "filling": "لوز أو كاوكاو، سكر، قرفة، سمن، ماء زهر.",
        "topping": "بياض بيضة، زيت، حليب، ليمون، ماء زهر، سكر ناعم.",
        "preparation": "تشكيل كرات، حشوها، خبز على 160-170°، تغطية بالطلية، تزيين.",
        "cooking": "خبز في فرن 160-170° حتى ينضج.",
        "secrets": "العجينة ترتاح، الطلية ثقيلة، التزيين بالورود.",
        "common_mistakes": "الطلية خفيفة، العجينة غير مرتاحة.",
        "storage": "في مكان بارد وجاف.",
        "shelf_life": "5–6 أيام."
    },
    {
        "id": "r_charak",
        "title": "التشاراك",
        "category": "حلويات اللوز",
        "definition": "حلوى على شكل هلال محشو باللوز أو الكاوكاو.",
        "ingredients": [("فرينة", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("ماء زهر", "حسب الحاجة")],
        "filling": "لوز أو كاوكاو، سكر، قرفة، ماء زهر.",
        "topping": "سكر ناعم للتغطية.",
        "preparation": "تشكيل دوائر، حشوها، إغلاقها على شكل هلال، خبز، تغطية بالسكر الناعم.",
        "cooking": "خبز في فرن 160-170° حتى ينضج.",
        "secrets": "العجينة طرية، التغطية بعد أن تبرد.",
        "common_mistakes": "تغطية ساخنة، العجينة جافة.",
        "storage": "في علبة محكمة.",
        "shelf_life": "5–7 أيام."
    },
    {
        "id": "r_harissa_almond",
        "title": "الهريسة باللوز",
        "category": "حلويات اللوز",
        "definition": "نسخة فاخرة من الهريسة تُحضَّر باللوز.",
        "ingredients": [("لوز", "حسب الحاجة"), ("سكر", "حسب الحاجة"), ("بيض", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("ماء زهر", "حسب الحاجة"), ("خميرة", "قليل")],
        "filling": "",
        "topping": "العسيلة.",
        "preparation": "خفق البيض والسكر، إضافة اللوز والزبدة، خبز، تسقية بالعسيلة.",
        "cooking": "خبز في فرن 170-180° حتى ينضج.",
        "secrets": "اللوز محمص، خفق جيد.",
        "common_mistakes": "اللوز غير محمص، العسيلة ساخنة.",
        "storage": "في علبة محكمة.",
        "shelf_life": "4–5 أيام."
    },
    {
        "id": "r_mashkouk",
        "title": "حلوة المشقوق",
        "category": "حلويات اللوز",
        "definition": "حلوى تُشقق أثناء الطهي لتعطي شكل مميز.",
        "ingredients": [("فرينة", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("بيض", "حسب الحاجة"), ("فانيليا", "حسب الرغبة"), ("خميرة", "قليل"), ("ماء زهر", "حسب الحاجة")],
        "filling": "لوز، سكر، قرفة، ماء زهر.",
        "topping": "سكر ناعم أو طلية حسب الرغبة.",
        "preparation": "تشكيل كرات محشوة، شقها بسكين، خبز، تغطية بالسكر أو الطلية.",
        "cooking": "خبز في فرن 160-170° حتى ينضج.",
        "secrets": "العجينة طرية، الشق واضح.",
        "common_mistakes": "العجينة قاسية، الشق سطحي.",
        "storage": "في علبة محكمة.",
        "shelf_life": "5–6 أيام."
    },
    {
        "id": "r_fruit",
        "title": "حلوة الفاكهة",
        "category": "حلويات اللوز",
        "definition": "تُشكل على هيئة فواكه صغيرة وتُلوَّن بالملونات.",
        "ingredients": [("لوز", "حسب الحاجة"), ("سكر ناعم", "حسب الحاجة"), ("زبدة", "حسب الحاجة"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة")],
        "filling": "بسكويت، مكسرات، زبدة، ماء زهر.",
        "topping": "ملونات غذائية، لمّاع، أعواد صغيرة.",
        "preparation": "تشكيل كرات بأشكال فواكه، تلوينها، تزيينها.",
        "cooking": "لا يحتاج طهي (تُشكل يدوياً).",
        "secrets": "العجينة ناعمة، التلوين خفيف.",
        "common_mistakes": "الملون زائد، العجينة خشنة.",
        "storage": "في علبة محكمة بعيداً عن الضوء.",
        "shelf_life": "7–10 أيام."
    },
    {
        "id": "r_thoumia",
        "title": "حلوة الثومية",
        "category": "حلويات اللوز",
        "definition": "تُشكل على شكل فصوص الثوم الصغيرة وتُلوَّن بالأبيض مع لمسة بنفسجي أو وردي.",
        "ingredients": [("لوز", "3 كيلات"), ("سكر ناعم", "2 كيلات"), ("زبدة", "50غ"), ("ماء زهر", "حسب الحاجة"), ("فانيليا", "حسب الرغبة")],
        "filling": "بسكويت، مكسرات، زبدة.",
        "topping": "ملون أبيض، بنفسجي أو وردي، لمّاع.",
        "preparation": "تشكيل كرات صغيرة على شكل فصوص ثوم، تلوينها، تزيينها.",
        "cooking": "لا يحتاج طهي (تُشكل يدوياً).",
        "secrets": "تشكيل دقيق، التلوين طبيعي.",
        "common_mistakes": "العجينة جافة، التلوين قوي جداً.",
        "storage": "في علبة محكمة.",
        "shelf_life": "7–8 أيام."
    }
]

# ============================================================
# 5) البيانات: بطاقات حلويات السميد والعسيلة
# ============================================================

RECIPES_SEMOLINA = [
    {
        "id": "r_mbradja",
        "title": "المبرجة (البراج)",
        "category": "حلويات السميد",
        "definition": "حلوى تقليدية تُحضّر في فصل الربيع، تعتمد على السميد المحشو بالغرس.",
        "ingredients": [("سميد متوسط", "3 كيلات"), ("سمن", "½ كيلة"), ("زيت", "½ كيلة"), ("ملح", "قليل"), ("ماء", "لجمع العجينة")],
        "filling": "تمر معجون + قرفة + جلجلان محمص.",
        "topping": "",
        "preparation": "يُعجن السميد بالسمن والزيت والملح والماء، يُفرد ويحشى بالتمر، يُقطع مربعات ويُطهى على الطاجين.",
        "cooking": "طهي على الطاجين لمدة 20 دقيقة.",
        "secrets": "عجن متوازن.",
        "common_mistakes": "العجينة جافة.",
        "storage": "في علبة محكمة.",
        "shelf_life": "5 أيام."
    },
    {
        "id": "r_makroud_oven",
        "title": "مقروط الفرن",
        "category": "حلويات السميد",
        "definition": "حلوى رمزية في الأعراس، يُخبز في الفرن ويُسقى بالعسل.",
        "ingredients": [("سميد متوسط", "1 كلغ"), ("زيت", "1 كأس"), ("سمن", "1 كأس"), ("ماء زهر", "1 كأس")],
        "filling": "تمر معجون + جلجلان + ماء زهر.",
        "topping": "عسل للتسقية.",
        "preparation": "يُعجن السميد بالسمن والزيت وماء الزهر، يُشكل معينات محشوة، يُخبز في فرن 180°، ثم يُسقى بالعسل.",
        "cooking": "خبز في فرن 180° لمدة 25 دقيقة.",
        "secrets": "استعمال عسل دافئ.",
        "common_mistakes": "قاسٍ أو لا يتشرب العسل.",
        "storage": "في علبة محكمة.",
        "shelf_life": "أسبوع."
    }
]

RECIPES_SYRUP = [
    {
        "id": "syrup_classic",
        "title": "العسيلة الكلاسيكية",
        "category": "العسيلة والقطر",
        "ingredients": [("سكر", "2 كوب"), ("ماء", "1 كوب"), ("عصير نصف ليمونة", "حسب الرغبة")],
        "common_mistakes": "خفيفة أو يتبلور السكر.",
        "storage": "قارورة زجاجية.",
        "shelf_life": "2–3 أسابيع."
    }
]

# ============================================================
# 6) البيانات الرئيسية
# ============================================================

DEFAULT_DATA = {
    "platform": {
        "name": "المنصة البيداغوجية للتكوين المهني (APC)",
        "subtitle": "منصة تعليمية وتنظيمية لدروس وبرامج التكوين المهني في صناعة الحلويات",
        "owner": "إعداد الأستاذة: فرحي حورية © 2026"
    },
    "programs": [
        {
            "id": "apprenticeship",
            "title": "برنامج التمهين",
            "icon": "👩‍🍳",
            "type": "main",
            "hours": 0,
            "status": "قيد التحديد",
            "description": "برنامج التكوين المهني عن طريق التمهين في تخصص صناعة الحلويات.",
            "objectives": [
                "اكتساب الكفاءات المهنية الأساسية في صناعة الحلويات.",
                "تطبيق قواعد النظافة والأمن والسلامة.",
                "إتقان استعمال الأدوات والتجهيزات المهنية."
            ],
            "modules": [
                {
                    "id": "app_m1",
                    "title": "الوحدة 01: النظافة والأمن والسلامة المهنية",
                    "objective": "تمكين المتربص من تطبيق قواعد النظافة الشخصية ونظافة الورشة.",
                    "lessons": [
                        {
                            "id": "app_l1",
                            "title": "النظافة الشخصية والمهنية",
                            "objective": "التعرف على قواعد النظافة الواجب احترامها قبل وأثناء العمل.",
                            "content": "تشمل النظافة الشخصية غسل اليدين بطريقة صحيحة، ارتداء اللباس المهني، وتغطية الشعر.",
                            "activities": ["مناقشة أخطار عدم احترام النظافة.", "تطبيق عملي لغسل اليدين."]
                        }
                    ],
                    "recipes": []
                }
            ]
        },
        {
            "id": "fulltime",
            "title": "البرنامج الحضوري",
            "icon": "🏫",
            "type": "main",
            "hours": 0,
            "status": "قيد التحديد",
            "description": "برنامج التكوين الحضوري في صناعة الحلويات.",
            "objectives": [
                "تطوير الكفاءة المهنية في صناعة الحلويات.",
                "إتقان قراءة البطاقة التقنية.",
                "تنظيم العمل داخل الورشة."
            ],
            "modules": []
        },
        {
            "id": "home_woman",
            "title": "برنامج المرأة الماكثة بالبيت",
            "icon": "🏠",
            "type": "parent",
            "hours": 84,
            "status": "جاهز",
            "description": "برنامج تكويني تطبيقي يهدف إلى تمكين المرأة الماكثة بالبيت من اكتساب مهارات صناعة الحلويات.",
            "objectives": [
                "اكتساب مهارات عملية في صناعة الحلويات.",
                "إتقان الوصفات التقليدية.",
                "حساب تكلفة المنتجات."
            ],
            "subPrograms": [
                {
                    "id": "traditional",
                    "title": "الحلويات التقليدية",
                    "icon": "🥮",
                    "hours": 84,
                    "status": "جاهز",
                    "description": "برنامج تطبيقي في صناعة الحلويات التقليدية الجزائرية.",
                    "modules": [
                        {
                            "id": "tr_m1",
                            "title": "المقياس 01: حلويات اللوز (8 حلويات)",
                            "objective": "إتقان تحضير وتشكيل 8 حلويات تقليدية معتمدة على اللوز.",
                            "lessons": [
                                {
                                    "id": "tr_l1",
                                    "title": "تحضير عجينة اللوز",
                                    "objective": "تعلم تحضير عجينة اللوز بقوام مناسب للتشكيل.",
                                    "content": "تمزج مكونات عجينة اللوز تدريجياً مع التحكم في كمية السائل.",
                                    "activities": ["وزن اللوز والسكر.", "اختبار القوام."]
                                },
                                {
                                    "id": "tr_l2",
                                    "title": "التشكيل والتزيين",
                                    "objective": "تطوير الدقة في تشكيل الحلويات.",
                                    "content": "يعتمد نجاح التشكيل على تجانس العجينة ودقة الوزن.",
                                    "activities": ["تقسيم العجينة.", "التزيين."]
                                }
                            ],
                            "recipes": RECIPES_ALMOND
                        },
                        {
                            "id": "tr_m2",
                            "title": "المقياس 02: حلويات السميد (7 حلويات)",
                            "objective": "إتقان تحضير حلويات السميد والمعسلات.",
                            "lessons": [
                                {
                                    "id": "tr_l3",
                                    "title": "تقنيات تبسيس السميد",
                                    "objective": "تعلم التعامل الصحيح مع السميد والدهون.",
                                    "content": "تحتاج عجائن السميد إلى عملية تبسيس جيدة حتى تتوزع الدهون.",
                                    "activities": ["عملية التبسيس.", "إضافة السائل."]
                                }
                            ],
                            "recipes": RECIPES_SEMOLINA + RECIPES_SYRUP
                        }
                    ]
                },
                {
                    "id": "oriental",
                    "title": "الحلويات الشرقية",
                    "icon": "🍯",
                    "hours": 0,
                    "status": "قيد التطوير",
                    "description": "برنامج تخصصي في الحلويات الشرقية.",
                    "modules": []
                },
                {
                    "id": "western",
                    "title": "الحلويات الغربية",
                    "icon": "🍰",
                    "hours": 0,
                    "status": "قيد التطوير",
                    "description": "برنامج تطبيقي في الحلويات الغربية.",
                    "modules": []
                }
            ]
        }
    ]
}

# ============================================================
# 7) إدارة الحالة
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

initialize()

# ============================================================
# 8) دوال المساعدة والتنقل
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

# ============================================================
# 9) عرض البطاقات والدروس
# ============================================================

def render_recipe_detail(rec):
    st.markdown(f"""
    <div class="recipe-box">
        <h3>🥮 {html.escape(rec['title'])}</h3>
        <span class="badge">{html.escape(rec['category'])}</span>
        <p><strong>🎯 التعريف:</strong> {html.escape(rec.get('definition', ''))}</p>
    </div>
    """, unsafe_allow_html=True)

    if rec.get("ingredients"):
        st.markdown("#### 🧺 المقادير")
        for name, qty in rec["ingredients"]:
            st.write(f"• **{name}** — {qty}")

    if rec.get("filling"):
        st.markdown("#### 🥜 الحشو")
        st.write(rec["filling"])

    if rec.get("topping"):
        st.markdown("#### 🎨 الطلاء/التزيين")
        st.write(rec["topping"])

    if rec.get("preparation"):
        st.markdown("#### 👩‍🍳 طريقة التحضير")
        st.write(rec["preparation"])

    if rec.get("cooking"):
        st.markdown("#### 🔥 الطهي")
        st.write(rec["cooking"])

    if rec.get("secrets"):
        st.markdown("#### ⭐ أسرار النجاح")
        st.write(rec["secrets"])

    if rec.get("common_mistakes"):
        st.markdown("#### ⚠️ الأخطاء الشائعة")
        st.write(rec["common_mistakes"])

    if rec.get("storage"):
        st.markdown("#### 📦 الحفظ")
        st.write(rec["storage"])

    if rec.get("shelf_life"):
        st.markdown("#### ⏱️ مدة الصلاحية")
        st.write(rec["shelf_life"])


def render_lesson_detail(les):
    st.markdown(f"""
    <div class="lesson-box">
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


# ============================================================
# 10) البحث
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
# 11) Breadcrumb
# ============================================================

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
            html += f'<span style="cursor:pointer;color:#d97706;text-decoration:underline;" onclick="window.location.reload();">{label}</span>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# 12) التقييم البيداغوجي
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
        {"id": "c6", "name": "دقة التنفيذ"},
        {"id": "c7", "name": "جودة المنتج النهائي"},
        {"id": "c8", "name": "التشطيب والتقديم"},
        {"id": "c9", "name": "الاستقلالية في العمل"}
    ]

    if "evaluations" not in st.session_state:
        st.session_state.evaluations = {}

    eval_key = f"{program_id}_{sub_id}" if sub_id else program_id
    if eval_key not in st.session_state.evaluations:
        st.session_state.evaluations[eval_key] = {
            "scores": {},
            "note": "",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

    eval_data = st.session_state.evaluations[eval_key]
    scores = eval_data["scores"]

    for crit in criteria:
        cid = crit["id"]
        if cid not in scores:
            scores[cid] = 0
        scores[cid] = st.slider(
            crit["name"],
            0, 5, scores[cid],
            key=f"eval_{eval_key}_{cid}"
        )

    note = st.text_area("ملاحظات الأستاذ", value=eval_data.get("note", ""))

    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("💾 حفظ التقييم"):
            eval_data["scores"] = scores
            eval_data["note"] = note
            eval_data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.success("✅ تم حفظ التقييم.")
            st.rerun()

    total = sum(scores.values())
    max_total = len(criteria) * 5
    percentage = (total / max_total) * 100 if max_total > 0 else 0
    level = "ممتاز" if percentage >= 85 else "جيد" if percentage >= 65 else "مقبول" if percentage >= 45 else "ضعيف"

    st.markdown(f"""
    <div class="success-box">
        <b>📊 النتائج:</b><br>
        مجموع النقاط: {total} / {max_total}<br>
        النسبة المئوية: {percentage:.1f}%<br>
        مستوى الإتقان: <strong>{level}</strong>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# 13) عرض محتوى البرنامج
# ============================================================

def render_program_content():
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

    col_back, _ = st.columns([1, 5])
    with col_back:
        if is_sub:
            if st.button("← العودة إلى البرامج الفرعية"):
                navigate_to_subprogram(None)
                st.session_state.subprogram_id = None
                st.rerun()
        else:
            if st.button("← العودة إلى الرئيسية"):
                navigate_to_home()

    modules = current_parent.get("modules", [])
    if not modules:
        st.info("لا توجد وحدات مسجلة في هذا البرنامج.")
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

            if mod.get("lessons"):
                st.markdown("#### 📝 الدروس")
                for les in mod["lessons"]:
                    render_lesson_detail(les)
            else:
                st.info("لا توجد دروس مسجلة.")

            if mod.get("recipes"):
                st.markdown("#### 🥮 البطاقات التقنية")
                for rec in mod["recipes"]:
                    render_recipe_detail(rec)
            else:
                st.info("لا توجد بطاقات تقنية مسجلة.")


# ============================================================
# 14) الصفحات الرئيسية
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

        role = st.radio("اختر طريقة الدخول", ["متربص", "أستاذ"], index=0 if st.session_state.role == "متربص" else 1)
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


def render_home():
    render_header()
    render_stats()
    st.markdown("## 🏛️ فضاء البرامج البيداغوجية")
    st.write("اختر البرنامج الذي تريد الدخول إليه للاطلاع على الوحدات والدروس والبطاقات التقنية.")

    programs = st.session_state.data["programs"]
    cols = st.columns(3)
    for idx, prog in enumerate(programs):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="program-box">
                <h3>{prog['icon']} {prog['title']}</h3>
                <p>{prog['description']}</p>
                <span class="badge">⏱️ {prog['hours']} ساعة</span>
                <span class="badge">{prog['status']}</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"📂 الدخول إلى {prog['title']}", key=f"open_{prog['id']}", use_container_width=True):
                if prog.get("type") == "parent":
                    st.session_state.program_id = prog["id"]
                    clear_navigation_state()
                    st.session_state.page = "subprograms"
                else:
                    st.session_state.program_id = prog["id"]
                    clear_navigation_state()
                    st.session_state.page = "program"
                st.rerun()

    render_search_results()


def render_subprograms():
    program = get_program(st.session_state.program_id)
    if not program:
        st.error("البرنامج غير موجود.")
        return

    render_breadcrumb()

    st.markdown(f"""
    <div class="card">
        <h2>{program['icon']} {program['title']}</h2>
        <p>{program['description']}</p>
        <span class="badge">⏱️ {program['hours']} ساعة</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🍰 التخصصات الفرعية")
    subs = program.get("subPrograms", [])
    if not subs:
        st.info("لا توجد برامج فرعية حالياً.")
        if st.button("← العودة إلى الرئيسية"):
            navigate_to_home()
        return

    cols = st.columns(3)
    for idx, sub in enumerate(subs):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="program-box">
                <h3>{sub['icon']} {sub['title']}</h3>
                <p>{sub['description']}</p>
                <span class="badge">⏱️ {sub['hours']} ساعة</span>
                <span class="badge">{sub['status']}</span>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"📂 استعراض {sub['title']}", key=f"sub_{sub['id']}", use_container_width=True):
                st.session_state.subprogram_id = sub["id"]
                st.session_state.module_id = None
                st.session_state.lesson_id = None
                st.session_state.recipe_id = None
                st.session_state.page = "program"
                st.rerun()

    if st.button("← العودة إلى الرئيسية", use_container_width=False):
        navigate_to_home()


# ============================================================
# 15) التشغيل الرئيسي
# ============================================================

def main():
    render_sidebar()

    page = st.session_state.page

    if page == "home":
        render_home()
        return

    if page == "subprograms":
        render_subprograms()
        return

    if page == "program":
        render_breadcrumb()
        render_program_content()
        render_evaluation()
        return

    render_home()


if __name__ == "__main__":
    main()
