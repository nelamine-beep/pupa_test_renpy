# #
# #      КАК ДЕЛАТЬ ДОСТИЖЕНИЯ
# # Если условия выполнились в скрипте, то прописать (пример ачивки с кубиком рубика):
# #  show screen notify_acievment("cuberube")
# #
# # переменные для разных достижений:
# #
# # cuberube - кубик рубика
# # genius - гении мыслят иначе
# # infinity - бесконечность не предел
# # friendson - сын маминой подруги


# #не забыть прописать кнопку на галлерею по типу action ShowMenu("gallery")



# init python:

#     gallery_ach = {"cuberube": {"name": "Кубик-Рубика", "how_to": "Собрать все кубики", "description": "Вы преисполнились в познании университета"},
#     "genius": {"name": "гении мыслят иначе", "how_to": "При сборе кода составить выражение: \"a+b=int c;\"", "description": "Гениев никогда не воспринимают всерьёз"},
#     "infinity": {"name": "Бесконечность не предел", "how_to": "Прочтите все истории студентов", "description": "Знания - сила"},
#     "friendson": {"name": "Сын маминой подруги", "how_to": "Пропустить все рассказы Гида", "description": "Вам не нужны помощники"}}


# screen gallery:
#     tag menu
#     modal True

#     add "images/achievements/bg gallery.jpg"

#     frame:
#         style "game_menu_content_frame"
#         xsize 1920
#         vbox:
#             xalign 0.5
#             hbox:
#                 ypos 0.25
#                 xalign 0.5
#                 ysize 300
#                 xsize 1100
#                 if kubik_catch == 4:
#                     imagebutton:
#                         idle "images/achievements/cuberube.png"
#                         action ShowMenu("show_achiev", ("cuberube", "True"))
#                         xalign 0.5
#                         xpos 0.3
                
#                 else:
#                     imagebutton:
#                         idle "images/achievements/cuberube_locked.png"
#                         action ShowMenu("show_achiev", ("cuberube", "False"))
#                         xalign 0.5
#                         xpos 0.3


#                 if persistent.genius=="yes":
#                     imagebutton:
#                         idle  "images/achievements/genius.png"
#                         action ShowMenu("show_achiev", ("genius", "True"))
#                         xalign 0.5
#                         xpos 0.5
#                 else:
#                     imagebutton:
#                         idle  "images/achievements/genius_locked.png"
#                         action ShowMenu("show_achiev", ("genius", "False"))
#                         xalign 0.5
#                         xpos 0.5
    

#                 if persistent.infinity=="yes":
#                     imagebutton:
#                         idle  "images/achievements/infinity.png"
#                         action ShowMenu("show_achiev", ("infinity", "True"))
#                         xalign 0.5
#                         xpos 0.7
#                 else:
#                     imagebutton:
#                         idle  "images/achievements/infinity_locked.png"
#                         action ShowMenu("show_achiev", ("infinity", "False"))
#                         xalign 0.5
#                         xpos 0.7

#             hbox:
#                 ypos 0.7
#                 xalign 0.5
#                 ysize 300
#                 xsize 1100
#                 if persistent.friendson=="yes":
#                     imagebutton:
#                         idle "images/achievements/friendson.png"
#                         action ShowMenu("show_achiev", ("friendson", "True"))
#                         xalign 0.5
#                         yalign 0.72
#                 else:
#                     imagebutton:
#                         idle  "images/achievements/friendson_locked.png"
#                         action ShowMenu("show_achiev", ("friendson", "False"))
#                         xalign 0.5
#                         yalign 0.72

    
#     textbutton "Главное меню" action Return() xalign 0.1 yalign 0.95



# screen show_achiev(name):
#     tag menu
#     modal True

#     add "images/achievements/bg gallery black.jpg"
#     add "images/achievements/gradient.png"

#     frame:
#         style "game_menu_content_frame"
#         xalign 0.1 

#         xsize 0.6

#         if (name[1]!="False"):
#             text "Название: " + gallery_ach[name[0]]["name"] size 70 yalign 0.4 color "#ffffff"

#             text "{i}" + gallery_ach[name[0]]["description"] + "{/i}" size 50 yalign 0.6 color "#ffffff"

#         text "Как получить: " + gallery_ach[name[0]]["how_to"] size 30 yalign 0.8 color "#a1a1a1"
#     if (name[1]!="False"):
#         image "images/achievements/"+name[0]+"_full.png" yalign 0.5 xalign 0.9
#     else:
#         image "images/achievements/"+name[0]+"_full_locked.png" yalign 0.5 xalign 0.9

#     textbutton "Вернуться" action ShowMenu("gallery") xalign 0.1 yalign 0.95



# init python:
#     def show_achiev(name):
#         if (name=="cuberube" and persistent.cuberube!="yes"):
#             persistent.cuberube="yes"
#             renpy.show_screen("show_notify", name)
#         elif (name=="genius" and persistent.genius!="yes"):
#             persistent.genius="yes"
#             renpy.show_screen("show_notify", name)
#         elif (name=="infinity" and persistent.infinity!="yes"):
#             persistent.infinity="yes"
#             renpy.show_screen("show_notify", name)
#         elif (name=="friendson" and persistent.friendson!="yes"):
#             persistent.friendson="yes"
#             renpy.show_screen("show_notify", name)
        
    
 
# screen show_notify(name):
#     tag noti
#     zorder 100
#     frame at notify_achievment_appear:
#         align (0.5, 0.0)
#         background "#67dcf185"
#         xsize 500
#         ysize 150
#         hbox:
#             align(0.5, 0.5)
#             vbox:
#                 text "Получено достижение!" size 23 color "#ffffffff"
#                 text gallery_ach[name]["name"] size 28 color "#ffffffff"
#             image "images/achievements/"+name+".png" zoom 0.5
#     timer 6.25 action Hide("show_notify") at notify_achievment_appear


# transform notify_achievment_appear:
#     on show:
#         alpha 0
#         linear .25 alpha 1.0
#     on hide:
#         linear .5 alpha 0.0

#
#      КАК ДЕЛАТЬ ДОСТИЖЕНИЯ
# Если условия выполнились в скрипте, то прописать (пример ачивки с кубиком рубика):
#  $notify_achievment("cuberube")
#
# переменные для разных достижений:
#
# cuberube - кубик рубика
# genius - гении мыслят иначе
# infinity - бесконечность не предел
# friendson - сын маминой подруги


#не забыть прописать кнопку на галлерею по типу action ShowMenu("gallery")



init python:

    gallery_ach = {"cuberube": {"name": "Кубик-Рубика", "how_to": "Собрать все кубики", "description": "Вы преисполнились в познании университета"},
    "genius": {"name": "гении мыслят иначе", "how_to": "При сборе кода составить выражение: \"a+b=int c;\"", "description": "Гениев никогда не воспринимают всерьёз"},
    "infinity": {"name": "Бесконечность не предел", "how_to": "Прочтите все истории студентов", "description": "Знания - сила"},
    "friendson": {"name": "Сын маминой подруги", "how_to": "Пропустить все рассказы Гида", "description": "Вам не нужны помощники"}}


screen gallery:
    tag menu
    modal True

    add "images/achievements/bg gallery.jpg"

    frame:
        style "game_menu_content_frame"
        xsize 1920
        vbox:
            xalign 0.5
            hbox:
                ypos 0.25
                xalign 0.5
                ysize 300
                xsize 1100
                if persistent.cuberube=="yes":
                    imagebutton:
                        idle "images/achievements/cuberube.png"
                        action ShowMenu("show_achiev", ("cuberube", "True"))
                        xalign 0.5
                        xpos 0.3
                
                else:
                    imagebutton:
                        idle "images/achievements/cuberube_locked.png"
                        action ShowMenu("show_achiev", ("cuberube", "False"))
                        xalign 0.5
                        xpos 0.3


                if persistent.genius=="yes":
                    imagebutton:
                        idle  "images/achievements/genius.png"
                        action ShowMenu("show_achiev", ("genius", "True"))
                        xalign 0.5
                        xpos 0.5
                else:
                    imagebutton:
                        idle  "images/achievements/genius_locked.png"
                        action ShowMenu("show_achiev", ("genius", "False"))
                        xalign 0.5
                        xpos 0.5
    

                if persistent.infinity=="yes":
                    imagebutton:
                        idle  "images/achievements/infinity.png"
                        action ShowMenu("show_achiev", ("infinity", "True"))
                        xalign 0.5
                        xpos 0.7
                else:
                    imagebutton:
                        idle  "images/achievements/infinity_locked.png"
                        action ShowMenu("show_achiev", ("infinity", "False"))
                        xalign 0.5
                        xpos 0.7

            hbox:
                ypos 0.7
                xalign 0.5
                ysize 300
                xsize 1100
                if persistent.friendson=="yes":
                    imagebutton:
                        idle "images/achievements/friendson.png"
                        action ShowMenu("show_achiev", ("friendson", "True"))
                        xalign 0.5
                        yalign 0.72
                else:
                    imagebutton:
                        idle  "images/achievements/friendson_locked.png"
                        action ShowMenu("show_achiev", ("friendson", "False"))
                        xalign 0.5
                        yalign 0.72

    
    textbutton "Вернуться" action Return() xalign 0.1 yalign 0.95



screen show_achiev(name):
    tag menu
    modal True

    add "images/achievements/bg gallery black.jpg"
    add "images/achievements/gradient.png"

    frame:
        style "game_menu_content_frame"
        xalign 0.1 

        xsize 0.6

        if (name[1]!="False"):
            text "Название: " + gallery_ach[name[0]]["name"] size 70 yalign 0.4 color "#ffffff"

            text "{i}" + gallery_ach[name[0]]["description"] + "{/i}" size 50 yalign 0.6 color "#ffffff"

        text "Как получить: " + gallery_ach[name[0]]["how_to"] size 30 yalign 0.8 color "#a1a1a1"
    if (name[1]!="False"):
        image "images/achievements/"+name[0]+"_full.png" yalign 0.5 xalign 0.9
    else:
        image "images/achievements/"+name[0]+"_full_locked.png" yalign 0.5 xalign 0.9

    textbutton "Вернуться" action ShowMenu("gallery") xalign 0.1 yalign 0.95



init python:
    def notify_achievment(name):
        if (name=="cuberube" and persistent.cuberube!="yes" and (not 0 in persistent.kubik_catch)):
            persistent.cuberube="yes"
            renpy.show_screen("show_notify", name)
        elif (name=="genius" and persistent.genius!="yes"):
            persistent.genius="yes"
            renpy.show_screen("show_notify", name)
        elif (name=="infinity" and persistent.infinity!="yes" and (not 0 in persistent.infinity_count)):
            persistent.infinity="yes"
            renpy.show_screen("show_notify", name)
        elif (name=="friendson" and persistent.friendson!="yes" and friendson_count):
            persistent.friendson="yes"
            renpy.show_screen("show_notify", name)
        

init:
    transform customzoom:
        zoom 0.5

screen show_notify(name):
    tag noti
    zorder 100
    frame at notify_achievment_appear:
        align (0.5, 0.0)
        background "#67dcf185"
        xsize 500
        ysize 150
        hbox:
            align(0.5, 0.5)
            vbox:
                text "Получено достижение!" size 23 color "#ffffffff"
                text gallery_ach[name]["name"] size 28 color "#ffffffff"
            imagebutton:
                idle "images/achievements/"+name+".png" 
                action ShowMenu("show_achiev", (name, "True"))
                at customzoom

    timer 6.25 action Hide("show_notify") at notify_achievment_appear


transform notify_achievment_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0