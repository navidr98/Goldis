from melipayamak import Api


def send_otp_code(phone_number, code):

    username = '93344440483'
    password = '84b7dc5'
    api = Api(username, password)
    sms = api.sms()
    to = f'{phone_number}'
    _from = '1000100120'
    text = f'{code}رمز حساب کابری '
    response = sms.send(to, _from, text)
    print(response)
