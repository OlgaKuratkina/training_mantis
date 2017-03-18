# -*- coding: utf-8 -*-
import pytest
from data.project_data import projects
from model.project import Project


@pytest.mark.parametrize("project", projects, ids=[repr(x) for x in projects])
def test_add_project(app, project):
    old_projects = app.project.get_project_list()
    app.project.add_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.get_name) == sorted(new_projects, key=Project.get_name)
