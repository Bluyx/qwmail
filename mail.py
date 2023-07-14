import httpx, time



def getVerification(email, password, verification_location, sender="ALL", waitForVerification=True):
    if verification_location not in ["subject", "body"]:
        raise ValueError("Invalid verification location. Valid options are 'subject' and 'body'")
    while True:
        getCode = httpx.post("http://mail.qwmail.xyz/v2/get_code", data={"email": email, "password": password, "verification_location": verification_location, "from": sender})
        if getCode.status_code == 200:
            if getCode.json()["success"]:
                return getCode.json()["response"]
            elif getCode.json()["message"] == "message not found":
                pass
        else:
            print((f"Error: {getCode.status_code}"))
            return False
        if not waitForVerification: break
        time.sleep(3)


def createEmail(username, password):
    createEmail = httpx.post("http://mail.qwmail.xyz/create_email", data={"username": username, "password": password})
    if createEmail.status_code == 200:
        if createEmail.json()["message"] == "Account Created":
            return createEmail.json()["account"]
        elif createEmail.json()["message"] == "Same name already exists":
            return False # Email already registered
    else:
        print((f"Error: {createEmail.status_code}"))
        return False


