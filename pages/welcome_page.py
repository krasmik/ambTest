from pages.base_page import BasePage

class WelcomePage(BasePage):
    welcome_text = {"title": "Welcome to the Prerequisites Setup Wizard", "control_type": "Text"}
    cancel_button = {"title": "Cancel", "control_type": "Pane"}

    def is_welcome_text_present(self):
        return self.wait_for_element(**self.welcome_text, timeout=3).exists()

    def click_cancel(self):
        self.window.child_window(**self.cancel_button).wait('exists', timeout=3).click_input()