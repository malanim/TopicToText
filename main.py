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
                        exit_code = codes.error(10)
                        eel.alert_msg('Вводимые значения не должны быть пустыми')
                out.line(info + ' | exit code: ' + str(exit_code), 'info')
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
                codes.info(2)
                try:
                        pstr = init.plan_formation(theme)
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
                                        data_item = init.item_process(item, theme)

                                        out.line('data item #' + str(i) + ' updating..', 'info')
                                        eel.say('item processing... data item #' + str(i) + ' updating..')

                                        data_item_update = init.item_updating(data_item)
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
                        'unknown button error',
                        'topic not found',
                        'text generation error',
                        'the plan could not be formed',
                        'the plan could not be normalized',
                        'nonefailed to generate last item',
                        'None',
                        'failed to generate document',
                        'unable to create configuration files',
                        'unknown error',
                        'input values ​​must not be empty'
                ]
                error_exit_codes_list = [
                        1000,
                        1,
                        50,
                        2,
                        3,
                        5,
                        4,
                        6,
                        8,
                        7000,
                        1010
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