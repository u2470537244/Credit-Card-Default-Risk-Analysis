import matplotlib.pyplot as plt
from config import VISUAL_CONFIG
class VisualizationForDefault:
    @staticmethod
    def plot_and_save(data, title, xlabel, ylabel, save_path):
        plt.figure(figsize=VISUAL_CONFIG["fig_size"])
        data.plot(kind="line", color=VISUAL_CONFIG["color"])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(alpha=VISUAL_CONFIG["grid_alpha"])
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

