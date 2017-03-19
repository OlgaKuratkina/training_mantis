from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.project import Project_helper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(firefox_binary=FirefoxBinary("c:\\Program Files\\Mozilla Firefox\\firefox.exe"))
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Can't recognize your browser %s" % browser)
        self.session = SessionHelper(self)
        self.config = config
        self.base_url = config["web"]["baseUrl"]
        self.project = Project_helper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def goto_groups_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        if not len(wd.find_elements_by_class_name("fdTableSortTrigger")) > 0:
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()