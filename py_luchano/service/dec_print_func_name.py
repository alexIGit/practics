def print_func_name(func):
  def wrapper(*args, **kwargs):
    print(f"'{func.__name__}'")
    return_value = func(*args, **kwargs)
    return return_value

  return wrapper
