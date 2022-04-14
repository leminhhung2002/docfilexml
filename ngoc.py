from bs4 import BeautifulSoup
with open('hung.xml', 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'xml')
ID=soup.find_all(attrs={"id"})
NAME = soup.find_all('name')
print(NAME)
AGE = soup.find_all("age")
CREATEAT = soup.find_all(attrs={"createAt"})
print('-'.center(35, '-'))
print('|'+"ID"+'|' + 'Name'.center(15) + '|' + ' Age ' + '|' + 'CREATEAT'.center(11) + '|')

for i in len(NAME):
    print('-'.center(35, '-'))
    print(ID[i])
    print(NAME[i])
    print(AGE[i])
    print(CREATEAT[i])
    print(
        f'|{ID[i].text.center(5)}|{NAME[i].text.center(15)}|{AGE[i].text.center(5)}|{CREATEAT[i].text.center(11)}|')
print('-'.center(35, '-'))
