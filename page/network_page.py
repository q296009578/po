from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Networkpage(BaseAction):
    # 更多按钮
    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    # 移动网络按钮
    network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    # 首选网络类型
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    # 2g按钮
    network_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    # 3g按钮
    network_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    # 点击更多
    def click_more(self):
        self.click(self.more_button)

    # 点击移动网络
    def click_network(self):
        self.click(self.network_button)

    # 点击首选网络类型
    def click_first_network(self):
        self.click(self.first_network_button)

    # 点击2G
    def click_2g(self):
        self.click(self.network_2g_button)

    # 点击3G
    def click_3g(self):
        self.click(self.network_3g_button)