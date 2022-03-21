class Bar:
  def __init__(self, total, current_step=0, symbol='#', update_terminal=True):
    self.total = total
    self.current_step = current_step
    self.symbol = symbol[0]
    self.update_terminal = update_terminal
    self.draw()

  def next(self):
    self.current_step += 1
    self.draw()
    
  def draw(self):
    progress_done = self.current_step * self.symbol
    progress_todo = (self.total - self.current_step - 1) * ' '
    bar = f'[{progress_done}{progress_todo}]'
    if self.update_terminal:
      print(f'\r{bar}', end='')
    else:
      print(f'{bar}')