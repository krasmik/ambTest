from pages.base_page import BasePage

class CancelPopup(BasePage):
    approve_text = {"title": "Are you sure you want to cancel Amberg Track Pro Field installation?", "control_type": "Text"}

    def is_approve_text_present(self):
        return self.wait_for_element(**self.approve_text, timeout=3).exists()