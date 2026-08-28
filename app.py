
<script src="https://cdn.tailwindcss.com"></script>
<style>
*{box-sizing:border-box}
body{
    font-family:'Tajawal','Segoe UI',system-ui,sans-serif;
    background:#faf8f5;
    color:#1f2937;
}
.shadow-soft{
    box-shadow:0 4px 20px rgba(0,0,0,.06)
}
.hover-lift{
    transition:all .3s ease
}
.hover-lift:hover{
    transform:translateY(-3px);
    box-shadow:0 8px 30px rgba(0,0,0,.1)
}
.transition-smooth{
    transition:all .3s ease
}
.watermark{
    opacity:.05;
    pointer-events:none;
    user-select:none
}
.footer-watermark{
    opacity:.15;
    font-size:.65rem;
    letter-spacing:1px
}
.badge{
    display:inline-block;
    font-size:.68rem;
    padding:.2rem .55rem;
    border-radius:999px;
    white-space:nowrap
}
.badge-reviewed{
    background:#d1fae5;
    color:#065f46
}
.badge-pending{
    background:#fef3c7;
    color:#92400e
}
.badge-draft{
    background:#e5e7eb;
    color:#4b5563
}
.badge-dev{
    background:#e0f2fe;
    color:#0369a1
}
.program-card{
    border:1px solid #e5e7eb;
    border-radius:16px;
    padding:1.5rem;
    background:#fff;
    cursor:pointer
}
.sub-program-card{
    border-right:4px solid #b8860b
}
.page-section{
    display:none
}
.page-section.active{
    display:block
}
.tech-sheet-card{
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:1rem;
    background:#fff;
    margin-bottom:.8rem
}
.tech-sheet-card h6{
    font-weight:700;
    color:#1f2937;
    margin-top:.9rem;
    margin-bottom:.35rem;
    border-bottom:1px solid #f3f4f6;
    padding-bottom:.25rem
}
.accordion-btn{
    background:#f9f7f4;
    border:1px solid #e5e7eb;
    border-radius:8px;
    padding:.7rem 1rem;
    width:100%;
    text-align:right;
    font-weight:600;
    display:flex;
    align-items:center;
    gap:.5rem;
    cursor:pointer
}
.accordion-content{
    padding:.8rem .5rem 1rem
}
.ingredient-list{
    display:flex;
    flex-wrap:wrap;
    gap:.5rem
}
.ingredient-item{
    background:#f9f7f4;
    padding:.3rem .65rem;
    border-radius:6px;
    border:1px solid #e5e7eb
}
.admin-panel{
    background:#f9f7f4;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:1rem;
    margin-top:1.5rem
}
.admin-panel input,
.admin-panel select,
.admin-panel textarea{
    width:100%;
    padding:.45rem .65rem;
    border:1px solid #d1d5db;
    border-radius:6px;
    background:#fff
}
.admin-panel label{
    font-weight:600;
    font-size:.85rem;
    margin-top:.3rem;
    display:block
}
.btn-admin{
    padding:.35rem .8rem;
    border-radius:6px;
    font-size:.8rem;
    border:none;
    cursor:pointer
}
.lesson-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
    gap:12px
}
.lesson-card{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:1rem
}
.lesson-number{
    width:34px;
    height:34px;
    border-radius:50%;
    background:#fef3c7;
    color:#92400e;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:bold;
    margin-bottom:8px
}
.small-note{
    font-size:.78rem;
    color:#6b7280
}
.scale-control{
    display:flex;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
    margin:8px 0
}
.scale-control label{
    font-weight:600;
    font-size:.9rem
}
.scale-control input{
    width:80px;
    padding:4px 8px;
    border:1px solid #d1d5db;
    border-radius:6px;
    text-align:center
}
@media print{
    .no-print{
        display:none!important
    }
    .page-section{
        display:block!important
    }
    body{
        background:#fff
    }
    .accordion-content{
        display:block!important
    }
}
</style>
</head>
<body>

<nav class="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50 no-print">
<div class="max-w-7xl mx-auto px-4">
<div class="flex justify-between items-center h-16">
<div class="flex items-center gap-2">
<span class="text-2xl">🍰</span>
<span class="font-bold text-lg">الشيف البيداغوجي</span>
<span class="text-xs text-gray-500 hidden sm:inline">| حورية فرحي</span>
</div>
<div class="flex items-center gap-3">
<button onclick="navigateTo('home')" class="text-sm text-gray-600 hover:text-amber-700">🏠 الرئيسية</button>
<button onclick="toggleAdmin()" class="text-sm text-gray-600 hover:text-amber-700">⚙️ إدارة</button>
</div>
</div>
</div>
</nav>

<header class="bg-gradient-to-l from-amber-50 to-white border-b border-amber-100 py-6 no-print relative">
<div class="max-w-7xl mx-auto px-4 text-center">
<h1 class="text-2xl sm:text-3xl font-bold">🍰 منصة <span class="text-amber-700">الشيف البيداغوجي</span></h1>
<p class="text-gray-600 mt-1 text-sm">منصة التكوين المهني في صناعة الحلويات وفق المقاربة بالكفاءات APC</p>
<div class="text-xs text-gray-500 mt-2">إعداد الأستاذة: <strong class="text-amber-800">حورية فرحي</strong> © 2026</div>
<div class="watermark text-4xl font-bold text-gray-300 absolute inset-0 flex items-center justify-center">حورية فرحي</div>
</div>
</header>

<main class="max-w-7xl mx-auto px-4 py-6">

<section id="page-home" class="page-section active">
<div class="flex flex-wrap items-center justify-between gap-4 mb-6">
<h2 class="text-2xl font-bold">📚 برامج التكوين المهني</h2>
<div class="flex gap-2">
<input id="globalSearch" type="text" placeholder="🔎 ابحث عن درس أو حلوى..." class="border rounded-lg px-3 py-1.5 w-64" oninput="performSearch(this.value)">
<button onclick="clearSearch()" class="text-xs text-gray-400">✕</button>
</div>
</div>
<div id="programList" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>
</section>

<section id="page-program" class="page-section">
<div class="flex items-center gap-3 mb-4 no-print">
<button onclick="navigateTo('home')" class="text-sm text-amber-700">← العودة إلى الرئيسية</button>
<span>|</span>
<span id="programBreadcrumb" class="text-sm text-gray-500">البرنامج</span>
</div>
<div id="subProgramsContainer" style="display:none">
<div class="bg-white rounded-xl shadow-soft p-6 mb-6 relative">
<div class="watermark absolute inset-0 flex items-center justify-center text-4xl font-bold">حورية فرحي</div>
<div class="relative">
<h3 id="parentProgramTitle" class="text-2xl font-bold">برنامج المرأة الماكثة بالبيت</h3>
<p class="text-gray-500 mt-1">اختر المسار الذي ترغب في الالتحاق به</p>
</div>
</div>
<div id="subProgramList" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>
</div>
<div id="programDetailContainer" style="display:none">
<div class="bg-white rounded-xl shadow-soft p-6 mb-8 relative">
<div class="watermark absolute inset-0 flex items-center justify-center text-4xl font-bold">حورية فرحي</div>
<div class="relative">
<div class="flex flex-wrap justify-between gap-4">
<div>
<h3 id="programTitle" class="text-2xl font-bold"></h3>
<p id="programDesc" class="text-gray-500 mt-1"></p>
</div>
<div class="flex gap-3">
<span id="programHours" class="bg-amber-100 text-amber-800 px-4 py-1 rounded-full text-sm"></span>
<span id="programType" class="bg-gray-100 text-gray-600 px-4 py-1 rounded-full text-sm"></span>
</div>
</div>
<div class="mt-4 grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm text-gray-600">
<div><b>المجال:</b> <span id="programField"></span></div>
<div><b>المكتسبات القبلية:</b> <span id="programPrereq"></span></div>
<div><b>الكفاءة البعدية:</b> <span id="programPostreq"></span></div>
<div><b>الحالة:</b> <span id="programStatus"></span></div>
</div>
<div class="text-xs text-gray-300 mt-3 border-t pt-2 text-center">إعداد الأستاذة: حورية فرحي © 2026</div>
</div>
</div>
<div class="bg-white rounded-xl shadow-soft p-6 mb-8">
<h4 class="font-bold mb-4">⏱️ مخطط الساعات</h4>
<div class="overflow-x-auto">
<table class="w-full text-sm">
<thead class="bg-gray-50"><tr><th class="p-2 border">المرحلة</th><th class="p-2 border">الساعات</th><th class="p-2 border">النشاط</th></tr></thead>
<tbody id="timeTableBody"></tbody>
</table>
</div>
<div class="text-xs text-gray-400 mt-2 text-center">مجموع الساعات: <span id="totalHoursDisplay"></span> ساعة</div>
</div>
<div id="competencyBox" class="bg-white rounded-xl shadow-soft p-6 mb-8"></div>
<div id="lessonPlanBox" class="bg-white rounded-xl shadow-soft p-6 mb-8"></div>
<div class="mb-8">
<div class="flex items-center justify-between mb-4">
<h4 class="font-bold">📚 الوحدات والدروس</h4>
<button onclick="addModule()" class="btn-admin bg-amber-600 text-white no-print">➕ إضافة وحدة</button>
</div>
<div id="modulesContainer"></div>
</div>
<div class="bg-white rounded-xl shadow-soft p-6 mb-8">
<h4 class="font-bold mb-3">🧼 النظافة والسلامة المهنية</h4>
<div class="grid sm:grid-cols-2 gap-3 text-sm text-gray-600">
<ul class="list-disc list-inside space-y-1"><li>غسل اليدين جيدًا قبل العمل.</li><li>تنظيف وتعقيم سطح العمل.</li><li>استعمال أدوات نظيفة.</li><li>ارتداء اللباس المهني.</li></ul>
<ul class="list-disc list-inside space-y-1"><li>الحذر عند التعامل مع الفرن.</li><li>الحذر عند التعامل مع الزيت الساخن.</li><li>الحذر عند التعامل مع العسيلة الساخنة.</li><li>احترام شروط حفظ المواد والمنتجات.</li></ul>
</div>
</div>
<div class="bg-white rounded-xl shadow-soft p-6 mb-8">
<h4 class="font-bold mb-3">⭐ معايير تقييم المنتوج النهائي</h4>
<div class="overflow-x-auto">
<table class="w-full text-sm">
<thead class="bg-gray-50"><tr><th class="p-2 border">المعيار</th><th class="p-2 border">مؤشر النجاح</th></tr></thead>
<tbody id="evalTableBody"></tbody>
</table>
</div>
</div>
<div class="grid sm:grid-cols-2 gap-6 mb-8">
<div class="bg-white rounded-xl shadow-soft p-6">
<h5 class="font-bold mb-2">📝 أسئلة نظرية</h5>
<ul id="theoryQuestions" class="text-sm text-gray-600 list-disc list-inside space-y-1"></ul>
</div>
<div class="bg-white rounded-xl shadow-soft p-6">
<h5 class="font-bold mb-2">👩‍🍳 وضعية تطبيقية</h5>
<p id="practicalSituation" class="text-sm text-gray-600 leading-7"></p>
</div>
</div>
<div id="integrationBox" class="bg-white rounded-xl shadow-soft p-6 mb-8"></div>
<div class="flex flex-wrap gap-4 justify-center no-print">
<button onclick="goBackFromProgram()" class="px-6 py-2 bg-gray-200 rounded-lg">← العودة</button>
<button onclick="window.print()" class="px-6 py-2 bg-amber-700 text-white rounded-lg">🖨️ طباعة البطاقة</button>
</div>
</div>
</section>

<section id="adminPanel" class="admin-panel hidden no-print">
<div class="flex items-center justify-between mb-4">
<h3 class="text-xl font-bold">🔐 إدارة المحتوى</h3>
<button onclick="toggleAdmin()">✕ إغلاق</button>
</div>
<p class="text-sm text-gray-500 mb-4">التعديلات تحفظ في متصفحك.</p>
<div id="adminContent"></div>
</section>

</main>

<footer class="bg-white border-t py-4 mt-6 no-print">
<div class="max-w-7xl mx-auto px-4 text-center">
<p class="text-sm text-gray-500">© 2026 الشيف البيداغوجي – التكوين المهني في الجزائر</p>
<p class="text-xs text-gray-400 mt-1">🛡️ من إعداد الأستاذة: <strong class="text-amber-700">حورية فرحي</strong></p>
<p class="footer-watermark mt-2">حورية فرحي | الشيف البيداغوجي © 2026</p>
</div>
</footer>

<script>
// ===== الوحدة الأولى: حلويات اللوز (تبقى كما هي) =====
const ALMOND_SHEETS = [
{id:'sheet_baklava',name:'البقلاوة الجزائرية التقليدية',objective:'أن يكون المتكوّن قادرًا على إعداد بقلاوة جزائرية تقليدية وفق التقنية المهنية.',prerequisites:'معرفة أنواع الطحين وتحضير العجائن الأساسية وتحضير العسيلة.',tools:'وعاء للعجن، صينية، فرشاة، سكين، مدلك.',ingredients:[['فرينة',4,'كيلات'],['سمن',1,'كيلة'],['ملح',1,'قرصة'],['ماء وماء زهر',1,'كيلة'],['لوز مرحي',3,'كيلات'],['سكر',0.5,'كيلة']],steps:['تحضير مكان العمل ووزن المواد.','تحضير العجينة.','ترك العجينة ترتاح.','فرد الرقائق.','ترتيب الطبقات والحشوة.','التقطيع.','الطهي.','التشريب بالعسيلة.'],cooking:'فرن متوسط الحرارة حسب التقنية المعتمدة.',commonMistakes:'سمن ساخن، عجينة قاسية، رقائق سميكة.',corrections:'استعمال السمن المناسب، ضبط الترطيب، فرد الرقائق جيدًا.',qualityCriteria:'طبقات رقيقة، لون ذهبي، حشوة متوازنة.',hygiene:'احترام النظافة والسلامة.',duration:'90 دقيقة',yield:'حسب حجم الصينية',storage:'تحفظ في وعاء مناسب حسب طبيعة المنتج.',serving:'تقدم في طبق مناسب.',evalQuestions:['ما أهمية راحة العجينة؟','ما دور السمن؟'],practicalActivity:'إنجاز بقلاوة كاملة.',status:'قيد التدقيق'},
{id:'sheet_kafta',name:'الكفتة الجزائرية',objective:'إعداد حلوة الكفتة بعجينة اللوز والحشو.',prerequisites:'معرفة عجينة اللوز والحشوات.',tools:'أوعية، أدوات تشكيل، صينية.',ingredients:[['لوز',3,'كيلات'],['سكر ناعم',2,'كيلتان'],['ماء زهر',3,'ملاعق'],['مكسرات',0.5,'كيلة']],steps:['تحضير عجينة اللوز.','تحضير الحشوة.','تشكيل الحشوة.','فرد العجينة.','غلق وتشكيل القطع.','التزيين والتشطيب.'],cooking:'لا تحتاج إلى فرن حسب الطريقة المعتمدة.',commonMistakes:'عجينة لينة أو تشقق السطح.',corrections:'ضبط القوام والتبريد عند الحاجة.',qualityCriteria:'نعومة العجينة وانتظام القطع.',hygiene:'النظافة واستعمال أدوات نظيفة.',duration:'60 دقيقة',yield:'حسب الحجم',storage:'حسب طبيعة الحشوة.',serving:'طبق تقديم مناسب.',evalQuestions:['ما شروط نجاح عجينة اللوز؟'],practicalActivity:'إنجاز الكفتة.',status:'قيد التدقيق'}
];

// ===== الوحدة الثانية: حلويات السميد (مضافة حديثاً) =====
const SEMOLINA_SHEETS = [
{id:'semolina_mbradja',name:'1. المبرجة',objective:'تحضير المبرجة التقليدية باستعمال السميد وحشوة التمر، مع التحكم في الترطيب والتشكيل والطهي.',prerequisites:'معرفة أنواع السميد، وزن المواد، مبادئ تحضير العجائن، واستعمال الطاجين أو المقلاة.',tools:'وعاء خلط، ميزان، غربال، مدلك، سكين، طاجين أو مقلاة مسطحة، أدوات القياس.',ingredients:[['سميد متوسط',3,'كيلات'],['سمن',0.5,'كيلة'],['زيت',0.5,'كيلة'],['ملح',1,'قرصة'],['ماء',1,'حسب الحاجة'],['تمر معجون',1,'حشوة'],['قرفة',1,'حسب الذوق'],['سمسم محمص',1,'حسب الاختيار']],steps:['تهيئة محطة العمل وتحضير الأدوات.','وزن السميد والمادة الدهنية.','وضع السميد في وعاء.','إضافة السمن والزيت وفرك السميد جيدًا.','إضافة الملح.','إضافة الماء تدريجيًا حتى تتجمع العجينة.','عدم الإفراط في العجن.','تحضير حشوة التمر وإضافة القرفة والسمسم حسب الوصفة.','تقسيم العجينة إلى جزأين.','فرد الطبقة الأولى.','وضع حشوة التمر وتوزيعها بالتساوي.','تغطية الحشوة بالطبقة الثانية.','تسوية السطح.','تقطيع المبرجة إلى مربعات أو معينات.','تسخين الطاجين أو المقلاة.','طهي المبرجة على نار معتدلة مع التقليب.','تركها تبرد قليلًا قبل التقديم.'],cooking:'تطهى على الطاجين أو المقلاة المسطحة على نار معتدلة. المدة التقريبية 15–20 دقيقة حسب السمك ودرجة الحرارة.',commonMistakes:'العجينة جافة، الحشوة تخرج، المبرجة تحترق من الخارج، أو تتفتت أثناء التقليب.',corrections:'إضافة الماء تدريجيًا عند الحاجة، إحكام غلق الطبقات، التحكم في حرارة الطاجين، وعدم قلب المنتج بعنف.',qualityCriteria:'لون ذهبي متجانس، طبقات متماسكة، حشوة موزعة بانتظام، قوام مناسب، وعدم وجود احتراق.',hygiene:'غسل اليدين، تنظيف سطح العمل، استعمال أدوات نظيفة، والحذر عند التعامل مع الطاجين الساخن.',duration:'60 دقيقة',yield:'حسب حجم القطع',storage:'تحفظ في علبة نظيفة ومحكمة الإغلاق، مع مراعاة طبيعة الحشوة ودرجة الحرارة.',serving:'تقدم دافئة أو بعد أن تبرد، وتقطع إلى أشكال منتظمة.',evalQuestions:['ما دور فرك السميد بالمادة الدهنية؟','لماذا يضاف الماء تدريجيًا؟','ما سبب خروج حشوة التمر أثناء الطهي؟','ما علامات نجاح المبرجة؟'],practicalActivity:'إنجاز مبرجة كاملة انطلاقًا من وزن المواد إلى التشكيل والطهي والتقديم.',status:'إعداد الأستاذة'},
{id:'semolina_makroud_oven',name:'2. مقروط الفرن',objective:'تحضير مقروط الفرن المحشو بالتمر وتشكيله وخبزه وفق المواصفات المهنية.',prerequisites:'معرفة السميد، المادة الدهنية، حشوة التمر، والتشكيل الأساسي للمقروط.',tools:'وعاء، ميزان، صينية، سكين أو أداة تقطيع، فرشاة، فرن.',ingredients:[['سميد متوسط',1,'كغ'],['مادة دهنية',1,'كأس'],['ماء زهر',1,'كأس حسب الوصفة'],['فرينة',1,'كمية حسب الوصفة المعتمدة'],['ملح',1,'قرصة'],['تمر معجون',1,'حشوة'],['سمسم',1,'حسب الاختيار'],['عسيلة',1,'للتشريب']],steps:['وزن جميع المواد.','تحضير السميد وإضافة المادة الدهنية.','فرك السميد جيدًا.','إضافة السائل تدريجيًا.','جمع العجينة دون الإفراط في العجن.','تحضير حشوة التمر.','تشكيل العجينة ووضع الحشوة.','إغلاق العجينة جيدًا.','تشكيل المقروط.','تقطيعه إلى معينات متساوية.','ترتيب القطع في الصينية.','الخبز في الفرن.','تحضير العسيلة.','تشريب المقروط حسب الوصفة.','التبريد والتقديم.'],cooking:'يخبز في فرن متوسط الحرارة، وتضبط المدة حسب حجم القطع وخصائص الفرن، مع مراقبة اللون والنضج.',commonMistakes:'المقروط قاسٍ، يتفتت، خروج الحشوة، عدم انتظام القطع، أو تحمير زائد.',corrections:'ضبط المادة الدهنية والترطيب، إحكام الغلق، توحيد حجم القطع، والتحكم في حرارة الفرن.',qualityCriteria:'قطع منتظمة، لون ذهبي، حشوة ثابتة، قوام مناسب، وتشريب متوازن.',hygiene:'النظافة الشخصية، نظافة الأدوات، وسلامة استعمال الفرن والعسيلة.',duration:'90 دقيقة',yield:'حسب حجم القطع والصينية',storage:'يحفظ في علبة مناسبة ومحكمة، وتراعى طبيعة التشريب والحشوة.',serving:'يقدم بعد استقرار التشريب وبشكل منتظم.',evalQuestions:['ما أهمية فرك السميد بالمادة الدهنية؟','لماذا يجب إحكام غلق الحشوة؟','ما علامات نضج المقروط؟'],practicalActivity:'تحضير كمية من مقروط الفرن وتشكيلها وخبزها وتشريبها.',status:'إعداد الأستاذة'},
{id:'semolina_makroud_fried',name:'3. المقروط المقلي',objective:'تحضير المقروط المقلي وقليه بطريقة صحيحة وتشريبه بالعسيلة.',prerequisites:'معرفة عجينة المقروط، الحشو، التشكيل، وقواعد السلامة عند استعمال الزيت الساخن.',tools:'وعاء، ميزان، سكين، مقلاة عميقة، ملقط، مصفاة، أوعية للعسيلة.',ingredients:[['سميد متوسط',3,'أكواب'],['فرينة',1,'كوب'],['سمن وزيت',1,'كوب تقريبًا'],['ماء',1,'حسب الحاجة'],['ماء زهر',1,'حسب الحاجة'],['تمر معجون',1,'حشوة'],['قرفة',1,'حسب الذوق'],['زيت للقلي',1,'كمية كافية'],['عسيلة',1,'للتشريب']],steps:['تحضير محطة العمل.','وزن المواد.','تحضير عجينة السميد.','ترطيب العجينة تدريجيًا.','تحضير حشوة التمر.','تشكيل المقروط.','تقطيعه إلى معينات.','تجهيز الزيت.','قلي القطع على حرارة مناسبة.','تقليب القطع حتى الحصول على لون ذهبي.','تصفية المقروط.','تشريبه بالعسيلة.','تركه يستقر ثم تقديمه.'],cooking:'القلي في زيت ساخن بدرجة مناسبة مع تجنب الحرارة المرتفعة جدًا. المدة تختلف حسب الحجم ودرجة حرارة الزيت.',commonMistakes:'امتصاص كمية كبيرة من الزيت، تفكك القطع، احتراق السطح، أو بقاء الداخل غير ناضج.',corrections:'ضبط حرارة الزيت، عدم ازدحام المقلاة، إحكام التشكيل، وعدم القلي على حرارة مرتفعة جدًا.',qualityCriteria:'لون ذهبي، قوام مناسب، عدم وجود زيت زائد، حشوة ثابتة وتشريب متوازن.',hygiene:'الحذر الشديد من الزيت الساخن، استعمال أدوات مناسبة، وعدم ترك المقلاة دون مراقبة.',duration:'60–75 دقيقة',yield:'حسب كمية العجين',storage:'تحفظ في علبة محكمة بعد أن تبرد، مع مراعاة التشريب.',serving:'يقدم بعد تصفية العسيلة الزائدة.',evalQuestions:['ما سبب امتصاص المقروط للزيت؟','لماذا لا يجب أن تكون حرارة الزيت مرتفعة جدًا؟','ما علامات نجاح القلي؟'],practicalActivity:'إنجاز المقروط المقلي من التحضير إلى القلي والتشريب.',status:'إعداد الأستاذة'},
{id:'semolina_basbousa',name:'4. البسبوسة',objective:'تحضير البسبوسة بالسميد وخبزها وتشريبها بالعسيلة مع التحكم في القوام.',prerequisites:'معرفة السميد، المواد السائلة، الخميرة الكيميائية، أساسيات الخَبز وتحضير العسيلة.',tools:'وعاء، خفاقة أو ملعقة، ميزان، صينية، فرن، سكين، أدوات التشريب.',ingredients:[['بيض',4,'حبات'],['سكر',1,'كأس'],['حليب',1,'كأس'],['سميد متوسط',2,'كأس'],['فرينة',1,'ملعقة'],['خميرة كيميائية',2,'أكياس حسب حجم الكيس'],['فانيليا',1,'حسب الوصفة'],['عسيلة',1,'للتشريب']],steps:['تحضير محطة العمل.','وزن جميع المواد.','خلط البيض والسكر.','إضافة الحليب والفانيليا.','إضافة السميد والفرينة.','إضافة الخميرة الكيميائية.','خلط المكونات حتى التجانس دون إفراط.','تحضير الصينية.','صب الخليط وتسوية السطح.','تزيين السطح حسب الوصفة.','خبز البسبوسة.','تحضير العسيلة.','تشريب المنتج بالطريقة المناسبة.','تركه يستقر ثم تقطيعه.'],cooking:'تخبز في فرن متوسط الحرارة، وتراقب حتى الحصول على لون ذهبي ونضج داخلي كامل.',commonMistakes:'الجفاف، عدم النضج، تشريب غير متوازن، أو انهيار القوام.',corrections:'ضبط نسبة السائل، عدم الإفراط في الخَبز، توزيع العسيلة بالتساوي.',qualityCriteria:'لون ذهبي، قوام طري ومتجانس، تشريب متوازن، وقطع منتظمة.',hygiene:'نظافة الأدوات، سلامة استعمال الفرن، وحفظ البيض والحليب بطريقة سليمة.',duration:'75 دقيقة',yield:'حسب حجم الصينية',storage:'تحفظ حسب تركيب الوصفة ودرجة رطوبتها، وتراعى شروط الحفظ المناسبة.',serving:'تقدم مقطعة إلى قطع متساوية.',evalQuestions:['ما دور السميد في البسبوسة؟','ما أهمية ضبط العسيلة؟','كيف نعرف أن البسبوسة ناضجة؟'],practicalActivity:'تحضير بسبوسة كاملة وخبزها وتشريبها وتقديمها.',status:'إعداد الأستاذة'},
{id:'semolina_harissa',name:'5. هريسة السميد',objective:'تحضير هريسة السميد وضبط قوامها وخَبزها وتشريبها.',prerequisites:'معرفة السميد، السكر، المادة الدهنية، اللبن أو الياغورت، والعسيلة.',tools:'وعاء، ميزان، ملعقة، صينية، فرن، أدوات التشريب.',ingredients:[['سميد خشن',2,'كوب'],['سكر',1,'كوب'],['لبن أو ياغورت',1,'كوب'],['سمن مذاب',0.5,'كوب'],['خميرة كيميائية',1,'كمية مناسبة'],['فانيليا',1,'حسب الوصفة'],['لوز',1,'للتزيين'],['عسيلة',1,'للتشريب']],steps:['وزن المواد.','خلط السميد والسكر.','إضافة السمن.','إضافة اللبن أو الياغورت.','إضافة الخميرة والفانيليا.','خلط المكونات حتى التجانس.','ترك الخليط يستقر حسب الوصفة.','وضعه في الصينية.','تسوية السطح.','التزيين باللوز.','الخبز.','تحضير العسيلة.','تشريب الهريسة.','التبريد والتقطيع.'],cooking:'تخبز في فرن متوسط الحرارة حتى النضج والحصول على لون مناسب.',commonMistakes:'الخليط كثيف جدًا، المنتج جاف، السطح غير متجانس، أو التشريب غير متوازن.',corrections:'ضبط كمية السائل، مراقبة الخَبز، تسوية السطح جيدًا، وتوزيع العسيلة بالتساوي.',qualityCriteria:'قوام طري ومتجانس، لون مناسب، قطع منتظمة وتشريب متوازن.',hygiene:'نظافة الأدوات، المحافظة على المواد اللبنية، وسلامة استعمال الفرن.',duration:'70 دقيقة',yield:'حسب حجم الصينية',storage:'يحفظ في وعاء مناسب، وتراعى طبيعة الرطوبة والحشوة.',serving:'يقدم في قطع منتظمة.',evalQuestions:['ما دور اللبن في هريسة السميد؟','ما أسباب جفاف الهريسة؟','كيف يتم توزيع العسيلة؟'],practicalActivity:'إنجاز هريسة السميد وفق بطاقة العمل.',status:'إعداد الأستاذة'},
{id:'semolina_maamoul',name:'6. المعمول',objective:'إعداد عجينة المعمول المصنوعة من السميد، حشوها وتشكيلها بالقوالب وخَبزها.',prerequisites:'معرفة عجائن السميد، الحشوات، التشكيل بالقوالب، واستعمال الفرن.',tools:'وعاء، ميزان، قوالب معمول، صواني، فرن، أدوات تشكيل.',ingredients:[['سميد خشن',3,'أكواب'],['سميد ناعم',2,'كوب'],['دقيق',1,'كوب'],['زبدة أو سمن',1.5,'كوب'],['حليب دافئ',1,'كوب حسب الحاجة'],['ماء زهر',1,'حسب الوصفة'],['تمر أو مكسرات',1,'حشوة'],['سكر',1,'حسب الحشوة']],steps:['تحضير مكان العمل.','وزن المواد.','خلط السميد والدقيق.','إضافة المادة الدهنية وفرك الخليط.','إضافة الحليب وماء الزهر تدريجيًا.','جمع العجينة.','تركها ترتاح حسب الوصفة.','تحضير الحشوة.','تقسيم العجين إلى كرات.','حشو الكرات.','إغلاق العجين.','وضع القطعة في قالب المعمول.','الضغط والتشكيل.','إخراج القطعة من القالب.','ترتيب القطع في الصينية.','الخبز.','التبريد والتقديم.'],cooking:'يخبز في فرن متوسط الحرارة حتى ينضج ويحصل على اللون المناسب حسب نوع المعمول.',commonMistakes:'تفتت العجينة، خروج الحشوة، فقدان النقوش، أو احتراق السطح.',corrections:'ضبط المادة الدهنية والترطيب، إحكام الغلق، استعمال القالب بطريقة صحيحة، والتحكم في الفرن.',qualityCriteria:'نقوش واضحة، قطع منتظمة، حشوة ثابتة، قوام مناسب ونضج جيد.',hygiene:'النظافة الشخصية ونظافة القوالب والأدوات وسلامة استعمال الفرن.',duration:'75 دقيقة',yield:'حسب حجم القالب',storage:'يحفظ في علبة محكمة ونظيفة حسب طبيعة الحشوة.',serving:'يقدم بعد أن يبرد تمامًا.',evalQuestions:['ما وظيفة المادة الدهنية في عجينة المعمول؟','ما سبب فقدان النقوش؟','كيف نحافظ على الحشوة داخل القطعة؟'],practicalActivity:'إعداد معمول محشو وتشكيله بالقالب وخَبزه.',status:'إعداد الأستاذة',note:'المعمول من حلويات المشرق العربي وليس من التراث الجزائري الأصلي، ويُدرج هنا كتطبيق تقني على عجائن السميد والحشو والتشكيل.'},
{id:'semolina_tamina',name:'7. الطمينة',objective:'تحضير الطمينة باستعمال السميد المحمص والمادة الدهنية ومادة التحلية مع التحكم في القوام.',prerequisites:'معرفة السميد، التحميص، المادة الدهنية، وطرق التحكم في الحرارة.',tools:'مقلاة أو طاجين، ملعقة خشبية، وعاء، ميزان، طبق تقديم.',ingredients:[['سميد',1,'كغ'],['زبدة أو سمن',250,'غ'],['عسل أو سكر',250,'غ حسب الوصفة'],['قرفة',1,'كمية مناسبة'],['مكسرات',1,'للتزيين']],steps:['وزن السميد.','تسخين المقلاة أو الطاجين.','تحميص السميد على نار هادئة.','التحريك المستمر.','مراقبة اللون والرائحة.','إضافة المادة الدهنية.','خلط السميد حتى يتشرب المادة الدهنية.','إضافة مادة التحلية تدريجيًا.','ضبط القوام.','وضع الطمينة في طبق التقديم.','تسوية السطح.','التزيين بالقرفة والمكسرات.'],cooking:'لا تحتاج إلى خبز في الفرن؛ تعتمد أساسًا على تحميص السميد على نار هادئة.',commonMistakes:'احتراق السميد، قوام دهني جدًا، جفاف الطمينة، أو طعم مر.',corrections:'خفض الحرارة، التحريك المستمر، ضبط المادة الدهنية والتحلية، وعدم الإفراط في التحميص.',qualityCriteria:'لون متجانس، رائحة سميد محمص جيدة، قوام متماسك وطري، دون طعم احتراق.',hygiene:'نظافة الأدوات والحذر عند التعامل مع المقلاة الساخنة.',duration:'45–60 دقيقة',yield:'حسب كمية السميد',storage:'تحفظ في وعاء نظيف ومناسب مع مراعاة طبيعة المادة الدهنية.',serving:'تقدم في طبق وتزين بالقرفة والمكسرات حسب الطريقة.',evalQuestions:['لماذا يجب تحميص السميد على نار هادئة؟','ما سبب الطعم المر؟','ما علامات نجاح الطمينة؟'],practicalActivity:'تحضير طمينة وضبط لونها وقوامها وتزيينها.',status:'إعداد الأستاذة'},
{id:'semolina_rafis_constantine',name:'8. الرفيس القسنطيني',objective:'تحضير الرفيس القسنطيني بالاعتماد على السميد المحمص والمادة الدهنية والتحلية، مع التحكم في اللون والقوام.',prerequisites:'معرفة السميد والتحميص والتحكم في الحرارة والمادة الدهنية.',tools:'طاجين أو مقلاة، ملعقة خشبية، وعاء، ميزان، طبق تقديم.',ingredients:[['سميد متوسط',1,'كغ'],['زبدة أو سمن',250,'غ'],['عسل أو مادة تحلية',250,'غ حسب الوصفة'],['قرفة',1,'ملعقة صغيرة'],['قرنفل',1,'كمية قليلة حسب الوصفة'],['لوز أو مكسرات',1,'للتزيين'],['تمر',1,'حسب طريقة التقديم']],steps:['تهيئة مكان العمل.','وزن السميد.','تحميص السميد على نار هادئة.','التحريك المستمر لمنع الاحتراق.','مراقبة اللون والرائحة.','إضافة المادة الدهنية.','خلط السميد جيدًا.','إضافة مادة التحلية تدريجيًا.','إضافة القرفة أو القرنفل حسب الوصفة.','ضبط القوام.','وضع الرفيس في طبق التقديم.','التزيين بالمكسرات أو التمر حسب الطريقة.'],cooking:'لا يعتمد على الخَبز في الفرن؛ تتم العملية الأساسية بتحميص السميد والتحكم في الخلط والقوام.',commonMistakes:'احتراق السميد، طعم مر، قوام جاف أو دهني جدًا، وعدم تجانس الخليط.',corrections:'التحميص على نار هادئة، التحريك المستمر، وضبط المادة الدهنية والتحلية تدريجيًا.',qualityCriteria:'لون متجانس، نكهة جيدة، قوام مناسب، وعدم وجود طعم احتراق.',hygiene:'تنظيف الأدوات والحذر من الحرارة أثناء التحميص.',duration:'45–60 دقيقة',yield:'حسب الكمية المحضرة',storage:'يحفظ في وعاء نظيف ومحكم، مع مراعاة طبيعة المادة الدهنية والمواد المضافة.',serving:'يقدم في طبق مناسب ويزين حسب الطريقة التقليدية المعتمدة.',evalQuestions:['لماذا يحمر السميد على نار هادئة؟','ما سبب الطعم المر؟','ما أهمية إضافة المادة الدهنية تدريجيًا؟'],practicalActivity:'تحضير الرفيس القسنطيني وضبط التحميص والقوام والتقديم.',status:'إعداد الأستاذة',note:'توجد اختلافات جهوية في تفاصيل تحضير الرفيس القسنطيني؛ تعتمد البطاقة التقنية النهائية على الوصفة المحلية المعتمدة في التكوين.'},
{id:'semolina_syrup',name:'درس تقني مشترك: تحضير العسيلة (القطر)',objective:'تحضير العسيلة وضبط تركيزها وقوامها واستعمالها بالطريقة المناسبة في الحلويات المشربة.',prerequisites:'معرفة السكر والماء، استعمال القدر والحرارة، وقواعد السلامة.',tools:'قدر، ميزان، ملعقة، مغرفة، قارورة أو وعاء نظيف.',ingredients:[['سكر',2,'كيلات'],['ماء',1,'كيلة'],['عصير الليمون',1,'كمية قليلة'],['ماء الزهر',1,'حسب النكهة'],['ماء الورد',1,'حسب النكهة'],['قرفة أو قرنفل',1,'حسب الاختيار'],['قشر البرتقال',1,'حسب الاختيار'],['عسل',1,'حسب النوع']],steps:['وزن السكر وقياس الماء.','وضع الماء والسكر في القدر.','إذابة السكر.','الوصول إلى الغليان.','إضافة الليمون حسب الوصفة.','التحكم في مدة الغلي والقوام.','إضافة ماء الزهر أو ماء الورد في المرحلة المناسبة.','إزالة التوابل أو قشر البرتقال عند الوصول إلى النكهة المطلوبة.','رفع العسيلة عن النار.','استعمالها حسب نوع الحلوى.'],cooking:'تطبخ على نار مناسبة مع مراقبة التركيز والقوام، وتختلف درجة التركيز المطلوبة حسب نوع الحلوى.',commonMistakes:'العسيلة خفيفة جدًا، كثيفة جدًا، متبلورة، داكنة، أو ذات نكهة قوية.',corrections:'ضبط مدة الغلي ونسبة الماء إلى السكر، التحكم في الحرارة، وإضافة المنكهات بكميات مناسبة.',qualityCriteria:'قوام مناسب، لون جيد، نكهة متوازنة، عدم وجود بلورات سكر، وعدم وجود طعم احتراق.',hygiene:'استعمال قدر وأدوات نظيفة، والحذر من العسيلة الساخنة لأنها قد تسبب حروقًا خطيرة.',duration:'30–45 دقيقة حسب الكمية والقوام المطلوب',yield:'حسب كمية السكر والماء',storage:'تبرد ثم تحفظ في وعاء نظيف ومحكم، وتحدد مدة الحفظ وفق التركيبة وشروط التخزين.',serving:'تستعمل في التشريب حسب نوع الحلوى.',evalQuestions:['ما دور الليمون في العسيلة؟','ما أسباب تبلور العسيلة؟','كيف نعالج العسيلة الخفيفة؟','متى يضاف ماء الزهر؟'],practicalActivity:'تحضير عسيلة أساسية ثم استعمالها في تشريب أحد منتجات الوحدة.',status:'إعداد الأستاذة'}
];

// ===== هيكل البرامج (يتضمن MQ1 و MQ2) =====
const DEFAULT_PROGRAM_DATA = {
woman_main:{id:'woman_main',title:'برنامج المرأة الماكثة بالبيت',desc:'برنامج شامل لتكوين المرأة الماكثة بالبيت في صناعة الحلويات.',field:'صناعة الحلويات التقليدية والشرقية والغربية',hours:'قيد التدقيق',type:'كفاءة مهنية',prereq:'قيد التدقيق',postreq:'قيد التدقيق',status:'قيد التدقيق',parent:true,subPrograms:['traditional_pastry','oriental_pastry','western_pastry']},
apprenticeship:{id:'apprenticeship',title:'برنامج التمهين',desc:'برنامج التكوين المهني عن طريق التمهين.',field:'التكوين المهني عن طريق التمهين',hours:'قيد التدقيق',type:'كفاءة مهنية',prereq:'قيد التدقيق',postreq:'قيد التدقيق',status:'قيد التطوير',timeDistribution:[],modules:[],evaluationCriteria:[],theoryQuestions:[],_pending:true,parent:false},
fulltime:{id:'fulltime',title:'برنامج التكوين الحضوري',desc:'برنامج التكوين المهني الحضوري في صناعة الحلويات.',field:'التكوين المهني الحضوري',hours:'قيد التدقيق',type:'كفاءة مهنية',prereq:'قيد التدقيق',postreq:'قيد التدقيق',status:'قيد التطوير',timeDistribution:[],modules:[],evaluationCriteria:[],theoryQuestions:[],_pending:true,parent:false},
traditional_pastry:{id:'traditional_pastry',title:'برنامج الحلويات التقليدية',desc:'برنامج مهني متخصص في صناعة الحلويات التقليدية وفق المقاربة بالكفاءات APC.',field:'صناعة الحلويات التقليدية الجزائرية',hours:138,type:'كفاءة مهنية',prereq:'المعارف الأساسية في النظافة والسلامة ووزن المواد واستعمال الأدوات.',postreq:'ينجز المتكوّن مجموعة متنوعة من الحلويات التقليدية المصنوعة من اللوز والسميد وفق المواصفات المهنية، مع احترام الجودة والنظافة والسلامة.',status:'إعداد الأستاذة',timeDistribution:[['MQ1 – حلويات اللوز','84 ساعة','تقنيات عجائن اللوز والتشكيل والتشطيب'],['MQ2 – حلويات السميد','54 ساعة','الوحدة الثانية: الحلويات المصنوعة من السميد']],modules:[{id:'module_mq1',title:'MQ1 – إعداد حلويات اللوز',desc:'الوحدة الأولى: إعداد الحلويات التقليدية المصنوعة من اللوز.',status:'قيد التدقيق',sheets:ALMOND_SHEETS},{id:'module_mq2',title:'MQ2 – الحلويات المصنوعة من السميد',desc:'الوحدة الثانية كاملة: الحلويات المصنوعة من السميد وفق المقاربة بالكفاءات APC.',status:'إعداد الأستاذة',sheets:SEMOLINA_SHEETS},{id:'module_syrup',title:'تقنية مشتركة – العسيلة والقطر',desc:'درس تقني داعم يستعمل في المنتجات المشربة داخل الوحدة.',status:'إعداد الأستاذة',sheets:[SEMOLINA_SHEETS[SEMOLINA_SHEETS.length-1]]}],competency:{title:'الكفاءة الختامية للوحدة الثانية',text:'ينجز المتكوّن مجموعة متنوعة من الحلويات المصنوعة من السميد، باستعمال المواد الأولية والتقنيات المناسبة، مع التحكم في العجن والترطيب والتحميص والتشكيل والخَبز والقلي والتشريب والتقديم، واحترام معايير الجودة والنظافة والسلامة المهنية.'},lessonPlan:[['1','مدخل إلى الحلويات المصنوعة من السميد','2','نظري','التعرف على أنواع السميد وخصائصه واستعمالاته.'],['2','تحضير العسيلة والقطر','4','نظري + تطبيقي','تحضير العسيلة وضبط القوام واستعمالها.'],['3','المبرجة','6','نظري + تطبيقي','تحضير المبرجة وحشوها وتشكيلها وطهيها.'],['4','مقروط الفرن','6','نظري + تطبيقي','تحضير المقروط وتشكيله وخبزه وتشريبه.'],['5','المقروط المقلي','6','نظري + تطبيقي','تحضير المقروط وقليه وتشريبه.'],['6','البسبوسة','6','نظري + تطبيقي','تحضير البسبوسة وخَبزها وتشريبها.'],['7','هريسة السميد','6','نظري + تطبيقي','تحضير الهريسة وضبط القوام والطهي والتشريب.'],['8','المعمول','6','نظري + تطبيقي','تحضير عجينة السميد والحشو والتشكيل بالقالب.'],['9','الطمينة','6','نظري + تطبيقي','تحميص السميد وتحضير الطمينة وضبط القوام.'],['10','الرفيس القسنطيني','6','نظري + تطبيقي','تحميص السميد وتحضير الرفيس وتقديمه.'],['11','المعالجة والتقييم النهائي','4','تقويم + إدماج','معالجة الأخطاء وإنجاز وضعية إدماجية وتقييم الكفاءة.']],evaluationCriteria:[['احترام الوصفة','احترام المواد والكميات والمراحل التقنية.'],['تنظيم العمل','ترتيب محطة العمل واستغلال الزمن.'],['اختيار المواد','اختيار السميد والمواد المرافقة المناسبة.'],['الترطيب والعجن','التحكم في القوام وعدم الإفراط في العجن.'],['التشكيل','انتظام القطع ودقة الأشكال.'],['التحميص','التحكم في اللون وعدم الاحتراق.'],['الطهي','التحكم في الحرارة والنضج.'],['القلي','التحكم في حرارة الزيت وسلامة العمل.'],['التشريب','توزيع العسيلة بالقوام والكمية المناسبين.'],['جودة المنتج','لون وقوام ومذاق ورائحة مناسبة.'],['النظافة والسلامة','احترام قواعد النظافة والسلامة المهنية.'],['التقديم','تنظيم المنتج وتقديمه بصورة مهنية.']],theoryQuestions:['ما أنواع السميد المستعملة في صناعة الحلويات؟','ما أهمية وزن المواد الأولية بدقة؟','ما دور المادة الدهنية في عجائن السميد؟','ما أسباب جفاف عجينة السميد؟','ما أسباب تفتت المقروط؟','ما أسباب امتصاص المقروط المقلي للزيت؟','ما علامات نجاح العسيلة؟','ما سبب احتراق السميد أثناء التحميص؟','ما الفرق بين الخَبز والقلي والتحميص في تحضير منتجات الوحدة؟','ما قواعد النظافة والسلامة عند تحضير الحلويات المصنوعة من السميد؟'],practicalSituation:'يُطلب من المتكوّن إعداد منتج من منتجات الوحدة الثانية وفق بطاقة تقنية محددة، ابتداءً من تنظيم محطة العمل ووزن المواد، مرورًا بالتحضير والتشكيل والطهي أو التحميص والتشريب عند الحاجة، وانتهاءً بالتقديم وتنظيف مكان العمل.',integration:{title:'الوضعية الإدماجية النهائية',text:'يقدم الأستاذ وضعية مهنية تحاكي طلبية حقيقية: إعداد تشكيلة من الحلويات المصنوعة من السميد لمناسبة تقليدية. يختار المتكوّن الوصفة المناسبة، يحدد المواد، ينظم محطة العمل، ينفذ مراحل التحضير، يتحكم في الطهي أو التحميص أو القلي، يستعمل العسيلة عند الحاجة، ثم يقدم المنتجات ويبرر اختياراته التقنية.'}},
oriental_pastry:{id:'oriental_pastry',title:'برنامج الحلويات الشرقية',desc:'قيد التطوير – سيتم الإعلان عن تفاصيله لاحقًا.',field:'صناعة الحلويات الشرقية',hours:'قيد التدقيق',type:'كفاءة مهنية',prereq:'قيد التدقيق',postreq:'قيد التدقيق',status:'قيد التطوير',timeDistribution:[],modules:[],evaluationCriteria:[],theoryQuestions:[],_pending:true,parent:false},
western_pastry:{id:'western_pastry',title:'برنامج الحلويات الغربية',desc:'قيد التطوير – سيتم الإعلان عن تفاصيله لاحقًا.',field:'صناعة الحلويات الغربية',hours:'قيد التدقيق',type:'كفاءة مهنية',prereq:'قيد التدقيق',postreq:'قيد التدقيق',status:'قيد التطوير',timeDistribution:[],modules:[],evaluationCriteria:[],theoryQuestions:[],_pending:true,parent:false}
};

let programData={};
let currentParent=null;
let currentProgramId=null;

function cloneDefaults(){return JSON.parse(JSON.stringify(DEFAULT_PROGRAM_DATA));}
function saveData(){localStorage.setItem('chef_pedagogique_data',JSON.stringify(programData));}
function loadData(){
try{const saved=localStorage.getItem('chef_pedagogique_data');programData=saved?JSON.parse(saved):cloneDefaults();}catch(e){programData=cloneDefaults();}
saveData();
}
loadData();

function badge(status){let cls='badge badge-pending';if(status==='تمت المراجعة')cls='badge badge-reviewed';if(status==='إعداد الأستاذة')cls='badge badge-draft';if(status==='قيد التطوير')cls='badge badge-dev';return `<span class="${cls}">${status||'قيد التدقيق'}</span>`;}
function esc(v){return String(v??'').replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}

function navigateTo(page){
document.querySelectorAll('.page-section').forEach(x=>x.classList.remove('active'));
if(page==='home'){
document.getElementById('page-home').classList.add('active');
document.getElementById('page-program').classList.remove('active');
document.getElementById('subProgramsContainer').style.display='none';
document.getElementById('programDetailContainer').style.display='none';
renderPrograms();
}
}

function renderPrograms(){
const c=document.getElementById('programList');
c.innerHTML='';
Object.entries(programData).filter(([k,p])=>p.parent===true||k==='apprenticeship'||k==='fulltime').sort((a,b)=>a[0]==='woman_main'?-1:b[0]==='woman_main'?1:0).forEach(([k,p])=>{
const pending=p._pending===true;
const d=document.createElement('div');
d.className='program-card hover-lift transition-smooth';
d.onclick=()=>{if(p.parent)selectParentProgram(k);else alert('هذا البرنامج قيد التطوير، وسيتم الإعلان عن تفاصيله عند اكتماله.');};
d.innerHTML=`<div class="flex justify-between gap-3"><div><div class="text-2xl">${p.parent?'📂':'🍰'}</div><h3 class="font-bold text-lg mt-1">${p.title}</h3><p class="text-sm text-gray-500 mt-1">${p.desc}</p></div><span class="bg-amber-100 text-amber-800 px-3 py-1 rounded-full text-xs">${pending?'⏳ قيد التطوير':(p.hours||'')}</span></div><div class="mt-2">${badge(p.status)}</div>`;
c.appendChild(d);
});
}

function selectParentProgram(id){
const p=programData[id];if(!p)return;
currentParent=id;
document.getElementById('page-home').classList.remove('active');
document.getElementById('page-program').classList.add('active');
document.getElementById('programBreadcrumb').textContent=p.title;
document.getElementById('subProgramsContainer').style.display='block';
document.getElementById('programDetailContainer').style.display='none';
document.getElementById('parentProgramTitle').textContent=p.title;
renderSubPrograms(p);
}

function renderSubPrograms(p){
const c=document.getElementById('subProgramList');
c.innerHTML='';
p.subPrograms.forEach(id=>{
const s=programData[id];if(!s)return;
const pending=s._pending===true;
const d=document.createElement('div');
d.className='program-card hover-lift transition-smooth sub-program-card';
d.onclick=()=>{if(pending)alert('هذا البرنامج قيد التطوير.');else selectSubProgram(id);};
d.innerHTML=`<div class="flex justify-between"><div><div class="text-2xl">${pending?'🔜':'🍰'}</div><h4 class="font-bold">${s.title}</h4><p class="text-sm text-gray-500">${s.desc}</p></div><span class="bg-amber-100 text-amber-800 px-2 py-1 rounded-full text-xs">${pending?'قيد التطوير':(s.hours+' ساعة')}</span></div><div class="mt-2">${badge(s.status)}</div>`;
c.appendChild(d);
});
}

function selectSubProgram(id){
const p=programData[id];if(!p)return;
currentProgramId=id;
document.getElementById('subProgramsContainer').style.display='none';
document.getElementById('programDetailContainer').style.display='block';
document.getElementById('programBreadcrumb').textContent=p.title;
document.getElementById('programTitle').textContent=p.title;
document.getElementById('programDesc').textContent=p.desc;
document.getElementById('programHours').textContent=(p.hours||'قيد التدقيق')+' ساعة';
document.getElementById('programType').textContent=p.type;
document.getElementById('programField').textContent=p.field;
document.getElementById('programPrereq').textContent=p.prereq;
document.getElementById('programPostreq').textContent=p.postreq;
document.getElementById('programStatus').innerHTML=badge(p.status);
const tb=document.getElementById('timeTableBody');tb.innerHTML='';let total=0;(p.timeDistribution||[]).forEach(r=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="p-2 border">${r[0]}</td><td class="p-2 border">${r[1]}</td><td class="p-2 border">${r[2]||''}</td>`;tb.appendChild(tr);const num=parseInt(String(r[1]).replace(/[^\d]/g,''))||0;total+=num;});document.getElementById('totalHoursDisplay').textContent=total;
renderCompetency(p);renderLessonPlan(p);renderModules(p);
const eb=document.getElementById('evalTableBody');eb.innerHTML='';(p.evaluationCriteria||[]).forEach(r=>{const tr=document.createElement('tr');tr.innerHTML=`<td class="p-2 border font-medium">${r[0]}</td><td class="p-2 border">${r[1]}</td>`;eb.appendChild(tr);});
const q=document.getElementById('theoryQuestions');q.innerHTML='';(p.theoryQuestions||[]).forEach(x=>q.innerHTML+=`<li>${x}</li>`);
document.getElementById('practicalSituation').textContent=p.practicalSituation||'';
const ib=document.getElementById('integrationBox');if(p.integration){ib.innerHTML=`<h4 class="font-bold mb-3">🏆 ${p.integration.title}</h4><p class="text-sm text-gray-600 leading-8">${p.integration.text}</p>`;}else ib.innerHTML='';
}

function goBackFromProgram(){
if(currentParent){document.getElementById('programDetailContainer').style.display='none';document.getElementById('subProgramsContainer').style.display='block';document.getElementById('programBreadcrumb').textContent=programData[currentParent].title;renderSubPrograms(programData[currentParent]);}else navigateTo('home');
}

function renderCompetency(p){const box=document.getElementById('competencyBox');if(!p.competency){box.innerHTML='';return;}box.innerHTML=`<h4 class="font-bold mb-3">🎯 ${p.competency.title}</h4><p class="text-sm text-gray-600 leading-8">${p.competency.text}</p>`;}
function renderLessonPlan(p){const box=document.getElementById('lessonPlanBox');if(!p.lessonPlan){box.innerHTML='';return;}let html=`<h4 class="font-bold mb-4">📋 مخطط الدروس وتقسيم الساعات</h4><div class="overflow-x-auto"><table class="w-full text-sm"><thead class="bg-gray-50"><tr><th class="p-2 border">الدرس</th><th class="p-2 border">العنوان</th><th class="p-2 border">الساعات</th><th class="p-2 border">النمط</th><th class="p-2 border">الكفاءة/النشاط</th></tr></thead><tbody>`;p.lessonPlan.forEach(r=>{html+=`<tr><td class="p-2 border text-center">${r[0]}</td><td class="p-2 border font-medium">${r[1]}</td><td class="p-2 border text-center">${r[2]}</td><td class="p-2 border">${r[3]}</td><td class="p-2 border">${r[4]}</td></tr>`;});html+=`</tbody></table></div>`;box.innerHTML=html;}

function renderModules(p){
const c=document.getElementById('modulesContainer');c.innerHTML='';if(!p.modules||!p.modules.length){c.innerHTML='<p class="text-gray-400 text-center py-6">لا توجد وحدات مسجلة.</p>';return;}
p.modules.forEach(m=>{
const d=document.createElement('div');d.className='bg-white rounded-xl shadow-soft border p-5 mb-4';
d.innerHTML=`<div class="flex justify-between gap-2"><h5 class="font-bold">📘 ${m.title}</h5><span class="text-xs text-gray-400">${(m.sheets||[]).length} درس/بطاقة ${badge(m.status)}</span></div><p class="text-sm text-gray-500 mt-1">${m.desc}</p><div id="sheets-${m.id}" class="mt-3 space-y-2"></div><div class="flex gap-2 mt-3 no-print"><button onclick="editModule('${m.id}')" class="btn-admin bg-blue-100 text-blue-700">✏️ تعديل</button><button onclick="deleteModule('${m.id}')" class="btn-admin bg-red-100 text-red-700">🗑️ حذف</button><button onclick="addSheet('${m.id}')" class="btn-admin bg-green-100 text-green-700">➕ إضافة درس</button></div>`;
c.appendChild(d);(m.sheets||[]).forEach(s=>renderSheet(m,s));
});
}

function renderSheet(m,s){
const c=document.getElementById('sheets-'+m.id);if(!c)return;
const d=document.createElement('div');d.className='tech-sheet-card';
d.innerHTML=`<button class="accordion-btn" onclick="toggleSheet('${s.id}')"><span class="flex-1">${badge(s.status)} ${s.name}</span><span id="arrow-${s.id}">▼</span></button><div id="sheet-${s.id}" class="accordion-content hidden">${renderSheetContent(s)}<div class="flex gap-2 mt-3 no-print"><button onclick="editSheet('${s.id}')" class="btn-admin bg-blue-100 text-blue-700">✏️ تعديل الاسم</button><button onclick="deleteSheet('${s.id}')" class="btn-admin bg-red-100 text-red-700">🗑️ حذف</button><button onclick="printSheet('${s.id}')" class="btn-admin bg-gray-200">🖨️ طباعة</button></div><div class="text-xs text-gray-300 mt-2 text-center">حورية فرحي | الشيف البيداغوجي © 2026</div></div>`;
c.appendChild(d);
}

function renderSheetContent(s){
let h='';const fields=[['🎯 الهدف التعلمي','objective'],['📚 المكتسبات القبلية','prerequisites'],['🧰 الأدوات والتجهيزات','tools'],['👩‍🍳 مراحل الإنجاز','steps'],['🔥 الطهي ودرجة الحرارة','cooking'],['⚠️ المشاكل الشائعة','commonMistakes'],['🔧 إجراءات التصحيح','corrections'],['✅ معايير الجودة','qualityCriteria'],['🧼 النظافة والسلامة','hygiene'],['⏱️ مدة الإنجاز','duration'],['📦 المردود','yield'],['🧊 الحفظ','storage'],['🍽️ التقديم','serving'],['📝 أسئلة التقويم','evalQuestions'],['👩‍🍳 النشاط التطبيقي','practicalActivity'],['📌 ملاحظة بيداغوجية','note']];
fields.forEach(([label,key])=>{if(!s[key])return;h+=`<h6>${label}</h6>`;if(Array.isArray(s[key])){if(key==='ingredients'){h+=`<div class="scale-control"><label>عامل القياس:</label><input id="scale-${s.id}" type="number" value="1" min="0.1" step="0.1" oninput="updateIngredients('${s.id}')"><span class="small-note">2 = مضاعفة، 0.5 = تنصيف</span></div><div id="ingredients-display-${s.id}" class="bg-gray-50 p-3 rounded-lg">${ingredientList(s.ingredients,1)}</div>`;}else{h+=`<ul class="list-disc list-inside text-sm text-gray-700 space-y-1">${s[key].map(x=>`<li>${x}</li>`).join('')}</ul>`;}}else{h+=`<div class="mb-2 text-sm text-gray-700 leading-7">${s[key]}</div>`;}});
h+=`<h6>📊 شبكة تقييم المتكوّن</h6><div class="overflow-x-auto"><table class="w-full text-sm border"><thead><tr><th class="p-1 border">المعيار</th><th class="p-1 border">ممتاز</th><th class="p-1 border">جيد</th><th class="p-1 border">مقبول</th><th class="p-1 border">ضعيف</th></tr></thead><tbody>`;['احترام المقادير','تنظيم العمل','استعمال الأدوات','التحضير','التشكيل','الطهي أو التحميص','التشريب','النظافة والسلامة','جودة المنتوج','التقديم'].forEach(x=>{h+=`<tr><td class="p-1 border">${x}</td><td class="p-1 border text-center">☐</td><td class="p-1 border text-center">☐</td><td class="p-1 border text-center">☐</td><td class="p-1 border text-center">☐</td></tr>`;});h+=`</tbody></table></div>`;return h;
}

function ingredientList(a,f){return `<div class="ingredient-list">${a.map(x=>{const n=x[1]*f;return `<span class="ingredient-item">${x[0]}: <strong>${Number.isInteger(n)?n:n.toFixed(2)}</strong> ${x[2]}</span>`;}).join('')}</div>`;}

function findSheet(id){for(const p of Object.values(programData)){for(const m of p.modules||[]){for(const s of m.sheets||[]){if(s.id===id)return [p,m,s];}}}return null;}
function updateIngredients(id){const x=findSheet(id);if(!x)return;const input=document.getElementById('scale-'+id);const output=document.getElementById('ingredients-display-'+id);if(input&&output){const factor=parseFloat(input.value)||1;output.innerHTML=ingredientList(x[2].ingredients,factor);}}
function toggleSheet(id){const e=document.getElementById('sheet-'+id);if(!e)return;e.classList.toggle('hidden');const a=document.getElementById('arrow-'+id);if(a)a.textContent=e.classList.contains('hidden')?'▼':'▲';}

function performSearch(q){
q=q.toLowerCase().trim();
if(!q){document.querySelectorAll('.tech-sheet-card').forEach(c=>c.style.display='block');return;}
if(currentProgramId!=='traditional_pastry')selectSubProgram('traditional_pastry');
setTimeout(()=>{document.querySelectorAll('.tech-sheet-card').forEach(c=>{c.style.display=c.textContent.toLowerCase().includes(q)?'block':'none';});},100);
}
function clearSearch(){document.getElementById('globalSearch').value='';performSearch('');}

function toggleAdmin(){const p=document.getElementById('adminPanel');p.classList.toggle('hidden');if(!p.classList.contains('hidden'))renderAdmin();}
function renderAdmin(){
const p=programData.traditional_pastry;const c=document.getElementById('adminContent');
c.innerHTML=`<h4 class="font-bold mb-3">📘 البرنامج: ${p.title}</h4><div class="grid sm:grid-cols-2 gap-3"><div><label>العنوان</label><input value="${esc(p.title)}" onchange="updateProgramField('title',this.value)"></div><div><label>الوصف</label><input value="${esc(p.desc)}" onchange="updateProgramField('desc',this.value)"></div><div><label>المجال</label><input value="${esc(p.field)}" onchange="updateProgramField('field',this.value)"></div><div><label>الساعات</label><input type="number" value="${p.hours}" onchange="updateProgramField('hours',parseInt(this.value))"></div><div><label>المكتسبات القبلية</label><input value="${esc(p.prereq)}" onchange="updateProgramField('prereq',this.value)"></div><div><label>الكفاءة البعدية</label><input value="${esc(p.postreq)}" onchange="updateProgramField('postreq',this.value)"></div></div><h4 class="font-bold mt-5 mb-2">⏱️ توزيع الساعات</h4><div class="overflow-x-auto"><table class="w-full text-sm"><thead><tr><th class="border p-2">المرحلة</th><th class="border p-2">الساعات</th><th class="border p-2">النشاط</th></tr></thead><tbody>${(p.timeDistribution||[]).map(r=>`<tr><td class="border p-2">${r[0]}</td><td class="border p-2">${r[1]}</td><td class="border p-2">${r[2]}</td></tr>`).join('')}</tbody></table></div><div class="mt-5"><b>📚 الوحدات:</b><p class="text-sm text-gray-500 mt-1">MQ1 – إعداد حلويات اللوز<br>MQ2 – الحلويات المصنوعة من السميد<br>تقنية مشتركة – العسيلة والقطر</p></div><button onclick="resetData()" class="btn-admin bg-red-100 text-red-700 mt-4">♻️ إعادة البيانات الأصلية</button>`;
}
function updateProgramField(k,v){programData.traditional_pastry[k]=v;saveData();selectSubProgram('traditional_pastry');renderAdmin();}

function addModule(){if(!currentProgramId){alert('افتحي برنامجًا أولًا.');return;}const p=programData[currentProgramId];const title=prompt('اسم الوحدة الجديدة:');if(!title)return;p.modules=p.modules||[];p.modules.push({id:'module_'+Date.now(),title:title,desc:'وحدة جديدة',status:'إعداد الأستاذة',sheets:[]});saveData();selectSubProgram(currentProgramId);}
function editModule(id){const p=programData[currentProgramId];const m=(p.modules||[]).find(x=>x.id===id);if(!m)return;const t=prompt('تعديل اسم الوحدة:',m.title);if(t){m.title=t;saveData();selectSubProgram(currentProgramId);}}
function deleteModule(id){if(!confirm('هل تريدين حذف هذه الوحدة؟'))return;const p=programData[currentProgramId];p.modules=p.modules.filter(x=>x.id!==id);saveData();selectSubProgram(currentProgramId);}
function addSheet(mid){const p=programData[currentProgramId];const m=(p.modules||[]).find(x=>x.id===mid);if(!m)return;const name=prompt('اسم الدرس أو البطاقة التقنية:');if(!name)return;m.sheets=m.sheets||[];m.sheets.push({id:'sheet_'+Date.now(),name:name,objective:'قيد الإعداد',prerequisites:'قيد الإعداد',tools:'قيد الإعداد',ingredients:[],steps:['قيد الإعداد'],cooking:'قيد التدقيق',commonMistakes:'قيد التدقيق',corrections:'قيد التدقيق',qualityCriteria:'قيد التدقيق',hygiene:'قيد التدقيق',duration:'قيد التدقيق',yield:'قيد التدقيق',storage:'قيد التدقيق',serving:'قيد التدقيق',evalQuestions:['قيد التدقيق'],practicalActivity:'قيد التدقيق',status:'إعداد الأستاذة'});saveData();selectSubProgram(currentProgramId);}
function editSheet(id){const x=findSheet(id);if(!x)return;const s=x[2];const name=prompt('تعديل اسم الدرس:',s.name);if(name){s.name=name;saveData();selectSubProgram(currentProgramId);}}
function deleteSheet(id){if(!confirm('هل تريدين حذف هذا الدرس؟'))return;const x=findSheet(id);if(!x)return;x[1].sheets=x[1].sheets.filter(s=>s.id!==id);saveData();selectSubProgram(currentProgramId);}
function printSheet(id){const x=findSheet(id);if(!x)return;const s=x[2];const w=window.open('','_blank');w.document.write(`<html lang="ar" dir="rtl"><head><title>${s.name}</title><style>body{font-family:Arial;padding:30px;line-height:1.9;color:#222}h1{color:#8a5a00}h2{border-bottom:1px solid #ddd;padding-bottom:5px}li{margin:5px}.box{border:1px solid #ddd;padding:15px;margin-bottom:15px;border-radius:8px}</style></head><body><h1>🍰 ${s.name}</h1><p>إعداد الأستاذة: حورية فرحي © 2026</p><div class="box"><strong>الهدف التعلمي</strong><p>${s.objective||''}</p></div><div class="box"><strong>المكتسبات القبلية</strong><p>${s.prerequisites||''}</p></div><div class="box"><strong>الأدوات</strong><p>${s.tools||''}</p></div><div class="box"><strong>المقادير</strong><ul>${(s.ingredients||[]).map(x=>`<li>${x[0]}: ${x[1]} ${x[2]}</li>`).join('')}</ul></div><div class="box"><strong>مراحل الإنجاز</strong><ol>${(s.steps||[]).map(x=>`<li>${x}</li>`).join('')}</ol></div><div class="box"><strong>الطهي</strong><p>${s.cooking||''}</p></div><div class="box"><strong>المشاكل والحلول</strong><p>${s.commonMistakes||''}</p><p>${s.corrections||''}</p></div><div class="box"><strong>معايير الجودة</strong><p>${s.qualityCriteria||''}</p></div><div class="box"><strong>النظافة والسلامة</strong><p>${s.hygiene||''}</p></div><div class="box"><strong>الحفظ</strong><p>${s.storage||''}</p></div><div class="box"><strong>التقييم</strong><ul>${(s.evalQuestions||[]).map(x=>`<li>${x}</li>`).join('')}</ul></div></body></html>`);w.document.close();w.focus();setTimeout(()=>w.print(),400);}
function resetData(){if(!confirm('سيتم حذف التعديلات المحلية وإعادة محتوى المنصة الأصلي. هل أنت متأكدة؟'))return;localStorage.removeItem('chef_pedagogique_data');loadData();renderPrograms();if(currentProgramId)selectSubProgram(currentProgramId);alert('تمت إعادة البيانات الأصلية بنجاح.');}
renderPrograms();
</script>

</body>
</html>
