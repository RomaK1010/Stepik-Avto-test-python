from selenium.common.exceptions import should_be_login_link
from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
	
    def open(self):
	    self.browser.get(self.url)
	
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)	
	
    def is_element_present(self, CSS_SELECTOR, "#login_link_invalid"):
        try:
            self.browser.find_element(CSS_SELECTOR, "#login_link_invalid")
        except (should_be_login_link):
            return False
        return True