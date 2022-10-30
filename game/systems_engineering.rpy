screen stand_map_systems_engineering:
    imagemap:
        hover 'images/stands/bg stand4(2).png'
        idle 'images/stands/bg stand4.png'
        hotspot (407, 257, 214, 269) action Jump('teachers_systems_engineering')
        hotspot (648, 257, 214, 269) action Jump('kafedra_systems_engineering')
        hotspot (873, 252, 211, 274) action Jump('book_systems_engineering')
        hotspot (1103, 254, 217, 269) action Jump('info_naprav_systems_engineering_menu')
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
    #     action Call("mini_game_systems_engineering")

screen info_prepod_systems_engineering:
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
                    text _("    Состав кафедры программной и системной инженерии")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Заведующий кафедрой, профессор, доктор технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Профессор, доктор технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Профессор, доктор технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
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
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Ассистент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
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
        textbutton _("Закрыть") action Hide("info_prepod_systems_engineering"), Jump ("systems_engineering_stand") xalign 0.96

screen info_kafedra_systems_engineering:
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
                    text _("    Кафедра является выпускающей по следующим образовательным программам: ")
                    text _("       {b}{color=#00bfff}Мехатроника и робототехника{/color}{/b}\n       {b}{color=#00bfff}Прикладная информатика{/color}{/b}")
                    text _("\n    У программы подготовки {b}МиР{/b} профиль {color=#00bfff}«Автоматизированные системы управления технологическим процессом».{/color}")
                    text _("    Программа готовит бакалавров, занимающихся {b}настройкой и эксплуатацией мехатронных и робототехнических систем для применения в автоматизированном производстве, а также диагностикой, контролем технического состояния и испытаниями подсистем.{/b}")
                    text _("    Подготовка ведется на базе профессиональных промышленных компонентов на станциях модульной производственной системы FESTO MPS - ведущего мирового поставщика технологий автоматизации, лидера в области производственного обучения и образовательных программ. Направление востребовано для интенсивно развивающихся производственных предприятий.  ")
                    text _("    Специалистов в данной компетенции выпускает около 50 российских вузов. Оборудование, аналогичное тому, что установлено в ТюмГУ, имеют {color=#00bfff}не более десяти университетов России.{/color} Возможность обучаться появилась благодаря появившейся в вузе уникальной для региона лаборатории.")
                    text _("\n    У программы подготовки {b}ПИ{/b} профиль {color=#00bfff}«Разработка информационных систем бизнеса».{/color}")
                    text _("    Студенты изучают дисциплины теоретического и прикладного практического характера, выполняют курсовые работы, связанные с созданием программных приложений и проектированием информационных систем, изучают современные языки и средства разработки программ, а также современные программные решения для построения корпоративных информационных систем и интеллектуального анализа данных. Большое внимание уделяется {b}разработке вопросам проектирования информационных систем - от моделирования и анализа бизнес-процессов до разработки приложений для автоматизации деятельности.{/b}")
                    text _("    Главным преимуществом программы является ее ориентация на практическое формирование компетенций программистов-разработчиков, которые не только знают отдельные языки программирования, но понимают и умеют {b}реализовать в проектах бизнес-потребности, умеют разрабатывать инновационные ИТ-решения, в том числе, используя сторонние сервисы и платформы.{/b}")
                    #text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_kafedra_systems_engineering"), Jump ("systems_engineering_stand") xalign 0.96

screen info_napravleniya_systems_engineering:
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
                    text _("    РОБОРТРОБОТРОБОТРОБОТтексттексттексттексттексттексттексттексттексттекст")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_napravleniya_systems_engineering"), Jump ("systems_engineering_stand") xalign 0.96

label mini_game_systems_engineering:
        scene bg 11 with fade
        if (p):
            menu:
                "{color=000000}Собери код":
                    call start_aplusb from _call_start_aplusb_4
                    jump mini_game_systems_engineering
                "{color=000000}Тренировка памяти":
                    call start_memoria from _call_start_memoria_4
                    jump mini_game_systems_engineering
                "{color=000000}Вернуться":
                    jump systems_engineering_stand
        else:
            show man_left at center with moveoutleft
            gid "Хочешь отдохнуть?"
            $p = True
            menu:
                "{color=000000}Да":
                    gid "Ну чтож, [name_reader]. Во что хочешь поиграть?"
                    menu:
                        "{color=000000}Собери код":
                            call start_aplusb from _call_start_aplusb_5
                        "{color=000000}Тренировка памяти":
                            call start_memoria from _call_start_memoria_5
                        "{color=000000}Вернуться":
                            jump systems_engineering_stand
                "{color=000000}Нет":
                    gid "До встречи!"
                    jump systems_engineering_stand

label systems_engineering_stand:
    show screen start_minigames
    call screen stand_map_systems_engineering

label teachers_systems_engineering:
    scene bg stand4
    call screen info_prepod_systems_engineering
    jump systems_engineering_stand
    return

label kafedra_systems_engineering:
    scene bg stand4
    call screen info_kafedra_systems_engineering
    jump systems_engineering_stand
    return

label info_naprav_systems_engineering_menu:
    scene bg stand4
    menu:
        "{color=000000}Мехатроника и роботехника":
            jump meh_roboth
        "{color=000000}Прикладная информатика":
            jump pi

label meh_roboth:
    scene bg stand4
    hide screen start_minigames
    show man_left at left with dissolve
    gid "Направление Мехатроника и робототехника звучит очень красиво и многообещающе неправда ли? "
    gid "Распространённая ошибка для первокурсников — это то, что они считают, что будут работать с какими-нибудь роботами или разрабатывать протез."
    gid "Ну, спешу огорчить это не так… "
    gid "На первом курсе ты познакомишься с такой программой, как автокад после у тебя появится три профильных предмета, первый из них это программирование "
    gid "Из раздела физики будет «Электротехника», это довольно интересный предмет "
    gid "Из математики «Основы статистической обработки данных измерений» или же ОСОДИ он включает в себя теорию вероятности.  "
    gid "По ней лучше искать дополнительные материалы, библиотека или интернет что тебе удобнее, и придется очень много решать, чтобы закрыть предмет. "
    scene bg 18
    show man_left at left with dissolve
    gid "На втором курсе, будет довольно интересный предмет «Гидропневмоавтоматика», на нем дадут пощупать стенды, гидропневмоприводы, посоставлять электро-схемы как в электронном варианте на компьютере, так и на стендах все это опробовать. "
    gid "Дальше начнется проектирование на этом предмете и знакомство с такой программой как Церис и автокад электрика. "
    gid "В Церисе будешь делать станции, которые в последствии нужно будет переносить в автокат и делать по ним несколько схем.  "
    gid "И в этот же год на втором курсе, появится предмет «Программирование промышленных контролеров», который будет сопровождать тебя до конца твоей профессиональной деятельности. "
    gid "На третьем курсе снова начнется математика, электрические двигатели, но "
    gid "Самое интересное это учебная практика, которая в себе совмещает большую часть профильных предметов, и накопленных знаний за эти годы в университете. "
    gid "Вот здесь как раз тебе дадут пощупать станции роботов, как это можно представить в конвейерах, как все это соединяется, как после написать на них программу.  "
    gid "Сделай все правильно и защищай спокойно свою практику. "
    scene bg 19
    show man_left at left with dissolve
    gid "По поводу летней производственной практики она случится после третьего курса и во втором семестре четвертого курса, когда уже будет подготовка к диплому.  "
    gid "Так каковой практики довольно мало и нужно заранее искать, куда ты захочешь пойти, чтобы в последствии не прыгать с одного места на другое, а пройти все в одном месте и получить опыт, который возможно поможет в университете. "
    gid "В целом с учебой не будет проблем если ты ходишь на пары и занимаешься нужным делом. "
    gid "Советую уделить особое внимание ОСОДИ, т. к. там нужно всегда приходить на пары и сдавать лабы вовремя, это все чтобы потом не нужно было разгребать в конце семестра то, что ты не сможешь разгрести. "
    gid "После выпуска, что ты сможешь работать по профессии Инженером АУТП, инженеры, программисты, будете программировать контролеры, схемы, делать документацию. "
    gid "В общем впереди все будет очень интересно."
    jump systems_engineering_stand

label pi:
    scene bg stand4
    hide screen start_minigames
    show man_right at right with dissolve
    gid "Профиль разработка информационных систем бизнеса"
    gid "Студенты изучают дисциплины теоретического и прикладного практического характера, выполняют курсовые работы, связанные с созданием программных приложений и проектированием информационных систем,"
    gid "изучают современные языки и средства разработки программ, а также современные программные решения для построения корпоративных информационных систем и интеллектуального анализа данных."
    gid "Студенты осваивают языки программирования и средства интернет-технологий, углубленно изучают вэб-программирование, а также программные платформы корпоративных информационных систем."
    gid "Большое внимание уделяется разработке вопросам проектирования информационных систем – от моделирования и анализа бизнес-процессов до разработки приложений для автоматизации деятельности."
    gid "Главным преимуществом программы является ее ориентация на практическое формирование компетенций программистов-разработчиков, которые не только знают отдельные языки с средства программирования,"
    gid "но понимают и умеют реализовать в проектах бизнес-потребности, умеют разрабатывать  инновационные ИТ-решения, в том числе, используя сторонние сервисы и платформы."
    jump systems_engineering_stand

label napravleniya_systems_engineering:
    scene bg stand4
    call screen info_napravleniya_systems_engineering
    jump systems_engineering_stand
    return

label book_systems_engineering:
    scene bg stand4
    show book_close with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    pause 0.5
    hide book_close with fade

label book_open_systems_engineering:
    call screen empty_page_systems_engineering
    return

screen empty_page_systems_engineering:
    imagemap:
        xalign 0.5
        yalign 0.5
        hover 'images/elements/empty_page.png'
        idle 'images/elements/empty_page.png'
        textbutton _("{size=26}Закрыть") action Hide("empty_page_systems_engineering"), Jump('systems_engineering_stand') xalign 0.85 yalign 0.05
