class Debug:
    """
    A utility class to allow an easier print/debug.
    Used like the print function.

    Example:

        ```python
        debug = Debug()
        debug("Hello", "world", sep=", ", end="!\n")
        # -> "Hello, world!"
        debug.set(False)
        debug("Disabled")
        # -> nothing
        debug.toggle()
        debug("Enabled")
        # -> "Enabled"
        ```
    """

    def __init__(self, debug: bool = True):
        self._debug = debug

    def __call__(self, *args, **kwargs):
        """
        Print if the debug is enabled.
        """

        if self._debug:
            print(*args, **kwargs)

    # Methods

    def enable(self):
        self._debug = True

    def disable(self):
        self._debug = False

    def toggle(self):
        """
        If enabled, disable.
        If disabled, enable.
        """

        self._debug = not self._debug
