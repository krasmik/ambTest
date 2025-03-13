class BasePage:
    def __init__(self, window):
        self.window = window

    def wait_for_element(self, title, control_type, timeout=5):
        element = self.window.child_window(title=title, control_type=control_type)
        element.wait('exists', timeout=timeout)
        return element
