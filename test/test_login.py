def test_login(app):
    #app.session.login("administrator", "root1")
    print(app.session.get_logged_username())
    assert app.session.is_logged_in_as('administrator')
