import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
# Configure display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.original_shape = None
    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            self.original_shape = self.df.shape
            print(f"✓ Data loaded successfully!")
            print(f"  Shape: {self.original_shape[0]} rows × {self.original_shape[1]} columns")
            return self.df
        except FileNotFoundError:
            print(f"✗ Error: File '{self.file_path}' not found")
            return None
        except Exception as e:
            print(f"✗ Error loading file: {str(e)}")
            return None
        def explore_data(self):
            if self.df is None:
                print("✗ No data loaded. Please load data first.")
                return None
            exploration_results = {}
            print("\n" + "="*60)
            print("DATA OVERVIEW")
            print("="*60)
            print(f"\nDataset Shape: {self.df.shape}")
            print(f"\nFirst 5 Rows:")
            print(self.df.head())
            print(f"\n\nLast 5 Rows:")
            print(self.df.tail())
            print(f"\n\nData Types:")
            print(self.df.dtypes)
            print(f"\n\nBasic Statistics:")
            print(self.df.describe())
            print(f"\n\nMissing Values:")
            missing_values = self.df.isnull().sum()
            missing_percent = (missing_values / len(self.df)) * 100
            missing_df = pd.DataFrame({
                'Column': self.df.columns,
                'Missing_Count': missing_values.values,
                'Missing_Percentage': missing_percent.values
                })
            print(missing_df[missing_df['Missing_Count'] > 0])
            print(f"\n\nData Information:")
            print(self.df.info())
            exploration_results['shape'] = self.df.shape
            exploration_results['missing_values'] = missing_df
            exploration_results['dtypes'] = self.df.dtypes
            return exploration_results
        def check_duplicates(self):
            duplicate_count = self.df.duplicated().sum()
            print(f"\nDuplicate Records: {duplicate_count}")
            return duplicate_count
        def get_statistical_summary(self):
            print("\n" + "="*60)
            print("STATISTICAL SUMMARY")
            print("="*60)
            return self.df.describe().T
        if __name__ == "__main__":
            loader = DataLoader('ecommerce_data.csv')
            df = loader.load_data()
            if df is not None:
                loader.explore_data()
                loader.check_duplicates()
                loader.get_statistical_summary()

