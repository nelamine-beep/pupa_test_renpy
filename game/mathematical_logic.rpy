screen stand_map_mathematical_logic:
    imagemap:
        hover 'images/stands/bg stand5(2).png'
        idle 'images/stands/bg stand5.png'
        hotspot (243, 274, 190, 253) action Jump('teachers_mathematical_logic')
        hotspot (448, 271, 190, 253) action Jump('kafedra_mathematical_logic')
        hotspot (649, 268, 201, 256) action Jump('info_naprav_mathematical_logic')
        hotspot (853, 261, 201, 264) action Jump('book_mathematical_logic')
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
    #     action Call("mini_game_mathematical_logic")

screen info_prepod_mathematical_logic:
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
                    text _("    Состав кафедры алгебры и математической логики")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Заведующий кафедрой, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат наук")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
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
                        text _("{image=images/prepods/female.png}")
                        text _("Ассистент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Ассистент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Ассистент.")
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_prepod_mathematical_logic"), Jump ("mathematical_logic_stand") xalign 0.96

screen info_kafedra_mathematical_logic:
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
                    text _("\n      Кафедра осуществляет подготовку по специальности {b}{color=#00bfff}«Педагогическое образование с 2 профилями: математика и информатика»{/color}{/b}.")
                    # text _("\n      Кафедра осуществляет подготовку по специальности {b}{color=#00bfff}«Педагогическое образование с 2 профилями: математика и информатика»{/color}{/b}. По этой программе готовит бакалавров, владеющих следующими {color=#00bfff}компетенциями:{/color}")
                    # text _("\n        {color=#00bfff}1.{/color} современные технологии образования школьников и ")
                    # text _("          знаниями по математике и информатике, достаточными")
                    # text _("          реализации образовательных программ в ")
                    # text _("          средних образовательных учреждениях, проведения")
                    # text _("          элективные курсов")
                    # text _("        {color=#00bfff}2.{/color} проектная деятельность учащихся")
                    # text _("        {color=#00bfff}3.{/color} организация и проведение турниров, конкурсов и олимпиад")
                    # text _("           по математике и информатике")
                    # text _("        {color=#00bfff}4.{/color} контакты с родителями школьников")
                    text _("\n      Сотрудники кафедры продолжают осуществлять преподавание таких основных дисциплин как алгебра, аналитическая и дифференциальная геометрия, математическая логика и теория алгоритмов, теория чисел, вариационное исчисление и методы оптимизации. Для других институтов университета читаются курсы по высшей математике (Институты геолого-географического и биологического направлений, ИНЗЕМ, ИНБИО).")
                    text _("\n      Выпускники данной специальности работают {b}в средних образовательных учреждениях, организации сферы культуры и социальной сферы, организации, активно применяющие в своей работе математические методы, (например, авиакомпания UTair){/b}.")
                    #text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_kafedra_mathematical_logic"), Jump ("mathematical_logic_stand") xalign 0.96

screen info_napravleniya_mathematical_logic:
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
                    text _("    ПЕДПЕДПЕДПЕДПЕДПЕДтексттексттексттексттексттексттексттексттексттекст")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_napravleniya_mathematical_logic"), Jump ("mathematical_logic_stand") xalign 0.96

# label mini_game_mathematical_logic:
#         scene bg 11 with fade
#         if (p):
#             menu:
#                 "{color=000000}Собери код":
#                     call start_aplusb from _call_start_aplusb_10
#                     jump mini_game_mathematical_logic
#                 "{color=000000}Тренировка памяти":
#                     call start_memoria from _call_start_memoria_10
#                     jump mini_game_mathematical_logic
#                 "{color=000000}Вернуться":
#                     jump mathematical_logic_stand
#         else:
#             show man_left at center with moveoutleft
#             gid "Хочешь отдохнуть?"
#             $p = True
#             menu:
#                 "{color=000000}Да":
#                     gid "Ну чтож, [name_reader]. Во что хочешь поиграть?"
#                     menu:
#                         "{color=000000}Собери код":
#                             call start_aplusb from _call_start_aplusb_11
#                         "{color=000000}Тренировка памяти":
#                             call start_memoria from _call_start_memoria_11
#                         "{color=000000}Вернуться":
#                             jump mathematical_logic_stand
#                 "{color=000000}Нет":
#                     gid "До встречи!"
#                     jump mathematical_logic_stand

label mathematical_logic_stand:
    show screen start_minigames
    call screen stand_map_mathematical_logic

label teachers_mathematical_logic:
    scene bg stand5
    call screen info_prepod_mathematical_logic
    jump mathematical_logic_stand
    return

label kafedra_mathematical_logic:
    scene bg stand5
    call screen info_kafedra_mathematical_logic
    jump mathematical_logic_stand
    return

label napravleniya_mathematical_logic:
    scene bg stand5:
    call screen info_napravleniya_mathematical_logic
    jump mathematical_logic_stand
    return

label book_mathematical_logic:
    scene bg stand5
    show book_close with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    pause 0.5
    hide book_close with fade

label book_open_mathematical_logic:
    call screen empty_page_mathematical_logic
    return

screen empty_page_mathematical_logic:
    imagemap:
        xalign 0.5
        yalign 0.5
        hover 'images/elements/empty_page.png'
        idle 'images/elements/empty_page.png'
        textbutton _("{size=26}Закрыть") action Hide("empty_page_mathematical_logic"), Jump('mathematical_logic_stand') xalign 0.85 yalign 0.05

label info_naprav_mathematical_logic:
    scene bg stand5
    hide screen start_minigames
    show man_right at right with dissolve
    gid "По этой программе готовит бакалавров, владеющих следующими компетенциями"
    gid "Современные технологии образования школьников и знаниями по математике и информатике, "
    gid "Достаточными для реализации образовательных программ в средних образовательных учреждениях, проведения элективные курсов"
    gid "Проектная деятельность учащихся"
    gid "Организация и проведение турниров, конкурсов и олимпиад по математике и информатике, "
    gid "Контакты с родителями школьников"
    gid "Выпускники данной специальности работают в средних образовательных учреждениях, организации сферы культуры и социальной сферы"
    gid "организации, активно применяющие в своей работе математические методы, (например, авиакомпания UTair)."
    gid "Приходи и попробуй. До скорого) "
    jump information_systems_stand
    return
