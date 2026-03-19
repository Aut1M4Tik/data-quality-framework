from abc import ABC, abstractmethod
import time

def timer(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    print(f'Funkcja {func.__name__} wykonała się w {time.time() - start_time:.4f} sekund')
    return result
  return wrapper

#klasa abstrakcyjna, która będzie bazą dla wszystkich walidatorów danych
class DataValidator(ABC):

  def __init__(self, sales_report: str):
    self._sales_report = sales_report
    self._errors = []
  
  def __str__(self):
    return self.report

  #getter, który zwraca raport z walidacji, zawiera informacje o liczbie znalezionych błędów
  @property
  def report(self) -> str:
    return f'Zbiór {self._sales_report}: znaleziono {len(self._errors)} błędów'
  
  @property
  def errors(self):
    return self._errors.copy()

  def add_error(self, message: str):
    self._errors.append(message)

  #szablon, który musi być zaimplementowany przez wszystkie walidatory
  @abstractmethod
  def validate(self, data: dict):
    pass