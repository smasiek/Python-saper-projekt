# Projekt Języki Symboliczne:

## Saper - Miłosz Momot

## [Publiczne repozytorium](https://github.com/smasiek/Python-saper-projekt.git)

### Opis zadania
+ Główne okno zawiera dwa pola tekstowe do wprowadzania rozmiaru planszy (n na m
pól), planszę o wymiarach n na m pól (np. siatka przycisków), pole tekstowe na
wprowadzenie liczby min na planszy, liczbę oznaczonych pól, liczbę min na planszy,
oraz przycisk rozpoczęcia nowej gry.

+ Wprowadzenie mniejszego rozmiaru planszy niż 2x2 lub większego niż 15x15, liczby
min mniejszej niż 0 lub większej niż m*n powoduje wyświetlenie komunikatu o
błędzie. Nie można rozpocząć gry dopóki te parametry nie są poprawne. Walidacja
danych powinna wykorzystywać mechanizm wyjątków.

+ Na początku gry na losowych polach umieszczane jest tyle min ile wskazano w polu
tekstowym (każde możliwe rozłożenie min jest równie prawdopodobne).

+ Po kliknięciu lewym przyciskiem na pole:
    + Jeśli jest tam mina, wyświetlana jest wiadomość o przegranej i gra się kończy,
    + Jeśli w sąsiedztwie pola są miny, na przycisku wyświetlana jest ich liczba a pole dezaktywuje się,
    + W przeciwnym razie sąsiednie pola są sprawdzane tak jakby zostały kliknięte a pole dezaktywuje się.

+ Po kliknięciu prawym przyciskiem pole może zostać oznaczone “tu jest mina”, po ponownym kliknięciu oznaczenie zmienia się na “tu może być mina”, a po kolejnym kliknięciu oznaczenie znika.

+ Gra kończy się po kliknięciu wszystkich pól bez min, lub oznaczeniu “tu jest mina” wszystkich pól z minami (i żadnych innych).

+ Po naciśnięciu kolejno klawiszy x, y, z, z, y, pola pod którymi są miny stają się ciemniejsze

+ Do tworzenia okien i obsługi eventów zostanie użyta biblioteka pygame

+ Początkowo stworzona zostanie część back-endowa odpowiadająca za reprezentacje min i planszy

+ Następnie powstanie podstawowa reprezentacja graficzna Sapera,
 użyte zostaną do niej ikony, które postaram się stworzyć w photoshopie:

  Odpowiednio reprezentować będą:
    + Minę
    + Flagę
    + Pytajnik
    + Pole domyślne
    + Przyciemnione pole domyślne pokazujace się po użyciu kodu

+ Po stworzeniu interface'u graficznego dodane zostaną funkcje odpowiadające za poprawne działanie Sapera:
    + funkcje wywoływane kliknięciami
        + odkrycie pola po wcześniejszym sprawdzeniu czy jest aktywne/flagowane
        + oflagowanie
        + podwójne oflagowanie
    - [x] weryfikacja czy kliknieta została mina bądź wyświetlenie odpowiedniej cyfry 
    - [x] uzupełnianie automatyczne pól bez min w pobliżu
    - [x] sprawdzenie wygranej 
    - [x] funkcja koncząca gre - ujawnienie wszystkich pól i odpowiedni komiunikat zależnie od wygranej/przegranej
    - [x] obsługa kodu xyzzy
    - [x] mozliwosc modyfikacji rozmiaru planszy danymi z klawiatury
    - [x] ... pomysły, które przyjdą mi do głowy w trakcie pisania programu
    
### Testy

1. Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (1 na 1; 1), (5 na 1; 2), (4 na
1; 2), (20 na 500; 12), (5 na 6; -4), (3 na 3; 10), (1 na 10; 5) - oczekiwane komunikaty
o błędzie. Wprowadzenie rozmiarów planszy 8 na 8 i liczby min równej 12 na
potrzeby kolejnych testów.
2. Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola,
3. Kliknięcie pola, wyświetla się mina, gra się kończy,
4. Kliknięcie pola, brak min w sąsiedztwie - oczekiwane automatyczne
sprawdzenie sąsiadów aż do wyznaczenia obszaru wyznaczonego przez pola
sąsiadujące z minami lub krawędzie planszy,
5. Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnąć o 1,
6. Oznaczenie innego pola jako “tu może być mina”,
7. Oznaczenie pola, odznaczenie go, ponowne oznaczenie i ponowne odznaczenie - licznik oznaczonych powinien się odpowiednio aktualizować,
8. Wygranie gry przez kliknięcie wszystkich pól bez min,
9. Wygranie gry przez oznaczenie wszystkich pól z minami (można skorzystać z
kodu xyzzy),
10. Próba oznaczenia sprawdzonego pola - oczekiwane niepowodzenie,
11. Sprawdzenie kilku pól bez min, oznaczenie pól “tu jest mina”, rozpoczęcie nowej gry -
licznik min powinien się zaktualizować, a pola zresetować.
12. Wpisanie kodu xyzzy, zresetowanie gry - wszystkie pola powinny odzyskać
standardowy kolor.

