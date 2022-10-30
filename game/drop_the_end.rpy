# init python:

#     def piece_dragged(drags, drop):

#         if not drop:
#             store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][0] = drags[0].x
#             store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][1] = drags[0].y
#             return

#         store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
#         store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]

#         return True

# # label main_menu:
# #     jump start

# screen jigsaw_drop_the_end:

#     draggroup:
#         # тут куда перемещать
#         drag:
#             drag_name "00"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[0]

#         drag:
#             drag_name "10"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[1]

#         drag:
#             drag_name "20"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[2]

#         drag:
#             drag_name "30"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[3]
        
#         drag:
#             drag_name "40"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[4]

#         drag:
#             drag_name "50"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[5]

#         drag:
#             drag_name "60"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[6]    

#         drag:
#             drag_name "70"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[7]

#         drag:
#             drag_name "80"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[8]

#         drag:
#             drag_name "90"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[9]

#         # тут то что можно перемещать вырезанное из картинки
#         drag:
#             drag_name "00 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 50 , 60, 220, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[0][0] ypos piecelist[0][1]

#         drag:
#             drag_name "01 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 310 , 60, 220, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[1][0] ypos piecelist[1][1]

#         drag:
#             drag_name "02 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 230, 280, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[2][0] ypos piecelist[2][1]

#         drag:
#             drag_name "03 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 390 , 230, 220, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[3][0] ypos piecelist[3][1]

#         drag:
#             drag_name "04 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 370, 350, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[4][0] ypos piecelist[4][1]

#         drag:
#             drag_name "05 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 510, 430, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[5][0] ypos piecelist[5][1]

#         drag:
#             drag_name "06 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 660, 170, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[6][0] ypos piecelist[6][1]

#         drag:
#             drag_name "07 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 350 , 660, 200, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[7][0] ypos piecelist[7][1]

#         drag:
#             drag_name "08 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 200 , 760, 250, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[8][0] ypos piecelist[8][1]

#         drag:
#             drag_name "09 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 110 , 900, 380, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[9][0] ypos piecelist[9][1]



# label puzzle_drop_the_end:
#     call screen jigsaw_drop_the_end
#     if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
#         python:
#             t1 = piecelist[movedpiece]
#             t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
#             piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
#             piecelist[t2] = t1
#     else:
#         $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
#     if piecelist == [[coorlistx[0],coorlisty[0]],
#                         [coorlistx[1],coorlisty[0]],
#                         [coorlistx[2],coorlisty[0]],
#                         [coorlistx[3],coorlisty[0]],
#                         [coorlistx[0],coorlisty[1]],
#                         [coorlistx[1],coorlisty[1]],
#                         [coorlistx[2],coorlisty[1]],
#                         [coorlistx[3],coorlisty[1]],
#                         [coorlistx[0],coorlisty[2]],
#                         [coorlistx[1],coorlisty[2]],
#                         [coorlistx[2],coorlisty[2]],
#                         [coorlistx[3],coorlisty[2]]]:
#         jump win_drop_the_end            

#     jump puzzle_drop_the_end

# label start_drop_the_end:
#     scene bg_fon2_the_end
#     image whole = "images/draganddrop/for_drop_the_end.png"
#     python:
#         coorlistx = [1100] # тут координата х по столбцам
#         coorlisty = [70, 180, 290, 380, 465, 550, 650, 735, 820, 910] # тут строки координата у
#         piecelist = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] # тут общее количество объектов
#         # тут чтоб картинки рандомно были по местоположению
#         for i in range(10):
#             x = renpy.random.randint(0, 559) + 621
#             y = renpy.random.randint(0, 480)
#             piecelist[i] = [x,y]
#         movedpiece = 0
#         movedplace = [0, 0]
#     show man_center at center with dissolve
#     gid "Тебе нужно разместить направление, как ты понял кто выпускается"
#     hide man_center
#     jump puzzle_drop_the_end

# label win_drop_the_end:
#     scene black
#     show whole
#     if(proverka == True):
#         gid "Ты справился, теперь мы можем пойти дальше"
#         jump next
#     #else:
#     #    jump mini_game
init python:
    
    def piece_dragged(drags, drop):
        
        if not drop:
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][0] = drags[0].x
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][1] = drags[0].y
            return
            
        store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
        store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]
        
        return True

# screen jigsaw_drop_the_end:
    
#     draggroup:
        
#         drag:
#             drag_name "00"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[0]
            
#         drag:
#             drag_name "01"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[1]
            
#         drag:
#             drag_name "02"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[2]
            
#         drag:
#             drag_name "03"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[3]
            
#         drag:
#             drag_name "04"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[4]
            
#         drag:
#             drag_name "05"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[5]
            
#         drag:
#             drag_name "06"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[6]
            
#         drag:
#             drag_name "07"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[7]
            
#         drag:
#             drag_name "08"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[8]
            
#         drag:
#             drag_name "09"
#             child "images/draganddrop/empty space the end.png"
#             draggable False
#             xpos coorlistx[0] ypos coorlisty[9]

            
#         drag:
#             drag_name "00 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 50 , 60, 220, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[0][0] ypos piecelist[0][1]
            
#         drag:
#             drag_name "01 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 310 , 60, 220, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[1][0] ypos piecelist[1][1]
            
#         drag:
#             drag_name "02 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 230, 280, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[2][0] ypos piecelist[2][1]
            
#         drag:
#             drag_name "03 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 390 , 230, 220, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[3][0] ypos piecelist[3][1]
            
#         drag:
#             drag_name "04 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 370, 350, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[4][0] ypos piecelist[4][1]
            
#         drag:
#             drag_name "05 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 510, 430, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[5][0] ypos piecelist[5][1]
            
#         drag:
#             drag_name "06 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 660, 170, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[6][0] ypos piecelist[6][1]
            
#         drag:
#             drag_name "07 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 350 , 660, 200, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[7][0] ypos piecelist[7][1]
            
#         drag:
#             drag_name "08 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 200 , 760, 250, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[8][0] ypos piecelist[8][1]
            
#         drag:
#             drag_name "09 piece"
#             child im.Crop("images/draganddrop/for_drop_the_end.png", 110 , 900, 380, 120)
#             droppable False
#             dragged piece_dragged
#             xpos piecelist[9][0] ypos piecelist[9][1]

screen jigsaw_drop_the_end:
    
    draggroup:
        
        drag:
            drag_name "10"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[0]
            
        drag:
            drag_name "01"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[1]
            
        drag:
            drag_name "12"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[2]
            
        drag:
            drag_name "03"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[3]
            
        drag:
            drag_name "14"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[4]
            
        drag:
            drag_name "05"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[5]
            
        drag:
            drag_name "16"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[6]
            
        drag:
            drag_name "07"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[7]
            
        drag:
            drag_name "18"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[8]
            
        drag:
            drag_name "09"
            child "images/draganddrop/empty space the end.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[9]

            
        drag:
            drag_name "00 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 50 , 60, 220, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[0][0] ypos piecelist[0][1]
            
        drag:
            drag_name "01 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 310 , 60, 220, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]
            
        drag:
            drag_name "02 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 230, 280, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]
            
        drag:
            drag_name "03 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 390 , 230, 220, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]
            
        drag:
            drag_name "04 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 370, 350, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[4][0] ypos piecelist[4][1]
            
        drag:
            drag_name "05 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 510, 430, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[5][0] ypos piecelist[5][1]
            
        drag:
            drag_name "06 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 100 , 660, 170, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[6][0] ypos piecelist[6][1]
            
        drag:
            drag_name "07 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 350 , 660, 200, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[7][0] ypos piecelist[7][1]
            
        drag:
            drag_name "08 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 200 , 760, 250, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[8][0] ypos piecelist[8][1]
            
        drag:
            drag_name "09 piece"
            child im.Crop("images/draganddrop/for_drop_the_end.png", 110 , 900, 380, 120)
            droppable False
            dragged piece_dragged
            xpos piecelist[9][0] ypos piecelist[9][1]

label puzzle_drop_the_end:
    call screen jigsaw_drop_the_end
    if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
        python:
            t1 = piecelist[movedpiece]
            t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
            piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
            piecelist[t2] = t1
    else:
        $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
    python:
        k=0
        for piece in piecelist:
            if piece in piecelist2:
                k = k + 1    
    if (k==10):
        jump end_tochno_end

    jump puzzle_drop_the_end

label start_drop_the_end:
    scene bg_fon2_the_end
    image whole = "images/draganddrop/bg_fon2_the_end.png"
    python:
        coorlistx = [670, 1100] 
        coorlisty = [70, 170, 270, 370, 450, 530, 640, 725, 810, 890]
        piecelist = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        for i in range(10):
            x = renpy.random.randint(0, 59) + 21
            y = renpy.random.randint(0, 280)
            piecelist[i] = [x,y]
        movedpiece = 0
        movedplace = [0, 0]
        piecelist2 =[[coorlistx[(y+1)%2], coorlisty[y]] for y in range(len(coorlisty))]

    jump puzzle_drop_the_end
    
