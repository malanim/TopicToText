from g4f.client import Client
import re
import out

def ask(prompt:str)->str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.choices[0].message.content
    return text

def read_files()->list:
    tn = open('tngc.txt', 'r')
    tngc = [line.strip() for line in tn]
    tn.close()
    return tngc

def get_theme(tngc:list)->str:
    theme = tngc[0]
    return theme

def plan_formation(theme:str)->str:
    pstr = ask('Мне нужен небольшой строгий план-содержание из 10 пунктов без лишних предисловий и выводов для курсовой работы на тему: ' + theme)
    return pstr

def plan_normalisation(pstr:str)->list:
    npstr = re.sub('[^А-Яа-я \n:,]', '', pstr)
    npstr = npstr.replace('\n ', '\n')
    npstr = npstr.replace(' ', '', 1)
    plan = npstr.split('\n')
    try:
        del plan[10:]
        plan.remove('')
    except:
        out.line('cannot remove empty lines', 'error')
    return plan

def item_process(item:str, theme:str)->str:
    data_item = ask('Помоги написать '+ item + ', связанное с темой: ' + theme + '; хочу получить только текст длиной от 100 до 1000 символов')
    data_item_normal = re.sub('[^А-Яа-я \n:,.]', '', data_item)
    return data_item_normal