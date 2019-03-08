import settings

from selenium import webdriver
import os
import sys

def platform_browser():
    if settings.PLATFORM == 'linux':
        if sys.maxsize > 2 ** 32:
            browser = webdriver.Firefox(executable_path=os.path.join(settings.BIN_PATH,
                                                                     'geckodriver64'))
        else:
            browser = webdriver.Firefox(executable_path=os.path.join(settings.BIN_PATH,
                                                                     'geckodriver'))

    elif settings.PLATFORM == 'windows':
        if sys.maxsize > 2 ** 32:
            browser = webdriver.Firefox(executable_path=os.path.join(settings.BIN_PATH,
                                                                     'geckodriver64.exe'))
        else:
            browser = webdriver.Firefox(executable_path=os.path.join(settings.BIN_PATH,
                                                                     'geckodriver.exe'))

    return browser
