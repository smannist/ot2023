## Viikko 3

- Lisätty Block-luokka, joka vastaa yksittäistä palikkaa pelissä
- Lisätty Renderer-luokka, joka vastaa pelin piirtämisestä pygame -ikkunaan
- Lisätty GameLoop-luokka, joka vastaa pelin toiminnallisuuksista
- Lisätty GameGrid-luokka, joka vastaa pelin matriisiesitystä
- Lisätty start_game-tiedosto josta pelin käynnistäminen tapahtuu sisältää myös mm. pelin dimensiot

- Render luokkaa muokattu:

  - Pygame -ikkunan täyttäminen harmaalla taustalla
  - Ruudukko piirtyy pygame -ikkunaan
  - Ruudukolle piirretään reunat

- Testattu:

  - GameGrid luokka muodostaa oikean kokoisen matriisin pelille
  - GameGrid luokka muodostaa matriisin, joka koostuu vain nollista

## Viikko 4

- Lisätty config -tiedosto, joka sisältää pelin dimensiot, käytettävät värit yms.
- Lisätty block_shape -tiedosto, joka sisältää palikoiden muodot NumPy arrayinä sekä palikoiden värit

- GameGrid luokkaa muokattu:

  - Soluissa säilytetään tieto nyt väreinä
    - Väri on aina joko alkuperäisen ruudukon väri tai sitten pelissä olevan palikan väri
  - Sallittavan siirron tunnistaminen
  - Värien palauttaminen ennalleen

- GameLoop luokkaa muokattu:

  - Palikat voivat nyt pudota
  - Palikoiden liikuttaminen ruudukossa on nyt mahdollista
  - Event handler jaettu pienemmiksi funtioiksi
  - Useita tietueita lisätty mm. edellisen rotaation tallennus, sillä pelin ominaisuudet vaativat niitä

- Renderer luokkaa muokattu:

  - Renderer piirtää nyt oikeanlaisesti ruudukon GameGridin datan avulla, eikä pelkästää GameGridin dimensioiden perusteella

- Block luokkaa muokattu:

  - Muodon muuttaminen koordinaateiksi joita voidaan sitten käyttää ruudukon värittämiseen
  - Toiminnallisuus palikoiden liikuttamiseksi
  - Palikan rotaatiofunktio

- Testattu:

  - Block luokka:

    - X ja y-koordinaatit päivittyvät kuten pitää jos palikkaa liikutettaan
    - Rotaation kutsuminen kääntää palikkaa oikein (käytännössä tämä on matriisin transpoosi)

  - GameGrid luokka:
    - Kaikki edelliset testit muokattu vastaamaan uutta rakennetta
    - Hyväksyttävät palikan siirrot sallitaan
    - Hyväksymättömät palikan siirrot hylätään
    - Värit resetoidaan oletettavasti kun palikkaa liikutetaan ruudukossa
