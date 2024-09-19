def line(arg:str):
        ir = open('inf.txt', 'r')
        information_number_list = [line.strip() for line in ir]
        number = int(information_number_list[0])
        ir.close()
        inf = str(number) + ' | INFORMATION: '
        print(inf + str(arg))
        iw = open('inf.txt', 'w')
        number = number + 1
        iw.write(str(number))