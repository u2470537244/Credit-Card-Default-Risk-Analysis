from DataProcessing import DataProcessing as dp
from visualization import VisualizationForDefault as VisualD
if __name__ == "__main__":
    df = dp.load_data("UCI_Credit_Card.csv")
    df_filtered = dp.clean_data(df)
    default_dict = dp.analyze_default_rate(df_filtered)
    VisualD.plot_and_save(
        data=default_dict['age_default_rate'],
        title="Default Rate by Age",
        xlabel="Age",
        ylabel="Default Rate",
        save_path="age_default_rate.png"
    )
    VisualD.plot_and_save(
        data=default_dict['limit_default_rate'],
        title="Default Rate by Credit Limit",
        xlabel="Credit Limit (LIMIT_BAL)",
        ylabel="Default Rate",
        save_path="limit_default_rate.png"
    )
    print("Analysis completed. Charts saved successfully!")
