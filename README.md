# Testerka na WDI

## Organizacja plików i sprawdzanie rozwiązań
W katalogu **WDI** należy znaleźć interesujący nas zestaw oraz zadanie. Następnie w tym katalogu umieścić kod w pliku o nazwie **prog.py**
i uruchomić plik core.py. Wynik sprawdzenia znajdzie się w pliku DATA.txt w katalogu z zadaniem.

Przykładowo aby sprawdzić zadanie 7 z zestawu 2 należy w pliku **./WDI/Set_2/Task_7/prog.py** umieścić kod, a następnie w pliku po uruchomieniu
**core.py** w pliku **./WDI/Set_2/Task_7/DATA.txt** pojawi się aktualna punktacja za zadanie.

Sprawdzić można jednocześnie wiele zadań. Jeżeli plik **prog.py** jest nowszy niż **DATA.txt**, to **core.py** automatycznie sprawdzi wszystkie 
zaktualizowane wersje dodanych rozwiązań zadań.

## Dodawanie własnych testów
Aby dodać testy do zadania należy utworzyć plik rozpoznawalny przez framework **pytest** w katalogu z zadaniem, a następnie
utowrzyć odpowiednie klasy testów. Program **core.py** automatycznie znajdzie liczbę plików z testami i następnie uruchomi
każdy z nich uwzględniając limity czasowe załączone w pliku **DATA.txt**.

### DATA.txt
Plik zawierający krótką informację o testach oraz wyniku sprawdzenia:

### TEST_NUMBER:
W następnej linii znajduje się liczba plików (możliwe że zostanie zamienione na liczbę klas w jednym teście), które zawierają testy.

### MAX_TIME:
W i-tej linii po nagłówku **MAX_TIME** znajduje się maksymalny czas wykonywania i-tego zestawu testów.

### POINT_PER_GROUP:
W i-tej linii po nagłówku **POINT_PER_GROUP** znajduje się liczba przynawanych punktów za poprawne zwrócenie wyniku we wszystkich
w testach w i-tej grupie.

### TEST_RESULT:
W i-tej linii po nagłówku **TEST_RESULT** krótka informacja o wyniku sprawdzenia i-tej grupy testów.

### SCORE:
W następnej linii znajduje się suma uzyskanych punktów za dane zadanie.
