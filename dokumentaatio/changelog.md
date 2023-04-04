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
