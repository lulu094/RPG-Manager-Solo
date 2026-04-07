from visualization import DataVisualization
import pandas as pd


class StatisticalAnalyzer:

    def __init__(self, characters):
        self.df = pd.DataFrame(characters)

    def overview(self):
        print("\nLEVEL STATS")
        print(self.df["Level"].describe())

    def class_distribution(self):
        print("\nCLASS COUNT")
        print(self.df["Class"].value_counts())

    def full_stats(self):
        print("\nSUMMARY")
        print("Mean:", self.df["Level"].mean())
        print("Median:", self.df["Level"].median())
        print("Max:", self.df["Level"].max())
        print("Min:", self.df["Level"].min())


class Dashboard:

    def __init__(self, characters):
        self.characters = characters
        self.analyzer = StatisticalAnalyzer(characters)
        self.viz = DataVisualization()

    def show_dashboard(self):
        print("\n=== DASHBOARD ===")
        print("Total Characters:", len(self.characters))

        self.analyzer.overview()
        self.analyzer.class_distribution()
        self.analyzer.full_stats()

    def visual_menu(self):
        while True:
            print("\n1. Compare Levels")
            print("2. Radar Chart")
            print("3. Bar Chart")
            print("4. Exit")

            choice = input("> ")

            if choice == "1":
                self.viz.compare_levels(self.characters)

            elif choice == "2":
                name = input("Name: ").lower()
                for c in self.characters:
                    if name in c["Name"].lower():
                        self.viz.radar_chart(c)

            elif choice == "3":
                name = input("Name: ").lower()
                for c in self.characters:
                    if name in c["Name"].lower():
                        self.viz.character_bar(c)

            elif choice == "4":
                break



