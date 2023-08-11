# from lesson_package.tools import utils
from ..tools import utils   # あんまり勧められてない

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')