# System Analizy Danych dot. Gier Komputerowych


## O projekcie
Aplikacja webowa służąca do interaktywnej analizy zbioru danych dotyczących gier komputerowych (dataset VGChartz-2024). System umożliwia eksplorację trendów rynkowych, generowanie wykresów oraz porównywanie kluczowych parametrów gier, co wspomaga podejmowanie decyzji biznesowych w sektorze gamedev.

### Autorzy 
*   **Kacper Dusza** 
*   **Radosław Cebula**

---

## Stack Technologiczny

| Kategoria | Technologia |
| :--- | :--- |
| **Backend** | Python 3.x, Django 4.2.23 |
| **Frontend** | HTML5, CSS3 (Custom Design System), JavaScript |
| **Analiza Danych** | Pandas |
| **Wizualizacja** | Plotly.js |

---

## Architektura Systemu
System został zrealizowany w architekturze **bezstanowej klient-serwer** zgodnie ze wzorcem **MVT (Model-View-Template)**:

1.  **Model**: Plik-baza danych oparty na formacie CSV (`vgchartz-2024.csv`).
2.  **View**: Logika biznesowa wykorzystująca Pandas do agregacji i Plotly do generowania wizualizacji.
3.  **Template**: Dynamiczne szablony HTML osadzające interaktywne wykresy.

---

## Funkcjonalności
*   **Analiza sprzedaży wg platform**: Wizualizacja popularności konsol.
*   **Analiza gatunkowa**: Zestawienie sprzedaży w zależności od gatunku gry.
*   **Rankingi**: Top 30 gier według średniej oceny krytyków.
*   **Analiza niestandardowa**: Możliwość samodzielnego wyboru osi X i Y, limitu rekordów oraz typu wykresu (słupkowy/punktowy).
*   **Interaktywność**: Filtrowanie danych za pomocą klikalnej legendy, zoom oraz podgląd szczegółów po najechaniu kursorem (hover).

---

## Preprocessing Danych
Zbiór danych został poddany procesowi czyszczenia, co pozwoliło na zmniejszenie rozmiaru pliku o **16,3%** (z 734 KiB do 614,5 KiB). Operacje obejmowały:
*   Usunięcie wierszy z brakującymi ocenami (`critic_score`).
*   Usunięcie zbędnych kolumn (`img`, `last_update`).

---

## Instalacja i Uruchomienie

### Wymagania
*   System operacyjny: Linux/Windows/macOS
*   RAM: min. 4GB

### Instrukcja
1. **Klonowanie repozytorium:**
   ```bash
   git clone [https://github.com/M3T1X1/Video_games_analytic_system](https://github.com/M3T1X1/Video_games_analytic_system)
   cd Video_games_analytic_system