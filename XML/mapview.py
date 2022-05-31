from tkinter import *
import tkintermapview

root = Tk()
root.geometry(f"{800}x{600}")
root.title("map_view.py")
map_widget = tkintermapview.TkinterMapView(root, width=800, height=500, corner_radius=0)
map_widget.pack()

marker_1 = map_widget.set_address("경기도 시흥시 산기대학로 237", marker=True)
print(marker_1.position, marker_1.text)
marker_1.set_text("한국공학대학교")
map_widget.set_zoom(15)

