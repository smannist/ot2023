# Arkkitehtuurikuvaus

## Pakkauskaavio

Rakenne noudattaa pääsäntöisesti kolmitasoista kerrosarkkitehtuuria ja sovelluksen kannalta oleellisten pakkauksien pakkausrakenne on alla oleva:

![Pakkausrakenne](https://github.com/smannist/ot2023/blob/master/dokumentaatio/images/package.png)

Sovelluslogiikan kannalta oleelliset tiedostot sijaitsevat src sekä services kansiossa, kun taas repositories vastaa pysyväistallennuksesta. Database kansio sisältää tiedostot tietokantayhteyden muodostamiseen ja luomiseen.


## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat Block, GameGrid sekä GameLoop. Block -luokka kuvastaa yksittäistä palikkaa pelin ruudukossa GameGrid. GameLoop vastaa pelisilmukan pyörittämisestä. GameLoopilla voi olla luonnollisesti vain yksi peliruudukko ja palikka käsittelyssä (current_block). GameLoop käsittelee varsinaisesti Renderer -luokassa sijaitsevaa ilmentymää GameGrid luokasta. Tämä tehtiin alunperin vain ruudukon piirtämisen helpottamiseksi. Luokkakaaviossa GameLoop -luokka on hieman yksinkertaistettu metodien/funktioiden suhteen sillä niitä on varsin monta.


```mermaid

 classDiagram
 
 direction LR
 
      Block "1" --> GameLoop
      GameLoop <-- "1" GameGrid
      
      
      class Block{
      x
      y
      shape_info_list
      shape
      color
      shape_to_coordinates()
      move_down()
      move_left()
      move_right()
      move_up()
      rotate()
      }
      
      class GameGrid{
      rows
      columns
      grid
      score
      is_valid_move()
      reset_cell_colors()
      clear_rows()
      _remove_rows_and_move()
      _remove_row()
      _move_blocks_down()
      _add_new_top()
      _get_rows_to_clear()
      _update_grid()
      _update_score()
      }
      
      class GameLoop{
      renderer
      display
      current_block
      highscore_service
      previous_tick
      fall_time
      fall_speed
      previous_rotation
      placed_blocks
      next_block
      score
      difficulty
      start()
      _handle_events()
      _handle_keydown()
      _handle_rotate_block()
      _handle_move_block_down()
      _handle_move_block_left()
      _handle_move_block_right()
      _block_movement()
      _block_dropping()
      ....()
      }
      
```

## Sekvenssikaavio tilanteesta jossa käyttäjä siirtää palikkaa alas

Kun käyttäjä siirtää ensiksi palikkaa alas validilla siirrolla tapahtumaketju etenee seuraavasti:


```mermaid
sequenceDiagram 
  actor Player
  participant GameLoop
  participant Pygame.Event
  participant Current_block
  participant Game_grid
 
  Player->>GameLoop: Nuolinäppäin alas
  GameLoop->>Pygame.Event: pygame.event.get()
  Pygame.Event->>GameLoop: Event(type=KDOWN, key=K_DOWN)
  GameLoop->>GameLoop: _handle_events()
  GameLoop->>GameLoop: _handle_keydown(K_DOWN)
  GameLoop->>Current_block: move_down()
  Current_block->>Current_block: self.y + 1
  GameLoop->>Game_grid: _is_valid_move(current_block, placed_blocks)
  Game_grid-->>GameLoop: True
```

Käyttäjä aloittaa painamalla nuolinäppäintä alas. Tämä vastaavasti laukaisee GameLoopissa sijaitevan tapahtumankäsittelijäkutsun Pygame kirjastossa sijaitsevalle moduulille Event. Event-moduuli palauttaa vastauksena annetun tyypin sekä avaimen ja muutaman muun oleellisen tiedon. Tässä tapauksessa type = KDOWN, key = K_DOWN. Tämä taas laukaisee GameLoopin sisäisen tapahtumankäsittelijän, jonka avulla käsitellään sekä näppäimen alaspainaminen että varsinainen näppäin (joka tässa tapauksessa siis oli nuolinäppäin alas). Tämän jälkeen GameLoop kutsuu Block -luokan ilmentymän current_block metodia move_down(), joka vastaavasti kasvattaa current_blockin y arvoa yhdellä. Lopuksi GameLoop kutsuu Renderer -luokassa sijaitsevaa ilmentymää GameGrid -luokasta metodikutsulla _is_valid(current_block, placed_blocks). Kun siirto on todettu validiksi, GameGrid palauttaa arvon True, jolloin muuta ei tehdä.

## Tietojen pysyväistallennus

Tiedon pysyväistallenuksesta vastaa repositories pakkauksessa sijaitseva luokka highscore_repository. Tiedot tallennetaan SQLite-tietokantaan. Tallennettu data on varsin yksinkertaista, sillä pelin on rakenteeltaan sellainen että se ei vaadi monimutkaista tietokantakäsittelyä. Tietokannan tauluun highscores tallennetaan id sekä sitä vastaava pistemäärä - josta ne sitten voidaan noutaa.
