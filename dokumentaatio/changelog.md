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

## Viikko 5

- GameLoop luokkaa muokattu:

  - Pudonneiden palikoiden värit ja sijainnit tallennetaan sanakirjaan
  - Palikoiden törmääminen pohjaan tarkastetaan
  - Palikoiden väliset törmäykset tarkastetaan
  - Uuden palikan "spawnaaminen" nyt mahdollista

- GameGrid luokkaa muokattu:

  - Lisätty funktio rivien hajotukseen kun ne ovat täynnä
  - Lisätty funktio kaikkien värien resetoimiseen
    - Tämä on apufunktio edelliselle

- Testattu:

  - GameGrid luokka:
    - Kaikki ruudukot palautuvat odotettavasti

## Viikko 6

- GameLoop luokkaa muokattu:

  - Lisätty ominaisuus pelin häviämisen tarkistamiseen
  - Lisätty ominaisuus palikan putoamisen nopeuttamiseksi
  - Lisätty ominaisuus pisteiden päivittämiseen
  - Pieni muokkaus koordinaatteihin joihin uusi palikka spawnataan, sillä edelliset koordinaatit aiheuttivat vaikeuksia värien piirtämiseen ruudukon katossa
  - Renderer kutsut game over ja highscore teksteille

- Renderer luokkaa muokattu:

  - Seuraavan palikan kuva renderöidään nyt ikkunan oikealle reunalle
  - Pisteet renderöidään vasemmalle reunalle
  - Jotain irrallisia funktioita fonttien ja tekstien luomisen/saamisen helpottamiseksi

- GameGrid luokkaa muokattu:

  - Clear rows korjattu, nyt yksinkertaisesti vain lisätään uusi rivi ylös ja päivitetään pudonneiden palikkojen sanakirjaa sen mukaisesti
  - Update grid päivittää värit kun tämä on tehty

- Uudet luokat:

  - Tietokannan luominen ja yhteys (initialize_database + database_connection)
  - Highscore_repository + service
    - Pitää yllä pysyväistallennusta pisteistä (ja noutaa tiedon tarvittaessa)

- Lisäksi lisätty fontti ja bängeri biisi

Testattu:

- GameGrid luokka:

  - Täydet rivit tunnistetaan
  - Täysi rivi tyhjennetään
  - Uusi rivi lisätään oikeanlaisesti

- GameLoop luokka:
  - Pelissä tapahtuvat kolliisiot tunnistetaan
  - Palikka liikkuu kuten pitää
  - Palikka tippuu ajankuluessa kuten pitää
