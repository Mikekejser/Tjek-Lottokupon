import requests
from bs4 import BeautifulSoup

# VÆLG LOTTOTYPE:
while True:
	lotto_type = input("Indtast nr. for lotto type:\n1) Onsdags lotto\n2) Lørdags lotto\n>> ")
	if lotto_type not in ['1', '2']:
		continue
	else:
		break

# TJEKKER LOTTOTYPE. HENTER DATA MED GET REQUEST. SÆTTER VARIABEL AntalTal. 
if lotto_type == '1':
	page = requests.get('https://vindertal.com/onsdags-lotto.aspx')
	antalTal = 6
elif lotto_type == '2':
	page = requests.get('https://vindertal.com/loerdags-lotto.aspx')
	antalTal = 7

# TJEKKER HTTP STATUS KODE. HVIS STATUS ER OK: LAVER SOUP OVER SIDENS INDHOLD.
# TILFØJER HVERT LOTTOTAL I RÆKKEN TIL LISTEN lotto_nums, 
if page.status_code == 200:
	lotto_nums = []
	soup = BeautifulSoup(page.content, 'html.parser')
	for i in range(antalTal):
		lotto_nums.append(soup.find(id="ContentPlaceHolderDefault_CphMain_AllNumbers_5_LvWinnerNumbers_LblNumber_"+str(i)).contents)
else:
	print(f'Kunne ikke hente vindertal. Prøv igen senere.\nStatus kode: {page.status_code}')
	quit()

# LISTEN lotto_nums ER EN LISTE AF LISTER MED HVERT LOTTONUMMER REPRÆSENTERET SOM EN STRENG.
# FØLGENDE LINJE UDJÆVNER LISTEN OG OMDANNER STRENGENE TIL HELTAL.
lotto_nums = [int(item) for sublist in lotto_nums for item in sublist]

# LISTE kupon OPRETTES. VARIABEL nr SÆTTES TIL VÆRDIEN 1. EN ORDBOG MED ORDENSTAL OPRETTES.
kupon = []
nr = 1
ordenstal = {
	1: 'første',
	2: 'andet',
	3: 'tredje',
	4: 'fjerde',
	5: 'femte',
	6: 'sjette',
	7: 'syvende'
}

# WHILE LOOP PROMPTER BRUGER FOR HVERT TAL. TAL INSÆTTES I LISTEN kupon.
while nr <= antalTal:
	try:
		kupon.append(int(input(f'Indtast {ordenstal[nr]} nummer på kupon: ')))
	except ValueError:
		print('Ikke et tal. Prøv igen...')
		continue
	nr += 1

# TJEKKER OM VINDERTAL MATCHER BRUGERS KUPON:
antalRigtige = 0
rigtige = []
for i in lotto_nums:
	if i in kupon:
		antalRigtige += 1
		rigtige.append(i)

if len(rigtige) == 0:
	print('Ingen rigtige.')
else:
	print(f'{antalRigtige} rigtige:')
	for i in rigtige:
print(i, " ", end="")
