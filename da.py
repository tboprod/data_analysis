import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysisTool:
    def __init__(self, file_path):
        """
        Inizializza l'analizzatore di dati con un file CSV
        """
        try:
            self.df = pd.read_csv(file_path)
            print("Dataset caricato con successo!")
        except FileNotFoundError:
            print("File non trovato. Creazione di un dataset di esempio.")
            self.create_sample_dataset()
    
    def create_sample_dataset(self):
        """
        Crea un dataset di esempio se non viene fornito un file
        """
        data = {
            'Nome': ['Mario', 'Luigi', 'Giovanna', 'Paolo', 'Anna'],
            'Eta': [35, 42, 28, 55, 33],
            'Stipendio': [35000, 45000, 32000, 62000, 38000],
            'Dipartimento': ['IT', 'Vendite', 'Marketing', 'Direzione', 'Risorse Umane']
        }
        self.df = pd.DataFrame(data)
    
    def describe_dataset(self):
        """
        Fornisce una descrizione statistica del dataset
        """
        print("\n--- Descrizione Statistica ---")
        print(self.df.describe())
    
    def analyze_salary_by_department(self):
        """
        Analizza lo stipendio medio per dipartimento
        """
        salary_by_dept = self.df.groupby('Dipartimento')['Stipendio'].mean()
        print("\n--- Stipendio Medio per Dipartimento ---")
        print(salary_by_dept)
        
        # Grafico a barre
        plt.figure(figsize=(10, 6))
        salary_by_dept.plot(kind='bar')
        plt.title('Stipendio Medio per Dipartimento')
        plt.xlabel('Dipartimento')
        plt.ylabel('Stipendio Medio')
        plt.tight_layout()
        plt.savefig('stipendio_dipartimenti.png')
        plt.close()
    
    def age_salary_correlation(self):
        """
        Analizza la correlazione tra età e stipendio
        """
        correlation = self.df['Eta'].corr(self.df['Stipendio'])
        print(f"\n--- Correlazione Età-Stipendio: {correlation:.2f} ---")
        
        # Scatter plot
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['Eta'], self.df['Stipendio'])
        plt.title('Correlazione Età-Stipendio')
        plt.xlabel('Età')
        plt.ylabel('Stipendio')
        plt.tight_layout()
        plt.savefig('eta_stipendio_scatter.png')
        plt.close()
    
    def filter_and_export(self, min_age=40):
        """
        Filtra dipendenti sopra una certa età ed esporta
        """
        filtered_df = self.df[self.df['Eta'] >= min_age]
        print(f"\n--- Dipendenti over {min_age} anni ---")
        print(filtered_df)
        
        # Esporta in CSV
        filtered_df.to_csv('dipendenti_senior.csv', index=False)
    
    def comprehensive_analysis(self):
        """
        Esegue un'analisi completa del dataset
        """
        self.describe_dataset()
        self.analyze_salary_by_department()
        self.age_salary_correlation()
        self.filter_and_export()

def main():
    # Usa il metodo di esempio interno
    analyzer = DataAnalysisTool('dummy_path.csv')
    analyzer.comprehensive_analysis()

if __name__ == "__main__":
    main()
