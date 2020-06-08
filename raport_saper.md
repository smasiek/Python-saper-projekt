#Raport z projektu
##Saper - Miłosz Momot
####Założenia i realizacja projektu:
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
+ Exception handling
+ Dodanie timer'a do okna gry
    + Problem: Odpowiednie resetowanie i ustawianie timera podczas pierwszego kliknięcia oflagowania
        + Rozwiązanie: Dodanie pola _started symbolizującego rozpoczęcie/zakonczenie gry i timera
+ Dodanie kota który jest odpowiednikiem słoneczka z oryginalnej wersji sapera
+ Obsługa większych ikon przy wybraniu planszy mniejszej niz 8
+ Dodanie nazwy okna i ikon
+ Dodanie komentarzy i docstringów
+ Stworzenie requirements.txt
+ Poprawienie nazewnictwa: camelCase -> snake_case
+ Podlinkowanie kluczowych elementów programu do raportu:
    + Lambda:
        + [#1](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/saper.py#L59-L62)
        + [#2](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/saper.py#L90)
        + [#3](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/saper.py#L108)
        + [#4](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L117-L119)
        + [#5](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L368-L372)

    + List comprehensions:
        + [#1](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L129-L153)
        + [#2](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/logic/fields.py#L45-L46)
        + [#3](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/logic/fields.py#L47-L48)
    
    + Klasy:
        + [#1 Error](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L13-L14)
            + [Dziedziczenie #1](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L17-L24)
            + [Dziedziczenie #2](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L27-L31)
            + [Dziedziczenie #3](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L34-L41)
            + [Dziedziczenie #4](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L44-L51)
        + [#2 Timer](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L54-L91)
        + [#3 Cat](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L54-L91)
        + [#4 GameWindow](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L113-L330)
        + [#5 Square](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/squares.py#L4-L70)
        + [#6 Field](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/logic/fields.py#L5-L39)
    + Wyjątki:
        + [#1](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L17-L24)
            + [raise](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L468)
        + [#2](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L27-L31)
            + [raise](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L428)
        + [#3](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L34-L41)
            + [raise](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L443)
        + [#4](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L44-L51)
            + [raise](https://github.com/smasiek/Python-saper-projekt/blob/1b33afe7975836be620a342831e791de49cd4a22/graphics/windows.py#L599)
     + Moduły:
        + Logika:
            + [Fields](https://github.com/smasiek/Python-saper-projekt/blob/master/logic/fields.py)
        + Grafika:
            + [Windows](https://github.com/smasiek/Python-saper-projekt/blob/master/graphics/windows.py)
            + [Squares](https://github.com/smasiek/Python-saper-projekt/blob/master/graphics/squares.py)
            + [Icons](https://github.com/smasiek/Python-saper-projekt/blob/master/graphics/icons.py)
        + Main:
            + [Saper](https://github.com/smasiek/Python-saper-projekt/blob/master/saper.py)
        
---
Koniec
---

