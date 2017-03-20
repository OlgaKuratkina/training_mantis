from fixture.application import Application

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


app = Application("firefox", "/target.json")
wd = app.wd
app.session.login("administrator", "root1")
print(wd.find_element_by_xpath("//span[@class = 'label hidden-xs label-default arrowed']").text)
print("executing")
app.project.open_project_page()
print(wd.find_element_by_xpath("//span[@class = 'label hidden-xs label-default arrowed']").text)
#print(app.session.get_logged_username())
#print(app.project.get_project_list())
# ls = wd.find_elements_by_css_selector("tbody tr")
#names = ls.find_element_by_css_selector("td a").text
# for elem in ls[:-1]:
#     #name = elem.find_element_by_css_selector("a").text
#     print("NEXT ONE")
#     name = elem.find_elements_by_css_selector("td")[0].text
#     descr = elem.find_elements_by_css_selector("td")[4].text
#     print(name, "", descr)
# app.project.open_project_by_name("567890ззшгнеку45678ш9щз0")
# wd.maximize_window()
# wd.find_element_by_xpath("//form[@id='project-delete-form']//input[@type='submit']").click()
# wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
# print("")

