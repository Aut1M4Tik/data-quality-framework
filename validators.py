from base import DataValidator

class NumericValidator(DataValidator):
  def __init__(self, sales_report, min_val: int = 0, max_val: int = 100):
    super().__init__(sales_report)
    self._min_value = min_val
    self._max_value = max_val
    
  @property
  def report(self):
    base_msg = super().report
    return f'[TYP: NUMERYCZNY] {base_msg}'

  @classmethod
  def create_standard_validator(cls, sales_report):
    return cls(sales_report, min_val=0, max_val=100)

  def validate_range(self, value, field_name, max_value):
    if value < self._min_value or value > max_value:
      self.add_error(f'Pole {field_name} nie w zakresie! Wartość: {value}')
  
  def validate(self, data: dict):
    for key, value in data.items():
      try:
        self.validate_range(value, key, self._max_value)
      except TypeError:
        self.add_error(f'Pole {key} musi być liczbą! Wartość: {value}')