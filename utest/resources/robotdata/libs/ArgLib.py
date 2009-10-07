class ArgLib(object):

    def __init__(self, mandatory_arg, default_arg=None):
        self._mandatory = mandatory_arg
        self._default =default_arg

    def get_mandatory(self):
        return self._mandatory

    def get_default(self):
        if not self._default:
            raise AssertionError("Default not properly set!")
        return self._default
