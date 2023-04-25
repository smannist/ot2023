# Arkkitehtuurikuvaus

## Sovelluslogiikan luokkakaavio


```mermaid

 classDiagram
 
 direction LR
 
      Block -- GameLoop
      GameLoop -- GameGrid
      
      
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
      _initialize_grid()
      is_valid_move()
      reset_cell_colors()
      }
      
      class GameLoop{
      renderer
      display
      previous_tick
      current_block
      previous_block_coordinates
      fall_time
      fall_speed
      key_pressed
      previous_rotation
      start()
      _handle_events()
      _handle_keydown()
      _handle_rotate_block()
      _handle_move_block_down()
      _handle_move_block_left()
      _handle_move_block_right()
      _block_moved()
      _drop_block()
      _update_elapsed_time()
      }
      
```

## Sekvenssikaavio

Yksinkertaistettu tilanne palikan siirrosta vasemmalle. GameLoop luokka saa Pygame -kirjaston tapahtumajonosta komennot KDOWN, K_LEFT. Tämä vastaavasti laukaisee metodikutsun move_left() Block -luokan olion ilmentymälle current_block. Palikan x-arvoa lasketaan yhdellä. Muut siirrot toteutetaan samaan tapaan - paitsi rotaatio, jossa suoritetaan palikan kuviomatriisin transponointi. Näppäimistön kautta tapahtuvat siirrot ovat mahdollisia vain jos palikka ei ole siirto hetkellä tippumassa eli kun is_dropping palauttaa arvon False.

```mermaid
sequenceDiagram 
  participant GameLoop
  participant Pygame.Event
  participant Current_block

  Pygame.Event->>GameLoop: event.type == KDOWN
  Pygame.Event->>GameLoop: event.key == K_LEFT
  GameLoop->>Current_block: move_left()
  GameLoop->>Current_block: move_left()
```
