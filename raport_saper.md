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
+ Wyjątki
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
za ujawnianie kolejnych pól aż do takiego które sąsiaduje z minami.
    + Problem: jak odpowiednio sprawdzać czy następne sprawdzenie nie wyjdzie za mape
        + Rozwiązanie: Odpowiednie rozrysowanie i przemyślenie architektury
    + Problem: funkcja ujawniająca pola blokująca się już na ostatnim niegraniczącym z żadną miną polu ( nie pokazuje tych z numerkiem)
         + Rozwiązanie: Tymczasowo rozwiązane przez isFlood
    + Problem: funkcja mimo dojscia do granicy ujawnia też w dziwny sposób pola na ukos
        + Rozwiązanie: ?