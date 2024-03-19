import matplotlib.pyplot as plt
import seaborn as sns

def calc_outliers(data):
    """
    Calculates outliers using Tukey's fences method,
    returns lower and upper boundaries.
    """
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
   
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    return lower_bound, upper_bound


def violin_outliers_gender(outliers: dict, df, feature) -> dict:
    """
    Plots violin plots for a given feature and highlights outliers.
    Input: dict of outliers (feature): tuple (lower_bound, upper_bound).
    """
    # create subplots
    fig, axes = plt.subplots(1, len(outliers), figsize = (8 * len(outliers), 4))
    
    # loop through outliers and plot violin plots
    for i, (gender, ax) in enumerate(zip(outliers, axes.flatten())):
        
        sns.violinplot(data = df[df["gender"] == i+1], y = feature, ax = ax)
        ax.set_title(gender)
        
        # horizontal lines for outlier boundaries 
        ax.axhline(y = outliers[gender][1], label = f"Upper bound outlier = {outliers[gender][1]:.1f}", 
                   color = "red", linestyle = "--", alpha = 0.7)
        ax.axhline(y = outliers[gender][0], label = f"Lower bound outlier = {outliers[gender][0]:.1f}",
                   color = "red", linestyle = "--", alpha = 0.7)
        ax.legend(loc = "upper right")
         
    plt.suptitle(f"{feature.capitalize()} Distribution and Outliers by Gender", fontsize = 16)
    # set title for the whole plot
    return outliers
