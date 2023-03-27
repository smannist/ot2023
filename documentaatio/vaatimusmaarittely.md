# Vaatimusmäärittely

## Sovelluksen tarkoitus

Tarkoituksena on toteutaa legendaarinen Tetris käyttäen apuna Pythonin Pygame -kirjastoa. Peli tulee sisältämään ainakin tavallisen Tetriksestä tutun pelitilan jossa palikoita tiputellaan yksitellen tasolle sekä mahdollisesti jotain erikoisempia ominaisuuksia. Tietokantaa (joko postgresql tai sqlite) tullaan hyödyntämään pistetaulukon tallentamiseen ja hakemiseen.

## Käyttäjät

Koska sovelluksessa ei ole moninpelitilaa käyttäjiä tulee olemaan vain yksi.

## Käyttöliittymä

Graafinen käyttöliittymä Pygame -kirjastolla.

## Perusversion tarjoama toiminnallisuus

Tetriksestä tuttu pelitila:

- Yksinpeli
- Erikokoisia ja muotoisia palikoita
- Tarkoituksena muodostaa suora pelin alatasolle
  - Palikat hajoavat suoran muodostuessa
    - Käyttäjä ansaitsee pisteitä
- Peli nopeutuu ajan kuluessa
  - Palikat tippuvat nopeammin

Muita ominaisuuksia:

- Käyttäjä pystyy tallentamaan pisteensä
  - Pisteiden tulee olla tarpeeksi korkeat
    - Esimerkiksi TOP 10

## Jatkokehitysideoita

Kun perusversiossa määritellyt toiminnallisuudet on saatu kasaan sovellusta voidaan täydentää mm. alla olevilla ominaisuuksilla:

- Satunnaisesti tapahtuvia asioita peliin esimerkiksi
  - Sumu joka vaikeuttaa näkemistä
  - Isommat bonuspalikat
  - Palikat jotka räjäyttävät koko rivin / tietyn alueen
- Vaikeusasteet
- Alkuikkuna jossa on mahdollista luoda omia palikoita

Muita ominaisuuksia lisäillään niiden sattuessa mieleen.
