# Hra Kámen, Nůžky, Papír

Jednoduchá implementace klasické hry "Kámen, Nůžky, Papír" v příkazové řádce, napsaná v Pythonu. Tento program umožňuje hrát proti počítači a nabízí zábavné a interaktivní prostředí. Program zaznamenává skóre a nabízí možnost hrát více kol.

## Funkce
- **Interaktivní hraní**: Uživatel si vybere Kámen, Nůžky nebo Papír a hraje proti počítači.
- **Zaznamenávání skóre**: Program udržuje přehled o skóre hráče a počítače.
- **Možnost opakování hry**: Po každém kole se můžete rozhodnout, zda chcete pokračovat nebo hru ukončit.

## Jak hra funguje
1. Program vás vyzve, abyste si vybrali jednu ze tří možností:
   - **[R]** pro Kámen
   - **[P]** pro Papír
   - **[S]** pro Nůžky
2. Po vašem výběru počítač náhodně zvolí také jednu z možností.
3. Program porovná volby a určí vítěze:
   - Kámen poráží Nůžky
   - Nůžky poráží Papír
   - Papír poráží Kámen
4. Program zobrazí průběžné skóre a vyzve vás, zda chcete hrát další kolo.

## Systém skóre
- Po každém kole se skóre aktualizuje a zobrazí:
  - **Vy**: skóre hráče
  - **Počítač**: skóre počítače
- Program se ptá, zda chcete pokračovat:
  - Pokud zadáte "Ano" nebo "Y", hra pokračuje.
  - Pokud zadáte "Ne", hra se ukončí a zobrazí finální skóre.

## Předpoklady
- Python 3.x

## Instalace
1. Ujistěte se, že máte nainstalovaný Python 3.x.
2. Naklonujte nebo stáhněte tento repozitář.
3. Ujistěte se, že máte nainstalované všechny potřebné knihovny (program využívá knihovny `random`, `os` a `re`, které jsou standardní součástí Pythonu).

## Jak spustit program
1. Otevřete terminál nebo příkazový řádek.
2. Přesuňte se do složky s tímto souborem.
3. Spusťte program příkazem:

   ```bash
   python main.py
