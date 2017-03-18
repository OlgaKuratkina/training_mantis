from model.project import Project
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Project_helper:
    def __init__(self, app):
        self.app = app

    def fill_text_field(self, field_id, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_id).click()
            wd.find_element_by_id(field_id).clear()
            wd.find_element_by_id(field_id).send_keys(text)

    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.2.1/manage_proj_page.php")
        #wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_data(self, project):
        self.fill_text_field("project-name", project.name)
        self.fill_text_field("project-description", project.description)

    project_cache = None

    def get_project_list(self):
        self.open_project_page()
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for elem in wd.find_elements_by_css_selector("tbody tr")[:-1]:
                name = elem.find_elements_by_css_selector("td")[0].text
                description = elem.find_elements_by_css_selector("td")[4].text
                self.project_cache.append(Project(name=name, description=description))
        return self.project_cache

    def open_project_by_name(self, name):
        wd = self.app.wd
        self.open_project_page()
        for elem in wd.find_elements_by_css_selector("tbody tr")[:-1]:
            if elem.find_elements_by_css_selector("td")[0].text == name:
                elem.find_elements_by_css_selector("td")[0].click()
                break

    def delete_opened_project(self):
        wd = self.app.wd
        try:
            element = WebDriverWait(wd, 10).until(
                EC.presence_of_element_located(wd.find_element_by_xpath("//input[@value = 'Delete Project']"))
            )
        finally:
            wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
            wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[type='submit']").click()
        self.fill_project_data(project)
        wd.find_element_by_css_selector("input[type='submit']").click()

    # wd.get("http://localhost/mantisbt-2.2.1/manage_proj_create_page.php")
    # wd.find_element_by_link_text("Manage Projects").click()
    # wd.find_element_by_xpath("//div[@class='row']/div/div[2]/div[2]/div[2]/form/fieldset/input[2]").click()
    # wd.find_element_by_id("project-name").click()
    # wd.find_element_by_id("project-name").clear()
    # wd.find_element_by_id("project-name").send_keys("New Project")
    # wd.find_element_by_id("project-description").click()
    # wd.find_element_by_id("project-description").clear()
    # wd.find_element_by_id("project-description").send_keys("Description")
    # wd.find_element_by_xpath("//form[@id='manage-project-create-form']/div/div[3]/input").click()