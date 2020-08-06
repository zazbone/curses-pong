# Char-art utils
BALL = '■'
RACKET_CHUNK = '║'

# Curses init_pair color flags
C_WHITE_BLACK = 0
C_YELLOW_BLACK = 1


def clamp(MIN: int, n: int, MAX: int) -> int:
    """Clam n in [MIN, MAX["""
    if MIN < MAX:
        return max(MIN, min(n, MAX - 1))
    else:
        raise ValueError("MAX value must be greater than MIN value")


def around(value: int, size: int, step=1) -> range:
    """Return an interval of size (size) around value (value)
    step argument optionnal"""
    half_size = size // 2
    return range(
        value - half_size,
        value + half_size + 1,
        step
    )
