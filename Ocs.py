from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from faker import Faker

class Ocs(object):
    
    def __init__(self, threeScreen):
        two_screen = 'https://www.ocs.fr/souscription/creation?offer=999'
        three_screen = 'https://www.ocs.fr/souscription/creation?offer=1199'

        if threeScreen:
            self.base_url = three_screen
        else:
            self.base_url = two_screen

        self.fake = Faker()

        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)

    def register(self, email, passwd, cbNumber, expireMonth, expireYear, cvv, cardLastName, cardFirstName):
        name = self.fake.name()
        firstname = name.split(' ')[0]
        lastname = name.split(' ')[1]

        self.browser.get(self.base_url)
        sleep(1)
        
        # Create account
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        firstNameEl = self.browser.find_element_by_name("firstname")
        firstNameEl.send_keys(firstname)
        lastNameEl = self.browser.find_element_by_name("name")
        lastNameEl.send_keys(lastname)
        
        emailEl = self.browser.find_element_by_name("email")
        emailEl.send_keys(email)
        emailConfEl = self.browser.find_element_by_name("email-confirmation")
        emailConfEl.send_keys(email)

        password = self.browser.find_element_by_name("password")
        password.send_keys(passwd)
        
        # Remove cookie overlay
        try:
            self.browser.find_elements_by_css_selector('button.eu-cookie-compliance-secondary-button')[0].click()
            sleep(1)
        except Exception as e:
            print("Failed to remove cookie overlay")        

        # Send create account
        container = self.browser.find_elements_by_css_selector('div.action')[0]
        button = container.find_elements_by_css_selector('button.btn--fill')[0]
        button.click()

        # Switch to credit card iframe
        sleep(2)
        iframeContainer = self.browser.find_elements_by_css_selector('div.iframe')[0]
        iframe = iframeContainer.find_element_by_id('ocs-activation')
        self.browser.switch_to.frame(iframe)
        
        # Fill cb owner name
        inputCbOwner = self.browser.find_element_by_name('pai_nom')
        inputCbOwner.clear()
        inputCbOwner.send_keys(cardLastName + ' ' +cardFirstName)

        # Fill cb number
        cbNumber = str(cbNumber)
        creditCard = self.browser.find_element_by_name("pai_numcb_1")
        creditCard.send_keys(cbNumber[0:4])

        creditCard = self.browser.find_element_by_name("pai_numcb_2")
        creditCard.send_keys(cbNumber[4:8])

        creditCard = self.browser.find_element_by_name("pai_numcb_3")
        creditCard.send_keys(cbNumber[8:12])

        creditCard = self.browser.find_element_by_name("pai_numcb_4")
        creditCard.send_keys(cbNumber[12:16])
        
        # cb month
        select = Select(self.browser.find_element_by_name('pai_expir_mm'))
        select.select_by_value(expireMonth)

        # cb year
        select = Select(self.browser.find_element_by_name('pai_expir_aa'))
        select.select_by_value(expireYear)

        # cb code
        creditCardCode = self.browser.find_element_by_name("pai_cvc")
        creditCardCode.send_keys(cvv)

        button = self.browser.find_element_by_id('btn-active-abo')
        button.click()
        sleep(20)
        
        self.browser.switch_to.default_content()
        self.browser.quit()

    def quit(self):
        self.browser.quit()

    def cancelSubscription(self):
        base_url = 'https://go.ocs.fr/'
        self.browser.get(base_url)
        sleep(1)
        self.browser.find_elements_by_css_selector('span.delete_profil')[0].click()
        sleep(1)
        self.browser.find_elements_by_css_selector('span.confirm_delete_profil')[0].click()


        cancelContainer.find_elements_by_css_selector('button.btn')[0].click()