import eel
import colorama
import init
import save_doc
import out

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
                else:
                        info = 'the function did not complete its work'
                        exit_code = codes.error(11)
                        print('все норм')
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
                        eel.alert_msg('Ошибка генерации текста.\nПроверьте свое подключение к интернету.')
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
                                        if meaning == True:
                                                data_item = init.item_process(item, theme)
                                        else:
                                                data_item = 'Ошибка генерации текста. Проверьте правильность набранной темы.'
                                                codes.error(2)

                                        out.line('data item #' + str(i) + ' updating..', 'info')
                                        eel.say('item processing... data item #' + str(i) + ' updating..')

                                        if meaning == True:
                                                data_item_update = init.item_updating(data_item)
                                        else:
                                                data_item_update = data_item
                                                codes.error(2)
                                        data_list.append(data_item_update)

                                        out.line('data item continue: ' + str(i) + ' / ' + str(l), 'info')
                                        eel.say('item processing... data item continue: ' + str(i) + ' / ' + str(l))
                                except:
                                        data_item = ' Ошибка генерации текста, проверьте свое подключение к интернету.'
                                        data_list.append(data_item)

                                        eel.say('nonefailed to generate item #' + str(i))
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
                error_codes_text_list = [
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
                text = error_codes_text_list[number]
                error_code = error_exit_codes_list[number]
                out.line(text, 'error')
                eel.say(text)
                return error_code
        def info(number:int=9):
                info_codes_text_list = [
                        'connect!',
                        'topic request...',
                        'plan formation...',
                        'plan normalisation...',
                        'item processing...',
                        'creating docx file...',
                        'continue!',
                        'creating config files...',
                        'configuration files have been created',
                        'the "theme" field is empty',
                        'unknown info'
                ]
                text = info_codes_text_list[number]
                out.line(text, 'info')
                eel.say(text)

eel.start("main.html", size=(700, 700), port=0)