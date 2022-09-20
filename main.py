import requests
import xmltodict


def get_new():
    url = "https://hazard.mf.gov.pl/api/Register"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
    data1 = data['Rejestr']
    filler = ('''{ type master; file "/var/named/db.hazard"; };''')
    for adress in data1['PozycjaRejestru']:
        with open('d:\python\hazard\list.txt', 'a') as file:
            file.write(
                f'''# LP: {adress['@Lp']} dodano: {adress['DataWpisu']}\nzone "{adress['AdresDomeny']}"  {filler}\n \n''')

    print("!!!ZAKTUALIZOWANO!!!")


url = "https://hazard.mf.gov.pl/api/Register/ModificationDate"
response = requests.get(url)
data = xmltodict.parse(response.content)
data_new = data['DataModyfikacji']['#text']
with open('d:\python\hazard\list.txt', 'r') as f:

    f.seek(25)
    data_old = f.read(19)
    if str(data_new) == str(data_old):
        print("BAZA AKTUALNA")
    else:
        with open('d:\python\hazard\list.txt', 'w') as file:
            file.write(
                f"# Ostatnia aktualizacja: {data_new} \n \n")
        get_new()
