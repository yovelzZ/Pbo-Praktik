import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, accuracy_score

def preprocess_data(df):
    # Mengisi nilai yang hilang
    df.fillna(df.mean(), inplace=True)
    return df

def analyze_data(df, target_col, algorithm):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Membagi data menjadi data latih dan uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if algorithm == 'linear_regression':
        model = LinearRegression()
    elif algorithm == 'decision_tree':
        model = DecisionTreeRegressor()
    elif algorithm == 'naive_bayes':
        model = GaussianNB()
        # Pastikan target adalah kategorikal
        y = y.astype('category')
    else:
        print("Algoritma tidak dikenali.")
        return

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    if algorithm == 'naive_bayes':
        accuracy = accuracy_score(y_test, predictions)
        print(f'Akurasi: {accuracy:.2f}')
    else:
        mse = mean_squared_error(y_test, predictions)
        print(f'Mean Squared Error: {mse:.2f}')

def display_statistics(df):
    print("\nStatistik Deskriptif:")
    print(df.describe())

def main():
    # Membaca data langsung dari file
    file_name = 'air_quality.xlsx'
    df = pd.read_excel(file_name)
    df = preprocess_data(df)

    while True:
        print("\nPilihan analisis:")
        print("1. Analisis menggunakan algoritma")
        print("2. Tampilkan statistik deskriptif")
        print("3. Tampilkan informasi data")
        print("4. Keluar")

        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            target_col = input("Masukkan nama kolom target: ")
            algorithm = input("Masukkan algoritma (linear_regression / decision_tree / naive_bayes): ")
            analyze_data(df, target_col, algorithm)
        elif choice == '2':
            display_statistics(df)
        elif choice == '3':
            print("\nInformasi Data:")
            print(df.info())
        elif choice == '4':
            print("Keluar dari analisis.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()