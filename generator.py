import random

class FileGenerator:
  def __init__(self, path: str, name: str, size: int, list: list = None, p_weights: list = None):
    self._name = name
    self._path = path
    self._size = size
    self.list = list if list is not None else ['Produkt A', 'Produkt B', 'Produkt C', 'Produkt D', 'Produkt E', 67, 'I Do pieca']
    self.p_weights = p_weights if p_weights is not None else [0.2, 0.2, 0.2, 0.2, 0.1, 0.03, 0.07]

  def generate(self):
    with open(f'{self._path}/{self._name}', 'w') as f:
      f.write('produkt,cena,ilosc,rng\n')
      for _ in range(self._size):
        random_value = random.random()
        
        prod = random.choices(self.list, weights = self.p_weights)[0]

        if random_value < 0.01:
          price = random.choices(self.list, weights = self.p_weights)[0]
          quanity = random.randint(1, 100)
        elif random_value > 0.99:
          price = random.randint(1, 1000)
          quanity = random.choices(self.list, weights = self.p_weights)[0]
        else:
          price = random.randint(1, 1000)
          quanity = random.randint(1, 100)
        
        f.write(f'{prod},{price},{quanity},{round(random_value, 2)}\n')

filegen = FileGenerator('data', 'data.csv', 100000)
filegen.generate()


