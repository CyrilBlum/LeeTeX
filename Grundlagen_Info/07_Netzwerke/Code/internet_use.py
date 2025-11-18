import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
plt.style.use('ggplot')

def plot_internet_use_by_income_class():
    """
    Reads internet use data and country metadata, maps countries to income class, and plots internet use evolution over time by income class.
    """
    # File paths
    internet_use_file = 'Grundlagen_Info/07_Netzwerke/Skript/Code/Files/API_IT.NET.USER.ZS_DS2_en_csv_v2_81221.csv'
    metadata_file = 'Grundlagen_Info/07_Netzwerke/Skript/Code/Files/Metadata_Country_API_IT.NET.USER.ZS_DS2_en_csv_v2_81221.csv'

    # Read metadata (country code, income group)
    meta = pd.read_csv(metadata_file)
    meta = meta[['Country Code', 'IncomeGroup']].dropna()
    meta = meta.rename(columns={'Country Code': 'Country Code', 'IncomeGroup': 'IncomeGroup'})

    # Read internet use data (skip metadata rows at top)
    df = pd.read_csv(internet_use_file, skiprows=4)
    # Keep only countries with a valid code (exclude aggregates)
    df = df[df['Country Code'].isin(meta['Country Code'])]

    # Melt the dataframe to long format: one row per country-year
    value_vars = [col for col in df.columns if col.isdigit()]
    df_long = df.melt(id_vars=['Country Name', 'Country Code'], value_vars=value_vars, var_name='Year', value_name='InternetUse')
    df_long['Year'] = df_long['Year'].astype(int)
    df_long['InternetUse'] = pd.to_numeric(df_long['InternetUse'], errors='coerce')

    # Merge with metadata to get income group
    merged = df_long.merge(meta, left_on='Country Code', right_on='Country Code', how='left')
    merged = merged.dropna(subset=['IncomeGroup'])

    # Mapping for German income class names
    income_class_de = {
        'Low income': 'Niedriges Einkommen',
        'Lower middle income': 'Unteres mittleres Einkommen',
        'Upper middle income': 'Oberes mittleres Einkommen',
        'High income': 'Hohes Einkommen'
    }
    merged['IncomeGroup'] = merged['IncomeGroup'].map(income_class_de).fillna(merged['IncomeGroup'])

    # Define ordered categories for plotting
    einkommen_order = [
        'Niedriges Einkommen',
        'Unteres mittleres Einkommen',
        'Oberes mittleres Einkommen',
        'Hohes Einkommen'
    ]
    merged['IncomeGroup'] = pd.Categorical(merged['IncomeGroup'], categories=einkommen_order, ordered=True)

    # Group by year and income group, calculate mean internet use
    grouped = merged.groupby(['Year', 'IncomeGroup'], observed=True)['InternetUse'].mean().reset_index()

    # Pivot for plotting
    pivot = grouped.pivot(index='Year', columns='IncomeGroup', values='InternetUse')

    # Plot
    plt.figure(figsize=(7, 5))
    ax = plt.gca()
    pivot.plot(ax=ax, marker='o')  # Add dots on the line

    # Annotate each point with its value as a percentage
    for income_class in pivot.columns:
        for x, y in zip(pivot.index, pivot[income_class]):
            if pd.notnull(y):
                ax.annotate(f"{y:.0f}%", (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)

    plt.ylabel('Personen, die das Internet nutzen\n (% der Bevölkerung)')
    plt.xlabel('Jahr')
    plt.grid(True)
    plt.legend(title='Einkommensklasse')
    plt.tight_layout()
    plt.ylim(0, 100)
    plt.savefig("Grundlagen_Info/07_Netzwerke/Figures/internet_use_by_income_class.pdf", format='pdf', bbox_inches='tight')

def plot_world_map_internet_use(year=None):
    """
    Plots a world map showing the percentage of individuals using the Internet by country for a given year.
    If year is None, uses the most recent year with data for each country.
    """
    # File paths
    internet_use_file = 'Grundlagen_Info/07_Netzwerke/Skript/Code/Files/API_IT.NET.USER.ZS_DS2_en_csv_v2_81221.csv'

    # Read internet use data (skip metadata rows at top)
    df = pd.read_csv(internet_use_file, skiprows=4)
    value_vars = [col for col in df.columns if col.isdigit()]
    if year is None:
        # Use the most recent year with data for each country
        df['latest_year'] = df[value_vars].apply(lambda row: max([y for y in value_vars if pd.notnull(row[y]) and row[y] != ''], default=None), axis=1)
        df['InternetUse'] = df.apply(lambda row: row[row['latest_year']] if row['latest_year'] else None, axis=1)
        df_map = df[['Country Name', 'Country Code', 'InternetUse']].copy()
        df_map['Year'] = df['latest_year']
    else:
        year = str(year)
        df_map = df[['Country Name', 'Country Code', year]].copy()
        df_map = df_map.rename(columns={year: 'InternetUse'})
        df_map['Year'] = year
    df_map['InternetUse'] = pd.to_numeric(df_map['InternetUse'], errors='coerce')
    # Ensure 'Year' is numeric and replace None/empty with np.nan
    df_map['Year'] = pd.to_numeric(df_map['Year'], errors='coerce')

    # Load world geometry
    world = gpd.read_file('Grundlagen_Info/07_Netzwerke/Skript/Code/Files/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp')
    # Remove Antarctica
    world = world[~world['iso_a3'].str.upper().isin(['ATA'])]
    # Merge on 'iso_a3' (lowercase)
    merged = world.merge(df_map, left_on='iso_a3', right_on='Country Code', how='left')

    # Plot with discrete color scheme (10 classes)
    import matplotlib.colors as mcolors

    # Define 10 bins for Internet use percentages
    bins = np.linspace(0, 100, 11)
    merged['InternetUse_binned'] = pd.cut(merged['InternetUse'], bins=bins, include_lowest=True)

    # Use a discrete colormap with 10 classes
    cmap = plt.get_cmap('RdYlGn', 10)
    norm = mcolors.BoundaryNorm(bins, ncolors=cmap.N)
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    # Plot the map
    merged.plot(column='InternetUse', ax=ax,
                legend=False,  # We'll add the colorbar below
                missing_kwds={"color": "lightgrey", "label": "Keine Daten"},
                cmap=cmap, norm=norm, edgecolor='black', linewidth=0.2)

    # Remove axis and whitespace around the map
    ax.set_axis_off()
    ax.margins(0)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    fig.tight_layout(pad=0)
    
    # Create a colorbar axis below the map
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('bottom', size='5%', pad=0.5)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, cax=cax, orientation='horizontal', boundaries=bins, ticks=bins, format='%.0f')
    cbar.set_label('% Zugang zum Internet')
    plt.tight_layout(pad=0)
    max_year = df_map["Year"].max()
    plt.savefig(f"Grundlagen_Info/07_Netzwerke/Figures/internet_use_map_{max_year:.0f}.pdf", format='pdf', bbox_inches='tight', pad_inches=0)

if __name__ == "__main__":
    plot_internet_use_by_income_class()
    plot_world_map_internet_use()


