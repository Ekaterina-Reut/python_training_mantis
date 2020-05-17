from model.project import Project

testdata = [
    Project(name="Project 1 Name", status="release", inherit_global=True,
            view_state="private", description="Project Descr 1"),
    Project(name="Project 2 Name", status="stable", inherit_global=True,
            view_state="public", description="Project Descr 2"),
    Project(name="Project 3 Name", status="obsolete", inherit_global=True,
            view_state="private", description="Project Descr 3"),
    Project(name="Project 4 Name", status="development", inherit_global=True,
            view_state="private", description="Project Descr 4")
]