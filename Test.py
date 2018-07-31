# -*- coding: utf-8 -*-
from selenium import webdriver
import time, unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):


    def setUp(self):
        self.wd = webdriver.Firefox(executable_path="C:/Users/Alex/AppData/Local/Programs/Python/Python37-32/geckodriver.exe")

    def test_test_add_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, 'admin', 'secret')
        self.open_groups_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, 'test', 'test', 'test')
        self.submit_group_creation(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text('Вийти').click()

    def submit_group_creation(self, wd):
        # submit group creation
        wd.find_element_by_name('submit').click()

    def fill_group_form(self, wd, name, header, footer):
        # fill group form
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_keys(name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_keys(header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_keys(footer)

    def init_group_creation(self, wd):
        # init group creation
        wd.find_element_by_name('new').click()

    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("Групи").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name('user').click()
        wd.find_element_by_name('user').clear()
        wd.find_element_by_name('user').send_keys(username)
        wd.find_element_by_name('pass').click()
        wd.find_element_by_name('pass').clear()
        wd.find_element_by_name('pass').send_keys(password)
        wd.find_element_by_css_selector('input[type=\"submit\"]').click()
        time.sleep(1)

    def open_home_page(self, wd):
        # open home page
        wd.get('http://localhost/addressbook/addressbook')

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()

