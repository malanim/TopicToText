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
                t = open('tngc.txt', 'w')
                t.write(theme + '\n' + name + '\n' + group + '\n' + colledge)
                t.close()
                
                inf = 'connect!'
                out.line(inf, 'info')
                eel.say(inf)

                exit_code = main()
                info = 'the function has completed its work'
                out.line(info + ' | exit code: ' + str(exit_code), 'info')
        except:
                inf = 'unknown button error'
                out.line(inf, 'error')
                eel.say(inf)

def main():
        try:
                exit_code = 0
                tngc = init.read_files()
                # print(tngc)
                inf = 'topic request...'
                out.line(inf, 'info')
                eel.say(inf)
                try:
                        theme = init.get_theme(tngc)
                        # print(theme)
                except:
                        inf = 'topic not found'
                        out.line(inf, 'error')
                        eel.say(inf)
                        exit_code = 1
                        return exit_code
                inf = 'plan formation...'
                out.line(inf, 'info')
                eel.say(inf)
                try:
                        pstr = init.plan_formation(theme)
                        # print(pstr)
                except:
                        pstr = ' Ошибка генерации текста, проверьте свое подключение к интернету.'
                        out.line('text generation error', 'error')
                        inf = 'the plan could not be formed'
                        out.line(inf, 'error')
                        eel.say(inf)
                        exit_code = 2
                        # return exit_code
                inf = 'plan normalisation...'
                out.line(inf, 'info')
                eel.say(inf)
                try:
                        plan = init.plan_normalisation(pstr)
                        # print(plan)
                except:
                        inf = 'the plan could not be normalized'
                        out.line(inf, 'error')
                        eel.say(inf)
                        exit_code = 3
                        return exit_code
                inf = 'item processing...'
                out.line(inf, 'info')
                eel.say(inf)
                try:
                        l = len(plan)
                        data_list = []
                        i=1
                        for item in plan:
                                try:
                                        data_item = init.item_process(item, theme)
                                        inf = 'data item #' + str(i) + 'updating..'
                                        eelinf = 'item processing... data item #' + str(i) + ' updating..'
                                        out.line(inf, 'info')
                                        eel.say(eelinf)
                                        data_item_update = init.item_updating(data_item)
                                        data_list.append(data_item_update)
                                        # print(data_item)
                                        inf = 'data item continue: ' + str(i) + ' / ' + str(l)
                                        eelinf = 'item processing... data item continue: ' + str(i) + ' / ' + str(l)
                                        out.line(inf, 'info')
                                        eel.say(eelinf)
                                except:
                                        data_item = ' Ошибка генерации текста, проверьте свое подключение к интернету.'
                                        data_list.append(data_item)
                                        out.line('text generation error', 'error')
                                        inf = 'nonefailed to generate item #' + str(i)
                                        out.line(inf, 'error')
                                        eel.say(inf)
                                        exit_code = exit_code + 50
                                        # return exit_code
                                i=i+1
                except:
                        inf = 'None'
                        out.line(inf, 'error')
                        eel.say(inf)
                        exit_code = 4
                        return exit_code
                inf = 'creating docx file...'
                out.line(inf, 'info')
                eel.say(inf)
                try:
                        save_doc.create_file_doc(tngc, plan, data_list)
                        inf = 'continue!'
                        out.line(inf, 'info')
                        eel.say(inf)
                        return exit_code
                except:
                        inf = 'failed to generate document'
                        out.line(inf, 'error')
                        eel.say(inf)
                        exit_code = 6
                        return exit_code
        except:
                inf = 'unknown error'
                out.line(inf, 'error')
                eel.say(inf)
                exit_code = 7
                return exit_code

eel.start("main.html", size=(700, 700), port=0)