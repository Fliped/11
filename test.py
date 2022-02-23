import wx #导入wx包

app = wx.App()#创建应用程序对象

win = wx.Frame(None,-1,'Python') #创建窗体

btn = wx.Button(win, label = 'BUTTON')  #创建Button

win.Show()#显示窗体

app.MainLoop()#运行程序

