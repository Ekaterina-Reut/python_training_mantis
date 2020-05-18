# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_delete_some_group(app):
    # if len(app.project.get_project_list()) == 0:
    #     app.project.create(Project(name='For delete'))

    app.soap.get_project_list()

    # old_projects = app.project.get_project_list()
    # project = random.choice(old_projects)
    # # app.project.delete_project_by_name(project.name)
    # # assert len(old_projects) - 1 == app.project.count()
    # new_projects = app.project.get_project_list()
    # old_projects.remove(project)
    # assert old_projects == new_projects
