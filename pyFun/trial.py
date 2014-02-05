import wx
class MenuExample(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 150))
        menubar = wx.MenuBar()
        file = wx.Menu()
        quit = wx.MenuItem(file, 1, 'Qu&it\tCtrl+q \tCtrl+t')
        #quit.SetBitmap(wx.Bitmap('icons/exit.png'))
        file.AppendItem(quit)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)
        self.Centre()
        self.Show(True)
    def OnQuit(self, event):
        self.Close()
app = wx.App()
MenuExample(None, -1, '')
app.MainLoop()
