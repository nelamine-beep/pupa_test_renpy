screen stand_map_fundamental_mathematics:
    imagemap:
        hover 'images/stands/bg stand1(2).png'
        idle 'images/stands/bg stand1.png'
        hotspot (263, 230, 190, 337) action Jump('teachers_fundamental_mathematics')
        hotspot (468, 230, 187, 337) action Jump('kafedra_fundamental_mathematics')
        hotspot (677, 230, 190, 337) action Jump('info_naprav_fundamental_mathematics_menu')
        hotspot (1062, 230, 190, 337) action Jump('book_fundamental_mathematics')
    button:
        xalign 0.0 yalign 0.0
        xsize 200 ysize 200
        idle_background "images/elements/icon_map_idle.png"
        hover_foreground "images/elements/icon_map_hover.png"
        action Jump("map_open")
    imagebutton:
        xalign 0.1
        yalign 0.0
        idle "images/elements/book_idle.png"
        hover "images/elements/book_hover.png"
        action Show("info_panel")
    # imagebutton:
    #     xalign 1.0
    #     yalign 0.5
    #     idle "images/elements/strelka.png"
    #     hover "images/elements/strelka_hover.png"
    #     action Call("mini_game_fundamental_mathematics")

screen info_prepod_fundamental_mathematics:
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 30 # Расстояние, между баром и боксом.
            xsize 1400 # Размер, дабы не растекалось по всему экрану.
            ysize 600
            align (.5, .5) # Центруем
            viewport id "view_id123": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
                xfill False
                yfill False
                mousewheel True # Разрешаем прокрутку мышью.
                vbox:
                    spacing 15
                    text _("    Кафедра образована слиянием кафедры математического анализа и теории функций и кафедры математического моделирования.\n     В его состав входят:")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("И. о. заведующего кафедрой, доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Профессор, доктор физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Профессор, доктор физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент. кандидат педагогических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат педагогических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Ассистент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Ассистент.")
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_prepod_fundamental_mathematics"), Jump ("fundamental_mathematics_stand") xalign 0.96

screen info_kafedra_fundamental_mathematics:
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 30 # Расстояние, между баром и боксом.
            xsize 1400 # Размер, дабы не растекалось по всему экрану.
            ysize 600
            align (.5, .5) # Центруем
            viewport id "view_id123": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
                xfill False
                yfill False
                mousewheel True # Разрешаем прокрутку мышью.
                vbox:
                    text _("    Математический анализ представляет собой составную часть и, пожалуй, большую долю той части математического знания, которая сейчас является общей для всех современных математических дисциплин. И поэтому понятна та исключительная роль, которую играет математический анализ в математическом образовании. ОН, по существу, является фундаментом математических знаний.")
                    text _("    Поэтому на кафедре всегда работали и продолжают работать известные специалисты по математическому анализу, теории функции, топологии, теории вероятностей, математической статистике, дифференциальным уравнениям и их приложениям.")
                    text _("    Кафедра осуществляет два направления подготовки, а именно:")
                    text _("    {b}Механика и математическое моделирование{/b} по профилю «Механика жидкости, газа и плазмы».")
                    text _("    За время обучения студенты приобретают научные знания по компьютерному моделированию различных механических процессов, развивают способности к аналитическому мышлению, учатся применять на практике основы фундаментальной математики, механики, физики и других естественных наук.")
                    text _("Выпускники находят применение своим знаниям в инжиниринговых центрах промышленных компаний, газовых и нефтяных отраслях, транснациональных корпорациях, исследовательских и конструкторских бюро, занимающихся разработкой новых инженерных технологий.")
                    text _("    {b}Математика{/b} по профилю «Вещественный, комплексный и функциональный анализ».")
                    text _("Бакалавр математики в ходе обучения вырабатывает особый способ мышления и становится способным решать задачи в различных областях деятельности человека. Он способен при помощи программного обеспечения и вычислительных приборов заниматься разработкой путей разрешения задач, связанных с информацией в областях техники, экономики, управления. Математик структурирует информацию, ее объем и способ ввода. Также он занимается проверкой готовых программ и написанием инструкций к их применению. В сферу деятельности математика входит анализ сложившейся экономический ситуации, разработка методов ее изменения и составление статистических данных. Анализ экономической ситуации осуществляется при помощи теории вероятности и математической статистики.")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_kafedra_fundamental_mathematics"), Jump ("fundamental_mathematics_stand") xalign 0.96

screen info_napravleniya_math_fundamental_mathematics:
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 30 # Расстояние, между баром и боксом.
            xsize 1400 # Размер, дабы не растекалось по всему экрану.
            ysize 600
            align (.5, .5) # Центруем
            viewport id "view_id123": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
                xfill False
                yfill False
                mousewheel True # Разрешаем прокрутку мышью.
                vbox:
                    text _("    МАТЕМАТИКАМАТЕМАТИКАМАТЕМАТИКАтексттексттексттексттексттексттексттексттексттекст")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_napravleniya_math_fundamental_mathematics"), Jump ("fundamental_mathematics_stand") xalign 0.96

screen info_napravleniya_mech_math_fundamental_mathematics:
    frame:
        xsize 1600
        ysize 800
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 30 # Расстояние, между баром и боксом.
            xsize 1400 # Размер, дабы не растекалось по всему экрану.
            ysize 600
            align (.5, .5) # Центруем
            viewport id "view_id123": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
                xfill False
                yfill False
                mousewheel True # Разрешаем прокрутку мышью.
                vbox:
                    text _("    МЕХМАТМЕХМАТМЕХМАТМЕХМАТМЕХМАТтексттексттексттексттексттексттексттексттексттекст")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_napravleniya_mech_math_fundamental_mathematics"), Jump ("fundamental_mathematics_stand") xalign 0.96

# label mini_game_fundamental_mathematics:
#         scene bg 11 with fade
#         if (p):
#             menu:
#                 "{color=000000}Собери код":
#                     call start_aplusb from _call_start_aplusb_2
#                     jump mini_game_fundamental_mathematics
#                 "{color=000000}Тренировка памяти":
#                     call start_memoria from _call_start_memoria_2
#                     jump mini_game_fundamental_mathematics
#                 "{color=000000}Вернуться":
#                     jump fundamental_mathematics_stand
#         else:
#             show man_left at center with moveoutleft
#             gid "Хочешь отдохнуть?"
#             $p = True
#             menu:
#                 "{color=000000}Да":
#                     gid "Ну чтож, [name_reader]. Во что хочешь поиграть?"
#                     menu:
#                         "{color=000000}Собери код":
#                             call start_aplusb from _call_start_aplusb_3
#                         "{color=000000}Тренировка памяти":
#                             call start_memoria from _call_start_memoria_3
#                         "{color=000000}Вернуться":
#                             jump fundamental_mathematics_stand
#                 "{color=000000}Нет":
#                     gid "До встречи!"
#                     jump fundamental_mathematics_stand

label fundamental_mathematics_stand:
    show screen start_minigames
    call screen stand_map_fundamental_mathematics

label teachers_fundamental_mathematics:
    scene bg stand1
    call screen info_prepod_fundamental_mathematics
    jump fundamental_mathematics_stand
    return

label kafedra_fundamental_mathematics:
    scene bg stand1
    call screen info_kafedra_fundamental_mathematics
    jump fundamental_mathematics_stand
    return

label info_naprav_fundamental_mathematics_menu:
    scene bg stand1
    menu info_naprav_fundamental_mathematics:
        "{color=000000}Математика":
            jump matem
        "{color=000000}Механика и математическое моделирование":
            jump mech_math

label matem:
    scene bg stand1
    hide screen start_minigames
    show man_left at left with dissolve
    gid "Интересный выбор."
    gid "В последнее время немногие целенаправленно выбирают данное направление."
    gid "Но раз уж выбрал, давай расскажу, что тебе предстоит."
    gid "Специальность «Математика»."
    gid "Ты не поверишь, но здесь ты будешь изучать… {w}МАТЕМАТИКУ"
    scene bg 14
    show man_left at left with dissolve
    gid "Знаю, знаю, ты её не боишься. Ты же, все-таки видел, название. Тогда подробнее."
    gid "Дифференциалы, со временем, станут твоим лучшим другом. Они будут встречаться с тобой часто. Чего только стоит дифференциальная геометрия. Что это такое - не скажу… {w}секрет."
    gid "Обучат тебя и элементам статистики."
    gid "На своей шкуре прочувствуешь, что такое корреляционные и регрессионные анализы."
    gid "Узнаешь, как происходит полный процесс расчёта статистики. От постановки гипотезы, до её подтверждения/опровержения."
    gid "И, наконец, поймешь, почему открытия «великих» великобританских учёных, что делают все свои выводы на основе статистики, не всегда являются правдой."
    gid "Но статистика - не математика, по заявлениям некоторых преподавателей института. Так что давай вернёмся к фундаментальной науке."
    gid "Ты ведь уже знаешь, что такое комплексные числа?"
    gid "Так вот, тебя обучат с ними оперировать, не волнуйся."
    gid "Если обобщить остальные математические дисциплины. Вы будете изучать все математические методы и модели для расчетов поведения физических объектов."
    gid "Без изучения вероятностей тоже не обойдётся."
    gid "Тебе дадут и минимальные базовые знания об одном из разделов физики, механикой прозывается. Она описывает процесс механического движения различных объектов в пространстве."
    gid "Проще говоря, движение."
    scene bg 12
    show man_left at left with dissolve
    gid "Если ты думал, что, придя сюда, ты убежишь от программирования."
    gid "Даже не надейся."
    gid "Тебя заставят научиться программировать, но лишь на базовом уровне. А основной упор будет производиться на специализированные под математику языки."
    gid "Языки на подобие MATLab."
    gid "У тебя появится возможность заниматься простой научной деятельностью и, если тебе понравится данный процесс, сможешь связать с ним своё будущее."
    gid "В общем, отсюда выходят «чистые» математики, способные применять свои знания в различных сферах."
    gid "С дипломом данной специализации можно идти и в банки, и в различные ресурсодобывающие компании. Можно стать ученым, если не останавливаться на бакалавриате, или преподавателем."
    gid "Если ты не испугался, после всего, что я тебе сказал, или тебе даже понравилось."
    gid "Тогда тебе прямиком на специальность под названием «математика». "
    gid "Мы будем ждать тебя, математик!"
    jump fundamental_mathematics_stand
    return

label mech_math:
    hide screen start_minigames
    scene bg stand1
    show man_right at right with dissolve
    gid "Хорошо."
    gid "Давай поведаю, что тебе предстоит, выбрав данное направление."
    gid "Ты мог сделать вывод, что здесь ты будешь изучать в большей мере различные разделы механики и математическое моделирование."
    gid "И ты будешь прав."
    gid "В большей мере, здесь таким и занимаются. "
    gid "Ты изучишь основы механики, как уже было сказано, как ведёт себя вязкая жидкость (нефть сразу приходит на ум) и газ в различных ситуациях с точки зрения и физики, и математического представления."
    gid "Помимо этого, ты вникнешь и в макросистемы, т.е тела, состоящие из более малых частиц (молекул или атомов)."
    gid "Как пример можно привести одну каплю в воде."
    gid "Тебе предстоит обучиться основам математического анализа, без которого здесь никуда."
    gid "Вас будут, как в школе, вызывать к доске, прося решить различные дифференциальные уравнения, интегральные, а также посчитать пределы различных функций."
    gid "Геометрия тоже не останется в стороне, не переживай."
    scene bg 10
    show man_left at left with dissolve
    gid "Конечно, тебя просветят, как именно протекает процесс математического моделирования, но сначала пояснят, что это вообще такое и в каких формах мат.модель может быть представлена."
    gid "Спойлер {w}уравнения и неравенства, в основном."
    gid "Если к этому моменту ты подумал, что здесь ты будешь изучать только математику и физику."
    gid "Не спеши."
    gid "Помимо всего перечисленного, ты также будешь изучать и программирование."
    gid "Не на высоком уровне, да, но все же будешь."
    gid "Сначала ты узнаешь об общих основах программирования: их  видах, основных операторах, различных коллекциях и т.д"
    gid "А затем вас подсадят на язык программирования python."
    gid "Он довольно прост в использовании, а главное, что он имеет огромное количество уже написанных библиотек, которые реализуют различные математические алгоритмы"
    gid "Их можно просто брать и использовать, что вы, по большей части, и будете делать "
    gid "Не одним python будешь обучаться "
    scene bg 9
    show man_left at left with dissolve
    gid "Ты узнаешь и о различных специализированных так называемых «системах компьютерной математики» "
    gid "Таких как matlab "
    gid "Это очень мощный инструментарий, который будет вами использоваться в основном для моделирования "
    gid "Для работы с ним потребуются навыки использования внутреннего языка программирования matlab, так что придется изучить и его "
    gid "У тебя появится возможность заниматься простой научной деятельностью и, если тебе понравится данный процесс, сможешь в последствии связать с ним своё будущее. "
    gid "В общем, если ты хочешь быть физиком-математиком в разделе механики "
    gid "Тебе к нам "
    gid "Выпустившись с корочкой данной специализации, тебе прямая дорога в различные ресурсодобывающие компании или различные компании, связанные с архитектурами различных жидкостных систем, а также инженеры"
    gid "Понравилось? Присоединяйся!"
    jump fundamental_mathematics_stand
    return

label book_fundamental_mathematics:
    scene bg stand1
    show book_close with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    pause 0.5
    hide book_close with fade

label book_open_fundamental_mathematics:
    call screen empty_page_fundamental_mathematics
    return

screen empty_page_fundamental_mathematics:
    imagemap:
        xalign 0.5
        yalign 0.5
        hover 'images/elements/empty_page.png'
        idle 'images/elements/empty_page.png'
        textbutton _("{size=26}Закрыть") action Hide("empty_page_fundamental_mathematics"), Jump('fundamental_mathematics_stand') xalign 0.85 yalign 0.05
