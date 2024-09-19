from g4f.client import Client
import re

def ask(prompt:str)->str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    r = response.choices[0].message.content
    return r

def read_files()->list:
    t = open('tngc.txt', 'r')
    tngc = [line.strip() for line in t]
    t.close()
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
        del plan[10:100]
        plan.remove('')
    except:
        print('Ошибка удаления')
    return plan

def item_process(item:str, theme:str)->str:
    data_item = ask('Помоги написать '+ item + ', связанное с темой: ' + theme + '; хочу получить только текст длиной от 100 до 1000 символов')
    data_item_normal = re.sub('[^А-Яа-я \n:,.]', '', data_item)
    return data_item_normal