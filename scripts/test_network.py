import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import Networkpage

class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.display_page = Networkpage(self.driver)

    def test_mobile_network_2g(self):
        # 点击更多
        self.display_page.click_more()
        # 点击移动网络
        self.display_page.click_network()
        # 点击首选网络类型
        self.display_page.click_first_network()
        # 点击2G
        self.display_page.click_2g()

    def test_mobile_network_3g(self):
        # 点击更多
        self.display_page.click_more()
        # 点击移动网络
        self.display_page.click_network()
        # 点击首选网络类型
        self.display_page.click_first_network()
        # 点击3G
        self.display_page.click_3g()
        
    def test_mobile_network_4g(self):
        # 点击更多
        self.display_page.click_more()
        # 点击移动网络
        self.display_page.click_network()
        # 点击首选网络类型
        self.display_page.click_first_network()
        # 点击3G
        self.display_page.click_3g()
        
    def test_mobile_network_5g(self):
        # 点击更多
        self.display_page.click_more()
        # 点击移动网络
        self.display_page.click_network()
        # 点击首选网络类型
        self.display_page.click_first_network()
        # 点击3G
        self.display_page.click_3g()
        
    def test_mobile_network_6g(self):
        # 点击更多
        self.display_page.click_more()
        # 点击移动网络
        self.display_page.click_network()
        # 点击首选网络类型
        self.display_page.click_first_network()
        # 点击3G
        self.display_page.click_3g()
        
    def test_mobile_network_7g(self):
        # 点击更多
        self.display_page.click_more()
        # 点击移动网络
        self.display_page.click_network()
        # 点击首选网络类型
        self.display_page.click_first_network()
        # 点击3G
        self.display_page.click_3g()
