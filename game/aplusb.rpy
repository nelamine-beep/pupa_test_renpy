init python:

    def piece_dragged(drags, drop):

        if not drop:
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][0] = drags[0].x
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][1] = drags[0].y
            return

        store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
        store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]

        return True

# label main_menu:
#     jump start

screen jigsaw:

    draggroup:
        # тут куда перемещать
        drag:
            drag_name "00"
            child "images/draganddrop/empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[0]

        drag:
            drag_name "10"
            child "images/draganddrop/empty space2.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[0]

        drag:
            drag_name "20"
            child "images/draganddrop/empty space3.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[0]

        drag:
            drag_name "30"
            child "images/draganddrop/empty space4.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[0]

        # тут то что можно перемещать вырезанное из картинки
        drag:
            drag_name "00 piece"
            child im.Crop("images/draganddrop/for_drop.png", 300 , 340, 250, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[0][0] ypos piecelist[0][1]

        drag:
            drag_name "01 piece"
            child im.Crop("images/draganddrop/for_drop.png", 550 , 340, 90, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]

        drag:
            drag_name "02 piece"
            child im.Crop("images/draganddrop/for_drop.png", 640 , 340, 260, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]

        drag:
            drag_name "03 piece"
            child im.Crop("images/draganddrop/for_drop.png", 910 , 340, 75, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]



label puzzle:
    call screen jigsaw

    # тут какая то хуйня но оно отвечает чтоб можно было перемещать и оно пермещалось на этот квадрат
    if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
        python:
            t1 = piecelist[movedpiece]
            t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
            piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
            piecelist[t2] = t1
    else:
        $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]

    # тут условие на правильность изображения
    if piecelist == [[coorlistx[2],coorlisty[0]],
                        [coorlistx[1],coorlisty[0]],
                        [coorlistx[0],coorlisty[0]],
                        [coorlistx[3],coorlisty[0]]]:
        $notify_achievment("genius")
    if piecelist == [[coorlistx[0],coorlisty[0]],
                        [coorlistx[1],coorlisty[0]],
                        [coorlistx[2],coorlisty[0]],
                        [coorlistx[3],coorlisty[0]]]:
        jump win

    jump puzzle

label start_aplusb:
    scene bg_fon2
    image whole = "images/draganddrop/for_drop.png"
    python:
        coorlistx = [300, 560, 650, 915] # тут координата х по столбцам
        coorlisty = [340] # тут строки координата у
        piecelist = [[0,0],[0,0],[0,0],[0,0]] # тут общее количество объектов
        # тут чтоб картинки рандомно были по местоположению
        for i in range(4):
            x = renpy.random.randint(0, 559) + 621
            y = renpy.random.randint(0, 480)
            piecelist[i] = [x,y]
        movedpiece = 0
        movedplace = [0, 0]
    show man_center at center with dissolve
    gid "Тебе нужно разместить объекты так, что бы код был правильным"
    gid "Здесь ничего сложного, ты справишься. Я в тебя верю!"
    hide man_center
    jump puzzle

label win:
    scene black
    show whole
    return
    # if(proverka == True):
    #     gid "Ты справился, теперь мы можем пойти дальше"
    #     jump next
    # else: 
        #jump mini_game_moais
    #else:
    #    jump mini_game
