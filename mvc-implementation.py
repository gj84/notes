#!/usr/bin/env python
# -*- coding: utf-8 -*-


#MVC (model view controller) implementation example
#The model is only a word
#The normal view shows the word as it, the inverted view shows the word inverted
#each one has a text input and a button to insert a new word to the model (via Controller), 
#wich notifies both views via Observer pattern, and both update the text ctrl.

import wx

class Observer(object):
    def __init__(self, name):
        self.name = name

    def listen(self, subject):
        self.subject = subject
        subject.add_observer(self)

    def notify(self, event):
        return "%s was notified of event %s" % (self.name, str(event))

class Subject(object):
    def __init__(self, name):
        self.name = name
        self.observers = {}

    def add_observer(self, observer):
        self.observers[observer] = None

    def remove_observer(self, observer):
        del self.observers[observer]

    def notify(self):
        for obs in self.observers:
            obs.notify("the object was an event")

class Model(Subject):
    def __init__(self, name, initial_word):
        super(Model, self).__init__(name)
        self.word = initial_word

    def set_word(self, word):
        self.word = word
        self.notify()

class View(Observer, wx.Frame):
    def __init__(self, name):
        Observer.__init__(self,name)
        wx.Frame.__init__(self, parent = None, title=self.name)

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.ctrl = wx.TextCtrl(self)
        sizer.Add(self.ctrl, 0, wx.EXPAND | wx.ALL)
        self.ctrl.SetEditable(True)

        self.submit = wx.Button(self, label="Submit word")
        sizer.Add(self.submit, 0, wx.EXPAND | wx.ALL)
        
        self.SetSizer(sizer)
        self.set_word(self.name)

    def set_word(self, word):
        self.ctrl.SetValue(str(word))
 
    def get_ctr_text(self):
        return str(self.ctrl.GetValue())

    def notify(self, *arg):
        word = self.subject.word
        self.set_word(word)

class InvertedView(View):
    def __init__(self, name):
        super(InvertedView, self).__init__(name)

    def set_word(self, word):
        self.ctrl.SetValue(str(word[::-1]))
        
class Controller:
    def __init__(self):
        self.model = Model("model","initial word")
        self.nview = View("nview")
        self.iview = InvertedView("iview")

        #both views subscribe to the model        
        self.nview.listen(self.model)
        self.iview.listen(self.model)
        
        #useful lambda :)
        self.nview.submit.Bind(wx.EVT_BUTTON, lambda evt: self.set_word(evt, self.nview.get_ctr_text()))
        self.iview.submit.Bind(wx.EVT_BUTTON, lambda evt: self.set_word(evt, self.iview.get_ctr_text()))
        self.nview.Show()
        self.iview.Show()

    def set_word(self, event, word):
        self.model.set_word(word)

def main():
    app = wx.App()
    controller = Controller()
    app.MainLoop()

main()
