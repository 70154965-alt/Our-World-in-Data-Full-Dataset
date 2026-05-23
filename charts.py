import matplotlib.pyplot as plt
import seaborn as sns

COLOR = "#1f77b4"

def pie_chart(df, col="energy_per_capita"):
    fig, ax = plt.subplots()
    data = df.groupby("country")[col].mean().dropna().nlargest(8)
    ax.pie(data.values, labels=data.index, autopct="%1.1f%%",
           colors=sns.color_palette("Blues", len(data)))
    ax.set_title(f"Top Countries by {col.replace('_',' ').title()}")
    return fig

def histogram(df, col="energy_per_capita"):
    fig, ax = plt.subplots()
    df[col].dropna().plot.hist(bins=30, color=COLOR, ax=ax)
    ax.set_title(f"Distribution of {col.replace('_',' ').title()}")
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
    return fig

def line_chart(df, col="energy_per_capita"):
    fig, ax = plt.subplots()
    top = df.groupby("country")[col].mean().nlargest(5).index
    for c in top:
        sub = df[df["country"] == c].sort_values("year")
        ax.plot(sub["year"], sub[col], label=c)
    ax.set_title(f"{col.replace('_',' ').title()} Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel(col)
    ax.legend()
    return fig

def bar_chart(df, col="energy_per_capita"):
    fig, ax = plt.subplots()
    data = df.groupby("country")[col].mean().dropna().nlargest(10)
    sns.barplot(x=data.values, y=data.index, palette="Blues_d", ax=ax)
    ax.set_title(f"Top 10 Countries — {col.replace('_',' ').title()}")
    ax.set_xlabel(col)
    return fig

def scatter_plot(df, x="gdp", y="energy_per_capita"):
    fig, ax = plt.subplots()
    df_clean = df[[x, y]].dropna()
    ax.scatter(df_clean[x], df_clean[y], alpha=0.5, color=COLOR)
    ax.set_title(f"{x.replace('_',' ').title()} vs {y.replace('_',' ').title()}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return fig

def box_plot(df, col="energy_per_capita"):
    fig, ax = plt.subplots()
    top = df.groupby("country")[col].mean().nlargest(6).index
    df[df["country"].isin(top)].boxplot(column=col, by="country", ax=ax)
    ax.set_title(f"Box Plot — {col.replace('_',' ').title()}")
    plt.suptitle("")
    return fig

def heatmap(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    num_cols = df.select_dtypes(include="number").dropna(axis=1, how="all")
    corr = num_cols.corr().iloc[:10, :10]
    sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    return fig

def area_chart(df, col="renewables_share_energy"):
    fig, ax = plt.subplots()
    world = df[df["country"] == "World"].sort_values("year")
    ax.fill_between(world["year"], world[col].fillna(0), color=COLOR, alpha=0.5)
    ax.set_title(f"World {col.replace('_',' ').title()} Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel(col)
    return fig

def count_plot(df, col="country"):
    fig, ax = plt.subplots()
    top = df[col].value_counts().head(10)
    sns.barplot(x=top.values, y=top.index, palette="Blues_d", ax=ax)
    ax.set_title(f"Record Count by {col.title()}")
    return fig

def violin_plot(df, col="energy_per_capita"):
    fig, ax = plt.subplots()
    top = df.groupby("country")[col].mean().nlargest(5).index
    sub = df[df["country"].isin(top)]
    sns.violinplot(data=sub, x="country", y=col, palette="Blues", ax=ax)
    ax.set_title(f"Violin Plot — {col.replace('_',' ').title()}")
    plt.xticks(rotation=30)
    return fig