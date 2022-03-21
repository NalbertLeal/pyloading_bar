# Pyloading  

## How to install  

Just use pip:  
  
```bash
$ pip install -i https://test.pypi.org/simple/ pyloading-bar==0.1.1
```  
  
## How to use:  

For now pyoading_bar is a very simple package that just support a simple progress bar that must be instantiated and after each step you must call the bar to update a step:

```python
from pyloading_bar import Bar

number_of_steps = 10
bar = bar(number_of_steps)
for step in range(number_of_steps):
  bar.next()
```

The usual bar is like this:  
[##########]  

But you can chage the bar by the symbol parameter:

```python
from pyloading_bar import Bar  
  
number_of_steps = 10
bar = bar(number_of_steps, symbol='@')
for step in range(number_of_steps):
  bar.next()
```

now the bar look like this:  
[@@@@@@@@@@]

And if you want that the terminal don't update the last line with the new progress bar state (the progress bar assume by default that you don't print anything to the terminal), just say to the progress bar print a new line to each step:

```python
from pyloading_bar import Bar

number_of_steps = 10
bar = bar(number_of_steps, symbol='@', update_terminal=False)
for step in range(number_of_steps):
  bar.next()
```