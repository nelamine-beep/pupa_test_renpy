# словарь подсказок (пары 'ключ':'значение')
# 'ключ' должен быть на латинице
# 'значение' может быть любым (возможен его перевод)
default glossary_dict = {
    'Test_1':_("Текст подсказки\n(может содержать символы (), [], {{}, :, \\, \', \", %, $ и т.д., и {i}текстовые тэги{/i})."),
    'TL':_("'Подсказка слева вверху'"),
    'TR':_("'Подсказка справа вверху'"),
    'BL':_("'Подсказка слева внизу'"),
    'BR':_("\"Подсказка справа внизу\""),
    'kaf':_("Это объединение преподавателей разных специализаций и квалификаций, ведущих одновременно педагогическую и научно-исследовательскую работу в какой-то отрасли науки."),
    }

init python:
    def glossary_handler(target):
        '''
        Функция, которая выполняется при нажатии на гиперссылку.
        Сейчас не делает ничего, но может открывать экран словаря
        или делать прыжок к метке.
        '''
        pass

    def glossary_hyperlink_sensitive(target=None):
        '''
        Функция, которая выполняется когда фокус установлен на гиперссылку
        (например, когда на нее наведен указатель мыши).
        '''

        # если гиперссылка в фокусе и экран 'glossary_scr' еще не показан
        if target and not renpy.get_screen('glossary_scr'):
            # если значение гиперссылки начинается с "glossary"
            if target.startswith("glossary"):
                # определим координаты для показа подсказки
                # (это будут координаты указателя мыши)
                x, y = renpy.get_mouse_pos()
                # определим привязку (anchor) для рамки с подсказкой
                xa = 1.0 if x > int(config.screen_width / 2) else 0.0
                ya = 1.0 if y > int(config.screen_height / 2) else 0.0
                # отбросим у ключевого слова начало "glossary:",
                # и получим текст подсказки из словаря
                glossary_text = glossary_dict[target[9:]]
                # покажем экран подсказки, передав в него необходимые значения
                renpy.show_screen('glossary_scr', txt=glossary_text, frame_pos=(x, y), frame_align=(xa, ya))
                # обновим объекты на экране
                renpy.restart_interaction()

        # если гиперссылка не в фокусе или подсказка уже показана
        else:
            # скроем экран подсказки
            renpy.hide_screen('glossary_scr')
            # обновим объекты на экране
            renpy.restart_interaction()


    # добавим обработчику гиперссылок новое значение "glossary"
    # и установим для него функцию glossary_handler
    config.hyperlink_handlers["glossary"] = glossary_handler

    # установим функцию glossary_hyperlink_sensitive в качестве функции,
    # которая исполняется когда гиперссылка оказывается в фокусе
    style.default.hyperlink_functions = (
        hyperlink_styler,
        hyperlink_function,
        glossary_hyperlink_sensitive)

# трансформация появления/скрытия подсказки
transform glossary_tr(t=0.5):
    on show:
        alpha 0.0
        linear t alpha 1.0
    on hide:
        linear t alpha 0.0

# экран подсказки
# в него необходимо передать значения:
# txt - текст подсказки
# frame_pos - положение рамки подсказки на экране
# frame_align - привязку (anchor) рамки
screen glossary_scr(txt, frame_pos=(0, 0), frame_align=(0.0, 0.0)):

    frame:
        xmaximum 500
        pos frame_pos
        align frame_align
        at glossary_tr

        text "{}".format(txt) slow_cps 50

# пример различных положений показа подсказки
screen test_glossary_in_screen_scr():
    text "... {a=glossary:TL}Текст 1{/a}..." align(0.35, 0.05)
    text "... {a=glossary:TR}Текст 2{/a}..." align(0.75, 0.05)
    text "... {a=glossary:BL}Текст 3{/a}..." align(0.35, 0.65)
    text "... {a=glossary:BR}Текст 4{/a}..." align(0.75, 0.65)
