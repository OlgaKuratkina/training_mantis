# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_delete_project(app):
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.open_project_by_name(project.name)
    app.project.delete_opened_project()
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)
