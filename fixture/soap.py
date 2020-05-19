from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_user_projects(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        project_list = []
        try:
            project_list_soap = client.service.mc_projects_get_user_accessible(
                username=self.app.config['webadmin']['username'], password=self.app.config['webadmin']['password'])
            for item in project_list_soap:
                project_list.append(Project(name=item.name, status=item.status.name, view_state=item.view_state.name,
                                            description=item.description, id=item.id))
            return project_list
        except WebFault:
            return None
