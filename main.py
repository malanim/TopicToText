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
        out.line(inf, 'inf')
        eel.say(inf)

        main()

        

def main():
        tngc = init.read_files()
        # print(tngc)
        inf = 'topic request...'
        out.line(inf, 'inf')
        eel.say(inf)
        try:
                theme = init.get_theme(tngc)
                # print(theme)
        except:
                inf = 'topic not found'
                out.line(inf, 'error')
                eel.say(inf)
        inf = 'plan formation...'
        out.line(inf, 'inf')
        eel.say(inf)
        try:
                pstr = init.plan_formation(theme)
                # print(pstr)
        except:
                inf = 'the plan could not be formed'
                out.line(inf, 'error')
                eel.say(inf)
        inf = 'plan normalisation...'
        out.line(inf, 'inf')
        eel.say(inf)
        try:
                plan = init.plan_normalisation(pstr)
                # print(plan)
        except:
                inf = 'the plan could not be normalized'
                out.line(inf, 'error')
                eel.say(inf)
        inf = 'item processing...'
        out.line(inf, 'inf')
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
                                out.line(inf, 'inf')
                                eel.say(inf)
                        except:
                                inf = 'nonefailed to generate item #' + str(i)
                                out.line(inf, 'error')
                                eel.say(inf)
                        i=i+1
        except:
                inf = 'None'
                out.line(inf, 'error')
                eel.say(inf)
        inf = 'creating docx file...'
        out.line(inf, 'inf')
        eel.say(inf)
        try:
                save_doc.create_file_doc(tngc, plan, data_list)
                inf = 'continue!'
                out.line(inf, 'inf')
                eel.say(inf)
        except:
                inf = 'failed to generate document'
                out.line(inf, 'error')
                eel.say(inf)

eel.start("main.html", size=(700, 700))