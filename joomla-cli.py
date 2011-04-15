#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from browser import get_browser

import sys

LOGOUT = '''input type="hidden" name="task" value="logout"'''


class Site(object):

    def __init__(self, site, user, password):
        self.browser = get_browser()
        self.site = site
        self.user = user
        self.password = password

    def _loggedin(self):
        html = self.browser.get_html()
        return LOGOUT in html if html else False

    def login(self):
        if not self._loggedin():
            form = self.browser.get_forms(self.site)[1]
            form["username"] = self.user
            form["passwd"] = self.password
        return self._loggedin()


def main():
    site, user, password = sys.argv[1:]
    site = Site(site, user, password)
    print(site.login())
    site.browser.show()


if __name__ == "__main__":
    exit(main())
