جPLATFORM_DATA = {
    "programs": [
        {
            "id": "prog_woman_home",
            "title": "برنامج المرأة الماكثة بالبيت",
            "description": "التكوين التأهيلي الموجه للمرأة الماكثة بالبيت لتطوير حرف الإنتاج المصغر.",
            "specialties": [
                {
                    "id": "spec_trad",
                    "title": "تخصص الحلويات التقليدية المنزلية",
                    "code": "PAT_HW_01",
                    "modules": [
                        {
                            "id": "mod_trad_1",
                            "title": "وحدة تقنيات صناعة الحلويات التقليدية",
                            "subjects": [
                                {
                                    "id": "subj_trad_1",
                                    "title": "مقياس العجائن والمعسلات التقليدية",
                                    "syllabus": "مخطط المقياس: دراسة عجائن المقيض والدزريات والمعسلات.",
                                    "lessons": [
                                        {
                                            "id": "les_dziriette",
                                            "title": "درس تحضير الدزريات الأصلية",
                                            "is_premium": False,
                                            "trainee_content": {
                                                "description": "تعلم كيفية تحضير العينة، التشكيل، والعسل الخاص بالدزريات.",
                                                "activities": "تطبيق عملية تزيين ووزن العجين والحشو.",
                                                "quiz": "ماهي درجات العسل المناسبة لسقي الدزريات؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط درس وفق المقاربة بالكفاءات (APC).",
                                                "objectives": "أن تتمكن المتربصة من إتقان قالب الدزريات بنسبة نجاح تامة.",
                                                "evaluation_grid": "شبكة التقييم: اللون، اللمعان، وطراوة الحشو.",
                                                "model_answers": "الإجابة النموذجية وطريقة تفادي جفاف الحشو.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: الدزريات",
                                                    "base_portions": 20,
                                                    "ingredients": [
                                                        {"item": "فرينة (طحين)", "qty": 500, "unit": "غرام"},
                                                        {"item": "سمن معطر", "qty": 125, "unit": "غرام"},
                                                        {"item": "لوز مطحون (الحشو)", "qty": 300, "unit": "غرام"},
                                                        {"item": "سكر عادي", "qty": 100, "unit": "غرام"},
                                                        {"item": "عسل", "qty": 250, "unit": "غرام"}
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "spec_oriental",
                    "title": "تخصص الحلويات الشرقية والمعاصرة",
                    "code": "PAT_HW_02",
                    "modules": [
                        {
                            "id": "mod_oriental_1",
                            "title": "وحدة الحلويات الشرقية",
                            "subjects": [
                                {
                                    "id": "subj_oriental_1",
                                    "title": "مقياس المعجنات الشرقية الدقيقة",
                                    "syllabus": "مخطط المقياس: تقنيات الطهي والتشكيل الشرقي.",
                                    "lessons": [
                                        {
                                            "id": "les_baklawa",
                                            "title": "درس البقلاوة الجزائرية التقليدية",
                                            "is_premium": False,
                                            "trainee_content": {
                                                "description": "حساب الطبقات، تورق العجين، وتوزيع الحشو.",
                                                "activities": "ترتيب 7 طبقات سفلية و 7 علوية.",
                                                "quiz": "كيف يتم تجنب انتفاخ طبقات البقلاوة أثناء الخبز؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط بيداغوجي لدرس البقلاوة.",
                                                "objectives": "التحكم في تقطيع ووزن الصينية.",
                                                "evaluation_grid": "التناسق، القرمشة، وتشرب العسل.",
                                                "model_answers": "الحل النموذجي لالتصاق الطبقات.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: البقلاوة الصينية القياسية",
                                                    "base_portions": 30,
                                                    "ingredients": [
                                                        {"item": "فرينة", "qty": 1000, "unit": "غرام"},
                                                        {"item": "سمن ابلح", "qty": 300, "unit": "غرام"},
                                                        {"item": "لوز مرحي", "qty": 3000, "unit": "غرام"},
                                                        {"item": "سكر", "qty": 1000, "unit": "غرام"}
                                                    ]
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": "spec_western",
                    "title": "تخصص الحلويات الغربية (Patisserie Fine)",
                    "code": "PAT_HW_03",
                    "modules": [
                        {
                            "id": "mod_western_1",
                            "title": "وحدة الترتلات والكريمة",
                            "subjects": [
                                {
                                    "id": "subj_western_1",
                                    "title": "مقياس العجائن الهشة والفاخرة",
                                    "syllabus": "مخطط المقياس: Pâte Sablée et Crèmes.",
                                    "lessons": [
                                        {
                                            "id": "les_tarts",
                                            "title": "درس تارتليت الفواكه الموسمية",
                                            "is_premium": False,
                                            "trainee_content": {
                                                "description": "إعداد العجينة الهشة، الخبز الأعمى، وترتيب الفواكه.",
                                                "activities": "تلبيس القوالب الصغرى بدقة.",
                                                "quiz": "لماذا نقوم بثقب العجينة الهشة قبل الخبز؟"
                                            },
                                            "teacher_content": {
                                                "apc_plan": "مخطط بيداغوجي لدرس الترتليت.",
                                                "objectives": "إتقان الطهي المتساوي لقواعد العجين.",
                                                "evaluation_grid": "لون الحواف، ثبات الكريمة، واللمعان.",
                                                "model_answers": "التعامل مع انكماش العجينة في الفرن.",
                                                "technical_card": {
                                                    "title": "البطاقة التقنية: تارتليت الفواكه",
                                                    "base_portions": 10,
                                                    "ingredients": [
                                                        {"item": "فرينة", "qty": 250, "unit": "غرام"},
                                                        {"item": "زبدة باردة", "qty": 125, "unit": "غرام"},
                                                        {"item": "سكر رطب", "qty": 75, "unit": "غرام"},
                                                        {"item": "بيضة", "qty": 1, "unit": "حبة"}
                                                    ]
                                                }
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
            "id": "prog_cap",
            "title": "شهادة الكفاءة المهنية (CAP)",
            "description": "برنامج التكوين المهني الأساسي.",
            "specialties": []
        }
    ]
}
