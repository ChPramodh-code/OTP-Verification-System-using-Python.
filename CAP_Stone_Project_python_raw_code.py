# For generating the OTP
import random
def generated_otp():
  return random.randint(100000,999999)
# For sending otp to user:
def sending_otp(otp,email):
  print(f'sending_otp {otp} to Email address')
  print('otp sent')
# For prompting the OTP and allow the user to enter the user:
# OTP verification system:
def prompt_the_user_to_enter_otp():
  return input(f'please enter otp sent to Email address or type resend:')
# for verify the OTP:
def verify_otp(generated_otp,entered_otp):
  try:
     entered_otp = int(entered_otp)
  except ValueError:
        return False
  return generated_otp == entered_otp
# Complete code with main function:
def main ():
  email='nonuser@gmail.com'    # exmaple email
  otp = generated_otp()
  sending_otp (otp,email)
  attempts = 3
  while attempts > 0:
    entered_otp = prompt_the_user_to_enter_otp()
    if entered_otp.lower() == 'resend':
        otp = generated_otp()
        sending_otp(otp, email)
        print('A new OTP has been sent to your email address.')
        continue
    if verify_otp(otp, entered_otp):
      print('Access Granted')
      break
    else:
      attempts-= 1
      print('Access denied')
      print(f'Entered wrong otp please try again,You have {attempts} attempt(s) left.')
  if attempts == 0:
   print(f'Too many Incorrect attempts.You have {attempts} attempt(s) left.')

# to run the above code:
if __name__ == "__main__":
    main()