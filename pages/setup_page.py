from pages.base_page import BasePage


class SetupPage(BasePage):
    next_button = {"title": "Next", "control_type": "Pane"}
    first_message = {"title": "Amberg Track Pro Field", "control_type": "Text"}

    def click_next(self):
        self.window.child_window(**self.next_button).wait('exists', timeout=3).click_input()

    def wait_for_load(self):
        self.window.child_window(**self.first_message).wait('exists', timeout=30)
