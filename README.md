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

