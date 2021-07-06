print('welcome to ATM')
print('swip your card here')
language=input('enter your language:')
pin=int(input('enter pin to process:'))
cash==50000
if language=='English':
	if pin==4353:
		print('choose your transaction:')
		transaction=input('enter the transaction')
		account_type=input('enter account type:')
		if transaction=='Balance enquiry':
			if account_type=='saving':
				print(cash)
				Recipt=input('do you want slip:')
				if Recipt=='yes':
					print('here your slip')
				else:
					print('thank you')
		elif transaction=='withdrawal':
			if account_type=='saving':
				amt=int(input('enter any amt:'))
				if amt>0 and amt<=cash:
					print('collect your amt Rs.',amt)
				else:
					print('enter valid amt')		
		elif transaction=='change pin':
			phone_no=int(input('enter phone no:'))
			otp=int(input('enter otp:'))
			cpin=int(input('enter your old pin'))
			if phone_no==8904937408:
				if otp==8999:
					if cpin==pin:
						npin=int(input('enter your new pin'))
						confirm_pin=int(input('re enter your newpin'))
						if npin==confirm_pin:
							print(' Done,your pin is changed sucessfully')
						else:
							print('pin is not matching try again')
				else:
					print('pin is not correct')
		elif transaction=='quit':
			quit=input('enter yes to quit ')
			if quit=='yes':
				print('thank you remove your card')
			else:
				print('enter transaction')
		else:
			print('entet valid transaction')
	else:
		print('worng pin try again')
else:
	print("invalid language")