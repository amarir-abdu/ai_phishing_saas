import pandas as pd
import sys

SEPARATOR = "-" * 60

def load_csv(path: str) -> pd.DataFrame:
    """
    Load a csv file safely using pandas
    """
    try:
        df = pd.read_csv(path)

        if df.empty:
            print("Error: CSV file contains no data rows.")
            sys.exit(1)

        print("CSV loaded successfully.\n")
        return df
    
    except FileNotFoundError:
        print(f"Error: File not found -> {path}")
        sys.exit(1)

    except pd.errors.EmptyDataError:
        print(f"Error: CSV file is empty.")
        sys.exit(1)

    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse CSV -> {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error while loading CSV -> {e}")    
        sys.exit(1)

def inspect_dataframe(df: pd.DataFrame) -> None:
    """
    Print basic information about the dataframe
    """
    print("DATASET SUMMARY")
    print(SEPARATOR)

    # Total rows and columns
    total_rows = df.shape[0]
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    # Column names
    print("Columns:")
    for col in df.columns:
        print(f"    - {col}")
    print()

    # First 5 rows
    print("First 5 rows")
    print(df.head())
    print()

def analyze_class_label(df: pd.DataFrame, column_name: str = "CLASS_LABEL") -> None:
    """
    Analyze the CLASS_LABEL column safely.
    """
    print("CLASS_LABEL ANALYSIS")
    print(SEPARATOR)

    if column_name not in df.columns:
        raise KeyError(f"Column '{column_name}' does not exist in the dataset.")

    series = df[column_name]

    if series.isnull().any():
        null_count = series.isnull().sum()
        print(f"Warning: {null_count} missing values detected\n")

    # Value distribution
    value_counts = series.value_counts(dropna=False)
    total = len(series)

    print("Value distribution:")
    for value, count in value_counts.items():
        percentage = (count / total) * 100
        print(f"    Label {value}:{count:>5} samples ({percentage:>5.1f}%)")
    print()

    # Check for binary classification
    unique_values = series.dropna().unique()
    if len(unique_values) > 2:
        print(f"Warning: More than two labels detected: {unique_values}\n")
    elif len(unique_values) == 2:
        print("Binary classification problem confirmed.\n")

def main():
    csv_path = "phishing_raw.csv"

    # Load data
    df = load_csv(csv_path)

    try:
        # Inspect dataset
        inspect_dataframe(df)

        # Analyze target variable
        analyze_class_label(df)

    except KeyError as e:
        print(f"Column error -> {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected runtime error -> {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()