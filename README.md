# xdotool_python_window_util

## Use

### Size
```
from main import Size

a = Size(40, 60)
a.size_win()
```

### Move
```
from main import Move

a = Move(True, 20, 30)
a.move_win()
```

## Test

```
PYTHONPATH=./src pytest
```


## Future Features
- Something to name windows<br>
- Something to use move and size with window by name<br>
- Something to get the size and position of a window by name<br>
- Something that uses the size and position of two windows by name and calculates distance between<br>

