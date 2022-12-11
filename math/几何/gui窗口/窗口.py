# coding=UTF-8
import wx
from 立体几何 import 立体几何

class GFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='', size=(600, 450), pos=(350, 100))
        self.panel      = wx.Panel     (parent=self)
        self.statictext = wx.StaticText(parent=self.panel, label = 'hello world', pos = (350, 100))
        self.bt         = wx.Button    (parent=self.panel, label='启用', pos=(400, 200))
        self.Bind(wx.EVT_BUTTON, self.fuction, self.bt)

    def fuction(self, event):
        # Bind方法被调用时, 传入它自己第1个参数作为event参数.
        # self.statictext.SetLabelText('nihao')
        cube = 立体几何(2, 2, 2)



app   = wx.App()

frame = GFrame()
frame.Show()

app  .MainLoop()
