import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, greeting):
        print(greeting)
        return(True,greeting)