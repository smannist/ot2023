# Tetris

Legendaarinen Tetris pygame kirjastolla

<img src="https://github.com/smannist/ot2023/blob/master/dokumentaatio/images/tetris.png" width="400" height="400">

Song: Caffeine Crazed Coin-Op Kids by Eric Matyas soundimage.org (https://opengameart.org/content/caffeine-crazed-coin-op-kids-looping)

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/smannist/ot2023/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/smannist/ot2023/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuurikuvaus](https://github.com/smannist/ot2023/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/smannist/ot2023/blob/master/dokumentaatio/changelog.md)
- [Käyttöohje](https://github.com/smannist/ot2023/blob/master/dokumentaatio/kayttoohje.md)

## Release

- [Release 1](https://github.com/smannist/ot2023/releases/tag/viikko5)
- [Release 2](https://github.com/smannist/ot2023/releases/tag/viikko6)

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
