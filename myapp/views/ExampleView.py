
from myapp.classes import reMarkable
from myapp.views.base import BaseView
from carta import Widget

class ExampleView(BaseView):
    def __init__(self, reMarkable: reMarkable, additional_args: dict = {}) -> None:
        super().__init__(reMarkable, additional_args)
        self.hooks["example_*"] = self.click_me
        pass

    def display(self):
        
        self.rm.add(
            Widget(
                id="example",
                value="Hello World!",
                typ="label",
                x="50%",
                y="50%",
                fontsize="50"
            )
        )
        self.rm.add(
            Widget(
                id="example_button",
                value="Click Me!",
                typ="button",
                x="50%",
                y="75%",
                fontsize="30"
            )
        )
    
    def click_me(self, clicked):
        w = self.rm.lookup("example_button")
        w.value = "Clicked!"

        
        