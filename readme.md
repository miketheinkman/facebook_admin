## Facebook Admin Tools
Hacky crap to automate admin tasks that most definitely violates FB
TOS, so **use at your own risk**. Based on Selenium for Linux and
Windows. No plans to ever add MAC support, but it may almost work
 already. The only hangups would be the geckodriver version in bin/
 and another elif statement in utils/browser.py
* Must have Firefox installed to use. May add support for Chrome if I
feel froggy.
* Automation on FB sucks and will always suck. These scripts will be
slow, but the will work **at least at the time they are uploaded**. They
are more of a labor saver than a time saver, as Selenium automation is
restricted by browser rendering speed. Even if that wasn't the case, FB
algorithms will flag you for moving too fast, and restrict you from
certain actions.

#
#### Installation
* Install/verify that python is installed on your machine. Written in
Python3, but should be compatible with Python2.
* Verify that you have a Firefox install.
* Download and extract the zip file or clone the repo.
* Install the project requirements using pip. Make sure you run the
 following command from the same directory as requirments.txt.
```
pip install -r requirements.txt
```
* That's it. Now we can use some tools!
#
#### Usage
If using python 2, and you get an import error when you try to run a
script, **navigate to the facebook_admin directory** on the commandline. In
Windows, type `set PYTHONPATH=.`. On Linux, type `export PYTHONPATH=.`

 Currently supplied scripts:
 * Post Approval - open terminal or cmd window. Navigate to the
 postapproval directory and type:
```
 python main.py
 ```
 or
 ```
 python3 main.py
 ```
 Depending on your Python install.
* Follow the scripted prompts to provide needed information.
* Once the script has the needed information, it will open a Firefox
window and log you into Facebook. It will then wait for 10 seconds
before completing the scripted actions. In that time, make sure any
dialog boxes that Firefox opens (eg: permission to send notifications)
are all closed.