import json
import os
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="الشيف البيداغوجي – النسخة المتقدمة", page_icon="🍰", layout="wide"
)

DATA_FILE = "platform_data.json"


def load_data():
  if os.path.exists(DATA_FILE):
    try:
      with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    except:
      pass

  # البيانات الافتراضية الشاملة مع تفاصيل المقياس والبطاقات
  return {
      "programs": [
          {
              "id": "p1",
              "title": "برنامج المرأة الماكثة بالبيت",
              "desc": (
                  "برنامج شامل لتكوين المرأة الماكثة بالبيت في صناعة الحلويات"
              ),
              "hours": 84,
              "status": "قيد التدقيق",
              "timeDistribution": [
                  {"stage": "المقدمة", "duration": "1 ساعة", "notes": "عرض شفهي"},
                  {
                      "stage": "تحضير الحشوة",
                      "duration": "10 ساعات",
                      "notes": "تطبيقي",
                  },
                  {
                      "stage": "إنجاز حلويات اللوز",
                      "duration": "29 ساعة",
                      "notes": "8 حلويات",
                  },
                  {"stage": "الطهي", "duration": "13 ساعة", "notes": "فرن وقلي"},
                  {
                      "stage": "التشطيب",
                      "duration": "21 ساعة",
                      "notes": "تطبيقي",
                  },
                  {
                      "stage": "النشاط الشامل",
                      "duration": "5 ساعات",
                      "notes": "إنتاج متكامل",
                  },
                  {
                      "stage": "التقييم",
                      "duration": "5 ساعات",
                      "notes": "نظري وعملي",
                  },
              ],
              "evaluationCriteria": [
                  {
                      "criterion": "احترام الوصفة",
                      "indicator": "احترام المقادير والمراحل",
                  },
                  {
                      "criterion": "التنظيم",
                      "indicator": "ترتيب العمل واستغلال الوقت",
                  },
                  {
                      "criterion": "التشكيل",
                      "indicator": "انتظام ودقة الأشكال",
                  },
                  {"criterion": "الطهي", "indicator": "لون وقوام مناسب"},
                  {"criterion": "التشطيب", "indicator": "نظافة ودقة التزيين"},
                  {"criterion": "الطعم", "indicator": "توازن النكهات"},
                  {"criterion": "القوام", "indicator": "مناسب لنوع الحلوى"},
                  {
                      "criterion": "النظافة",
                      "indicator": "احترام قواعد النظافة والسلامة",
                  },
                  {"criterion": "التقديم", "indicator": "مظهر مهني جذاب"},
              ],
              "theoryQuestions": [
                  "ما أهمية وزن المواد الأولية بدقة؟",
                  "ما دور راحة العجينة؟",
                  "ما العوامل التي تؤثر في جودة الطهي؟",
                  "كيف نميز الحلوى المطهية جيدًا؟",
                  "ما شروط نجاح عجينة اللوز؟",
                  "ما أهمية التحكم في قوام الحشوة؟",
                  "ما قواعد النظافة الواجب احترامها أثناء العمل؟",
              ],
              "modules": [
                  {
                      "id": "m1",
                      "title": "MQ1 – إعداد حلويات اللوز",
                      "desc": (
                          "إنجاز الحلويات التقليدية الجزائرية المصنوعة من اللوز"
                          " (84 ساعة)"
                      ),
                      "cards": [
                          {
                              "id": "c1",
                              "title": "البقلاوة الجزائرية التقليدية",
                              "content": (
                                  "المقادير: لوز، عسل، عجين...\nالخطوات:"
                                  " التحضير، الطهي، التشطيب."
                              ),
                          },
                          {
                              "id": "c2",
                              "title": "الكفتة الجزائرية",
                              "content": (
                                  "المقادير: لوز، سكر، زبدة...\nالخطوات: العجن،"
                                  " التشكيل، التزيين."
                              ),
                          },
                          {
                              "id": "c3",
                              "title": "حلوة الفاكهة",
                              "content": (
                                  "المقادير: عجينة اللوز، ألوان غذائية...\nالخطوات:"
                                  " التلوين، التشكيل."
                              ),
                          },
                          {
                              "id": "c4",
                              "title": "الثومية",
                              "content": (
                                  "المقادير: لوز، سكر، ماء زهر...\nالخطوات:"
                                  " التشكيل، التلوين."
                              ),
                          },
                          {
                              "id": "c5",
                              "title": "حلوة المشكلة",
                              "content": (
                                  "المقادير: لوز، سكر، مكسرات...\nالخطوات:"
                                  " تحضير العجينة، الحشو، التشكيل."
                              ),
                          },
                          {
                              "id": "c6",
                              "title": "العرايش الجزائرية",
                              "content": (
                                  "المقادير: فرينة، سمن، لوز...\nالخطوات: العجن،"
                                  " الحشو، الخبز."
                              ),
                          },
                          {
                              "id": "c7",
                              "title": "التشاراك التقليدي",
                              "content": (
                                  "المقادير: فرينة، زبدة، سكر...\nالخطوات: العجن،"
                                  " التشكيل، الخبز."
                              ),
                          },
                          {
                              "id": "c8",
                              "title": "الهريسية باللوز",
                              "content": (
                                  "المقادير: لوز، سكر، بيض...\nالخطوات: الخلط،"
                                  " الطهي، التسقية."
                              ),
                          },
                      ],
                  },
                  {
                      "id": "m2",
                      "title": "MQ2 – تحضير الحشوات والكريمات",
                      "desc": "تحضير الحشوات المختلفة المستخدمة في الحلويات",
                      "cards": [
                          {
                              "id": "c9",
                              "title": "كريمة اللوز",
                              "content": (
                                  "مقادير وطريقة تحضير كريمة اللوز التقليدية."
                              ),
                          },
                          {
                              "id": "c10",
                              "title": "الحشوة بالتمر",
                              "content": "مقادير وطريقة تحضير حشوة التمر.",
                          },
                      ],
                  },
              ],
          }
      ],
  }


def save_data(data):
  with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


if "data" not in st.session_state:
  st.session_state.data = load_data()

# تصميم الواجهة الرئيسية باستخدام Streamlit
st.markdown(
    "<h1 style='text-align: center; color: #b8860b;'>🍰 الشيف البيداغوجي</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #666;'>منصة تكوين مهني جزائرية في"
    " صناعة الحلويات التقليدية</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 0.85rem; color: #888;'>إعداد"
    " الأستاذة: <b>حورية فرحي</b> © 2026</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# القائمة الجانبية أو الاختيارية
menu = st.sidebar.selectbox(
    "القائمة الرئيسية", ["الرئيسية وبرامج التكوين", "🧮 حاسبة التكاليف", "الإدارة"]
)

if menu == "الرئيسية وبرامج التكوين":
  st.subheader("📚 برامج التكوين المهني")
  programs = st.session_state.data["programs"]

  for prog in programs:
    with st.expander(f"📂 {prog['title']} ({prog['hours']} ساعة)"):
      st.write(f"**الوصف:** {prog['desc']}")
      st.write(f"**الحالة:** {prog['status']}")

      st.markdown("---")
      st.markdown("### ⏱️ التوزيع الزمني")
      for row in prog.get("timeDistribution", []):
        st.write(
            f"- **{row['stage']}**: {row['duration']} ({row.get('notes', '')})"
        )

      st.markdown("---")
      st.markdown("### ⭐ معايير تقييم المنتوج النهائي")
      for crit in prog.get("evaluationCriteria", []):
        st.write(f"- **{crit['criterion']}**: {crit['indicator']}")

      st.markdown("---")
      st.markdown("### 📚 الوحدات والبطاقات التقنية")
      for mod in prog.get("modules", []):
        st.markdown(f"**📘 {mod['title']}")
        st.write(f"_{mod['desc']}_")
        for card in mod.get("cards", []):
          with st.container():
            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;📄 **")
            st.text(card["content"])
        st.markdown("---")

elif menu == "🧮 حاسبة التكاليف":
  st.subheader("🧮 حاسبة تكاليف الوصفات والحلويات")
  recipe_name = st.text_input("اسم الوصفة أو المنتج:")
  total_cost = st.number_input(
      "إجمالي تكلفة المكونات (دج):", min_value=0.0, value=500.0
  )
  profit_margin = st.slider("نسبة هامش الربح (%):", 10, 200, 50)
  packaging_cost = st.number_input("تكلفة التغليف والعلب (دج):", min_value=0.0, value=50.0)

  if st.button("حساب التكلفة وسعر البيع النهائي"):
    net_cost = total_cost + packaging_cost
    profit_amount = net_cost * (profit_margin / 100)
    final_price = net_cost + profit_amount

    st.success(f"📊 تقرير التكاليف لـ: {recipe_name or 'الوصفة'}")
    st.write(f"- **التكلفة الإجمالية (مواد + تغليف):** {net_cost:.2f} دج")
    st.write(f"- **قيمة الربح الصافي:** {profit_amount:.2f} دج")
    st.markdown(
        f"### 🏷️ السعر المقترح للبيع: **{final_price:.2f} دج**"
    )

elif menu == "الإدارة":
  st.subheader("🔐 لوحة تحكم الإدارة")
  admin_pass = st.text_input("كلمة مرور الإدارة:", type="password")
  if admin_pass == "1234":
    st.success("مرحباً بكِ أستاذة حورية في لوحة التحكم!")
    new_title = st.text_input("إضافة عنوان برنامج جديد:")
    if st.button("إضافة البرنامج"):
      if new_title:
        st.session_state.data["programs"].append({
            "id": str(len(st.session_state.data["programs"]) + 1),
            "title": new_title,
            "desc": "برنامج جديد مضاف",
            "hours": 30,
            "status": "قيد التطوير",
            "modules": [],
        })
        save_data(st.session_state.data)
        st.success("تم إضافة البرنامج بنجاح! حدجي الصفحة لرؤيته.")
  elif admin_pass:
    st.error("كلمة المرور غير صحيحة.")
