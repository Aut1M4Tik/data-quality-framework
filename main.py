from pipeline import DataQualityPipeline
from validators import NumericValidator

def main():

  pipeline = DataQualityPipeline()

  pipeline.add_validator(NumericValidator("Ceny", min_val=10, max_val=500))

  dirty_data = {'Produkt A': 15,
                'Produkt B': 'elo', 
                'Produkt C': 100 }

  pipeline.run_all(dirty_data)
  pipeline.show_final_report()
  

if __name__ == '__main__':
  main()
