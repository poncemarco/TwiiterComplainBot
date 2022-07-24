from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

url_test = 'https://www.speedtest.net/es'
url_twitter = 'https://twitter.com/'


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url=url_test)
        start = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start.click()
        sleep(70)
        self.down = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"down: {self.down} \n up: {self.up}")
        self.driver.quit()

    def tweet_at_provider(self, user, password, promised_up, promised_down):
        self.driver.get(url=url_twitter)
        sleep(3)
        sign_in_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in_button.click()
        sleep(5)
        # base_window = self.driver.window_handles[0]
        # sign_in_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(sign_in_window)
        entry_username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        entry_username.send_keys(user)
        entry_username.send_keys(Keys.ENTER)
        sleep(3)
        entry_password = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        entry_password.send_keys(password)
        entry_password.send_keys(Keys.ENTER)
        tweet_space = self.driver.find_element(By.XPATH, '//*[@id="placeholder-24h8p"]')
        tweet_space.send_keys(f"Excuse me Internet Provider, why my internet speed {self.down} down/{self.up}up"
                              f"when I pay for {promised_down} down/ {promised_up} up?")
        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        self.driver.quit()




