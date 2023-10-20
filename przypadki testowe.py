# Happy Path :

# Test dodawania wydatku:

# Sprawdzenie, czy program poprawnie dodaje wydatek do listy.
# Wykorzystanie funkcji add() do dodania wydatku o ustalonej kwocie i opisie.
# Asercja, że wydatek został dodany poprawnie.


# Test generowania raportu:

# Sprawdzenie, czy program generuje raport na podstawie dodanych wydatków.
# Wykorzystanie funkcji report() do wygenerowania raportu.
# Asercja, że raport został wygenerowany poprawnie.


# Extended Happy Path (skomplikowane przypadki, szczególnie integracyjne):
# Test importu danych z pliku CSV:

# Sprawdzenie, czy program poprawnie importuje dane z pliku CSV.
# Stworzenie tymczasowego pliku CSV z danymi wydatków.
# Użycie funkcji import_csv() do zaimportowania danych.
# Asercja, że dane zostały zaimportowane poprawnie.

# Test eksportu danych do pliku Python:

# Sprawdzenie, czy program poprawnie eksportuje dane do pliku Python.
# Dodanie kilku przykładowych wydatków do listy.
# Użycie funkcji export_python() do eksportu danych.
# Asercja, że dane zostały zapisane w formie Pythonowego listy.
# 
# 
# Edge Cases :
# 
# Test wczytywania uszkodzonego pliku CSV:

# Sprawdzenie, czy program obsługuje sytuację, gdy plik CSV jest uszkodzony.
# Stworzenie tymczasowego pliku CSV, który zawiera nieprawidłowe dane.
# Użycie funkcji import_csv() do próby zaimportowania tych danych.
# Asercja, że program obsługuje błędy i nie zawiesza się.


# Test zarządzania ID wydatków: 

# Sprawdzenie, czy program poprawnie zarządza identyfikatorami wydatków.
# Dodanie kilku wydatków, usunięcie niektórych z nich.
# Użycie funkcji find_new_id() do znalezienia nowego dostępnego ID.
# Asercja, że program przydziela ID w sposób poprawny.