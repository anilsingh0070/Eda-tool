import pandas as pd
import os 

print()
print("===============================================")
print("Loading EDA Tool...\n\n")
print("***** Welcome to Exploratory Data Analysis Tool *****\n")
print("\nSelect file type (1 = csv, 2 = xlsx, 3 = json, 4 = txt)")

file_type = input("Enter choice: ")

file_path = None  

match file_type:
    case "1":
        file_path = input("Enter CSV file path: ")
    case "2":
        file_path = input("Enter Excel file path: ")
    case "3":
        file_path = input("Enter JSON file path: ")
    case "4":
        file_path = input("Enter TXT file path: ")
    case _:
        print("Invalid choice!")
        exit()

print("\nLoading file...")

if os.path.exists(file_path):
    try:
        match file_type:
            case "1":
                df = pd.read_csv(file_path)
            case "2":
                df = pd.read_excel(file_path)
            case "3":
                df = pd.read_json(file_path)
            case "4":
                df = pd.read_csv(file_path, delimiter="\t")
        
        print("✅ File loaded successfully!")
    except Exception as e:
        print("Error loading file:", e)
        exit()
else:
    print("File not found!")
    exit()

# ===== MENU =====
while True:
    print("\nChoose option:")
    print("1 = View Top 5 rows")
    print("2 = Summary statistics")
    print("3 = Smart Auto Clean")
    print("4 = Null values (Manual)")
    print("5 = Data shape")
    print("6 = Column names")
    print("7 = Remove duplicates")
    print("8 = Save cleaned file")
    print("9 = Dataset info")
    print("0 = Exit")

    option = input("Enter choice: ")

    match option:
        case "1":
            print(df.head())

        case "2":
            print(df.describe())

        case "3":
            print("\nSmart Cleaning Started...\n")

            missing_percent = df.isnull().mean() * 100

            for col in df.columns:
                if missing_percent[col] > 40:
                    df.drop(columns=[col], inplace=True)
                    print(f"✅ {col}: Dropped (>40% missing)")

                elif df[col].dtype in ['int64', 'float64']:
                    df[col].fillna(df[col].median(), inplace=True)
                    print(f"✅ {col}: Filled with median")

                else:
                    df[col].fillna(df[col].mode()[0], inplace=True)
                    print(f"✅ {col}: Filled with mode")

            print("\n✅ Smart cleaning completed!")

        case "4":
            print("\nNull Values\n:", df.isnull().sum())
            print("1 = Drop | 2 = Fill | 3 = Skip")

            null_option = input("Enter choice: ")

            if null_option == "1":
                df = df.dropna()
                print("✅ Null values dropped")

            elif null_option == "2":
                df.fillna(df.select_dtypes(include='number').median(), inplace=True)
                print("✅ Numeric null values filled with median")

                df.fillna("Default", inplace=True)
                print("✅ Categorical null values filled with Default")

                print("✅ Null values filled")

            elif null_option == "3":
                print("Skipped")

            else:
                print("Invalid choice")

        case "5":
            print("Shape:", df.shape)

        case "6":
            print("Columns:", df.columns)

        case "7":
            before = df.shape[0]
            df = df.drop_duplicates()
            after = df.shape[0]
            print(f"✅ Removed {before - after} duplicate rows")

        case "8":
            save_path = "cleaned_output.csv"
            df.to_csv(save_path, index=False)
            print(f"✅ File saved as {save_path}")

        case "9":
            print("\nDataset Info:\n")
            df.info()
            print("\nNull Values:\n", df.isnull().sum())

        case "0":
            print("Exiting...")
            print("Thank you for using the EDA Tool!\nMade with ❤️ by Anil Singh - https://github.com/anil-singh")
            break

        case _:
            print("Invalid option")