"""

"""
import os
import sys

# Paths
BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BIN_PATH = os.path.join(BASE_DIRECTORY, 'facebook_admin', 'bin')


INSTALLED_APPS = [
    {'postapproval': 'Post Approval'},
]

if sys.platform.startswith('linux'):
    PLATFORM = 'linux'
elif sys.platform.startswith('win'):
    PLATFORM = 'windows'