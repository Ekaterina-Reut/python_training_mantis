# -*- coding: utf-8 -*-
# from operator import attrgetter
from model.project import Project


def test_add_project(app, data_projects):
    project = data_projects
    # old_projects = app.project.get_project_list()
    old_projects = app.soap.get_user_projects()
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    # new_projects = app.project.get_project_list()
    new_projects = app.soap.get_user_projects()
    old_projects.append(project)
    # assert sorted(old_projects, key=attrgetter('name')) == sorted(new_projects, key=attrgetter('name'))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
