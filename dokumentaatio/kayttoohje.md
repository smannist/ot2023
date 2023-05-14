# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/smannist/ot2023/releases/tag/viikko7) lähdekoodi valitsemalla Assets-osion alta Source code.

Vaihtoehtoisesti voit halutessasi kloonata projektin suoraan tietokoneellesi komenolla:

```
git clone https://github.com/smannist/ot2023
```

## Ohjelman käynnistäminen

Asenna ensiksi vaadittavat riippuvuudet komennolla:

```
poetry install
```

Tämän jälkeen ohjelma on heti käyttövalmis ja sen voi suorittaa komennolla:

```
poetry run invoke start
```

## Pelaaminen

Palikan ohjaukseen on neljä peruskomentoa ja ne tapahtuvat käyttämällä nuolinäppäimiä:

← käänny vasemmalle

→ käänny oikealle

↓ pudota palikkaa alemmas

↑ rotaatio

Peli nopeutuu ajan kuluessa ja peli päättyy kun "palikkatorni" saavuttaa ruudukon katon. Jos pisteesi ovat tarpeeksi korkeat ne tallennetaan.
