# Proces testowy w CI/CD


Proces testowy utrzymany jest w duchu Continous Testing - zautomatyzwowania wykonywania testów w pipelinie w CI/CD.

**Testy są automatycznie odpalane po każdym pushu do repozytorium w momencie gdy trafiają na Travis CI/Gitlab.**

W każdym momencie można je również odpalać z linii komend.

Linter tool
-----------
Narzędzie: flake8
Analiza kodu pod względem poprawności składni i zgodności z PEP8, pozwala tworzyć czytelniejszy kod. Oszczedność czasu przy debugowaniu kodu (wyłapywanie "w locie" literówek, formatowania, składni, stylu).

    # uruchomienie
    $ make lint

Smoke Test
----------
Sprawdzenie krytycznej funkcjonalności aplikacji. W przypadku tej aplikacji _smoke test_ wykonuje prostą komendę _'curl'_

    # uruchomienie
    $ make test_smoke

Testy jednostkowe
-----------------
Weryfikacja działania pojedyńczych modułów programu. Pozwalają na szybkie wychwycenie i zlokalizowanie zaistnienia defektu w kodzie.

    # uruchomienie
    $ make test


Metryki pokrycia i złożoności kodu
----------------------------------
Metryki pozwają na ilościową analizę jakości kodu. Ukazują które moduły programu wymagają jeszcze pokrycia testami czy refraktoryzacji.

- testy pokrycia kodu (coverage tests):

      # uruchomienie
      $ make test_cov
      $ make test_xunit

  Używane narzędzie - Coveralls - dostarcza statystyk i grafik dotyczących pokrycia kody testami.

- testy złożoności (complexity tests):

      # uruchomienie
      $ make test_complexity



Testy akceptacyjne/ testy UI
----------------------------
Testy automatyczne: biblioteka Selenium i Robot Framework.
Weryfikacja poprawności działania aplikacji zgodnie ze specyfikacją i opracowanymi przypadkami testowymi.
Dostarcza raportów i logów z przeprowadzonych testów a także screenshotów z ew. awarii.

      # uruchamianie
      $ make robot_test


testy obciążeniowe / performance test
-------------------------------------
Sprawdzają działnie/dostępność aplikacji przy symulowanym ruchu użytkowników.

     # instalacja siege
     $ sudo apt install siege

     # uruchomienie
     $ make test_siege


Monitoring
----------
Statuscake - administrator dostaje informację e-mail w momencie braku dostępności aplikacji i powrotu do działania z czasem trwania awarii.


Ponadto w kodzie aplikacji zaimplemetnowana jest funkcja, która wysyła do administratora e-maila z logiem awarii, gdy strona odpowie na zapytanie użytkownika kodem HTTP - '500'.
