# -*- coding: utf-8 -*-

import wx

# app=wx.App()
# frame=wx.Frame(None,wx.ID_ANY,"hello,wrold")
# frame.Show(True)
# app.MainLoop()
class Mainwindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,title=title,size=(200,200))
        self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.Show(True)

app=wx.App(False)
frame=Mainwindow(None,"02")
app.MainLoop()