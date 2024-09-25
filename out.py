import tempfile
import os

temp_dir_path = tempfile.gettempdir()
inf_tmp = os.path.join(temp_dir_path, 'inf.tmp')

name_program = 'TopicToText'

def line(arg:str, parameter:str):
        try:
                # ir = open('inf.txt', 'r')
                # information_number_list = [line.strip() for line in ir]
                # number = int(information_number_list[0])
                # ir.close()
                with open(inf_tmp, 'r') as inf_read:
                        information_number_list = [line.strip() for line in inf_read]
                        number = int(information_number_list[0])
        except:
                number = 100
                print(str(number) + ' | ' + name_program + ' | ERROR: configuration file not found')
        if (parameter=='info'):
                perinf = 'INFO'
        elif (parameter=='error'):
                perinf = 'ERROR'
        else:
                perinf = 'UNKNOWN'
                print(str(number) + ' | ' + name_program + ' | UNKNOWN: configuration parameter passed incorrectly')
        inf = str(number) + ' | ' + name_program + ' | ' + perinf + ': '
        print(inf + str(arg))
        # iw = open('inf.txt', 'w')
        # number = number + 1
        # iw.write(str(number))
        with open(inf_tmp, 'w') as inf_write:
                number = number + 1
                inf_write.write(str(number))