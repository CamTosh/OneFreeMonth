from Netflix import Netflix
from Ocs import Ocs
from uuid import uuid4
import os
from dotenv import load_dotenv
import argparse

if __name__ == "__main__":
	ap = argparse.ArgumentParser()

	ap.add_argument("--env", type=str, required=False, help="Select .env file")
	ap.add_argument("--netflix", type=bool, required=False, help="Create Netflix account")
	ap.add_argument("--ocs", type=bool, required=False, help="Create Ocs account")
	
	args = vars(ap.parse_args())
	
	if args['env']:
		load_dotenv(args['env'])
	else:
		load_dotenv('.env')

	if args['netflix']:
		print('Selected provider: Netflix')
		provider = Netflix()
	if args['ocs']:
		print('Selected provider: Ocs with three screen plan')
		provider = Ocs(threeScreen=True)
	
	email 			= str(uuid4())[:8] + "@yopmail.com"
	password 		= str(uuid4()) + '@//*'
	cardLastName 	= os.getenv('CARD_LAST_NAME')
	cardFirstName 	= os.getenv('CARD_FIRST_NAME')
	cbNumber 		= os.getenv('CARD_NUMBER')
	expireMonth		= os.getenv('CARD_EXPIRE_MONTH')
	expireYear 		= os.getenv('CARD_EXPIRE_YEAR')
	cvv 			= os.getenv('CARD_CVV')

	print('email: ' + email, 'password: ' + password)

	try:
		account = provider.register(email, password, cbNumber, expireMonth, expireYear, cvv, cardLastName, cardFirstName)
	except Exception as e:
		provider.quit()
		raise e
