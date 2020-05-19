from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
            WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-title")))

    def return_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-title")))


    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]")[index].click()

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("%s" % name).click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.app.change_field_value(name="name", value=project.name)
        if project.status is not None:
            wd.find_element_by_name("status").click()
            Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        if not project.inherit_global:
            wd.find_element_by_name("inherit_global").click()
        if project.view_state is not None:
            wd.find_element_by_name("view_state").click()
            Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        self.app.change_field_value(name="description", value=project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        # init group creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill group form
        self.fill_project_form(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        # return to groups page
        self.return_to_project_page()
        self.project_cache = None

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        # return to groups page
        self.return_to_project_page()
        self.project_cache = None

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_project_page()
        self.select_project_by_name(name)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        # return to groups page
        self.return_to_project_page()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"))

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            all_elements = wd.find_elements_by_xpath("//table[3]/tbody/tr")
            rows = all_elements[2:]
            for element in rows:
                cells = element.find_elements_by_tag_name("td")
                self.project_cache.append(Project(name=cells[0].text, status=cells[1].text,
                                                  inherit_global=cells[2].text, view_state=cells[3].text,
                                                  description=cells[4].text))
        return list(self.project_cache)
