from base import DataValidator, timer

class DataQualityPipeline:
  def __init__(self):
    self._validators = []

  def add_validator(self, validator: DataValidator):
    self._validators.append(validator)

  #dekorator timer, który mierzy czas wykonania funkcji run_all
  @timer
  def run_all(self, data: dict):
    for val in self._validators:
      val.validate(data)

  def show_final_report(self):
    for val in self._validators:
        print(val)
