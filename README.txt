Pytest-Marks
============

The ability to set 'marks' on py.test test methods is pretty cool.

    @pytest.mark.red
    def some_test_method(self):
        # some check-y stuff

But if you have a half dozen marks that you want to put on a method, it gets kinda yucky.

    @pytest.mark.red
    @pytest.mark.green
    @pytest.mark.blue
    @pytest.mark.black
    @pytest.mark.orange
    @pytest.mark.pink
    def some_test_method(self):
        # some check-y stuff

What would be nice is if you could apply them all in a single decorator.

    @pytest.marks('red', 'green', 'blue', 'black', 'orange', 'pink')
    def some_test_method(self):
        # some check-y stuff

Well, now you can.

To install, either
* pip install pytest-marks
* python setup.py install
