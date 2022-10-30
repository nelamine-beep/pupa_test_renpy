screen buklet:
    imagemap:
        xalign 0.5
        hover "images/elements/buklet2.png"
        idle "images/elements/buklet1.png"
        hotspot (536, 439, 227, 181) action Jump('history_tumgu')
        hotspot (1018, 454, 173, 296) action Jump('history_imikn')
        hotspot (764, 278, 291, 195) action Return('True')

image buklet_rotate:
    xalign 0.5 yalign 0.5
    "buklet1"
    zoom 0.1
    rotate 0
    linear 2 rotate 1080 zoom 1.0 xalign 0.5 yalign 0.5

image bg_atl:
    "bg story 7" with dissolve
    pause 2.0
    "bg story 8" with dissolve

transform sepiya:
    zoom 1.02
    #yalign 0 xalign 1
    pos (0,0)
    linear 0.3 pos (-2,-1)
    linear 0.3 pos (0,0)
    pause 0.2
    pos (0,0)
    linear 0.3 pos (2,-1)
    linear 0.3 pos (0,0)
    repeat

transform sepiya2:
    zoom 1.02
    #yalign 0 xalign 1
    pos (0,0)
    linear 0.3 pos (-3,-1)
    linear 0.3 pos (0,0)
    pause 0.2
    pos (0,0)
    linear 0.3 pos (3,-1)
    linear 0.3 pos (0,0)
    repeat

label history_tumgu:
    scene bg black with fade
    show animaciya at sepiya
    centered "{font=Vivaldi script.ttf}{size=80}{cps=20}{color=#ffffff}Открытие в Тюмени в 1930 году Агропединститута –\nпервого высшего учебного заведения в городе."
    scene bg story 17 at sepiya2 with fade:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 30.0 xalign 0.5 yalign 0.8 zoom 1.3
    show animaciya at sepiya
    "С 1934 по 1940 год происходит переименования в Тюменский педагогический институт."
    "Сюда начинают приезжать специалисты из разных высших учебных заведений страны."
    "Активно развивается научно-исследовательская деятельность в институте."
    "Выходит первый выпуск научно-исследовательского издания «Ученые записки»."
    "Защищены первые кандидатские диссертации."
    "Проводятся межрегиональные научные конференции."
    scene bg story 6 at sepiya with dissolve
    show animaciya at sepiya
    "В 1941-1945 годах все силы и средства института мобилизованы на оборону страны."
    "Десятки преподавателей уходят на фронт, один из корпусов становится госпиталем, а общежития передаются военному ведомству."
    "Но даже в военных условиях институт продолжает выполнять свою главную задачу - готовить педагогические кадры."
    "Также продолжается и научная деятельность института."
    scene bg_atl with dissolve
    "В послевоенное время жизнь в вузе постепенно приходит в норму."
    "Проводится первый день открытых дверей."
    "Спортивные команды института получают призовые места на всесоюзных первенствах."
    scene bg black with fade
    centered "{font=Vivaldi script.ttf}{size=80}{cps=20}{color=#ffffff}1 января 1973 года Тюменский педагогический институт был преобразован в государственный университет."
    scene bg story 10 with fade
    "На базе ТюмГУ создается Международная высшая школа банковского дела и Международный лингвистический центр, который становится методической базой новых технологий в обучении иностранным языкам."
    scene bg story 11 with dissolve
    "ТюмГУ входит в топ-50 лучших вузов стран СНГ, Грузии, Латвии, Литвы и Эстонии. В университете созданы новые учебные структуры."
    scene bg story 13 with dissolve
    "90 лет непрерывного роста и покорения новых вершин, достижения высоких планок и грандиозных целей."
    #scene bg5 with dissolve
    "Как провинциальный пединститут стал одним из самых динамично развивающихся университетов России?"
    scene bg black with dissolve
    centered "{font=Vivaldi script.ttf}{size=80}{cps=20}{color=#ffffff}Ответ - в самой истории университета, богатого ключевыми событиями."
    show podsvetka at sepiya2 with fade
    show logo with dissolve:
        xalign 0.5 yalign 0.5
        zoom 3.0
        linear 5.0 zoom 2.0
    centered ""
    jump buklet_show

label history_imikn:
    scene bg black with fade
    centered "{font=Vivaldi script.ttf}{size=80}{cps=20}{color=#ffffff}Поговорим о математиках?"
    scene bg story 4 with fade:
        xalign 0.5
    "В 1990-е годы значительно возрос интерес к проблемам информационных технологий и в 2000 году Физико-математический факультет переименован в Факультет математики и компьютерных наук."
    scene bg story 15 with dissolve
    "Чуть позднее из факультета создан Институт математики и компьютерных наук. В 2007 году Институт математики и компьютерных наук начал переход на двухуровневую систему высшего образования."
    scene bg story 22 with dissolve
    "Институт принимал участие в реализации Программы развития инновационной инфраструктуры ТюмГУ, что позволило существенно укрепить его материально-лабораторную базу."
    scene bg imikn with dissolve
    "В настоящее время в состав Института математики и компьютерных наук вошли кафедры:"
    "алгебры и математической логики:"
    "информационных систем,"
    "информационной безопасности,"
    "программного обеспечения,"
    "программной и системной инженерии,"
    "фундаментальной математики и механики."
    jump buklet_show
