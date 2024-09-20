import eel
import colorama
import init
import save_doc
import out

colorama.init()
eel.init("web")

@eel.expose
def get_text(theme, name, group, colledge):
        t = open('tngc.txt', 'w')
        t.write(theme + '\n' + name + '\n' + group + '\n' + colledge)
        t.close()
        
        inf = 'connect!'
        out.line(inf, 'info')
        eel.say(inf)

        exit_code = main()
        info = 'the function has completed its work'
        out.line(info + ' | exit code: ' + str(exit_code), 'info')

def main():
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
                return 1
        inf = 'plan formation...'
        out.line(inf, 'info')
        eel.say(inf)
        try:
                pstr = init.plan_formation(theme)
                # print(pstr)
        except:
                inf = 'the plan could not be formed'
                out.line(inf, 'error')
                eel.say(inf)
                return 2
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
                return 3
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
                                data_list.append(data_item)
                                # print(data_item)
                                inf = 'item processing... data item: ' + str(i) + ' / ' + str(l)
                                out.line(inf, 'info')
                                eel.say(inf)
                        except:
                                inf = 'nonefailed to generate item #' + str(i)
                                out.line(inf, 'error')
                                eel.say(inf)
                                return 5
                        i=i+1
        except:
                inf = 'None'
                out.line(inf, 'error')
                eel.say(inf)
                return 4
        inf = 'creating docx file...'
        out.line(inf, 'info')
        eel.say(inf)
        try:
                save_doc.create_file_doc(tngc, plan, data_list)
                inf = 'continue!'
                out.line(inf, 'info')
                eel.say(inf)
        except:
                inf = 'failed to generate document'
                out.line(inf, 'error')
                eel.say(inf)
                return 0

eel.start("main.html", size=(700, 700))