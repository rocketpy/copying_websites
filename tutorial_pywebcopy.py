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
