from Netflix import Netflix
from uuid import uuid4
import os
from dotenv import load_dotenv

load_dotenv('.env')

if __name__ == "__main__":
	netflix = Netflix()
	try:
		email 			= str(uuid4()) + "@yopmail.com"
		password 		= str(uuid4()) + '@//*'
		cardLastName 	= os.getenv('CARD_LAST_NAME')
		cardFirstName 	= os.getenv('CARD_FIRST_NAME')
		cbNumber 		= os.getenv('CARD_NUMBER')
		expireDate 		= os.getenv('CARD_EXPIRE_DATE')
		cvv 			= os.getenv('CARD_CVV')

		print('email: ' + email, 'password: ' + password)
		account = netflix.register(email, password, cbNumber, expireDate, cvv, cardLastName, cardFirstName)

	except Exception as e:
		netflix.quit()
		raise e
