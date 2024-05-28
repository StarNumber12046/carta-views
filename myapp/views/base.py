from carta import ReMarkable

from myapp.classes import reMarkable

class BaseView(object):
    def __init__(self, reMarkable: reMarkable, additional_args: dict = {}) -> None:
        self.rm = reMarkable
        self.hooks = {}
        self.additional_args = additional_args
        pass

    def display(self):
        pass
    
    def handle_buttons(self, clicked): # Clicked is a tuple, the docs are wrong
        for hook in self.hooks.keys():
            if clicked and clicked[0] == hook:
                self.hooks[hook](clicked)
            