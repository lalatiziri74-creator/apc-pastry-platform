# data.py
# بنية البيانات الهيكلية المنظمة للمنصة البيداغوجية للتكوين المهني (APC)
# إعداد وتصميم بيداغوجي: الأستاذة فرحي حورية
# الهيكل الهرمي: برنامج -> تخصص -> وحدة -> مقياس -> درس -> (محتوى متربص / محتوى أستاذ)

PLATFORM_DATA = {
    "programs": [
        {
            "id": "prog_apprentice",
            "title": "📖 برنامج التمهين",
            "description": "نظام التكوين عن طريق التمهين بالمؤسسات المستقبلة.",
            "visibility": "public",  # public, hidden, draft
            "specialties": [
                {
                    "id": "spec_app_pastry",
                    "title": "صناعة الحلويات / Pâtisserie",
                    "code": "PAT_APP_01",
                    "visibility": "public",
                    "modules": [
                        {
                            "id": "mod_app_01",
                            "title": "الوحدة 01: الأساسيات والمواد الأولية",
                            "code": "MOD_01",
                            "visibility": "public",
                            "subjects": [
                                {
                                    "id": "subj_app_01",
                                    "title": "مقياس التقنيات التطبيقية والمواد",
                                    "syllabus": "مخطط المقياس التجريبي: التعرف على خامات الحلويات، المعايير الكيميائية والفيزيائية للمكونات، وضوابط السلامة.",
                                    "visibility": "public",
                                    "lessons": [
                                        {
                                            "id": "les_app_01_01",
                                            "title": "الدرس 01: المكونات الأساسية ودورها في العجائن",
                                            "access": "free",  # free, premium, restricted
                                            "is_premium": False,
                                            "visibility": "public",
                                            "trainee_content": {
                                                "description": "شرح تجريبي للمكونات الأساسية وتأثيرها على قوام العجين.",
                                                "activities": "تمرين تطبيقي تجريبي: حساب نسب المكونات في وصفة معيارية.",
                                                "quiz": "سؤال تقييمي تجريبي حول دور المواد الدسمة."
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط الدرس وفق المقاربة بالكفاءات (APC) - نموذج تجريبي.",
                                                "objectives": "الأهداف التعليمية والكفاءات المستهدفة للدرس.",
                                                "evaluation_grid": "شبكة معايير ومؤشرات التقييم النموذجية.",
                                                "model_answers": "التصحيح والإجابة النموذجية للتطبيقات.",
                                                "technical_card": "البطاقة التقنية البيداغوجية للدرس."
                                            }
                                        },
                                        {
                                            "id": "les_app_01_02",
                                            "title": "الدرس 02: التقنيات الاحترافية في إدارة الحرارة والطهي",
                                            "access": "premium",
                                            "is_premium": True,
                                            "visibility": "public",
                                            "trainee_content": {
                                                "description": "شرح تجريبي لضبط حرارة الأفران وحساب أوقات الطهي.",
                                                "activities": "نشاط عملي تجريبي: ضبط مخطط الطهي.",
                                                "quiz": "اختبار تقييمي تجريبي حول أخطاء الطهي."
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط الدرس APC التجريبي المخصص للأستاذ.",
                                                "objectives": "الكفاءات الخاصة بإدارة الأفران والورشة.",
                                                "evaluation_grid": "معايير تقييم نضج واستواء المنتج النهائي.",
                                                "model_answers": "الإجابات النموذجية الخاصة باختبار الأخطاء.",
                                                "technical_card": "بطاقة السلامة والتحكم في المعدات."
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "id": "prog_presence",
            "title": "🏫 التكوين الحضوري",
            "description": "التكوين المهني الأساسي الحضوري بالداخلية ونصف الداخلية.",
            "visibility": "public",
            "specialties": [
                {
                    "id": "spec_pres_pastry",
                    "title": "صناعة الحلويات / Pâtisserie",
                    "code": "PAT_PRES_01",
                    "visibility": "public",
                    "modules": [
                        {
                            "id": "mod_pres_01",
                            "title": "الوحدة 01: أساسيات الورشة الحضورية",
                            "code": "MOD_PRES_01",
                            "visibility": "public",
                            "subjects": [
                                {
                                    "id": "subj_pres_01",
                                    "title": "مقياس النظافة والتطبيق الحضوري",
                                    "syllabus": "مخطط المقياس التجريبي للتكوين الحضوري.",
                                    "visibility": "public",
                                    "lessons": [
                                        {
                                            "id": "les_pres_01_01",
                                            "title": "الدرس 01: قواعد السلامة والنظافة في ورشة الحلويات",
                                            "access": "free",
                                            "is_premium": False,
                                            "visibility": "public",
                                            "trainee_content": {
                                                "description": "مقدمة تجريبية عن النظافة الشخصية ونظافة المعدات.",
                                                "activities": "نشاط تطبيقي تجريبي لتعقيم أدوات الورشة.",
                                                "quiz": "أسئلة مراجعة حول شروط السلامة."
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط الدرس الحضوري وفق المقاربة بالكفاءات.",
                                                "objectives": "تطبيق شروط الوقاية والأمن الداخلي.",
                                                "evaluation_grid": "شبكة ملاحظة السلوك والتطبيق العملي.",
                                                "model_answers": "حلول أسئلة المراجعة.",
                                                "technical_card": "بطاقة المعايير الصحية للورشات."
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "id": "prog_housewife",
            "title": "🏠 المرأة الماكثة بالبيت",
            "description": "برامج التكوين التأهيلي الموجهة للمرأة الماكثة بالبيت.",
            "visibility": "public",
            "specialties": [
                {
                    "id": "spec_hw_traditional",
                    "title": "الحلويات التقليدية المنزلية",
                    "code": "PAT_HW_01",
                    "visibility": "public",
                    "modules": [
                        {
                            "id": "mod_hw_01",
                            "title": "الوحدة 01: تحضير العجائن التقليدية الأساسية",
                            "code": "MOD_HW_01",
                            "visibility": "public",
                            "subjects": [
                                {
                                    "id": "subj_hw_01",
                                    "title": "مقياس الحلويات التقليدية التأهيلية",
                                    "syllabus": "مخطط المقياس التجريبي للمرأة الماكثة بالبيت.",
                                    "visibility": "public",
                                    "lessons": [
                                        {
                                            "id": "les_hw_01_01",
                                            "title": "الدرس 01: تقنيات بس العجين والتحكم في القوام",
                                            "access": "free",
                                            "is_premium": False,
                                            "visibility": "public",
                                            "trainee_content": {
                                                "description": "شرح تجريبي لأساسيات تحضير العجائن التقليدية.",
                                                "activities": "تطبيق تجريبي منزلي.",
                                                "quiz": "أسئلة مراجعة المكونات."
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط التكوين التأهيلي الخفيف.",
                                                "objectives": "إتقان القوام التقليدي للحلويات.",
                                                "evaluation_grid": "شبكة تقييم المنتج المنزلي.",
                                                "model_answers": "الإجابات النموذجية.",
                                                "technical_card": "بطاقة المقادير المعيارية للإنتاج المنزلي."
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
