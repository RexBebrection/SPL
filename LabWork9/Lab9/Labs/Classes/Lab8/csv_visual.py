import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

class DataVisualizer:
    def __init__(self, csv_file_path, output_folder, output_path):
        self.df = pd.read_csv(csv_file_path)
        self.output_folder = output_folder
        self.output_path = output_path
        self.create_output_directory()

    def create_output_directory(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def explore_data(self):
        min_values = self.df.min()
        max_values = self.df.max()

        print("Мінімальні значення:")
        print(min_values)

        print("\nМаксимальні значення:")
        print(max_values)

    def visualize_data(self, user_choice):
        if user_choice == "1":
            self.pie_chart()
        elif user_choice == "2":
            self.scatter_plot()
        elif user_choice == "3":
            self.bar_chart()
        elif user_choice == "4":
            self.show_all_plots()
        else:
            print("Невірний вибір. Будь ласка, введіть номер від 1 до 4.")

    def save_plot(self, plot_type, filename):
        filepath = os.path.join(self.output_path, filename).replace("\\", "/")
        plt.savefig(filepath)
        print(f"Зображення '{plot_type}' збережено за шляхом: {filepath}")

    def pie_chart(self):
        car_make_distribution = self.df['car_make'].value_counts()
        car_make_distribution.plot(kind='pie', autopct='%1.1f%%', title='Розподіл марок автомобілів')
        self.save_plot('pie_chart', 'pie_chart.png')
        plt.show()

    def scatter_plot(self):
        plt.scatter(self.df['car_model_year'], self.df['car_model'], alpha=0.5)
        plt.xlabel('Рік виробництва')
        plt.ylabel('Модель автомобіля')
        plt.title('Взаємозв\'язок року виробництва та моделі автомобіля')
        self.save_plot('scatter_plot', 'scatter_plot.png')
        plt.show()

    def bar_chart(self):
        car_make_counts = self.df['car_make'].value_counts()
        car_make_counts.plot(kind='bar', xlabel='Марка автомобіля', ylabel='Кількість',
                             title='Кількість автомобілів за маркою', rot=45)
        self.save_plot('bar_chart', 'bar_chart.png')
        plt.show()

    def show_all_plots(self):
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        car_make_distribution = self.df['car_make'].value_counts()
        axes[0, 0].pie(car_make_distribution, autopct='%1.1f%%', labels=car_make_distribution.index, startangle=90)
        axes[0, 0].set_title('Розподіл марок автомобілів')

        axes[0, 1].scatter(self.df['car_model_year'], self.df['car_model'], alpha=0.5)
        axes[0, 1].set_xlabel('Рік виробництва')
        axes[0, 1].set_ylabel('Модель автомобіля')
        axes[0, 1].set_title('Взаємозв\'язок року виробництва та моделі автомобіля')

        car_make_counts = self.df['car_make'].value_counts()
        axes[1, 0].bar(car_make_counts.index, car_make_counts)
        axes[1, 0].set_xlabel('Марка автомобіля')
        axes[1, 0].set_ylabel('Кількість')
        axes[1, 0].set_title('Кількість автомобілів за маркою')
        axes[1, 0].tick_params(axis='x', labelrotation=90)
        plt.delaxes(axes[1, 1])

        plt.subplots_adjust(wspace=0.5, hspace=0.5)

        self.save_plot('all_plots', 'output_plot.png')
        fig = px.scatter(self.df, x='car_model_year', y='car_model',
                         title='Взаємозв\'язок року виробництва та моделі автомобіля')
        fig.write_html(os.path.join(self.output_path, 'output_plot.html').replace("\\", "/"))

        plt.show()
