# Origin taked here: https://habr.com/ru/post/669766/ - Download site

from pywebcopy import save_webpage, save_website
import validators


def warning(text):
    print("\033[1m\033[31m{}\033[0m".format(text))

def webpage(url, folder, name):
    save_webpage(url=url,
		 project_folder=folder,
		 project_name=name,
		 bypass_robots=True,
		 debug=True,
		 open_in_browser=True,
		 delay=None,
		 threaded=False,
    )

def website(url, folder, name):
	save_website(
		url=url,
		project_folder=folder,
		project_name=name,
		bypass_robots=True,
		debug=True,
		open_in_browser=True,
		delay=None,
		threaded=False,
	)

print("""Choose a number:
1 - Save page
2 - Save page""")

b=False	
  
