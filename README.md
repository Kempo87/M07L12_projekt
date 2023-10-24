
# Opis programu:

Ten program to prosty budżet domowy, który umożliwia użytkownikowi zarządzanie wydatkami. Oto główne cechy i funkcje programu:

Definicja klasy Expense: Klasa reprezentuje pojedynczy wydatek. Wydatek ma identyfikator, kwotę i opis. Wydatki nie mogą mieć wartości ujemnych ani równej zero.

Funkcje load_or_init_expenses() i save_expenses(): Są odpowiedzialne za wczytywanie i zapisywanie listy wydatków do pliku 'budget.db'.

Funkcja find_new_id(): Służy do znalezienia nowego, unikalnego identyfikatora dla wydatku, aby uniknąć konfliktów.

Funkcja compute_total(): Oblicza łączny koszt wszystkich wydatków w bazie danych.

Funkcja print_report(): Wyświetla raport z wydatkami, prezentując identyfikator, kwotę, informację, czy wydatek jest duży (jeśli przekracza określony próg) oraz opis.

Grupa poleceń Click cli(): Definiuje grupę poleceń dostępnych w programie.

Polece report(): Wyświetla raport z wydatkami i łączny koszt.

Polece add(amount, desc): Pozwala użytkownikowi dodać nowy wydatek, podając kwotę i opis.

Polece import_csv(csv_file): Importuje wydatki z pliku CSV i dodaje je do bazy danych.

Polece export_python(): Wyświetla wydatki w formie listy Python.

## Ten program umożliwia użytkownikowi śledzenie i zarządzanie wydatkami, generowanie raportów oraz importowanie danych z pliku CSV. Jest przykładem prostego budżetu domowego napisanego w języku Python.
