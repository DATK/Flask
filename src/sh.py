alf = "QWERTYUIOPASDFGHJKLZXCVBNMabcdefghiЙФЯЧЫЦУКАВСМИПЕНРТЬОГШЩДЛБЮЖЗХЭЪЬjklmnopqrstuvwxyz123456789_йфячыцувсмипакенртьогшлбюдщзжэхъ*-+=*&:;?!@"
table = ["q", "w", "e", "r", "t",
         "y", "u", "i", "o", "p",
         "a", "s", "d", "f", "g",
         "h", "j", "k", "l", "z",
         "x", "c", "v", "b", "n",
         "m", "1", "2", "3", "4",
         '5', '6', '7', '8', '9',
         '0', 'й', 'ц', 'у', 'к',
         'е', 'н', 'г', 'ш', 'щ',
         'з', 'х', 'ъ', 'ф', 'ы',
         'в', 'а', 'п', 'р', 'о',
         'л', 'д', 'ж', 'э', 'я',
         'ч', 'с', 'м', 'и', 'т',
         'ь', 'б', 'ю', '_', '!',
         '_', '?', '*', '!', '@',
         '=', '+', '&', ';', ':',
         "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
         "A", "S", "D", "F", "G", "H", "J", "K", "L",
         "Z", "X", "C", "V", "B", "N", "M", "Й", "Ц", "У", "К", "Е",
         "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д",
         "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"]

cezar_shifr, cezar_un, polibia_shifr, polibia_un,pol_sh= [], [], [], "",[]


def cezar(text, alf=alf, key=2):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                if i + key > len(alf):
                    # print("          ",i,j)
                    continue
                else:
                    # print("                          ",i,j)
                    cezar_shifr.append(alf[i + key])
                    continue
    return ''.join(cezar_shifr)


def cezar_unsc(text, alf=alf, key=2):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                if i + key > len(alf):
                    # print("          ",i,j)
                    continue
                else:
                    # print("                          ",i,j)
                    cezar_un.append(alf[i - key])
                    continue
    return ''.join(cezar_un)

""" Otkas
def polibia(text, table=table):
    for i in range(0, len(text)):
        for j in range(0, len(table)):
            if text[i] == table[j]:
                polibia_shifr.append(j)
    for i in range(len(polibia_shifr)):
        pol_sh.append(str(polibia_shifr[i]))
    return " ".join(pol_sh)


def polibia_unsc(text, table=table):
    global polibia_un
    tex=[]
    for i in range(len(text)):
        if text[i]!=" ":
            tex.append(int(text[i]))
        else:
            continue
    for j in tex:
        polibia_un += table[j]
    return polibia_un

"""
def cls():
    cezar_shifr.clear()
    cezar_un.clear()
    return cezar_shifr, cezar_un

