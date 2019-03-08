from __future__ import print_function
from utils import browser, menu
from selenium.common.exceptions import ElementNotInteractableException

from time import sleep
import sys
if sys.version_info[0] < 3:
    from utils.compat import input


# scripting to collect input
act = input("To delete all posts, press 0. To approve press 1. Then Hit ENTER.")

if str(act) == '0':
    action = 'Approve'
elif str(act) == '1':
    action = 'Delete'
else:
    raise ValueError

data = menu.get_data()
asked_count = input("How many posts would you like to approve/delete?\n"
                    "Enter a number and press ENTER.\n"
                    "Press Enter to skip")
if asked_count:
    count = int(asked_count)
else:
    count = 10000
posts_url = data['url'] + '/pending'
print(posts_url)


# initialize browser and login to pending posts page
browser = browser.platform_browser()
browser.get(posts_url)
menu.login(browser, data)
sleep(10)
posts = browser.find_elements_by_xpath("//*[contains(text(), '{}')]".format(action))


# loop to delete/approve posts
addressed = 0
for i in range(count):
    while posts:
        try:
            # you can try to run without this sleep command,
            # but will might trip FB anti-botting.
            # just delete it or comment it out with a # if you want
            sleep(1)

            post = posts.pop(0)
            post.click()
            addressed += 1
            print("Posts addressed: {}".format(str(addressed)))
        except ElementNotInteractableException:
            continue

browser.close()
