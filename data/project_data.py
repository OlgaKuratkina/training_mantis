from model.project import Project
import random
import string

symb = string.ascii_letters + string.digits + " "*10

projects = [Project(name="".join([random.choice(symb) for i in range(10)]), description="Its a project about something")]

#projects = [Project(name="lksuu67jk", description="Its a project about something")]

