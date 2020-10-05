--------
# Amagi 
--------
This repo contains notes on getting setup and using the code to pull feeds media information.

The setup has three parts:

1. Prerequisites
2. Setup for running the code
3. Run

__1. Prerequisites__

a) Install Python 3.6.x or greater.

b) Add Python 3.6.x to your PATH environment variable.

c) If you do not have it already, get pip (NOTE: Most recent Python distributions come with pip).

d) Clone or download the repository.

e) pip install -r requirements.txt to install dependencies.

__2. Setup for running the code__

a) Update the retrieve_feeds_media_details/conf.py file to include the API method, auth token, feed id and required aspect ratio & resolution.

__3. Run__

a) python3 media_info.py

--------
ISSUES?
-------

a) If Python complains about an "Import" exception, please 'pip3 install $module_name'.
