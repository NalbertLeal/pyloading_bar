import math
import os

class Bar:
  def __init__(self, total, current_step=0, symbol='#', update_terminal=True, length=None, template=None):
    self._total = total
    self._length = self._calc_length(length, total)
    self._current_step = current_step
    self._symbol = symbol
    self._update_terminal = update_terminal
    self._char_step = self._total / self._length
    self._inner_step = self._char_step / len(self._symbol)
    self._walls = '[]'
    self._extract_template(template)
    self._draw()

  def _extract_template(self, template):
    if (template):
      self._symbol = template[1:-1]
      self._inner_step = self._char_step / len(self._symbol)
      self._walls = template[0] + template[-1]

  def _calc_length(self, length, total):
    (columns, _) = os.get_terminal_size()

    final_length = length if length is not None else total

    if final_length > columns - 10:
      return columns - 10
    else:
      return final_length
    

  def _loading_bar(self):
    full_symbol = self._symbol[-1]
    full_step = math.floor(self._current_step / self._char_step)
    
    rest = int(self._current_step % self._char_step)
    char_index = math.floor(rest / self._inner_step)
    
    progress_done = full_step * full_symbol
    progress_todo = (self._length - full_step - 1 ) * ' '

    if (self._current_step == self._total):
      bar = f'{self._walls[0]}{progress_done}{self._walls[1]}'
    else:
      bar = f'{self._walls[0]}{progress_done}{self._symbol[char_index]}{progress_todo}{self._walls[1]}'

    percentage = round((self._current_step / self._total) * 100, 2)
    str_percentage = f' {percentage}%'

    return f'{bar}{str_percentage}'
    
  def _draw(self):
    bar = self._loading_bar()

    if self._update_terminal:
      print(f'\r{bar}', end='')
    else:
      print(f'{bar}')

  def next(self):
    self._current_step += 1
    self._draw()