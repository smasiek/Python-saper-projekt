#\#TODO
1. Raport ma być treściwy i w miarę krótki. Ma zawierać założenia projektowe
kodu, ogólny opis kodu, co udało się zrobić, z czym były problemy, dodane
elementy specjalne, zauważone problemy z testami.

2. Na końcu raportu muszą się znaleźć opisane linki do istotnych fragmentów
kodu (w źródłach na GitHub) który obrazuje wymagane w projekcie
konstrukcje takie jak:
+ Lambda-wyrażenia
+ List comprehensions
+ Klasy
+ Wyjątki - rzucany przy złych wymiarach
+ Moduły

#Raport z projektu
##Saper - Miłosz Momot
####Założenia projektu:
+ Utworzenie podstawy Sapera - stworzenie tablicy dwu wymiarowej zawierającej
informacje o lokalizacji bomb na planszy
+ Zaprojektowanie systemu badającego ilość bomb w pobliżu każdego z pól
+ Zaimplementowanie pygame
+ Stworzenie okna
+ Zaprojektowanie grafik w Photoshopie
+ Załadowanie grafik do programu
+ Wyświetlanie kwadratów w odpowiednich wymiarach
+ Dodanie funkcji wywoływanej kliknięciem
+ Interaktywne pola
+ Pola pokazują odpowiednie grafiki w zalezności od rodzaju kliknięcia
+ Pola które nie mają wokół siebie min włączają funkcje flood, która odpowiada
za ujawnianie kolejnych pól aż do takiego które sąsiaduje z minami
    + Problem: jak odpowiednio sprawdzać czy następne sprawdzenie nie wyjdzie za mape
        + Rozwiązanie: Odpowiednie rozrysowanie i przemyślenie architektury
    + Problem: funkcja ujawniająca pola blokująca się już na ostatnim niegraniczącym z żadną miną polu ( nie pokazuje tych z numerkiem)
         + Rozwiązanie: Tymczasowo rozwiązane przez isFlood
    + Problem: funkcja mimo dojscia do granicy ujawnia też w dziwny sposób pola na ukos
        + Rozwiązanie: ?
+ Zmiana podejścia do funkcji flood i ujawnienia poprzez klikniecie LPM(teraz: reveal).
Funkcja reveal jest w stanie wywołać funkcje flood, która aktualnie zajmuje się jedynie ponownym wywołaniem funkcji reveal
na sąsiednich polach, które nie sa bombą
+ Napotkałem problem z minami które powstawały w tym samym miejscu
     + Rozwiązanie: Stworzenie listy przechowującej wszystkie możliwe koordynaty, wybór i usunięcie wybranych koordynatow z listy.
     W kolejnej iteracji niemożliwe będzie stworzenie bomby na miejscu innej bomby.
+ Dodanie funkcji ujawniającej wszystkie pola
+ Obsługa przegranej
+ Obsługa wygranej
+ Dodanie obsługi kodu "xyzzy" do gry
+ Wygranie przez oflagowanie tylko i wyłącznie bomb
+ Okno wybierania wymiarów pojawiające sie przed rozpoczeciem gry
    + Weryfikacja poprawności danych 2<=(n,m)<=15
    + Wszystkie pola musza być uzupelnione (tymczasowa walidacja danych:
    nie da się wyjść z okna dopóki nie wpisze się poprawnych danych.
    Po wyjsciu z okna pojawia sie okno gry na podstawie danych)
+ Duży problem z koordynatami
    + Wczesniejsze testy robiłem na kwadratowym oknie, 
    przy próbie na prostokątnym wszystko sie posypało a program
    był juz na tyle rozwinięty, że ciężko było mi znaleźć rozwiązanie.
    **Finalnie działa**.
+ Podział programu na moduły zgodnie z założeniami projektu: moduł związany z ***logiką*** i moduł związany z ***interfacem***
+ Dodanie do okna konfiguracji:
    + Przycisku przejscia do gry
    + Obsługi tabulatora do poruszania się między inputami
        + Poruszanie się jest przemyślane tzn. jeśli n lub m juz jest podane to próba tabulacji nie zadziała
        + Jeśli n i m jest wpisane to pole bomby automatycznie staje sie aktywne - przyspiesza wpisywanie danych 
        i jest intuicyjne
        + Jeśli nie zatwierdzimy wpisanego tekstu co zwiększa estetyke i przypomina o zatwierdzaniu danych
    + Blokady inputu bomby dopóki nie są podane wymiary:
        + Zmiast łapać wyjątki w których ktoś wpisałby ilosc bomb przed podaniem n i m to blokuje taką możliwość.
        Myślę, że to lepsza praktyka 