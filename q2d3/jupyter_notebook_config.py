# Configuration file for q2d2 ipython-notebook environment.

c = get_config()  # noqa

# load markdown notebooks with ipymd
c.NotebookApp.contents_manager_class = 'ipymd.IPymdContentsManager'
