import platform
import allure
import pytest
from pywinauto import Application
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(BASE_DIR, "..", "app", "amb.exe")

@pytest.fixture()
def app():
    app = Application(backend="uia").start(app_path, timeout=10000)
    time.sleep(2)
    app.connect(best_match="Amberg Track Pro Field Installer", timeout=5)
    yield app.window()
    app.kill(soft=True)

@pytest.fixture(scope="session", autouse=True)
def add_environment_info():
    os.makedirs("allure-results", exist_ok=True)
    env_info = {
        "OS": f"{platform.system()} {platform.release()}",
        "Python Version": platform.python_version(),
        "Processor": platform.processor(),
    }
    with open(os.path.join("allure-results", "environment.properties"), "w") as f:
        for key, value in env_info.items():
            f.write(f"{key}={value}\n")

    allure.attach(str(env_info), name="System Info", attachment_type=allure.attachment_type.TEXT)
