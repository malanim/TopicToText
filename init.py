from g4f.client import Client
import re
import out
import tempfile
import os

temp_dir_path = tempfile.gettempdir()
tngc_tmp = os.path.join(temp_dir_path, 'tngc.tmp')

def ask(prompt:str)->str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    text = response.choices[0].message.content
    return text

def read_files()->list:
    with open(tngc_tmp, 'r') as t:
        tngc = t.read().split('//')
    return tngc

def get_theme(tngc:list)->str:
    theme = tngc[0]
    return theme

def topic_check(theme:str)->str:
    result = ask('Это выражение имеет смысл: "' + theme + '"? Ответь "Да" если смысл есть, или "Нет" если смысла нет')
    result_normalizade = re.sub('[^А-Яа-я]', '', result)
    return result_normalizade

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
    data_item_normal = re.sub('[^А-Яа-я0-9 \n:,.]', '', data_item)
    return data_item_normal

def item_updating(item:str)->str:
    data_item_update = ask('Исправь ошибки среди текста, если они есть, и представь информацию более понятно или развернуто: "' + item + '"; хочу получить только получившийся текст')
    # data_item_normal = re.sub('[^А-Яа-я \n:;,.]', '', data_item_update)
    return data_item_update