import eel
import colorama
import init
import save_doc

colorama.init()
eel.init("web")

@eel.expose
def get_text(theme, name, group, colledge):

        # print('theme: ' + theme + '\nname: ' + name + '\ngroup: ' + group + '\ncolledge: ' + colledge)
        t = open('tngc.txt', 'w')
        t.write(theme + '\n' + name + '\n' + group + '\n' + colledge)
        t.close()

        # Запуск основной программы
        # os.system('python init.py')
        main()

        eel.say('continue!')   # Call a Javascript function

def main():
        tngc = init.read_files()
        print(tngc)
        eel.say('topic request...')
        theme = init.get_theme(tngc)
        print(theme)
        eel.say('plan formation...')
        pstr = init.plan_formation(theme)
        print(pstr)
        eel.say('plan normalisation...')
        plan = init.plan_normalisation(pstr)
        print(plan)
        eel.say('item processing...')
        l = len(plan)
        data_list = []
        i=1
        for item in plan:
                data_item = init.item_process(item, theme)
                data_list.append(data_item)
                print(data_item)
                i=i+1
                eel.say('item processing... data item: ' + str(i) + ' / ' + str(l))
        eel.say('creating docx file...')
        save_doc.create_file_doc(tngc, plan, data_list)
        eel.say('continue!')

eel.start("main.html", size=(700, 700))