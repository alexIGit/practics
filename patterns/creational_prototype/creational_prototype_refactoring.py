import copy

class SelfReferencingEntity:
  def __init__(self):
    self.parent = None

  def set_parent(self, parent):
    self.parent = parent


class SomeComponent:
  def __init__(self, some_int, some_list_of_objects, some_circular_ref):
    self.some_int = some_int
    self.some_list_of_objects = some_list_of_objects
    self.some_circular_ref = some_circular_ref

  def __copy__(self):
    new = self.__class__(
      self.some_int, self.some_list_of_objects, self.some_circular_ref
    )

    new.__dict__.update(self.__dict__)

    new.some_list_of_objects = copy.copy(self.some_list_of_objects)
    new.some_circular_ref = copy.copy(self.some_circular_ref)
    return new

  def __deepcopy(self, memo={}):
    new = self.__class__(
      self.some_int, self.some_list_of_objects, self.some_circular_ref
    )

    new.__dict__.update(self.__dict__)

    new.some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
    new.some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)
    return new
    


if __name__ == "__main__":
  list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
  circular_ref = SelfReferencingEntity()

  component = SomeComponent(23, list_of_objects, circular_ref)

  # 1. проверяем copy
  shallow_copied_component = copy.copy(component)

  # изменяем shallow_copied_component
  shallow_copied_component.some_list_of_objects.append("another object")
  
  print(shallow_copied_component.some_list_of_objects[-1]) # shallow_copied_component изменился
  print(component.some_list_of_objects[-1], end='\n\n') # component не изменился


  # 2. проверяем deepcopy
  deep_copied_component = copy.deepcopy(component)

  # изменяем deep_copied_component
  deep_copied_component.some_list_of_objects.append("another object")

  print(deep_copied_component.some_list_of_objects[-1]) # deep_copied_component изменился
  print(component.some_list_of_objects[-1], end='\n\n') # component не изменился


  # 3. изменяем component
  component.some_list_of_objects[1].add(10)

  check_deep = 10 in deep_copied_component.some_list_of_objects[1]
  check_copy = 10 in shallow_copied_component.some_list_of_objects[1]

  print(check_deep) # deep_copied_component не изменилcя
  print(check_copy, end='\n\n') # shallow_copied_component изменился

  # conclusion  deep_copied_component
  print(f"id(component.some_circular_ref.parent): {id(component.some_circular_ref.parent)}")
  print(f"id(shallow_copied_component.some_circular_ref.parent): {id(shallow_copied_component.some_circular_ref.parent)}")
  print(f"id(deep_copied_component.some_circular_ref.parent): {id(deep_copied_component.some_circular_ref.parent)}", end='\n\n')


  # print(f"id(component.some_circular_ref.parent.some_circular_ref.parent): {id(component.some_circular_ref.parent.some_circular_ref.parent)}")
  # print(f"id(shallow_copied_component.some_circular_ref.parent.some_circular_ref.parent): {id(shallow_copied_component.some_circular_ref.parent.some_circular_ref.parent)}")
  # print(f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): {id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}", end='\n\n')
  print(f"id(component): {id(component)}")
  print(f"id(shallow_copied_component): {id(shallow_copied_component)}")
  print(f"id(deep_copied_component): {id(deep_copied_component)}", end='\n\n')
  
  print(
        "^^ This shows that deepcopied objects contain same reference, they are not cloned repeatedly." , end='\n\n\n'
  )
