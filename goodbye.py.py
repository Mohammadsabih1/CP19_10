#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Good Bye'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)

root = Tk()
quitButton(root)
mainloop()


# In[ ]:




