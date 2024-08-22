from appJar import gui
import random


# OTP functions
def generated_otp():
    return random.randint(100000, 999999)


def sending_otp(otp):
    print(f'Sending OTP {otp} to the registered email address')
    print('OTP sent')


def verify_otp(generated_otp, entered_otp):
    try:
        entered_otp = int(entered_otp)
    except ValueError:
        return False
    return generated_otp == entered_otp


# handle button events for the OTP window
def press_otp(button):
    if button == "Cancel":
        app.stop()
    elif button == "Resend OTP":
        resend_otp()
    else:
        entered_otp = app.getEntry("OTP")
        if verify_otp(app.otp, entered_otp):
            print('Access Granted')
            app.infoBox("Success", "Access Granted")
            app.stop()
        else:
            app.attempts -= 1
            if app.attempts > 0:
                app.errorBox("Error", f'Access Denied. You have {app.attempts} attempt(s) left.')
            else:
                app.errorBox("Error", 'Too many incorrect attempts. Access Denied.')
                app.stop()


# OTP prompt window
def prompt_otp():
    app.otp = generated_otp()
    sending_otp(app.otp)

    app.setBg("White")
    app.setFont(18)
    app.attempts = 3

    app.addLabel("otp_title", "Enter the OTP sent to your email")
    app.setLabelBg("otp_title", "blue")
    app.setLabelFg("otp_title", "gray")

    app.addLabelSecretEntry("OTP")

    app.addButtons(["Submit", "Resend OTP", "Cancel"], press_otp)

    app.go()


# Resend OTP function
def resend_otp():
    app.otp = generated_otp()
    sending_otp(app.otp)
    app.infoBox("Info", "A new OTP has been sent to your email address.")


# create a GUI variable called app
app = gui("OTP Verification", "400x200")
prompt_otp()
