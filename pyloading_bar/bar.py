class Bar:
  def __init__(self, total, current_step=0, symbol='#', update_terminal=True):
    self._total = total
    self._current_step = current_step
    self._symbol = symbol[0]
    self._update_terminal = update_terminal
    self._draw()

  def _loading_bar(self):
    progress_done = self._current_step * self._symbol
    progress_todo = (self._total - self._current_step ) * ' '
    bar = f'[{progress_done}{progress_todo}]'

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