from pywebcopy import save_webpage, save_website
import validators


def warning(text):
    print("\033[1m\033[31m{}\033[0m".format(text))

def webpage(url, folder, name):
    save_webpage(
      url=url,
		  project_folder=folder,
		  project_name=name,
		  bypass_robots=True,
		  debug=True,
		  open_in_browser=True,
		  delay=None,
		  threaded=False,
    )
		
  
