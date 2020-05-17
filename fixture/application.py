from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.project = ProjectHelper(self)

    # Auxiliary

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def change_field_value(self, name, value):
        wd = self.wd
        if value is not None:
            element = wd.find_element_by_name(name)
            element.click()
            element.clear()
            element.send_keys(value)

    # Home page

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    # Teardown

    def destroy(self):
        self.wd.quit()