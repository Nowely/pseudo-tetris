# pseudo-tetris

![pseudo-tetris 6x6x6](https://user-images.githubusercontent.com/37639183/208927676-64476bcd-8051-4468-9788-0c2cf0227f75.gif)
![pseudo-tetris 20x20x20](https://user-images.githubusercontent.com/37639183/208927854-15b701fd-cd45-4f1c-8e61-5676977caac7.gif)

## Prerequisites

* [Python 3.11](https://www.python.org/downloads/) or newer
* pipenv

## Getting started

1. Install the `pipenv` if it needs:

```sh
pip install pipenv
```

2. Install dependencies, create a virtual env if not present, activate this

```sh
pipenv install
```

3. Start the `main.py` script

### Other commands

Activate / create virtual env:

```sh
pipenv shell
```

## Example

```python
from Field import Field
from Figure import Figure
from Visualization import show, show_gif


# Show a small field 6x6x6 with determine figures
def show_small_field():
    # Init a field with width = 6, depth = 6, height = 6
    field = Field(6, 6, 6)
    # Add the figure with width = 2, depth = 2, height = 1 and the start position width = 2, depth = 1 of field
    field.add_figure(Figure(2, 2, 1), (2, 1))
    field.add_figure(Figure(2, 5, 2))
    field.add_figure(Figure(1, 1, 1))
    field.add_figure(Figure(2, 2, 2))
    field.add_figure(Figure(2, 2, 2), (3, 2))
    field.add_figure(Figure(1, 1, 3), (4, 1))

    # Show plot with added figures
    show(field.map)
    # Show gif with stages of adding figures 
    # Gif can be saved with the save method
    show_gif(field.slices)  # .save('pseudo-tetris.gif', writer='pillow', fps=5)


# Show a big field 20x20x20 with random figures
def show_big_field():
    field = Field(20, 20, 20)
    [field.add_random_figure() for _ in range(20)]

    show(field.map)
    show_gif(field.slices)  # .save('pseudo-tetris 20x20x20.gif', writer='pillow', fps=30)


if __name__ == '__main__':
    show_small_field()
    # show_big_field()

```
