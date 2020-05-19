# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name='For delete'))
    old_projects = app.soap.get_user_projects()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.soap.get_user_projects()
    old_projects.remove(project)
    assert old_projects == new_projects

