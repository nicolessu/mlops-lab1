def _validate_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise ValueError(f"{name} must be a number (int/float).")

def fun1(x, y):
    """
    Adds two numbers together.
    """
    _validate_number(x, "x")
    _validate_number(y, "y")
    return x + y

def fun2(x, y):
    """
    Subtracts y from x.
    """
    _validate_number(x, "x")
    _validate_number(y, "y")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    """
    _validate_number(x, "x")
    _validate_number(y, "y")
    return x * y

def fun4(x, y, z):
    """
    Adds three numbers together.
    """
    _validate_number(x, "x")
    _validate_number(y, "y")
    _validate_number(z, "z")
    return x + y + z

# ✅ 你自己的新增功能（讓它跟原 repo 不一樣）
def average(x, y):
    """
    Returns the average of two numbers.
    """
    _validate_number(x, "x")
    _validate_number(y, "y")
    return (x + y) / 2

