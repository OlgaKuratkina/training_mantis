

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.maxim()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.get('http://localhost/mantisbt-2.2.1/login_page.php')

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def maxim(self):
        wd = self.app.wd
        wd.maximize_window()

    def is_logged_in_as(self, username):
        return self.get_logged_username() == username

    def get_logged_username(self):
        wd = self.app.wd
        self.maxim()
        return wd.find_element_by_xpath("//span[@class = 'user-info']").text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)