from abc import ABC, abstractmethod

class DataValidator(ABC):

  def __init__(self, sales_report: str):
    self._sales_report = sales_report
    self._errors = []
  
  @property
  def report(self) -> str:
    return f'Zbiór {self._sales_report}: znaleziono {len(self._errors)} błędów'
  
  @property
  def errors(self):
    return self._errors.copy()

  def add_error(self, message: str):
    self._errors.append(message)

  def validate_positive(self, value: int, field_name: str):
    if value <= 0:
      self.add_error(f'Pole {field_name} musi być dodatnie! Wartość: {value}')

  @abstractmethod
  def validate(self, data: dict):
    pass

class NumericValidator(DataValidator):
  def __init__(self, sales_report, min_val: int = 0, max_val = 100):
    super().__init__(sales_report)
    self._min_value = min_val
    self._max_value = max_val
  
  @property
  def report(self):
    return f'[TYP: NUMERYCZNY]: znaleziono {len(self._errors)} błędów'

  def validate_range(self, value, field_name, max_value):
    if value < self._min_value or value > max_value:
      self.add_error(f'Pole {field_name} nie w zakresie! Wartość: {value}')
  
  def validate(self, data: dict):
    for key, value in data.items():
      self.validate_positive(value, key)
      self.validate_range(value, key, self._max_value)

  class DataQualityPipeline:
    ...


def main():

  num_val = NumericValidator('raport_cen', 10, 100)
  num_val.validate({'cena': -5})
  num_val.validate({'cena': 101})
  print(num_val.report)
  

if __name__ == '__main__':
  main()
