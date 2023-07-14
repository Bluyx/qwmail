from mail import createEmail, getVerification



# Create an email first
createEmail("example@qwmail.xyz", "myPassword")


# Send message to email...

# receive verification
verification = getVerification(email="example@qwmail.xyz", password="myPassword", verification_location="subject") # verification_location "subject" or "body"

print(verification) # example output: 562858 - Sign Up Verification Code.

