screen stand_map_moais:
    imagemap:
        hover 'images/stands/bg stand6(2).png'
        idle 'images/stands/bg stand6.png'
        hotspot (107, 272, 243, 317) action Jump('teachers')
        hotspot (358, 272, 243, 319) action Jump('kafedra')
        hotspot (609, 272, 238, 315) action Jump('storyNapravleniy')
        hotspot (1072, 268, 244, 319) action Jump('book')
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
    #     action Call("mini_game_moais")


screen info_prepod:
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
                    text _("    К преподаванию привлекаются специалисты, имеющие большой опыт практической работы в области создания программного обеспечения компьютерных систем и вычислительных сетей.\n     В его состав входят:")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Заведующий кафедрой, доцент, кандидат технических наук. Отличный научный руководитель, всегда сможет направить на хорошую дорогу.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Профессор, доктор педагогических наук. Работает с самого открытия института, много выпущенных научных статей и свои и совместно со студентами.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат физико-математических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент, кандидат технических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат педагогических наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент, кандидат физико-математических наук. Добрый человек, но справедливый, любит, когда используют маленькие формы.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент. Директор в компании Блондинка.Ру, также эксперт по обучению в яндексе.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент. Человек загадка..")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Доцент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Доцент. Гуру по базы данным, хорошо знает английский.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Старший преподаватель, кандидат наук.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель. Страшно, страшно… Боятся все студенты…")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Старший преподаватель. Светлейший человек, прекрасный преподаватель, не строгий но справедливый.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Ассистент. Эксперт по олимпиадным задачам и турниров. ")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/man.png}")
                        text _("Ассистент.")
                    hbox:
                        spacing 15
                        text _("{image=images/prepods/female.png}")
                        text _("Ассистент. Эксперт по олимпиадным задачам и турниров. ")
                    #text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_prepod"), Jump ("moais_stand") xalign 0.96

screen info_kafedra:
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
                    text _("\n      Кафедра осуществляет подготовку по специальности {b}{color=#00bfff}«Математическое обеспечение и администрирование информационных систем»{/color}{/b}, также обеспечивает преподавание дисциплин, связанных с {b}программированием и прикладной математикой{/b}, для всех специальностей Института математики и компьютерных наук.\n     {b}Выпускники{/b} специальности «МОиАИС» работают на должностях {b}системных администраторов, инженеров-программистов, сетевых инженеров, руководителей проектов и ИТ- подразделений{/b} в Главном управлении Банка России по Тюменской обл., Департаменте образования администрации г. Тюмени, подразделениях администраций Тюменской области и др.")
                    #text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_kafedra"), Jump ("moais_stand") xalign 0.96

screen info_napravleniya:
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
                    text _("    Профиль\n   - Технологии программирования и анализа больших данных\n    Базовые дисциплины ориентированы на подготовку студентов к профессиональной деятельности в соответствии с требованиями ИТ-отрасли и обеспечивают освоение современных технологий программирования, работы с базами данных, администрирования компьютерных сетей. Особенность программы – подготовка студентов к решению практических задач в области разработки программного обеспечения и системного администрирования, активное привлечение к учебному процессу руководителей и сертифицированных ИТ-специалистов инновационных фирм.")
                    text _("{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_napravleniya"), Jump ("moais_stand") xalign 0.96

label mini_game:
        scene bg 11 with fade
        $renpy.hide_screen("start_minigames")
        if (p):
            menu:
                "{color=000000}Собери код":
                    call start_aplusb from _call_start_aplusb
                    jump mini_game
                "{color=000000}Тренировка памяти":
                    call start_memoria from _call_start_memoria
                    jump mini_game
                "{color=000000}Вернуться":
                    jump next
        else:
            show man_left at center with moveoutleft
            gid "Хочешь отдохнуть?"
            $p = True
            menu:
                "{color=000000}Да":
                    gid "Ну чтож, [name_reader]. Во что хочешь поиграть?"
                    menu:
                        "{color=000000}Собери код":
                            call start_aplusb from _call_start_aplusb_1
                            jump mini_game
                        "{color=000000}Тренировка памяти":
                            call start_memoria from _call_start_memoria_1
                            jump mini_game
                        "{color=000000}Вернуться":
                            jump next
                "{color=000000}Нет":
                    gid "До встречи!"
                    jump next

screen story_page1:
    imagemap:
        xalign 0.5
        yalign 0.5
        hover 'images/elements/moais/pagebook1_2.png'
        idle 'images/elements/moais/pagebook1_1.png'
        hotspot (312, 363, 224, 43) action Jump('story1')
        hotspot (824, 405, 217, 41) action Jump('story2')
        hotspot (952, 671, 203, 46) action Jump('book_open2')
        textbutton _("{size=26}Закрыть") action Hide("story_page1"), Jump('moais_stand') xalign 0.85 yalign 0.05
screen story_page2:
    imagemap:
        xalign 0.5
        yalign 0.5
        hover 'images/elements/moais/pagebook2_2.png'
        idle 'images/elements/moais/pagebook2_1.png'
        hotspot (312, 363, 224, 43) action Jump('story3')
        hotspot (830, 358, 205, 41) action Jump('story4')
        hotspot (213, 674, 224, 41) action Jump('book_open1')
        textbutton _("{size=26}Закрыть") action Hide("story_page2"), Jump('moais_stand') xalign 0.85 yalign 0.05

label moais_stand:
    show screen start_minigames
    call screen stand_map_moais




label teachers:
    scene bg stand6
    call screen info_prepod
    jump moais_stand
    return

label kafedra:
    scene bg stand6
    call screen info_kafedra
    jump moais_stand
    return

label napravleniya:
    scene bg stand6:
    call screen info_napravleniya
    jump moais_stand
    return

label book:
    scene bg stand6
    show book_close with dissolve:
        xalign 0.5
        yalign 0.5
        zoom 0.5
    pause 0.5
    hide book_close with fade
label book_open1:
    call screen story_page1
    return
label book_open2:
    call screen story_page2
    return

label story1:
    scene bg 3 with fade
    show noname_girl at right

    girl "Как мне кажется, каждый второй школьник не знает куда и на кого поступать после выпуска."
    girl "В столь юном возрасте выбирать, как говорят родители, профессию на всю жизнь."
    girl "Это страшно, трудно и сильно бьёт по нервам."
    girl "Они бояться ошибиться, и большая часть как раз таки ошибается."
    girl "Я не стала исключением."
    girl "Выбирая направление, я знала только то, что хотела бы связать свою жизнь с IT и математикой, поэтому ткнула пальцем в небо и оказалась на мясе."
    girl "Спустя месяц пришло осознание, что это совсем не то, чего я ожидала и хотела."
    girl "Закончив первый семестр, ушла в академ."
    girl "Родители, конечно, были в гневе, это же позор!"
    girl "Хотя, как мне кажется, это было одним из самых лучших решений."
    girl "Старая программа была действительно старой, как будто ничего не менялось сто тысяч лет."
    if (persistent.kubik_catch[2]==0):
        show screen kubik("2")
    girl "Примерно, как в школе, контрольные, домашки, больше нагрузки, мало разнообразия, утомительные серые дни с 8:00 до 15:00, 6 дней в неделю."
    girl "Взяв академ, я дала себе время подумать, чего я хочу, поработала, посетила несколько новых для себя городов,"
    girl "а также узнала, что теперь программа изменится, добавится индивидуальная траектория, элективы и пр."
    girl"Вышла досрочно из академа, чтобы не закрывать разницу предметов, а просто начать всё с нуля."
    girl "И да, свершилось!"
    if (persistent.kubik_catch[2]==0):
        hide screen kubik
    girl "Учиться стало интересно, хотя были и минусы, но сравнивая с прошлой программой, это просто пустяки)"
    girl "Всё это я рассказала, чтобы наглядно показать: делать ошибки не плохо! На них учишься и развиваешься."
    girl "Новейшая программа, как мне кажется, учитывает подобные ситуации."
    girl "Осознав, например, на втором курсе, что направление не нравится, можно спокойно перевестись на другое."
    girl "И это крутая возможность для тех, кто ещё не определился."

    $persistent.infinity_count[0] = 1
    $notify_achievment("infinity")
    scene bg stand6 with fade:
        yalign 0.65
    jump book_open1
    return

label story2:
    scene bg 5 with fade:
    show noname_girl at right

    girl "Изначально было страшно переходить в университет, здесь же всё новое - новый вид занятий, новая ответственность."
    girl "Поступление было напряжённым, потому что никогда не знаешь, пройдёшь ли ты в списки, а понравится ли направление…"
    girl "Особенно, когда подаёшь заявление только в один университет - нет подушки безопасности."
    girl "Хотя, можно было и отдохнуть годик после экзаменов, но не важно."

    if (persistent.kubik_catch[3]==0):
        show screen kubik("3")
    girl "А когда ты всё-таки поступил, начинается этап адаптации - изучение системы обучения, новые понятия и привыкание к темпу обучения."
    if (persistent.kubik_catch[3]==0):
        hide screen kubik
    girl "Главное отличие от моего обучения в школе - задания дают не на день-два, а на неделю и больше. Предметы разделены на две части: теоретическая и практическая."
    girl "Плюс экзамены теперь каждые полгода, но, по секрету скажу, закрыть предмет автоматом — это лучшее, что может быть."
    girl "Поэтому за три года обучения я сдавала только один экзамен из множества."
    girl "Немаловажно в первые две недели начать общаться с кем-то из своей группы."
    girl "Так будет проще адаптироваться, да и помощь лишняя не помешает."
    scene bg stand6 with fade

    $persistent.infinity_count[1] = 1
    $notify_achievment("infinity")
    jump book_open1
    return

label story3:
    scene bg 6 with fade
    show noname_girl at right
    girl "Год назад дали роль администратора баз данных, но я ничего не знала и не понимала."
    girl "Было много истерик, панических атак, сонный паралич, бессонницы. Никто не мог направить."
    girl "Когда пришла к преподавателю спросить про бд проекта прошлого года, он сказал писать ему в тимс, с того дня он больше туда не заходил."
    girl "В итоге того проекта(бд) собралась, нашла человека, который понимает базы данных, мне все рассказали, дали статьи и стала мудрецом бд."
    girl "Сейчас бд приносит только улыбку: кто-то говорит бд, я сразу же поворочаюсь в сторону, где было это сказано."
    scene bg stand6 with fade
    $persistent.infinity_count[2] = 1
    $notify_achievment("infinity")
    jump book_open2
    return

label story4:
    scene bg 7 with fade
    show noname_man at right
    boy "Нас также обучают сетевым технологиям, мы работаем в циско и настраиваем ДНС сервера, но это не очень интересно, постоянно сидишь и пишешь айпишники и тд."
    boy "Но вот я помню на одной паре по сетям мы работали с коммутатором, кабелями и др. мне это понравилось."
    boy "К тому же сам процесс происходил в такой форме, что мы разбивались на команды, и пытались сначала сломать все настройки, а потом менялись и настраивали."
    boy "В одной из лабораторных работ нас обучали анимации."
    boy "Ты не поверишь это так круто, когда ты смотришь на это с точки зрения разработки, и теперь я знаю, как это делается."
    scene bg stand6 with fade
    $persistent.infinity_count[3] = 1
    $notify_achievment("infinity")
    jump book_open2
    return

label storyNapravleniy:
    scene bg stand6
    hide screen start_minigames
    show man_right at right with dissolve

    gid "Я очень рад что ты выбрал это направление"
    gid "Сейчас я немного расскажу о том, что тебе предстоит если ты выберешь эту специальность."
    gid "Если ты не знал, что выбрал, то я тебе скажу, что ты выбрал направление подготовки «Математическое обеспечение и администрирование информационных систем», сокращенно МОиАИС, а если еще сокращенно, то МЯСО."
    gid "Интересно почему мясо? К сожалению, я тебе не смогу рассказать, это нужно понять и прочувствовать самому)"
    gid "Ну, что начнем?"
    gid "Как ты уже понял в самом названии говорится о математике и администрировании систем."
    gid "Если ты при виде слова «математика» испугался, то тебе точно не сюда, и скорее всего не на наш институт."
    gid "Но если ты не испугался, то знай, что на данном направлении тебя не будут мучать с решением разных уравнений и задач на бумажке, ты будешь их программировать, а не сидеть с ручкой и листочком."
    gid "Сейчас ты наверно подумал: «И СЛАВА БОГУ, не надо ничего писать» но тут тебе могу сказать, что нет."
    gid "Ну ладно пугать не буду, но будь готов что программирование математики (программирование по формулам, и математическим алгоритмам) та еще задачка."
    gid "Но не только они программируют математику, но еще работают с большими данными в народе таких людей называют специалистами по Data Scientist."
    scene bg 22 with fade
    show man_left at left with dissolve
    gid "Программирования тут очень много, ты научишься проектировать пользовательский интерфейс, сможешь создать свое оконное приложение, где будут куча кнопочек, картинок, разных переключателей, анимаций и многое другое."
    scene bg 23 with fade
    show man_left at left with dissolve
    gid "Как только ты разберешься с простым приложением, ты сможешь отточить свои уже имеющиеся навыки и получить новый опыт в следующем:"
    gid "добавление в свое приложения базы данных для работы с ним, интегрировать разные языки программирования, а также ты сможешь создать свой собственный фотошоп."
    scene bg 24 with fade
    show man_right at right with dissolve

    if (persistent.kubik_catch[1]==0):
        show screen kubik("1")

    gid "Да, да… фотошоп. На одной из дисциплин тебе будут рассказывать про то как устроено изображение, как работает тот или иной фильтр, и любая другая обработка изображения."
    gid "На самом деле это действительно интересно. Причем ты будешь это делать как говорится: «Ручками, все ручками», то есть без использования библиотек, у которых эти методы уже сделаны."

    if (persistent.kubik_catch[1]==0):
        hide screen kubik

    scene bg 25 with fade
    show man_right at right with dissolve
    gid "Интересный на мой взгляд предмет, это «Алгоритмы параллельных вычислений», если у тебя процессор имеет несколько ядер, то ты сможешь разбить свою программу на нескольких потоках."
    scene bg stand6 with fade
    show man_right at right with dissolve
    gid "Сложно звучит? Ну ничего, сейчас тебе не обязательно это понимать, но представлять о своих возможностях после прохождения курса никто не запрещал *)"
    gid "Администрирование систем, непонятно да?"
    menu:
        "{color=000000}Да":
            gid "Я тебя понимаю, но сейчас попробую объяснить."
        "{color=000000}Нет":
            gid "О, ты уже что-то знаешь, раз тебя не пугает."
    gid "Тебя научат как обслуживать вычислительные машины (сервера и тд), на эту тему будет много лекций и практик, где вы будете осуществлять как в реальном времени разные ситуации, так и в виртуальном пространстве Циско."
    gid "Ты наверно видел, в школе когда у учителя не работал компьютер, приходил какой то чел и что то там делал. У этого человека должность системный администратор."
    scene bg 26 with fade
    show man_center at center with dissolve
    gid "Но думаю самое интересное на нашем направлении это заниматься научной деятельностью. Да-да, это действительно интересно, когда ты начинаешь сам исследовать тему, и в ходе ты восполняешься полученными знаниями."
    gid "Первый опыт написании статьи, полученный опыт на научной конференции, это все полезно, как и для тебя так и для науки. А еще ты сможешь получить плюшки в виде повышенной стипендии."
    scene bg stand6 with fade
    show man_right at right with dissolve
    gid "В основном выпускники данного направления идут работать программистом/разработчиком, т. к. дают очень хорошую базу, связанную с программированием математики."
    gid "Здесь не будут обучать разрабатывать сайты, тут больше уклон обучению студентов к решению практических задач. Отрабатываются практикумы на реальном и виртуальном сетевом и компьютерном оборудовании."
    gid "Если ты хочешь реально сидеть и писать код для различных компаний или же заниматься администрированием, то это точно для тебя. Приходи мы тебя ждем)"
    hide man_right with dissolve
    jump moais_stand
