from .bar import Bar

class RangeBar(Bar):
  def __init__(self, total, current_step=0, symbol='#', update_terminal=True):
    super(RangeBar, self).__init__(total, current_step=current_step, symbol=symbol, update_terminal=update_terminal)

  def __iter__(self):
    return self

  def __next__(self):
    if self.total > self.current_step:
      self.next()
      return self.current_step
    raise StopIteration