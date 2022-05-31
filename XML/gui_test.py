from tkinter import *
from tkinter import font
from PIL import ImageTk
import parsing
import tkintermapview

data = []
data2 = []
citylist = ['오산시', '부천시', '광주시', '포천시', '평택시', '안산시', '양평군', '김포시', '파주시',
                 '고양시', '성남시', '여주시', '수원시', '양주시', '연천군', '화성시', '과천시', '시흥시',
                 '구리시', '남양주시', '의왕시', '안성시', '하남시', '용인시', '안양시', '광명시', '의정부시',
                 '가평군', '동두천시', '이천시', '군포시']

bgColor ='#8BDDD7'
mainText = "WhereFi"
g_Tk = Tk()
g_Tk.title(mainText)
g_Tk.geometry("1200x800+450+100")  # {width}x{height}+-{xpos}+-{ypos}

images = {'Wifi': PhotoImage(file="image/WifiLogo.png"), 'Map': PhotoImage(file="image/map.png"),
          'Email': PhotoImage(file="image/email.png"), 'Title': PhotoImage(file="image/Title2.png")}
class GUI:
    def __init__(self):
        global mainText, WifiButtonImg, Search
        self.fontNormal2 = font.Font(g_Tk, size=15, weight='bold')
        self.fontNormal = font.Font(g_Tk, size=10, weight='bold')

        self.frameTitle = Frame(g_Tk, padx=10, pady=10, bg=bgColor)
        self.frameCombo = Frame(g_Tk, pady=10, bg=bgColor)
        self.frameEntry = Frame(g_Tk, pady=10, bg=bgColor)
        self.frameList = Frame(g_Tk, padx=10, pady=10, bg=bgColor)


        self.initLogo()
        self.initSearchButton()

        self.draw()

    def initLogo(self):
        self.frameTitle.pack(side="top", fill="x")
        self.frameCombo.pack(side="top", fill="x")
        self.frameEntry.pack(side="top", fill="x")
        self.frameList.pack(side="bottom", fill="both", expand=True)

        WhereFiIconBox = Label(self.frameCombo, image=images['Title'], bg=bgColor)
        WhereFiIconBox.pack(side='left', padx=10, fill='y', expand=True)

        MapIconButton = Button(self.frameCombo, image=images['Map'], bg=bgColor, command=self.onMapPopup)
        MapIconButton.pack(side='left', padx=10, fill='y', expand=True)

        sendEmailButton = Button(self.frameCombo, image=images['Email'], command=self.onEmailPopup, bg=bgColor)
        sendEmailButton.pack(side='right', padx=10, fill='y', expand=True)

    def initSearchButton(self):
        global InputLabel
        SearchButton = Button(self.frameEntry, font=self.fontNormal, text="검색", command=self.GetInfo)
        InputLabel = Entry(self.frameEntry, font=self.fontNormal2, width=10, borderwidth=12, relief='ridge')

        SearchButton.pack(side="right", padx=10)
        InputLabel.pack(side="right", anchor='n', fill="x", expand=True)

    def initListbox(self):
        global SearchListBox, LBScrollbar
        LBScrollbar = Scrollbar(self.frameEntry)
        SearchListBox = Listbox(self.frameEntry, font=self.fontNormal2, activestyle='none', width=11, height=1,
                                borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set,
                                selectbackground='thistle4')
        for s in citylist:
            SearchListBox.insert(END, s)
        SearchListBox.bind('<<ListboxSelect>>', event_for_listbox)
        SearchListBox.pack(side='left', anchor='n', expand=True, fill="x")
        LBScrollbar.pack(side="left")
        LBScrollbar.config(command=SearchListBox.yview)

        # 목록 부분
        global listBox, LBScrollbar2, listBox2, RBScrollbar
        LBScrollbar2 = Scrollbar(self.frameList)
        listBox = Listbox(self.frameList, selectmode='extended', font=self.fontNormal2, width=10, height=15, borderwidth=12,
                          relief='ridge', yscrollcommand=LBScrollbar2.set)

        for s in parsing.wifi_list:
            listBox.insert(END, s['TMP01'])

        listBox.pack(side='left', anchor='n', expand=True, fill="both")
        LBScrollbar2.pack(side="left", fill='y')
        LBScrollbar2.config(command=listBox.yview)

        RBScrollbar = Scrollbar(self.frameList)
        listBox2 = Listbox(self.frameList, selectmode='extended', font=self.fontNormal2, width=10, height=15, borderwidth=12,
                          relief='ridge', yscrollcommand=RBScrollbar.set)

        for s in parsing.wifi_list:
            if s['TMP01'] == data2:
                listBox2.insert(END,'====================상세정보====================',
                                '설치장소상세 - ' + s['INSTL_PLC_DETAIL_DTLS'],
                                '도로명 주소 - ' + s['REFINE_ROADNM_ADDR'],
                                '지번 주소 - ' + s['REFINE_LOTNO_ADDR'],
                                'SSID - ' + s['WIFI_SSID_INFO'],
                                '관리 기관명 - ' + s['MANAGE_INST_NM'],
                                '전화번호 - ' + s['MANAGE_INST_TELNO'],
                                '===============================================')

        listBox.bind('<<ListboxSelect>>', clicked_listbox)
        listBox2.pack(side='left', anchor='n', expand=True, fill="both")
        RBScrollbar.pack(side="right", fill='y')
        RBScrollbar.config(command=listBox2.yview)

    def GetInfo(self):
        global data, SearchListBox, listBox, listBox2, LBScrollbar, LBScrollbar2, RBScrollbar
        parsing.SearchWifi(data)
        print("검색...")
        if (parsing.wifi_list):
            print(parsing.wifi_list[0])
        LBScrollbar.destroy()
        LBScrollbar2.destroy()
        RBScrollbar.destroy()
        SearchListBox.destroy()
        listBox.destroy()
        listBox2.destroy()
        self.draw()

    def onSearch(self):  # "검색" 버튼 이벤트처리
        global SearchListBox
        sels = SearchListBox.curselection()
        iSearchIndex = \
            0 if len(sels) == 0 else SearchListBox.curselection()[0]
        if iSearchIndex == 0:
            pass
        elif iSearchIndex == 1:
            pass
        elif iSearchIndex == 2:
            pass
        elif iSearchIndex == 3:
            pass

    def onMapPopup(self):
        global g_Tk, data2
        for s in parsing.wifi_list:
            if s['TMP01'] == data2:
                popup = Toplevel(g_Tk)  # popup 띄우기
                popup.geometry(f"{800}x{600}")
                popup.title("map.py")
                map_widget = tkintermapview.TkinterMapView(popup, width=800, height=500, corner_radius=0)
                map_widget.pack()
                marker_1 = map_widget.set_address(s['REFINE_ROADNM_ADDR'], marker=True)
                print(marker_1.position, marker_1.text)
                marker_1.set_text(s['TMP01'])
                map_widget.set_zoom(15)

    def getStr(s):
        return '' if not s else s

    def onEmailInput(self):
        global addrEmail
        addrEmail = inputEmail.get()
        popup.destroy()  # popup 내리기

    def onEmailPopup(self):
        global g_Tk, addrEmail, popup
        addrEmail = None
        popup = Toplevel(g_Tk)  # popup 띄우기
        popup.geometry("300x150")
        popup.title("받을 이메일 주소 입력")
        global inputEmail, btnEmail
        inputEmail = Entry(popup, width=200, )
        inputEmail.pack(fill='x', padx=10, expand=True)
        btnEmail = Button(popup, text="확인", command=self.onEmailInput)
        btnEmail.pack(anchor="s", padx=10, pady=10)

    def draw(self):
        self.initListbox()

popup = inputEmail = btnEmail = None
addrEmail = None

def event_for_listbox(event):  # 리스트 선택 시 내용 출력
    global data
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

def clicked_listbox(event):  # 리스트 선택 시 내용 출력
    global data2
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data2 = event.widget.get(index)
        print(data2)
    print('클릭')

gui = GUI()  # 화면 전체 구성

g_Tk.mainloop()
