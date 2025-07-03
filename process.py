import pandas as pd

df = pd.read_csv('m1_comp_raw.csv')

df = df.rename(columns={
    'DATE': 'date',
    'LPMB5S9': 'household_non_interest',
    'LPMB6S2': 'ofc_non_interest',
    'LPMB6S3': 'nfc_non_interest',
    'LPMB75C': 'ofc_cash',
    'LPMB76C': 'nfc_cash',
    'LPMVYWO': 'household_cash',
    'LPMZ3TT': 'household_interest',
    'LPMZ3TV': 'ofc_interest',
    'LPMZ3TX': 'nfc_interest',
    'LPMVWLQ': 'general_gov',
    'LPMVWLW': 'public_corp',
    'RPMB3OM': 'non_residents'
})


df['date'] = pd.to_datetime(df['date'], format='%d %b %Y').dt.strftime('%Y-%m-%d')

df['m1'] = df.iloc[:, 1:].sum(axis=1)


df['cash_percent'] = (((df['household_cash'] + df['nfc_cash'] + df['ofc_cash']) / df['m1']) * 100).round(2)
df['household_percent'] = (((df['household_cash'] + df['household_interest'] + df['household_non_interest']) / df['m1']) * 100).round(2)
df['nfc_percent'] = (((df['nfc_cash'] + df['nfc_interest'] + df['nfc_non_interest']) / df['m1']) * 100).round(2)
df['ofc_percent'] = (((df['ofc_cash'] + df['ofc_interest'] + df['ofc_non_interest']) / df['m1']) * 100).round(2)
df['non_residents_percent'] = ((df['non_residents'] / df['m1']) * 100).round(2)
df['government_percent'] = (((df['general_gov'] + df['public_corp'])  / df['m1']) * 100).round(2)


df.to_csv('m1_comp_processed.csv', index=False)