from selenium import webdriver
from time import sleep

class Netflix(object):
    
    def __init__(self):
        self.base_url = 'https://www.netflix.com/signup/regform'

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        
        self.browser = webdriver.Chrome(options=options)

    def register(self, email, passwd, cbNumber, expireMonth, expireYear, cvv, cardLastName, cardFirstName):
        expireDate = str(expireMonth) + str(expireYear)[2:4]
        self.browser.get(self.base_url)
        sleep(1)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # First step
        centerContainer = self.browser.find_elements_by_css_selector('div.centerContainer')[0]
        container = centerContainer.find_elements_by_css_selector('div.submitBtnContainer')[0]
        button = container.find_elements_by_css_selector('button.nf-btn')[0]
        button.click()
        sleep(1)
        
        # Select plan
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        centerContainer = self.browser.find_elements_by_css_selector('div.centerContainer')[0]
        container = centerContainer.find_elements_by_css_selector('div.submitBtnContainer')[0]
        button = container.find_elements_by_css_selector('button.nf-btn')[0]
        button.click()
        sleep(1)
        
        # Go to create account page
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        centerContainer = self.browser.find_elements_by_css_selector('div.centerContainer')[0]
        container = centerContainer.find_elements_by_css_selector('div.submitBtnContainer')[0]
        button = container.find_elements_by_css_selector('button.nf-btn')[0]
        button.click()
        sleep(1)

        # Create account
        # Find and input user and password
        username = self.browser.find_element_by_name("email")
        username.send_keys(email)

        password = self.browser.find_element_by_name("password")
        password.send_keys(passwd)
        
        # Send create account
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        container = self.browser.find_elements_by_css_selector('div.submitBtnContainer')[0]
        button = container.find_elements_by_css_selector('button.nf-btn')[0]
        button.click()
        sleep(1)

        # Select card payement
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        centerContainer = self.browser.find_elements_by_css_selector('div.paymentContainer')[0]
        link = centerContainer.find_elements_by_css_selector('a.nfTabSelection--active')[0]
        link.click()
        sleep(1)

        # Add credit card information
        firstName = self.browser.find_element_by_name("firstName")
        firstName.send_keys(cardFirstName)

        lastName = self.browser.find_element_by_name("lastName")
        lastName.send_keys(cardLastName)

        creditCard = self.browser.find_element_by_name("creditCardNumber")
        creditCard.send_keys(cbNumber)
        
        creditExpiration = self.browser.find_element_by_name("creditExpirationMonth")
        creditExpiration.send_keys(expireDate)
        
        creditCardCode = self.browser.find_element_by_name("creditCardSecurityCode")
        creditCardCode.send_keys(cvv)
        
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        container = self.browser.find_elements_by_css_selector('div.submitBtnContainer')[0]
        button = container.find_elements_by_css_selector('button.nf-btn')[0]
        button.click()
        self.browser.quit()

    def quit(self):
        self.browser.quit()

    def cancelSubscription(self):
        accountUrl = 'https://www.netflix.com/CancelPlan'
        self.browser.get(accountUrl)
        cancelContainer = self.browser.find_elements_by_css_selector('div.cancelContainer')[0]
        cancelContainer.find_elements_by_css_selector('button.btn')[0].click()