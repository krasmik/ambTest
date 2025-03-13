from pages.base_page import BasePage

class SetupPage(BasePage):
    next_button = {"title": "Next", "control_type": "Pane"}

    def click_next(self):
        self.window.child_window(**self.next_button).wait('exists', timeout=3).click_input()