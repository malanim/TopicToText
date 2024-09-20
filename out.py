def line(arg:str, parameter:str):
        try:
                ir = open('inf.txt', 'r')
                information_number_list = [line.strip() for line in ir]
                number = int(information_number_list[0])
                ir.close()
        except:
                number = 100
                print(str(number) + ' |ttd| ERROR: configuration file not found')
        if (parameter=='info'):
                perinf = 'INFO'
        elif (parameter=='error'):
                perinf = 'ERROR'
        else:
                perinf = 'INFO'
                print(str(number) + ' |ttd| ERROR: configuration parameter passed incorrectly')
        inf = str(number) + ' |ttd| ' + perinf + ': '
        print(inf + str(arg))
        iw = open('inf.txt', 'w')
        number = number + 1
        iw.write(str(number))