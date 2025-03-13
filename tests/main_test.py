import allure
from pages.setup_page import SetupPage
from pages.welcome_page import WelcomePage
from pages.popups.cancel_popup import CancelPopup



@allure.title("Verify that welcome text appears after clicking Next")
def test_welcome_text(app):
    with allure.step("Open Setup Page and click Next"):
        print(app.print_control_identifiers())
        setup_page = SetupPage(app)
        setup_page.click_next()

    with allure.step("Verify that the welcome text is displayed"):
        welcome_page = WelcomePage(app)
        assert welcome_page.is_welcome_text_present(), "Welcome text not found"


@allure.title("Verify that cancel popup appears when clicking Cancel")
def test_cancel_popup(app):
    with allure.step("Open Setup Page and click Next"):
        setup_page = SetupPage(app)
        setup_page.click_next()

    with allure.step("Verify that the welcome text is displayed"):
        welcome_page = WelcomePage(app)
        assert welcome_page.is_welcome_text_present(), "Welcome text not found"

    with allure.step("Click Cancel and verify the popup appears"):
        welcome_page.click_cancel()
        cancel_popup = CancelPopup(app)
        assert cancel_popup.is_approve_text_present(), "Cancel confirmation popup not found"
