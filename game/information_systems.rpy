screen stand_map_information_systems:
    imagemap:
        hover 'images/stands/bg stand3(2).png'
        idle 'images/stands/bg stand3.png'
        hotspot (625, 277, 206, 273) action Jump('teachers_information_systems')
        hotspot (830, 277, 202, 273) action Jump('kafedra_information_systems')
        hotspot (1043, 277, 206, 273) action Jump('info_naprav_information_systems')
        hotspot (1259, 277, 212, 273) action Jump('book_information_systems')
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
    #     action Call("mini_game_information_systems")

screen info_prepod_information_systems:
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
                    text _("    Состав кафедры Информационных систем")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Заведующий кафедрой, профессор, доктор технических наук. Автор более 150 научных и учебно-методических трудов в области интеллектуальных систем поддержки принятия решений, методов ситуационного управления, компьютерных технологий обучения  и интернет-технологий.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Профессор, доктор технических наук.")
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
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель.")
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_prepod_information_systems"), Jump ("information_systems_stand") xalign 0.96

screen info_kafedra_information_systems:
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
                    text _("    Кафедра является выпускающей по образовательной программе {color=#00bfff}Информационные системы и технологии{/color} (академический и прикладной бакалавриат).")
                    text _("    Образовательная программа ориентирована на современные профессиональные стандарты «Разработчик Web и мультимедийных приложений» и \"Программист\". Студенты изучают дисциплины теоретического и практического характера, выполняют работы по созданию программных приложений. Значительный объем занимают прикладные технологические дисциплины и проектный практикум. Особенностью обучения является не только глубокое {b}освоение технологий   вэб- и мобильной разработки, но также изучение методов управления созданием информационных ресурсов и систем.{/b}")
                    text _("    В 2014 году при кафедре организован Центр сертифицированного ИТ-образования, который предлагает обучение по программам дополнительного образования в сфере ИТ (освоение платформы 1С, программирование на языках 1C, Java, вэб-дизайн и др.)")
                    text _("    {color=#00bfff}Важным преимуществом{/color} образовательной программы является то, что ее студенты не только знают отдельные языки программирования, но {b}понимают и умеют реализовать в проектах бизнес-потребности, могут создавать инновационные ИТ-решения, используя современные технологии разработки, сервисы и платформы.{/b} Это позволяет выпускникам успешно продолжать профессиональную карьеру как в качестве программиста-разработчика, так и в роли системного аналитика, а далее - стать архитектором продукта и руководителем ИТ-разработкой.")
                    #text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_kafedra_information_systems"), Jump ("information_systems_stand") xalign 0.96

screen info_napravleniya_isit_information_systems:
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
                    text _("    ИСИТИСИТИСИТИСИИТтексттексттексттексттексттексттексттексттексттекст")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_napravleniya_isit_information_systems"), Jump ("information_systems_stand") xalign 0.96

# label mini_game_information_systems:
#         scene bg 11 with fade
#         if (p):
#             menu:
#                 "{color=000000}Собери код":
#                     call start_aplusb from _call_start_aplusb_6
#                     jump mini_game_information_systems
#                 "{color=000000}Тренировка памяти":
#                     call start_memoria from _call_start_memoria_6
#                     jump mini_game_information_systems
#                 "{color=000000}Вернуться":
#                     jump information_systems_stand
#         else:
#             show man_left at center with moveoutleft
#             gid "Хочешь отдохнуть?"
#             $p = True
#             menu:
#                 "{color=000000}Да":
#                     gid "Ну чтож, [name_reader]. Во что хочешь поиграть?"
#                     menu:
#                         "{color=000000}Собери код":
#                             call start_aplusb from _call_start_aplusb_7
#                         "{color=000000}Тренировка памяти":
#                             call start_memoria from _call_start_memoria_7
#                         "{color=000000}Вернуться":
#                             jump information_systems_stand
#                 "{color=000000}Нет":
#                     gid "До встречи!"
#                     jump information_systems_stand

label information_systems_stand:
    show screen start_minigames
    call screen stand_map_information_systems

label teachers_information_systems:
    scene bg stand3
    call screen info_prepod_information_systems
    jump information_systems_stand
    return

label kafedra_information_systems:
    scene bg stand3
    call screen info_kafedra_information_systems
    jump information_systems_stand
    return

label info_naprav_information_systems:
    scene bg 14
    hide screen start_minigames
    show man_right at right with dissolve
    gid "Кафедра информационных систем и технологии это лучшие место для того, чтобы стать именно программистом, причем в самом его понимании этого слова."
    gid "На кафедре даются базовые компетенции такие как, базы данных, математики и дают их довольно четко."
    gid "Действительно обучают правильным языкам программирования, с которыми ты сто процентов столкнешься при поиске или приеме на работу. "
    gid "Интересно знать какие это языки?"
    menu:
        "{color=#000000}Да, мне интересно":
            gid "Это языки веб разработчиков такие как php, java, javaScript."
            gid "Хотел бы узнать подробнее?"
            menu:
                "{color=#000000}Да":
                    scene bg 8
                    show man_right at right with dissolve
                    gid "Ну поехали, начнем с HTML и CSS"
                    gid "Они используются в связке, HTML и CSS, по сути, не являются языками программирования. Они определяют не то, как будет действовать сайт, а лишь то, как он будет выглядеть."
                    gid "Если написать сайт, применяя только HTML и CSS, он окажется набором статических страниц, где единственными интерактивными элементами будут ссылки."
                    gid "По сути это лицо сайта, и ни один сайт не обходится без HTML, поэтому его базовое знание необходимо каждому, кто планирует заниматься веб-разработкой."
                    gid "Язык JavaScript отвечает за интерактивность и динамически меняющуюся информацию на страницах сайта."
                    gid "Например, когда вы вводите в форму сайта номер телефона в неверном формате или забываете о значке @ при вводе электронного адреса, JavaScript позволяет сайту моментально об этом узнать и подсветить поле красным."
                    gid "А вот счётчик просмотров этой страницы, меняющийся в реальном времени: на HTML-сайте можно было бы показать только статическое число. "
                    gid "Кратко, он служит для того, чтобы научить сайт понимать тебя. "
                    gid "Java — не просто другой язык, а почти противоположность JavaScript хотя название порой путают с JavaScript.  "
                    gid "Он более консервативный выбор, проверенный годами. Его предпочитают использовать в бэкенде тех проектов, для которых надежность куда важнее веяний моды, — например, банковских систем. "
                    gid "Python и если его сравнивать с Java, то он будет выигрывать в объёме кода, но проигрывать в скорости выполнения.  "
                    gid "Для большого высоконагруженного проекта, где важна производительность, Python будет не лучшим выбором."
                    gid "Язык отлично подойдёт для стартапа: например, чтобы показать инвестору прототип до того, как закончатся все инвестиционные деньги."
                    gid "Ну и наконец, PHP — популярный и относительно несложный.  "
                    gid "Его используют Facebook, «ВКонтакте», «Википедия» и, к слову, vc.ru. На нём также основана система WordPress, под управлением которой работает около четверти всех сайтов. "
                    gid "PHP лёгок в освоении, однако у него спорная репутация, и две эти вещи связаны.  "
                    gid "Из-за простоты языка в индустрии появилось много новичков с непреодолимым желанием профессионально заниматься PHP-разработкой, не вникая в детали.  "
                    gid "Так появилось много плохого PHP-кода. Именно из-за этого одни люди критикуют PHP, а другие возражают, что в умелых руках он показывает себя только с лучшей стороны. "
                "{color=#000000}Нет":
                    gid "Все, правильно. Узнаешь все когда поступишь, нечего сейчас голову забивать лишней информацией."
        "{color=#000000}Нет":
            gid "Пошли дальше."
    scene bg 7
    show man_right at right with dissolve
    gid "Также преподаватели очень лояльно относятся к тому если студент работает. "
    gid "Конечно, если ты работаешь уже по своей профессии, а не в Макдональдсе или в этажах. "
    gid "Не, ничего против данных компаний никто не имеет, но тогда не жди к себе поблажек. "
    gid "Если ты еще не понял, то ты будешь изучать все что связанно с веб-разработкой, сейчас это очень востребовано, у каждой компании, неважно большой или маленькой есть свой сайт. И как ты думаешь кем они создаются?)"
    gid "Приходи и попробуй. До скорого) "
    jump information_systems_stand
    return

label book_information_systems:
    scene bg stand3
    show book_close with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    pause 0.5
    hide book_close with fade

label book_open_information_systems:
    call screen empty_page_information_systems
    return

screen empty_page_information_systems:
    imagemap:
        xalign 0.5
        yalign 0.5
        hover 'images/elements/empty_page.png'
        idle 'images/elements/empty_page.png'
        textbutton _("{size=26}Закрыть") action Hide("empty_page_information_systems"), Jump('information_systems_stand') xalign 0.85 yalign 0.05
