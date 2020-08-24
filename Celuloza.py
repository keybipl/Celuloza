from bs4 import BeautifulSoup
from requests import get
import datetime
import ctypes

def fonts():
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 11
    font.dwFontSize.Y = 18
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Lucida Console"

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))


def akademia():
    URLa = 'http://www.lubuskizpn.pl/extranet/?action=getTimeSchedulesList&play_id=37525'
    akademia = get(URLa)
    bs = BeautifulSoup(akademia.content, 'html.parser')

    wyniki = []
    for wynik in bs.find_all('tr'):
        if wynik.find_all('td', string='AKADEMIA FUTBOLU KOSTRZYN NAD ODRĄ'):
            w = wynik.get_text().strip()
            wyniki.append(w)

    lista = []
    for i in range(len(wyniki)):
        string = str([wyniki[i]])
        a = string.replace(r'\n', '.').replace('[', '').replace('\'', '').replace(']', '')
        a = a.split('.')
        lista.append(a)

    for i in range(13):  # 13 kolejek
        data = str(lista[i][4])
        year = data[0:4]
        year = int(year)
        month = data[5:7]
        month = int(month)
        day = data[8:10]
        day = int(day)
        date = datetime.datetime(year=year, month=month, day=day)
        date = date.strftime('%d.%m.%Y')
        print(f'Kolejka nr {i + 1} z dnia {date} godzina: {lista[i][5]}')
        print(f'{lista[i][9]}')
        print(f'{lista[i][0]} - {lista[i][3]} ')
        print(f'{lista[i][1]} - {lista[i][2]}')
        print()


# JUNIORZY STARSI
def juniorzy_starsi():
    URLj = 'http://www.lubuskizpn.pl/extranet/?action=getTimeSchedulesList&play_id=37061'
    juniorzy = get(URLj)
    bs = BeautifulSoup(juniorzy.content, 'html.parser')

    wyniki = []
    for wynik in bs.find_all('tr'):
        if wynik.find_all('td', string='TS CELULOZA  KOSTRZYN  n/o'):
            w = wynik.get_text().strip()
            wyniki.append(w)


    lista = []
    for i in range(len(wyniki)):
        string = str([wyniki[i]])
        a = string.replace(r'\n', '.'). replace('[', '').replace('\'', '').replace(']', '')
        a = a.split('.')
        lista.append(a)


    for i in range(14):  # 14 kolejek
        data = str(lista[i][4])
        year = data[0:4]
        year = int(year)
        month = data[5:7]
        month = int(month)
        day = data[8:10]
        day = int(day)
        date = datetime.datetime(year=year, month=month, day=day)
        date = date.strftime('%d.%m.%Y')
        print(f'Kolejka nr {i+1} z dnia {date} godzina: {lista[i][5]}')
        print(f'{lista[i][9]}')
        print(f'{lista[i][0]} - {lista[i][3]} ')
        print(f'{lista[i][1]} - {lista[i][2]}')
        print()


# TRAMPKARZE
def trampkarze():
    URLt = 'http://www.lubuskizpn.pl/extranet/?action=getTimeSchedulesList&play_id=37271'
    trampkarze = get(URLt)
    bst = BeautifulSoup(trampkarze.content, 'html.parser')

    wyniki = []
    for wynik in bst.find_all('tr'):
        if wynik.find_all('td', string='TS CELULOZA  KOSTRZYN  n/o'):
            w = wynik.get_text().strip()
            wyniki.append(w)


    lista = []
    for i in range(len(wyniki)):
        string = str([wyniki[i]])
        a = string.replace(r'\n', '?'). replace('[', '').replace('\'', '').replace(']', '')
        a = a.split('?')
        lista.append(a)


    for i in range(14):  # 14 kolejek
        data = str(lista[i][4])
        year = data[0:4]
        year = int(year)
        month = data[5:7]
        month = int(month)
        day = data[8:10]
        day = int(day)
        date = datetime.datetime(year=year, month=month, day=day)
        date = date.strftime('%d.%m.%Y')
        print(f'Kolejka nr {i+1} z dnia {date} godzina: {lista[i][5]}')
        try:
            print(lista[i][9])
        except IndexError:
            'nic się nie pokazuje'

        print(f'{lista[i][0]} - {lista[i][3]}')
        print(f'{lista[i][1]} - {lista[i][2]}')
        print()

def seniorzy():
    print('seniorzy')


fonts()
trampkarze()
juniorzy_starsi()
akademia()











