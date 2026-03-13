# Django Bauhaus Database

Tento Django projekt slouží jako databáze výtvorů, studentů a učitelů umělecké školy Bauhaus. Cílem projektu je vytvořit databázi, která bude obsahovat designové, architektonické a řemeslné práce této německé umělecké školy. Databáze umožní evidenci jednotlivých děl a jejich autorů. Správa dat probíhá pomocí knihovny Django.

## Odborný článek

Tento projekt je webová aplikace vytvořená pomocí frameworku _Django_. Jejím účelem je vytvořit přehlednou _databázi_ děl spojených s uměleckou školou _Bauhaus_. Tato škola patřila mezi důležité směry moderního umění a ovlivnila oblasti jako _architektura_, _design_, _grafika_ a _řemeslo_. Aplikace slouží k ukládání informací o jednotlivých _dílech_, jejich autorech a jejich vztahu ke škole Bauhaus.

Základní položkou databáze je _dílo_. U každého díla se ukládají informace jako _název_, _rok vzniku_, _popis_ a _obrázek_. Každé dílo je spojeno s jeho _autorem_. Autorem může být _student_ nebo _učitel_, kteří na škole působili nebo studovali. Informace o autorech jsou uložené v části databáze označené jako _osoba_. Ta obsahuje například _jméno_ a krátkou _biografii_. Díky tomu je možné zobrazit nejen jednotlivá díla, ale také přehled tvorby konkrétního autora.

Aplikace pracuje s několika typy uživatelů. _Anonymní návštěvník_ může stránku volně procházet a zobrazovat si uložená díla i informace o jejich autorech. _Registrovaný uživatel_ má navíc možnost přidat k dílu vlastní _hodnocení_ nebo napsat _komentář_. Tím může vyjádřit svůj názor nebo doplnit další informace.

Speciální roli má _administrátor_. Ten spravuje obsah celé databáze pomocí administračního rozhraní, které poskytuje _Django_. Administrátor může přidávat nová _díla_, upravovat údaje o _autorech_ nebo odstraňovat nesprávná _data_. Díky tomu zůstává databáze aktuální a přehledná.

Projekt tak vytváří místo, kde je možné jednoduše vyhledávat informace o tvorbě školy _Bauhaus_, jejích _studentech_, _učitelích_ a jejich uměleckých _dílech_.

## Wireframe

<img width="1587" height="2245" alt="www webp comwireframe" src="https://github.com/user-attachments/assets/6e7a0ad4-9820-4532-90a1-32dc3e0ca9ab" />

![IMG_1020](https://github.com/user-attachments/assets/5856519b-4a88-4fc5-901f-89fef5d65e92)

## User flow

![IMG_1021](https://github.com/user-attachments/assets/3ab35ee6-287c-4830-b066-5f9d0ebd6c68)

## E-R Graph

![IMG_1034](https://github.com/user-attachments/assets/5cffe15c-3b18-4b33-a335-007354a3e87c)

## Funkce
- Evidence děl, studentů a učitelů Bauhausu
- Správa databáze pomocí Django adminu
- Přehledné uživatelské rozhraní pro zobrazování dat


https://github.com/user-attachments/assets/673f5096-9b46-414c-a77c-6eda8f002bbd


## Spuštění projektu

### Vytvoření a aktivace virtuálního prostředí
```bash
# Linux
python3 -m venv venv

# Windows
py -3 -m venv venv
```

Dále je třeba venv aktivovat:

```bash
# [Linux]
source ./venv/bin/activate

# Windows - Bash
source ./venv/Scripts/activate

# Windows - Power shell
...
```
```bash
./manage.py runserver
```
