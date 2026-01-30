import pandas as pd
import sys


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a csv file safely using pandas
    """
    try:
        df = pd.read_csv(path)
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
        print(f"Enexpected error while loading CSV -> {e}")    
        sys.exit(1)

def inspect_dataframe(df: pd.DataFrame) -> None:
    """
    Print basic information about the dataframe
    """
    if df.empty:
        raise ValueError("DataFrame is empty after loading.")

    print("DATASET SUMMARY")
    print("-"*60)

    # Total rows
    total_rows = df.shape[0]
    print(f"Total rows: {total_rows}\n")

    # Column names
    print("Columns:")
    for col in df.columns:
        print(f"    - {col}")
    print()

    # First 5 rows
    print("First 5 rows")
    print(df.head(), "\n")

def analyze_class_label(df: pd.DataFrame, column_name: str = "CLASS_LABEL") -> None:
    """
    Analyze the CLASS_LABEL column safely.
    """
    print("CLASS_LABEL ANALYSIS")
    print("-"*60)

    if column_name not in df.columns:
        raise KeyError(f"Column '{column_name}' does not exist in the dataset.")

    series = df[column_name]

    if series.isnull().any():
        print("Warning: CLASS_LABEL contains missing values.\n")

    value_counts = series.value_counts(dropna=False)

    print("Value distribution:")
    for value, count in value_counts.items():
        print(f"Label {value} -> {count} samples")

    print()

    unique_values = series.dropna().unique()
    if len(unique_values) > 2:
        print(f"Warning: More than two labels detected: {unique_values}\n")

def main():
    csv_path = "phishing_raw.csv"

    df = load_csv(csv_path)

    try:
        inspect_dataframe(df)
        analyze_class_label(df)

    except KeyError as e:
        print(f"Column error -> {e}")

    except ValueError as e:
        print(f"Data error -> {e}")

    except Exception as e:
        print(f"Unexpected runtime error -> {e}")


if __name__ == "__main__":
    main()