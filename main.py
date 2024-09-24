import eel
import colorama
import init
import save_doc
import out
# import tempfile
# import os

colorama.init()
eel.init("web")

@eel.expose
def get_text(theme, name, group, colledge):
        try:
                if ((theme!='')and(name!='')and(group!='')and(colledge!='')):
                        t = open('tngc.txt', 'w')
                        t.write(theme + '\n' + name + '\n' + group + '\n' + colledge)
                        t.close()

                        codes.info(0)

                        exit_code = main()
                        info = 'the function has completed its work'
                        if exit_code == 52: eel.alert_msg('Ошибка генерации текста.\nПроверьте свое подключение к интернету.')
                else:
                        info = 'the function did not complete its work'
                        exit_code = codes.error(11)
                        eel.alert_msg('Вводимые значения не должны быть пустыми')
                out.line(info + ' | exit code: ' + str(exit_code), 'info')
                print('---------------------------------------------------------------------')
        except:
                codes.error(0)

def main():
        try:
                exit_code = 0
                tngc = init.read_files()
                codes.info(1)
                try:
                        theme = init.get_theme(tngc)
                except:
                        exit_code = 1
                        return codes.error(1)
                try:
                        if ('Да' in init.topic_check(theme))or('да' in init.topic_check(theme)):
                                meaning = True
                                codes.info(2)
                                pstr = init.plan_formation(theme)
                        else:
                                meaning = False
                                pstr = ' Ошибка генерации текста, проверьте правильность набранной темы.'
                                exit_code = codes.error(11)
                                codes.error(2)
                except:
                        pstr = ' Ошибка генерации текста, проверьте свое подключение к интернету.'
                        exit_code = codes.error(3)
                        codes.error(2)
                codes.info(3)
                try:
                        plan = init.plan_normalisation(pstr)
                except:
                        return codes.error(4)
                codes.info(4)
                try:
                        l = len(plan)
                        data_list = []
                        i=1
                        for item in plan:
                                try:
                                        if meaning != False:
                                                data_item = init.item_process(item, theme)
                                        else:
                                                data_item = 'Ошибка генерации текста. Проверьте правильность набранной темы.'
                                                codes.error(2)

                                        out.line('data item #' + str(i) + ' updating..', 'info')
                                        eel.say('обработка элемента... сейчас #' + str(i) + ' двойной анализ..')

                                        if meaning != False:
                                                data_item_update = init.item_updating(data_item)
                                        else:
                                                data_item_update = data_item
                                                codes.error(2)
                                        data_list.append(data_item_update)

                                        out.line('data item continue: ' + str(i) + ' / ' + str(l), 'info')
                                        eel.say('обработка элемента... завершено: ' + str(i) + ' / ' + str(l))
                                except:
                                        data_item = ' Ошибка генерации текста.'
                                        data_list.append(data_item)

                                        eel.say('невозможно сгенерировать элемент #' + str(i))
                                        exit_code = exit_code + codes.error(2)
                                        codes.error(5)
                                i=i+1
                except:
                        return codes.error(6)
                codes.info(5)
                try:
                        save_doc.create_file_doc(tngc, plan, data_list)
                        codes.info(6)
                except:
                        return codes.error(7)
                codes.info(7)
                try:
                        plan_txt = open('plan.txt', 'w')
                        plan_txt.write('//'.join(plan))
                        plan_txt.close()
                        codes.info(8)
                        codes.info(6)
                        return exit_code
                except:
                        return codes.error(8)
        except:
                return codes.error(9)

class codes():
        def error(number:int)->int:
                error_codes_text_list_en = [
                        'unknown button error', # 0
                        'topic not found', # 1
                        'text generation error', # 2
                        'the plan could not be formed', # 3
                        'the plan could not be normalized', # 4
                        'nonefailed to generate last item', # 5
                        'None', # 6
                        'failed to generate document', # 7
                        'unable to create configuration files', # 8
                        'unknown error', # 9
                        'input values ​​must not be empty', # 10
                        'unable to generate text on the entered topic' # 11
                ]
                error_codes_text_list_ru = [
                        'неизвестная ошибка кнопки', # 0
                        'тема не найдена', # 1
                        'ошибка генерации текста', # 2
                        'план не может быть сформирован', # 3
                        'план не может быть нормализован', # 4
                        'не удалось сгенерировать последний элемент', # 5
                        'None', # 6
                        'не удалось сгенерировать документ', # 7
                        'не удалось создать файлы конфигурации', # 8
                        'неизвестная ошибка', # 9
                        'входные значения не должны быть пустыми', # 10
                        'не удалось сгенерировать текст по введенной теме' # 11
                ]
                error_exit_codes_list = [
                        1000, # 0
                        1, # 1
                        50, # 2
                        2, # 3
                        3, # 4
                        5, # 5
                        4, # 6
                        6, # 7
                        8, # 8
                        7000, # 9
                        1010, # 10
                        5010 # 11
                ]
                text_en = error_codes_text_list_en[number]
                text_ru = error_codes_text_list_ru[number]
                error_code = error_exit_codes_list[number]
                out.line(text_en, 'error')
                eel.say(text_ru)
                return error_code
        def info(number:int=9):
                info_codes_text_list_en = [
                        'connect!', # 0
                        'topic request...', # 1
                        'plan formation...', # 2
                        'plan normalisation...', # 3
                        'item processing...', # 4
                        'creating docx file...', # 5
                        'continue!', # 6
                        'creating config files...', # 7
                        'configuration files have been created', # 8
                        'the "theme" field is empty', # 9
                        'unknown info' # 10
                ]
                info_codes_text_list_ru = [ 
                        'подключено!', # 0 
                        'запрос темы...', # 1 
                        'формирование плана...', # 2 
                        'нормализация плана...', # 3 
                        'обработка элемента...', # 4 
                        'создание файла docx...', # 5 
                        'завершено!', # 6 
                        'создание файлов конфигурации...', # 7 
                        'файлы конфигурации созданы', # 8 
                        'поле темы пусто', # 9 
                        'неизвестная информация'#10
                ]
                text_en = info_codes_text_list_en[number]
                text_ru = info_codes_text_list_ru[number]
                out.line(text_en, 'info')
                eel.say(text_ru)

eel.start("main.html", size=(700, 700), port=0)