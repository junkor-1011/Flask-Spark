"""
TestClass module for test.

This is the test.

"""


class TestClass(object):
    """
    This is the TestClass.

    This is the pen.
    Is this the apple pen?
    Pen pineapple apple pen!

    ToDo: improve document

    Note:
        It is the note.

    Args:
        msg (str): message
        code (:obj:`int`, optional): Error code

    Attributes:
        attr1 (int): test attributes1
        attr2 (str): test attributes2
        msg (str): test message
        code: test code
    """
    attr1 = 10
    attr2 = "apple"

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code

    def method1(self, arg, str_arg="aaa"):
        """
        test methods.

        Note:
            it is the note for method.

        Args:
            arg (int): parameter
            str_arg (str): parameter_2
        Returns:
            print attr2 and return attr1
        """
        self.attr1 = arg
        self.attr2 = str_arg

        print(self.attr2)

        return self.attr1



