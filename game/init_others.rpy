define gid = Character('[name_gid]')
define noname = Character('???', color = "#808080")
define girl = Character('Девушка')
define boy = Character('Парень')


image bg black = "#000000"

init:
    $math = False
    $moais = False
    $pi = False
    $isit = False
    $roboth = False
    $model = False
    $ibis = False
    $ped = False
    $persistent.kubik_catch = [0,0,0,0]
    $proverka=False
    $p = False
    $kb = False
    $ib = False
    $ibas = False
    $friendson_count = True
    $persistent.infinity_count = [0,0,0,0]

init python:
    def null_next():
        math = False
        moais = False
        pi = False
        isit = False
        roboth = False
        model = False
        ibis = False
        ped = False
        kb = False
        ib = False
        ibas = False

    def set_kubik_catch(index): 
        persistent.kubik_catch[int(index)] = 1

    def showStand(standName):
        renpy.show_screen("helpimages")
        renpy.show_screen(standName)



screen start_minigames:
    zorder 100
    imagebutton:
        xalign 1.0
        yalign 0.5
        idle "images/elements/strelka.png"
        hover "images/elements/strelka_hover.png"
        action Call("mini_game")


screen kubik(index):
    imagebutton:
        xalign 0.9
        yalign 0.9
        hover "images/achievements/cuberube.png"
        idle "images/achievements/cuberube.png"
        # action SetVariable("kubik_catch", kubik_catch + 1), Hide('kubik')
        action Function(set_kubik_catch, index), Function(notify_achievment, "cuberube"), Hide("kubik")

screen helpimages:
    zorder 100
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


screen info_panel:
    modal True
    zorder 100
    frame:
        xsize 1200
        ysize 800
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 30 # Расстояние, между баром и боксом.
            xsize 1000 # Размер, дабы не растекалось по всему экрану.
            ysize 600
            align (.5, .5) # Центруем
            viewport id "view_id123": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
                xfill False
                yfill False
                mousewheel True # Разрешаем прокрутку мышью.
                vbox:
                    text _("{b}{color=#00bfff}Модеус{/color}{/b} это сервис, который включает индивидуальное расписание, выбор элективов/модулей, промежуточные оценки и итоговые, описание программ и заданий.")
                    text _("\n{b}{color=#00bfff}Электив{/color}{/b} - это дисциплина по выбору, исходя из интересов. А также это возможность познакомиться с новыми преподавателями и студентами для проектной работы в различных областях.")
                    text _("\n{b}{color=#00bfff}Корпоративная почта{/color}{/b} - это личная почта, после зачисления для каждого студента создается учетная запись, в Microsoft. С помощью нее, будет осуществляться диалог с преподавателями, и еще один не мало важный факт, при ее использовании предоставляется бесплатно лицензия на Microsoft office и другие.")
                    text _("\n{b}{color=#00bfff}Лабораторная работа (лаба, лр){/color}{/b} - это задание, которое предоставляет лектор, на практических занятиях, для определения усвоения пройденного материала на основе лекции.")
                    text _("\n{b}{color=#00bfff}Технологическая практика{/color}{/b} - это дисциплина, на которой можно опробовать все знания, которые получили за время учебы, создать свой проект и его защитить.")
                    text _("\n{b}{color=#00bfff}Научный руководитель{/color}{/b} - это преподаватель, который отвечает за твою научную работу или же проект, к нему можно обращаться по любым вопросам связанных с работой.")
                    text _("\n{b}{color=#00bfff}Базы данных{/color}{/b} - это множество данных, которые включают в себя определённые правила, принципы хранения, описания и управления этими данными.")
                    text _("\n{b}{color=#00bfff}Семестр{/color}{/b} - это определение учебного процесса, длится он полгода (6 месяцев). В него входят занятия, сессия и каникулы.")
                    text _("\n{b}{color=#00bfff}ДНС сервер{/color}{/b} - это специализированный компьютер (или группа), который хранит IP-адреса сайтов. Последние, в свою очередь, привязаны к именам сайтов и обрабатывает запросы пользователя.")
                    text _("\n{b}{color=#00bfff}Коммутатор{/color}{/b} - это устройство, предназначенное для соединения нескольких узлов компьютерной сети в пределах одного или нескольких сегментов сети.")
                    text _("\n{b}{color=#00bfff}Алгоритм{/color}{/b} - это математически выверенная и точная последовательность действий для достижения определённого результата или решения какой-либо задачи.")
                    text _("\n{b}{color=#00bfff}Data Science{/color}{/b} - это область информатики, которая специализируется на вопросах анализа и обработки Big Data (массивных объемов информации, находящихся в неструктурированном виде).")
                    text _("\n{b}{color=#00bfff}Библиотека{/color}{/b} - это набор готовых функций, классов и объектов для решения каких-то задач.")
                    text _("\n{b}{color=#00bfff}Пользовательский интерфейс{/color}{/b} - это набор инструментов, позволяющих пользователю взаимодействовать с операционной системой компьютера, мобильного устройства или других видов техники.")
                    text _("\n{b}{color=#00bfff}Научная деятельность{/color}{/b} - это направленная на получение и применение новых знаний для решения технологических, гуманитарных и иных проблем обеспечения функционирования науки, техники и производства как единой системы")
                    text _("\n{b}{color=#00bfff}Исследование{/color}{/b} — это процесс изучения чего-либо; результат такого действия (исследования), научный труд, документ с описанием изученного объекта или чего-то.")
                    text _("\n{b}{color=#00bfff}Стенд{/color}{/b} — это лабораторные стенды предназначены для изучения базовых узлов и принципов построения автоматических линий и мехатронных систем.")
                    text _("\n{b}{color=#00bfff}Гидропневмопривод{/color}{/b} — это две части связанные механизмом управления, обеспечивающим регулирование скорости и давления, необходимую последовательность движений в цикле и реверсирование двигателя, состоит из насоса (компрессора) и питаемого им гидро-пневмодвигателя.")
                    text _("\n{b}{color=#00bfff}Электро-схема{/color}{/b} — это документ, составленный в виде условных изображений или обозначений составных частей изделия, действующих при помощи электрической энергии, и их взаимосвязей.")
                    text _("\n{b}{color=#00bfff}AutoCAD{/color}{/b} — это двух- и трёхмерная система автоматизированного проектирования и черчения.")
                    #text _("\n{b}{color=#00bfff}Исследование{/color}{/b} — это ")
                    #text _("\n{color=ff0000}Раздел находится в разработке{/color}") xalign 0.5
        vbar value YScrollValue("view_id123") xalign 1.0# Бар, как второй элемент hbox-а.
        textbutton _("Закрыть") action Hide("info_panel") xalign 0.96
