# Testausdokumentti

Ohjelman testaus on suoritettu yksikkö- ja integraatiotestauksilla Pythonin unittest kirjastolla. Pelin pelaaminen on testattu manuaalisesti.

## Yksikkötestaus- ja integraatiotestaus

### Sovelluslogiikka

Luokkia GameGrid, GameLoop, Block ja HighscoreService on testattu niitä vastaavilla testiluokilla: TestGameGrid, TestGameLoop, TestBlock ja TestHighscoreService. Luokat jotka sisältävät riippuuksia
on testattu injektoimalla riippuvuudet. Joissan tapauksissa kuten esim. GameLoopin kohdalla on myös käytetty Mock -olioita, vaikka tämä ei varsinaisesti pakollista olisi ollutkaan. HighscoreRepositoriota testataan erillisen testitietokannan "test-database.sqlite" avulla.

### Repositorio-luokat

Tällä hetkellä repository-luokkaa HighscoreRepository testataan pelkästään HighscoreService luokan testin luokan TestHighscoreService kautta.

### Testikattavuus

Sovelluksen testauksen haaraumakattavuus on 70%. Testien ulkopuolelle jätettiin luokat: config, start_game, initialize_database ja database_connection.

![Testikattavuusraportti](https://github.com/smannist/ot2023/blob/master/dokumentaatio/images/coverage_rep.png)

### Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on asennettu ja testattu käyttöohjeiden mukaisesti Linux ympäristössä. Tietokannan osalta ei vaadita erillisiä testaustiedostoja, vaan sovellus luo testitietokannan testien suorituksen aikana.

### Toiminnallisuudet

Kaikki määrittelydokumentin ja käyttöohjeen ilmoittamat toiminnallisuudet on suoritettu ongelmitta. Sovellus on rakennettu niin, että tietoa ei voi "vuotaa" esimerkiksi pelin matriisin ruudukon
ulkopuolelle, jolloin peli kaatuisi indeksivirheeseen.
