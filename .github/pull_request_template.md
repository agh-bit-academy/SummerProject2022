# PR Template
## Skrót zmian
### Lista dodanych plików + uzasadnienie
-
-

### Lista dodanych testów + opis testów
-
-

### Lista usuniętych plików + uzasadnienie
-
-

### Lista usuniętych testów + uzasadnienie
-
-

### Lista zmodyfikowanych plików + uzasadnienie
-
-

### Lista zmodyfikowanych testów + uzasadnienie
-
-

## Lista Wymagań
### Ogólna lista wymagań
- [ ] Pycodestyle
- [ ] Pliki odnoszą się do odpowiedniego katalogu
- [ ] Brak "Magic Number"
- [ ] Komentarz zawierający listę autorów dla niepustych plików

### Lista wymagań dla testów
- [ ] Uruchomienie przez *core.py*
- [ ] Uruchomienie przez pytest *nazwa_pliku.py*
- [ ] Dodanie plików DATA.txt i \_\_init\_\_.py

### Lista wymagań dla plików źródłowych
- [ ] Napisanie testów dla funkcji oraz metod w klasach
- [ ] Oznaczenie otestowanych funkcji oraz metod w klasach
- [ ] Samodokumentujące się zmienne oraz funkcje
- [ ] Import *nazwa* -> from *nazwa* import *nazwa1*, *nazwa2*, ...
- [ ] Import w kolejności alfabetycznej bibliotek  

### Nazewnictwo 
- [ ] Makra -> PIERWSZE_DRUGIE_TRZECIE
- [ ] Zmienne -> pierwszeDrugieTrzecie
- [ ] Funkcje -> pierwszeDrugieTrzecie
- [ ] Klasy -> PierwszeDrugieTrzecie
- [ ] Pliki -> pierwsze_drugie_trzecie
- [ ] Katalogi -> Pierwsze_Drugie_Trzecie

### pytest
- [ ] Kolejność markerów: order -> dependency -> parametrize
- [ ] Jeżeli możliwe, markery *order* i *dependency* przy klasie
- [ ] Marker *parametrize* przy funkcji
- [ ] Pliki -> test_pierwszeDrugieTrzecie
- [ ] Funkcje -> test_PierwszeDrugieTrzecie
- [ ] Klasy -> TestPierwszeDrugieTrzecie
- [ ] Listy testów -> pierwszeDrugieTrzecieTests
- [ ] Dependency_name -> test\[*nazwa_pliku*\]
- [ ] Nazwa funkcji zawiera analogiczny człon jak testy w markerze parametrize
