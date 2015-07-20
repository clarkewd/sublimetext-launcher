#!/usr/bin/env python

import sys
from urlparse import urlparse
from urlparse import parse_qs
from urllib import unquote
import subprocess

# this will handle the following type of link:
# subl://open?url=file://%2FUsers%2Fexample%2Frails%2Fapp1%2Fapp%2Fmodels%2Ftest.rb&line=123
#
# tested and debugged from the command line by running something like:
# ./subl-launcher.py 'subl://open?url=file://%2FUsers%2Fexample%2Frails%2Fapp1%2Fapp%2Fmodels%2Ftest.rb&line=123'
#
# it could use a little work with better error handling for when
# it gets a string that doesn't fit the desired format, but if
# the format is right it seems to work well

x = parse_qs(urlparse(unquote(sys.argv[1])).query)
path = x['url'][0].replace('file://','')
line = x['line'][0]
subprocess.call(['/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl', '%s:%s' % (path, line)])

