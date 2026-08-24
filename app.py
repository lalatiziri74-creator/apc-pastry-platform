import streamlit.components.v1 as components

# تصميم المنصة المتكامل بملف HTML واحد (واجهة رئيسية وعوالم مستقلة)
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المنصة البيداغوجية للتكوين المهني (APC)</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --accent-color: #4ca1af;
            --bg-color: #f4f7f6;
            --card-bg: #ffffff;
            --text-color: #333333;
            --border-radius: 12px;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            direction: rtl;
            text-align: right;
        }
        header {
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            color: white;
            padding: 25px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        header h1 {
            margin: 0 0 10px 0;
            font-size: 24px;
        }
        header p {
            margin: 0;
            font-size: 16px;
            opacity: 0.9;
        }
        .container {
            max-width: 1100px;
            margin: 20px auto;
            padding: 0 15px;
        }
        .view-section {
            display: none;
            background: var(--card-bg);
            padding: 25px;
            border-radius: var(--border-radius);
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .view-section.active {
            display: block;
        }
        .grid-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .card {
            background: var(--card-bg);
            border: 2px solid #e0e0e0;
            border-radius: var(--border-radius);
            padding: 25px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        }
        .card:hover {
            border-color: var(--accent-color);
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(76, 161, 175, 0.2);
        }
        .card h3 {
            color: var(--primary-color);
            margin-top: 0;
        }
        .btn {
            background-color: var(--accent-color);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
            transition: background 0.2s;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: var(--primary-color);
        }
        .btn-back {
            background-color: #6c757d;
            margin-bottom: 20px;
        }
        .btn-back:hover {
            background-color: #5a6268;
        }
        .calculator-box {
            background: #f9fbfb;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #d1e7ed;
            margin-top: 15px;
        }
        .calculator-box input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
        }
    </style>
</head>
<body>

    <header>
        <h1>🎓 المنصة البيداغوجية للتكوين المهني (APC)</h1>
        <p>تحت إشراف الأستاذة فرحي حورية | التكوين المهني في صناعة الحلويات</p>
    </header>

    <div class="container">

        <!-- الواجهة الرئيسية -->
        <div id="main-view" class="view-section active">
            <h2>البرامج التكوينية الأساسية</h2>
            <p>اختر البرنامج المطلوب للولوج إلى العالم الخاص به:</p>
            <div class="grid-cards">
                <div class="card" onclick="switchView('apprenticeship-view')">
                    <h3>📘 برنامج التمهين</h3>
                    <p>الجمع بين التربص التطبيقي في الورشات المهنية والدروس النظرية.</p>
                    <button class="btn">دخول العالم</button>
                </div>
                <div class="card" onclick="switchView('presence-view')">
                    <h3>🏫 البرنامج الحضوري</h3>
                    <p>التكوين النظامي المكثف داخل الهياكل البيداغوجية.</p>
                    <button class="btn">دخول العالم</button>
                </div>
                <div class="card" onclick="switchView('homemaker-view')">
                    <h3>👩‍🍳 برنامج المرأة الماكثة بالبيت</h3>
                    <p>مشاريع مصغرة وتطبيق ميداني للحرف والحلويات.</p>
                    <button class="btn">دخول العالم</button>
                </div>
            </div>
        </div>

        <!-- 1. برنامج التمهين -->
        <div id="apprenticeship-view" class="view-section">
            <button class="btn btn-back" onclick="switchView('main-view')">⬅ رجوع إلى الواجهة الرئيسية</button>
            <h2>📘 عالم برنامج التمهين</h2>
            <p>المحتويات والأدوات الخاصة ببرنامج التمهين:</p>
            <ul>
                <li>الدروس النظرية والتطبيقية للتمهين</li>
                <li>المخططات البيداغوجية</li>
                <li>📝 الامتحانات والتقييم البيداغوجي للتمهين</li>
            </ul>
        </div>

        <!-- 2. البرنامج الحضوري -->
        <div id="presence-view" class="view-section">
            <button class="btn btn-back" onclick="switchView('main-view')">⬅ رجوع إلى الواجهة الرئيسية</button>
            <h2>🏫 عالم البرنامج الحضوري</h2>
            <p>المحتويات والأدوات الخاصة بالتكوين الحضوري:</p>
            <ul>
                <li>برنامج الدروس الحضورية بالمعهد</li>
                <li>أدوات الورشة التطبيقية</li>
                <li>📝 الامتحانات والتقييم البيداغوجي للحضوري</li>
            </ul>
        </div>

        <!-- 3. برنامج المرأة الماكثة بالبيت -->
        <div id="homemaker-view" class="view-section">
            <button class="btn btn-back" onclick="switchView('main-view')">⬅ رجوع إلى الواجهة الرئيسية</button>
            <h2>👩‍🍳 برنامج المرأة الماكثة بالبيت</h2>
            <p>اختر التخصص الفرعي:</p>
            <div class="grid-cards">
                <div class="card" onclick="switchView('traditional-view')">
                    <h3>🍰 الحلويات التقليدية</h3>
                    <p>العالم الخاص بتراث الحلويات التقليدية العريقة.</p>
                    <button class="btn">دخول التخصص</button>
                </div>
                <div class="card" onclick="switchView('eastern-view')">
                    <h3>🧁 الحلويات الشرقية</h3>
                    <p>العالم الخاص بالحلويات الشرقية المتنوعة.</p>
                    <button class="btn">دخول التخصص</button>
                </div>
                <div class="card" onclick="switchView('western-view')">
                    <h3>🍰 الحلويات الغربية</h3>
                    <p>العالم الخاص بالحلويات الغربية والتقنيات العصرية.</p>
                    <button class="btn">دخول التخصص</button>
                </div>
            </div>
        </div>

        <!-- تفرعات المرأة الماكثة -->
        <div id="traditional-view" class="view-section">
            <button class="btn btn-back" onclick="switchView('homemaker-view')">⬅ رجوع إلى برنامج المرأة الماكثة</button>
            <h2>🍰 عالم الحلويات التقليدية</h2>
            <p>المحتويات، البطاقات التقنية الفارغة، والتقييمات الخاصة بهذا التخصص:</p>
            <ul>
                <li>دروس ومخططات التقليدي</li>
                <li>🛠️ البطاقات التقنية (فارغة بانتظار المحتوى المهني)</li>
                <li>📝 الامتحانات والتقييم البيداغوجي للتقليدي</li>
            </ul>
        </div>

        <div id="eastern-view" class="view-section">
            <button class="btn btn-back" onclick="switchView('homemaker-view')">⬅ رجوع إلى برنامج المرأة الماكثة</button>
            <h2>🧁 عالم الحلويات الشرقية</h2>
            <p>المحتويات، البطاقات التقنية الفارغة، والتقييمات الخاصة بهذا التخصص:</p>
            <ul>
                <li>دروس ومخططات الشرقي</li>
                <li>🛠️ البطاقات التقنية (فارغة بانتظار المحتوى المهني)</li>
                <li>📝 الامتحانات والتقييم البيداغوجي للشرقي</li>
            </ul>
        </div>

        <div id="western-view" class="view-section">
            <button class="btn btn-back" onclick="switchView('homemaker-view')">⬅ رجوع إلى برنامج المرأة الماكثة</button>
            <h2>🍰 عالم الحلويات الغربية</h2>
            <p>المحتويات، البطاقات التقنية الفارغة، والتقييمات الخاصة بهذا التخصص:</p>
            <ul>
                <li>دروس ومخططات الغربي</li>
                <li>🛠️ البطاقات التقنية (فارغة بانتظار المحتوى المهني)</li>
                <li>📝 الامتحانات والتقييم البيداغوجي للغربي</li>
            </ul>
            
            <div class="calculator-box">
                <h3>🧮 حاسبة المقادير الدقيقة للورشات</h3>
                <label for="flour-input">أدخل كمية الفرينة (بالغرام):</label>
                <input type="number" id="flour-input" value="1000" oninput="calculateRecipe()">
                <p id="calc-result">الزبدة المقترحة (50%): 500 غ | السكر (30%): 300 غ | البيض (20%): 200 غ</p>
            </div>
        </div>

    </div>

    <script>
        function switchView(viewId) {
            const sections = document.querySelectorAll('.view-section');
            sections.forEach(section => {
                section.classList.remove('active');
            });
            document.getElementById(viewId).classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function calculateRecipe() {
            const flour = document.getElementById('flour-input').value;
            const butter = flour * 0.5;
            const sugar = flour * 0.3;
            const eggs = flour * 0.2;
            document.getElementById('calc-result').innerText = 
                `الزبدة المقترحة (50%): ${butter} غ | السكر (30%): ${sugar} غ | البيض (20%): ${eggs} غ`;
        }
    </script>

</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)
