label start:
    #call screen test
    scene bg story 15

    $friendson_count = True

    show man_left at center with moveoutleft
    noname "Здравствуй! Ты здесь, чтобы узнать об университете и нашем скромном ИМиКН поближе?"
    noname "Я твой гид на сегодняшнюю прогулку."
    noname "Давай для начала познакомимся. Как мне тебя называть?"
    label name_reader:
        $ name_reader = renpy.input("Введите имя:", length = 20, exclude="0123456789!@*&^%$#.,+=_?<>/\|()").strip()
        if name_reader == "":
            noname "Я бы хотел знать, как тебя называть..."
            jump name_reader
    noname "[name_reader] - красивое имя."
    noname "Теперь, для равноценного знакомства, я должен бы назвать тебе свое, но..."
    noname "Знаешь, [name_reader], этот мир давно прогнил... Имена, они не являются такой значимой вещью..."
    noname "Однажды меня уже назвали, только не смейся, но мое имя {w}Гид..."
    noname "Оно и определило мою дальнейшую судьбу."
    noname "Поэтому я бы хотел от тебя подарок, дай мне имя, которое тебе приходить в голову."
    noname "В общем, скажи как ты хочешь меня называть?"
    $ name_gid = renpy.input("Введите имя:", length = 20, default = "Элайджа", exclude="0123456789!@*&^%$#.,+=_?<>/\|()").strip()
    if name_gid.lower() == "элайджа":
        gid "Ого! Это мое любимое имя. Спасибо!"
    elif name_gid.lower() == "гид":
        gid "Ох, ладно..."
    elif name_gid.lower() == "хуй":
        gid "Я не мог подумать, что тебе нравится такое..."
    else:
        gid "Отлично! Тогда продолжим нашу экскурсию."
    gid "Прежде чем мы начнем нашу экскурсию, давай я тебе покажу буклет."
    gid "На нем ты сможешь просмотреть историю университета, историю имикна или же продолжить уже по самому корпусу математиков и узнать о них уже."
    label buklet_show:
        scene bg story 15 with dissolve
        show buklet_rotate
        pause 2
        hide buklet_rotate
        call screen buklet
    scene bg 0 with fade
    show man_center with dissolve
    gid "[name_reader], думаю тебе понятно, что я буду тебя сопровождать на протяжении всей экскурсии."
    gid "В конце нашей экскурсии мне предстоит узнать, понравилось тебе или нет. Полезно ли было наше времяпровождение."
    gid "[name_reader], может ты хочешь понять почему я так стараюсь?"
    menu:
        "{color=000000}Да":
            gid "Знаешь, меня заставили."
            gid "Да-да, все так. И все из-за злополучного имени..."
            gid "Но вообще, от твоего ответа будет зависить только моя премия в этом месяце."
            $friendson_count = False

        "{color=000000}Нет":
            gid "Что ж, твое право. Но чтоб ты знал, от этого зависеть моя премия в этом месяце."
    gid "Сейчас мы пойдем дальше по коридору, на {a=glossary:kaf}{color=#DC143C}кафедры{/color}{/a}, к которым относятся направления."
    gid "Ты уже знаешь на какое направление ты хочешь поступить?"
    menu:
        "{color=000000}Да":
            gid "Отлично, тогда пойдем!"
        "{color=000000}Нет":
            gid "Тогда, я даю тебе выбор, что тебе нравится, и на основе этого я проведу тебя к похожему на твои интересы направлению."
            menu:
                "{color=000000}Решать математические задачи":
                    $math = True
                "{color=000000}Написать калькулятор":
                    $moais = True
                "{color=000000}Управлять людьми":
                    $pi = True
                "{color=000000}Делать сайты":
                    $isit = True
                "{color=000000}Роботы":
                    $roboth = True
                "{color=000000}Моделирование":
                    $model = True
                "{color=000000}Защищать информацию":
                    $ibis = True
                "{color=000000}Учить детей:)":
                    $ped = True
            gid "Отлично, тогда пойдем!"
    gid "[name_reader], кажется, мы немного торопимся!"
    gid "Скажи, [name_reader], как много ты знаешь об обучении в универстите?"
    menu:
        "{color=000000}Много":
            gid "Тогда тебе не нужно знать о нашей системе обучения?"
            gid "У нее еще такое забавное название “2+2”. Так и хочется ответить 4!"
            menu:
                "{color=000000}Я хочу узнать":
                    gid "Тогда я тебе расскажу об этом."
                    jump obshiy_block
                "{color=000000}Не хочу узнавать":                  
                    gid "Тогда наш маршрут был верным."
                    gid "Мы познакомились всего 5 минут, а уже понимаем друг друга с полуслова."
        "{color=000000}Практические ничего...":
            gid "Тогда я тебе сейчас расскажу о нашей системе “2+2”."
            jump obshiy_block
    # if (moais == True):
    #     $proverka = True
    #     gid "Слушай, а ты не хочешь попробовать себя в программировании?"
    #     menu prog_aplusb:
    #         "{color=000000}Да":
    #             jump start_aplusb
    #         "{color=000000}Нет":
    #             jump next
    #     $proverka = False
    # if(roboth==True):
    #     gid "Слушай, а ты не хочешь проверить свою память?"
    #     menu prog_memoria:
    #         "{color=000000}Да":
    #             jump start_memoria
    #         "{color=000000}Нет":
    #             gid "Тогда пойдем дальше!"
    #             jump next
    #else:
    jump next
    return

label next:
    if (moais == True):
        jump moais_stand
    elif (math == True):
        jump fundamental_mathematics_stand
    elif (pi  or isit):
        jump information_systems_stand
    elif (roboth == True):
        jump systems_engineering_stand
    elif (model == True):
        jump fundamental_mathematics_stand
    elif (ibis == True):
        jump information_security_stand
    elif (ped == True):
        jump mathematical_logic_stand
    else:
        call screen map

label the_end:
    $renpy.hide_screen("start_minigames")
    scene bg 15 with fade
    
    show man_center at center with dissolve
    gid "[name_reader], теперь, как и обещал мне нужно услышать твое мнение."
    gid "Тебе понравилась наша экскурсия?"
    menu:
        "{color=000000}Да":
            show podsvetka at sepiya2 with dissolve
            gid "Я очень рад это слышать."
            gid "В этом месяце мне наконец выплатят премию!"
            hide podsvetka with dissolve
            gid "Не желаешь проверить себя?"
            menu:
                "{color=000000}Да":
                    jump start_drop_the_end
                "{color=000000}Нет":
                    jump end_tochno_end
            #jump end_tochno_end
        "{color=000000}Нет":
            gid "Очень жаль, я хотел создать для тебя незабываемое впечатление."
            gid "Ну, за премию, конечно, жаль больше..."
            gid "В любом случае, я надеюсь, что мы еще встретимся, если вдруг решишь поступать к нам."
            gid "Не желаешь проверить себя?"
            menu:
                "{color=000000}Да":
                    jump start_drop_the_end
                "{color=000000}Нет":
                    jump end_tochno_end
            #jump end_tochno_end
    
    #return

label end_tochno_end:
    gid "Надеюсь, мы с тобой еще встретимся, когда ты будешь поступать к нам."
    gid "Я верю в тебя, [name_reader]."
    gid "До встречи!"