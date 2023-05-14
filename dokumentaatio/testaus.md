# Testausdokumentti

Ohjelman testaus on suoritettu yksikkö- ja integraatiotestauksilla Pythonin unittest kirjastolla. Pelin pelaaminen on testattu manuaalisesti.

## Yksikkötestaus- ja integraatiotestaus

### Sovelluslogiikka

Luokkia GameGrid, GameLoop, Block ja HighscoreService on testattu niitä vastaavilla testiluokilla: TestGameGrid, TestGameLoop, TestBlock ja TestHighscoreService. Luokat jotka sisältävät riippuuksia
on testattu injektoimalla riippuvuudet. Joissan tapauksissa kuten esim. GameLoopin kohdalla on myös käytetty Mock -olioita, vaikka tämä ei varsinaisesti pakollista olisi ollutkaan. HighscoreRepositoriota testataan erillisen testitietokannan "test-database.sqlite" avulla.

### Testikattavuus

Sovelluksen testauksen haaraumakattavuus on 70%. Testien ulkopuolelle jätettiin luokat: config, start_game, initialize_database ja database_connection

![Testikattavuusraportti](https://github.com/smannist/ot2023/blob/master/dokumentaatio/images/coverage_rep.png)
