# Pyloading  

## How to install  

Just use pip:  
  
```bash
$ pip install -i https://test.pypi.org/simple/ pyloading-bar==0.1.6
```  
  
## How to use:  

For now pyloading_bar is a very simple package to draw a simple progress bar in the terminal:

There's two versions of the bar. The Bar (most simple version of the bar):

```python
from pyloading_bar import Bar

number_of_steps = 2
bar = bar(number_of_steps)
# do something
bar.next()
# do something
bar.next()
```

The usual bar is like this:  
[##########]  

And the RangeBar, this object is created to be used just like an interator on the for loop:

```python
from pyloading_bar import RangeBar

for i in RangeBar(10):
  print(i)
```

You can chage the bar by the symbol parameter:

```python
from pyloading_bar import RangeBar
  
number_of_steps = 10
for step in RangeBar(number_of_steps):
  print(step)
```

now the bar look like this:  
[@@@@@@@@@@]

And if you want that the terminal don't update the last line with the new progress bar state (the progress bar assume by default that you don't print anything to the terminal), just say to the progress bar print a new line to each step:

```python
from pyloading_bar import Bar

number_of_steps = 10
for step in RangeBar(number_of_steps, symbol='@', update_terminal=False):
  print(step)
```