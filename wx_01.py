import wx 
class MyFrame(wx.Frame): 

    def __init__(self): 
        wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300)) 
        panel = wx.Panel(self, -1) 
        panel.Bind(wx.EVT_MOTION,  self.OnMove) 
        wx.StaticText(panel, -1, "Pos:", pos=(10, 12)) 
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10),size=(200,50),style=wx.CB_READONLY) 
        font = wx.Font(30,wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.posCtrl.SetFont(font)
        self.posCtrl.SetBackgroundColour('black')
        self.posCtrl.SetForegroundColour('white')
        #self.StaticTextPort.SetForegroundColour('white')
        #self.StaticTextPort.SetBackgroundColour('black') 
    def OnMove(self, event): 
        pos = event.GetPosition() 
        self.posCtrl.SetValue("%s : %s" % (pos.x, pos.y)) 

if __name__ == '__main__': 
    app = wx.App(False) 
    frame = MyFrame() 
    frame.Show(True) 
    app.MainLoop() 
