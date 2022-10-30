label map_open:
    call screen map

screen map:
    modal True
    zorder 100
    fixed:
        xsize 1920 ysize 1080
        add "images/elements/map.jpg" align (.5, .5)
    fixed:
        xsize 1920 ysize 1080
        button:
            xpos 560 ypos 130
            xsize 143 ysize 133
            idle_background "images/elements/icon_map1.png"
            hover_foreground "images/elements/icon_map.png"
            tooltip "{b}Кафедра программного обеспечения{/b}"
            action Function(null_next), SetVariable("moais", True), Jump("moais_stand")
        button:
            xpos 530 ypos 230
            xsize 143 ysize 133
            idle_background "images/elements/icon_map1.png"
            hover_foreground "images/elements/icon_map.png"
            tooltip "{b}Кафедра алгебры и математической логики{/b}"
            action Function(null_next), SetVariable("ped", True), Jump("mathematical_logic_stand")
        button:
            xpos 1140 ypos 130
            xsize 143 ysize 133
            idle_background "images/elements/icon_map1.png"
            hover_foreground "images/elements/icon_map.png"
            tooltip "{b}Информационная безопасность{/b}"
            action  Function(null_next), SetVariable("ibis", True), Jump("information_security_stand")
        button:
            xpos 530 ypos 640
            xsize 143 ysize 133
            idle_background "images/elements/icon_map1.png"
            hover_foreground "images/elements/icon_map.png"
            tooltip "{b}Кафедра программной\nи системной инженерии{/b}"
            action  Function(null_next), SetVariable("roboth", True), Jump("systems_engineering_stand")
        button:
            xpos 760 ypos 130
            xsize 143 ysize 133
            idle_background "images/elements/icon_map1.png"
            hover_foreground "images/elements/icon_map.png"
            tooltip "{b}Кафедра информационных систем{/b}"
            action  Function(null_next), SetVariable("pi", True), Jump("information_systems_stand")
        button:
            xpos 530 ypos 490
            xsize 143 ysize 133
            idle_background "images/elements/icon_map1.png"
            hover_foreground "images/elements/icon_map.png"
            tooltip "{b}Кафедра фундаментальной математики\nи механики{/b}"
            action  Function(null_next), SetVariable("math", True), Jump("fundamental_mathematics_stand")
        button:
            xpos 1400 ypos 850
            xsize 143 ysize 133
            idle_background "images/elements/icon_map2.png"
            hover_foreground "images/elements/icon_map3.png"
            tooltip "{b}Завершить экскурсию{/b}"
            action  Function(null_next), Jump("the_end")

    $ tooltip = GetTooltip()
    if tooltip:
        fixed:
            xpos 840 ypos 800
            text "{color=#000000}[tooltip]{/color}"
