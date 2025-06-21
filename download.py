import requests   
from datetime import datetime
url_endpoint = 'http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes'

today = datetime.now().strftime('%d/%b/%Y')
print(today)

payload = {
    'Datefrom'   : '01/Jan/2010',
    'Dateto'     :  today,
    'SeriesCodes': 'LPMB5S9,LPMB6S2,LPMB6S3,LPMB75C,LPMB76C,LPMVYWO,LPMZ3TT,LPMZ3TV,LPMZ3TX,LPMVWLQ,LPMVWLW,RPMB3OM',
    'CSVF'       : 'TN',
    'UsingCodes' : 'Y',
    'VPD'        : 'Y',
    'VFD'        : 'N'
}

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/54.0.2840.90 '
                 'Safari/537.36'
}

response = requests.get(url_endpoint, params=payload, headers=headers)


# Check if the response was successful, it should return '200'
print(response.status_code)

with open('m1_comp_raw.csv', 'w', encoding='utf-8') as f:
    f.write(response.text)


