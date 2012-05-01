import xbmcgui
import xbmcaddon
import xbmc

from framework.settings import SCRIPT_ID


class XMLWindowMetaclass(type):
    def __new__(metacls, name, bases, dct):

        if len(bases):
            parent_callback_click_stack = getattr(bases[0], "callback_click_stack", {})
            parent_callback_focus_stack = getattr(bases[0], "callback_focus_stack", {})

        callback_click_stack = dct.get('callback_click_stack', {})
        callback_focus_stack = dct.get('callback_focus_stack', {})

        # combine dictionaries from base class
        callback_focus_stack = dict(callback_focus_stack, **parent_callback_focus_stack)
        callback_click_stack = dict(callback_click_stack, **parent_callback_click_stack)

        for func_name, func in dct.items():
            # if on click callbacks declared
            if hasattr(func, "_callback_to_click_on"):
                for controlId in func._callback_to_click_on:
                    callback_list = callback_click_stack.get(controlId)
                    if callback_list is not None:
                        callback_list.append(func)
                        callback_click_stack[controlId] = callback_list
                    else:
                        callback_click_stack[controlId] = [func]

            # if on focus callbacks declared
            if hasattr(func, "_callback_to_focus_on"):
                for controlId in func._callback_to_focus_on:
                    callback_list = callback_focus_stack.get(controlId)
                    if callback_list is not None:
                        callback_list.append(func)
                        callback_focus_stack[controlId] = callback_list
                    else:
                        callback_focus_stack[controlId] = [func]


        dct["callback_click_stack"] = callback_click_stack
        dct["callback_focus_stack"] = callback_focus_stack
        return type.__new__(metacls, name, bases, dct)

class Manager(object):

    def __init__(self, window):
        self.window = window


    def show(self, *ids):
        for id in ids:
            self.window.getControl(id).setVisible(True)


    def hide(self, *ids):
        for id in ids:
            self.window.getControl(id).setVisible(False)




class Progress(object):
    def __init__(self):
        self.progress = xbmcgui.DialogProgress()
        

    def show(self, message="Loading"):
        self.progress.create(message)


    def hide(self):
        self.progress.close()


def with_progress(func):
    def with_progress_func(self, *args, **kwargs):
        progress = Progress()
        progress.show(message="Loading")
        resp = func(self, *args, **kwargs)
        progress.hide()
        return resp
    return with_progress_func


class XMLWindow(xbmcgui.WindowXML):


    # extra methods you can define to react on actions
    action_callbacks = {10: 'onExit',
                        0: 'onCtrl'
                       }

    def __init__(self,*args,**kwargs):
        super(XMLWindow,self).__init__(*args,**kwargs)


        self.params = None
        if kwargs.get('params'):
            self.params = kwargs['params']
 
        self.manager = Manager(self)

        self.config = xbmcaddon.Addon(id=SCRIPT_ID)


    __metaclass__ = XMLWindowMetaclass


    def onFocus(self, controlID):
        callbacks_list = self.callback_focus_stack.get(controlID)
        if callbacks_list is not None:
            for callback in callbacks_list:
                callback(self)


    def onClick(self, controlID):
        callbacks_list = self.callback_click_stack.get(controlID)
        if callbacks_list is not None:
            for callback in callbacks_list:
                callback(self)


    def onAction(self, action):
        id = action.getId()
        callback_name = self.action_callbacks.get(id,None)
        if callback_name is not None:
            callback = getattr(self,callback_name,None)
            if callback is not None:
                callback()
        # define low level on action behavior
        return super(XMLWindow,self).onAction(action)


    def notify(self, message, header="Message"):
        xbmc.executebuiltin("XBMC.Notification(%s,%s)" % (header,message))

   
def onclick(*controlIDs):
    def real_decorator(func):
        control_ids = getattr(func,"_callback_to_click_on",None)
        if control_ids is not None:
            control_ids.extend(list(controlIDs))
            setattr(func, "_callback_to_click_on", control_ids)
        else:
            setattr(func, "_callback_to_click_on", list(controlIDs))
        return func
    return real_decorator


def onfocus(*controlIDs):
    def real_decorator(func):
        control_ids = getattr(func,"_callback_to_focus_on",None)
        if control_ids is not None:
            control_ids.extend(list(controlIDs))
            setattr(func, "_callback_to_focus_on", control_ids)
        else:
            setattr(func, "_callback_to_focus_on", list(controlIDs))
        return func
    return real_decorator








