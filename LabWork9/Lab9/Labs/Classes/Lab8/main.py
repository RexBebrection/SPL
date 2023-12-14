from Labs.Classes.Lab8.csv_visual import DataVisualizer

def main():
    csv_file_path = 'D:/Labs/Спец. мови програмування/Lab9/Data/Lab8/mock_data.csv'
    output_folder = 'D:/Labs/Спец. мови програмування/Lab9/Data/Lab8'  # Змінено шлях для зберігання
    output_path = 'D:/Labs/Спец. мови програмування/Lab9/Data/Lab8'  # Шлях для збереження графіків

    while True:
        data_visualizer = DataVisualizer(csv_file_path, output_folder, output_path)

        data_visualizer.explore_data()

        user_choice = input("1. Кругова діаграма \n2. Діаграма розсіювання \n3. Стовпцева діаграма \n4. Вивести всі діаграми \nВведіть номер діаграми (1-4) або 'x' для виходу: ")

        if user_choice.lower() == 'x':
            break

        data_visualizer.visualize_data(user_choice)

if __name__ == "__main__":
    main()
