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
    return f'[TYP: NUMERYCZNY]: {self._sales_report} znaleziono {len(self._errors)} błędów'

  def validate_range(self, value, field_name, max_value):
    if value < self._min_value or value > max_value:
      self.add_error(f'Pole {field_name} nie w zakresie! Wartość: {value}')
  
  def validate(self, data: dict):
    for key, value in data.items():
      self.validate_range(value, key, self._max_value)

class DataQualityPipeline:
  def __init__(self):
    self._validators = []

  def add_validator(self, validator: DataValidator):
    self._validators.append(validator)

  def run_all(self, data: dict):
    for val in self._validators:
      val.validate(data)

  def show_final_report(self):
    for val in self._validators:
      print(val.report)

def main():

  pipeline = DataQualityPipeline()

  pipeline.add_validator(NumericValidator("Ceny", min_val=10, max_val=500))
  pipeline.add_validator(NumericValidator("Ilości", min_val=1, max_val=100))

  data = {"produkt_cena": -9, "produkt_ilosc": 99}
  pipeline.run_all(data)
  pipeline.show_final_report()
  

if __name__ == '__main__':
  main()
