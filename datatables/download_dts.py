import requests   
import os
from datetime import datetime
url_endpoint = 'http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?csv.x=yes'

today = datetime.now().strftime('%d/%b/%Y')
print(today)

datatables = {'A1_1_1' : 'LPMAVAA,LPMBL22',
              'A2_2_1' : 'LPMVRJX,LPMZ597,LPMZ598,LPMVQKT,LPMVQXV,LPMVRJV,LPMVWDO,LPMAUYM,LPMVWXL',
              'A2_3' : 'LPMVWXL,LPMVWYC,LPMVWYD,LPMVWYE,LPMVWYF,LPMVWYG,LPMVWYH,LPMVWYI,LPMVWYJ',
              'private_m1' : 'RPMB3NM','LPMB5S9','LPMB6S2','LPMB6S3','LPMZ3TT','LPMZ3TV','LPMZ3TX'}
            

for dt in datatables:
    payload = {
        'Datefrom'   : '01/Jan/2010',
        'Dateto'     : today,
        'SeriesCodes': datatables[dt],
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

    path = os.path.join('datatables',f'{dt}.csv')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(response.text)


