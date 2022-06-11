# PyWebCopy is a free tool for copying full or partial websites locally onto your hard-disk for offline viewing.

# https://github.com/rajatomar788/pywebcopy/

# Installation
pip install pywebcopy

import pywebcopy

# pywebcopy.__version___


# To save any single page
from pywebcopy import save_webpage

save_webpage(
      url="https://httpbin.org/",
      project_folder="E://savedpages//",
      project_name="my_site",
      bypass_robots=True,
      debug=True,
      open_in_browser=True,
      delay=None,
      threaded=False,
)


# To save full website (This could overload the target server, So, be careful) !!!
from pywebcopy import save_website

save_website(url="https://httpbin.org/",
             project_folder="E://savedpages//",
             project_name="my_site",
             bypass_robots=True,
             debug=True,
             open_in_browser=True, 
             delay=None, 
             threaded=False,
            )


# Running Tests
# Running tests is simple and doesn't require any external library. Just run this command from root directory of pywebcopy package.

# python -m pywebcopy --tests


# Using CLI

# Getting list of commands
# python -m pywebcopy --help

"""
Usage: pywebcopy [-p|--page|-s|--site|-t|--tests] [--url=URL [,--location=LOCATION [,--name=NAME [,--pop [,--bypass_robots [,--quite [,--delay=DELAY]]]]]]]

Python library to clone/archive pages or sites from the Internet.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --url=URL             url of the entry point to be retrieved.
  --location=LOCATION   Location where files are to be stored.
  -n NAME, --name=NAME  Project name of this run.
  -d DELAY, --delay=DELAY
                        Delay between consecutive requests to the server.
  --bypass_robots       Bypass the robots.txt restrictions.
  --threaded            Use threads for faster downloading.
  -q, --quite           Suppress the logging from this library.
  --pop                 open the html page in default browser window after
                        finishing the task.

  CLI Actions List:
    Primary actions available through cli.

    -p, --page          Quickly saves a single page.
    -s, --site          Saves the complete site.
    -t, --tests         Runs tests for this library.

"""

