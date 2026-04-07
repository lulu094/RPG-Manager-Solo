import matplotlib.pyplot as plt
import numpy as np


class DataVisualization:

    def character_bar(self, character):
        stats = character["Stats"]

        plt.figure()
        plt.bar(stats.keys(), stats.values())
        plt.title(character["Name"] + " Stats")
        plt.show()

    def compare_levels(self, characters):
        names = [c["Name"] for c in characters]
        levels = [c["Level"] for c in characters]

        plt.figure()
        plt.bar(names, levels)
        plt.title("Level Comparison")
        plt.xticks(rotation=45)
        plt.show()

    def radar_chart(self, character):
        stats = character["Stats"]

        labels = list(stats.keys())
        values = list(stats.values())

        values += values[:1]

        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
        angles += angles[:1]

        plt.figure()
        ax = plt.subplot(111, polar=True)

        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.3)

        ax.set_thetagrids(np.degrees(angles[:-1]), labels)
        plt.title(character["Name"] + " Radar")

        plt.show()