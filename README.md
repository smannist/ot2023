# Tetris

Legendaarinen Tetris pygame kirjastolla

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/smannist/ot2023/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/smannist/ot2023/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/smannist/ot2023/blob/master/dokumentaatio/changelog.md)

## Nykytila

Tällä hetkellä pelissä on peruspalikat, palikat putoavat ja niitä voi käännellä. Muu perustoiminnalisuus rakennetaan ensiviikkoon mennessä.

## Asennus

1. Asenna riipuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Muita komentoja

1. Testaus

```bash
poetry run invoke test
```

2. Testikattavuus

```bash
poetry run invoke coverage-report
```

3. Testikattavuusraportin aukaiseminen selaimeen (Linux)

```bash
poetry run invoke open-report
```

4. Koodin laatutarkistus

```bash
poetry run invoke lint
```
