#Projekt Języki Symboliczne:
#Deadline 27 maja
##Saper - Miłosz Momot
###Opis zadania
+ Główne okno zawiera dwa pola tekstowe do wprowadzania rozmiaru planszy (n na m
pól), planszę o wymiarach n na m pól (np. siatka przycisków), pole tekstowe na
wprowadzenie liczby min na planszy, liczbę oznaczonych pól, liczbę min na planszy,
oraz przycisk rozpoczęcia nowej gry.

_W trakcie dodawania funkcji zmieniać opis zadania i linkować w raporcie_

_Tymczasowo umieszczone w opisie zadania pełnią rolę informacyjną dla mnie bym wiedział co robić_

[Poradnik permanent linki](https://help.github.com/en/github/managing-your-work-on-github/creating-a-permanent-link-to-a-code-snippet)
+ Wprowadzenie mniejszego rozmiaru planszy niż 2x2 lub większego niż 15x15, liczby
min mniejszej niż 0 lub większej niż m*n powoduje wyświetlenie komunikatu o
błędzie. Nie można rozpocząć gry dopóki te parametry nie są poprawne. Walidacja
danych powinna wykorzystywać mechanizm wyjątków.
+ Na początku gry na losowych polach umieszczane jest tyle min ile wskazano w polu
tekstowym (każde możliwe rozłożenie min jest równie prawdopodobne).
+ Po kliknięciu lewym przyciskiem na pole:
+ Jeśli jest tam mina, wyświetlana jest wiadomość o przegranej i gra się
kończy,
+ Jeśli w sąsiedztwie pola są miny, na przycisku wyświetlana jest ich liczba a
pole dezaktywuje się,
+ W przeciwnym razie sąsiednie pola są sprawdzane tak jakby zostały kliknięte
a pole dezaktywuje się.
+ Po kliknięciu prawym przyciskiem pole może zostać oznaczone “tu jest mina”, po
ponownym kliknięciu oznaczenie zmienia się na “tu może być mina”, a po kolejnym
kliknięciu oznaczenie znika.
+ Gra kończy się po kliknięciu wszystkich pól bez min, lub oznaczeniu “tu jest mina”
wszystkich pól z minami (i żadnych innych).
+ Po naciśnięciu kolejno klawiszy x, y, z, z, y, pola pod którymi są miny stają się
ciemniejsze

#####Nie zapomnij!

+ _Prowadzić sprawozdanie z testów, odpowiednio komentując i linkując_
