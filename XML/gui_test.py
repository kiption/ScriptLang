from tkinter import *
from tkinter import font
from PIL import ImageTk


mainText = "WhereFi"
g_Tk = Tk()
g_Tk.title(mainText)
g_Tk.geometry("400x600+450+100")  # {width}x{height}+-{xpos}+-{ypos}

images = {'Wifi': PhotoImage(file="circleGif.gif"), 'Map': PhotoImage(file="map.png"), 'Email': PhotoImage(file="email.png")}

def event_for_listbox(event):  # 리스트 선택 시 내용 출력
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

def InitScreen():
    global mainText, WifiButtonImg
    fontTitle = font.Font(g_Tk, size=18, weight='bold', family='여기어때 잘난체 OTF')
    fontNormal2 = font.Font(g_Tk, size=15, weight='bold')
    fontNormal = font.Font(g_Tk, size=14, weight='bold')
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#909090')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#909090')
    frameCombo.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, pady=10, bg='#909090')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#909090')
    frameList.pack(side="bottom", fill="both", expand=True)
    MainText = Label(frameTitle, font=fontTitle, text=mainText)
    MainText.pack(anchor="center", fill="both")


    WhereFiIconBox = Label(frameCombo, image=images['Wifi'])
    WhereFiIconBox.pack(side='left', padx=10, fill='y', expand=True)

    MapIconButton = Button(frameCombo, image=images['Map'])
    MapIconButton.pack(side='left', padx=80, fill='y', expand=True)

    sendEmailButton = Button(frameCombo, image=images['Email'], command=onEmailPopup)
    sendEmailButton.pack(side='right', padx=10, fill='y')

    global SearchListBox
    LBScrollbar = Scrollbar(frameEntry)
    SearchListBox = Listbox(frameEntry, font=fontNormal, activestyle='none', width=13, height=1, borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    slist = ["도서관", "모범음식점", "마트", "문화공간"]
    for i, s in enumerate(slist):
        SearchListBox.insert(i, s)
    SearchListBox.pack(side='left', padx=10,  fill="both")
    LBScrollbar.pack(side="left")
    LBScrollbar.config(command=SearchListBox.yview)

    global InputLabel
    InputLabel = Entry(frameEntry, font=fontNormal, width=8, borderwidth=12, relief='ridge')
    InputLabel.pack(side="left", padx=10)
    SearchButton = Button(frameEntry, font=fontNormal, text="검색", command=onSearch)
    SearchButton.pack(side="right", fill='y', padx=10)

    # 목록 부분
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended', font=fontNormal2, width=10, height=15, borderwidth=12,
                      relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    LBScrollbar.pack(side="left", fill='y')
    LBScrollbar.config(command=listBox.yview)

    RBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended', font=fontNormal2, width=10, height=15, borderwidth=12,
                      relief='ridge', yscrollcommand=RBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    RBScrollbar.pack(side="right", fill='y')
    RBScrollbar.config(command=listBox.yview)


def onSearch():  # "검색" 버튼 이벤트처리
    global SearchListBox
    sels = SearchListBox.curselection()
    iSearchIndex = \
        0 if len(sels) == 0 else SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass
    elif iSearchIndex == 2:
        pass
    elif iSearchIndex == 3:
        pass


def getStr(s):
    return '' if not s else s


def SearchLibrary():  # "검색" 버튼 -> "도서관"
    from xml.etree import ElementTree
    global listBox
    listBox.delete(0, listBox.size())
    with open('서울도서관.xml', 'rb') as f:
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml)
    elements = parseData.iter('row')
    i = 1
    for item in elements:  # " row“ element들
        part_el = item.find('CODE_VALUE')
        if InputLabel.get() not in part_el.text:
            continue
        _text = '[' + str(i) + '] ' + \
                getStr(item.find('LBRRY_NAME').text) + \
                ' : ' + getStr(item.find('ADRES').text) + \
                ' : ' + getStr(item.find('TEL_NO').text)
        listBox.insert(i - 1, _text)
        i = i + 1


popup = inputEmail = btnEmail = None
addrEmail = None

def onEmailInput():
    global addrEmail
    addrEmail = inputEmail.get()
    popup.destroy()  # popup 내리기


def onEmailPopup():
    global g_Tk, addrEmail, popup
    addrEmail = None
    popup = Toplevel(g_Tk)  # popup 띄우기
    popup.geometry("300x150")
    popup.title("받을 이메일 주소 입력")
    global inputEmail, btnEmail
    inputEmail = Entry(popup, width=200, )
    inputEmail.pack(fill='x', padx=10, expand=True)
    btnEmail = Button(popup, text="확인", command=onEmailInput)
    btnEmail.pack(anchor="s", padx=10, pady=10)


InitScreen()  # 화면 전체 구성

g_Tk.mainloop()
