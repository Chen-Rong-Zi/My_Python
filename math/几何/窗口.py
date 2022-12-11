# coding=UTF-8
import wx
from 立体几何 import 立体几何
from 立体几何 import Cube
from 立体几何 import main


class GFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='', size=(900, 670), pos=(350, 100))
        self.panel      = wx.Panel     (parent=self)
        self.statictext = wx.StaticText(parent=self.panel, label = 'hello world', pos = (350, 100))
        self.bt         = wx.Button    (parent=self.panel, label='启用', pos=(400, 200))
        self.Bind(wx.EVT_BUTTON, self.fuction, self.bt)

    def fuction(self, event):
        # self.Bind方法会将它第一个参数(EVT_BUTTON)作为event参数传入
        self.statictext.SetLabelText('nihao')
        main()



app   = wx.App()

frame = GFrame()
frame.Show()

app  .MainLoop()
