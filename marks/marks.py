import pytest, py
from _pytest.mark import MarkInfo

def pytest_namespace():
    return {'marks': MarksDecorator}

class MarksDecorator(object):
    """ A decorator.  Example::

         import py
         @py.test.marks('mark_one', 'mark_two', 'mark_n')
         def test_function():
            pass

    will set a 'slowtest' :class:`MarkInfo` object
    on the ``test_function`` object. """
    
    def __init__(self, *args):
        self.marks = args
        
    def __call__(self, f):
        for mark in self.marks:
            info = MarkInfo(mark, (), {})
            setattr(f, mark, info)
        return f