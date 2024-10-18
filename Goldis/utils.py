from http.client import responses

from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('33323265434643785A4B6E316F4C6E48454357714272547A497A46784232587338685877326631395848553D')
        params = {
            'sender':'',
            'receptor': phone_number,
            'message': f'{code}کد تایید شما '
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
