import time
from userInfo import username,password
from selenium import webdriver


class Instagram:
    def __init__(self,username,password):

        self.browser = webdriver.Chrome("path of chromedriver")
        self.username = username
        self.password = password

    def SignIn(self):

        self.browser.get("https://www.instagram.com/accounts/login/")    #instagram login page
        time.sleep(3)

        #we take xpath of username div and write username send keys
        self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(username)

        #we take xpath of password div and write password send keys
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)

        #we take xpath of loginbutton and click
        self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(2)


insta = Instagram(username,password)
insta.SignIn()