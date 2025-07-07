import pandas as pd
import xlsxwriter

# Replace the path with the actual location of your Excel file if different
file_path = 'Grundlagen_Info/Various/Semesterplanung/schultermine_klw.xlsx'
output_path = 'Grundlagen_Info/Various/Semesterplanung/termine_nach_kw.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path, skiprows=3)

# Convert KW to int (if not already)
df['KW'] = pd.to_numeric(df['KW'], errors='coerce').astype('Int64')

# Convert Startdatum and Enddatum to datetime (DD.MM.YYYY)
df['Startdatum'] = pd.to_datetime(df['Startdatum'], format='%d.%m.%Y', errors='coerce').dt.normalize()
df['Enddatum'] = pd.to_datetime(df['Enddatum'], format='%d.%m.%Y', errors='coerce').dt.normalize()

# Helper: German weekday abbreviations
german_weekdays = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']

def weekday_short(dt):
    if pd.isnull(dt):
        return ''
    return german_weekdays[dt.weekday()]

# Instead of grouping by KW, group by the first day of the week of Startdatum
# Add a column for the first day of the week (Monday) and the corresponding KW

df = df[pd.notnull(df['Titel']) & pd.notnull(df['Startdatum'])].copy()
df['Wochentag_Mo'] = df['Startdatum'] - pd.to_timedelta(df['Startdatum'].dt.weekday, unit='D')
df['KW'] = df['Wochentag_Mo'].dt.isocalendar().week

# For entries spanning multiple weeks, make them appear in every calendar week
expanded_rows = []
for _, row in df.iterrows():
    start = row['Startdatum']
    end = row['Enddatum'] if pd.notnull(row['Enddatum']) else start
    # Generate all Mondays between start and end
    monday = start - pd.to_timedelta(start.weekday(), unit='D')
    last_monday = end - pd.to_timedelta(end.weekday(), unit='D')
    mondays = pd.date_range(start=monday, end=last_monday, freq='W-MON')
    for mo in mondays:
        expanded_rows.append({
            'Wochentag_Mo': mo,
            'KW': mo.isocalendar().week,
            'Startdatum': row['Startdatum'],
            'Titel': row['Titel']
        })
expanded_df = pd.DataFrame(expanded_rows)

# Group by week and format as before
grouped = expanded_df.groupby('Wochentag_Mo').apply(
    lambda g: ', '.join([
        f"[{german_weekdays[row['Startdatum'].weekday()]}:{str(row['Titel']).strip()}]"
        for _, row in g.iterrows()
    ])
).reset_index(name='Events')
grouped['KW'] = grouped['Wochentag_Mo'].dt.isocalendar().week

# Ensure every calendar week (KW) from min to max is present, fill missing with blank Events
min_monday = expanded_df['Wochentag_Mo'].min()
max_monday = expanded_df['Wochentag_Mo'].max()
all_mondays = pd.date_range(start=min_monday, end=max_monday, freq='W-MON')
all_kws = all_mondays.isocalendar().week
full_index = pd.DataFrame({'Wochentag_Mo': all_mondays, 'KW': all_kws})

# Merge with grouped to ensure all weeks are present
result = pd.merge(full_index, grouped, on=['Wochentag_Mo', 'KW'], how='left')
result['Events'] = result['Events'].fillna('')

# Write to Excel with partial color formatting for 'note' and 'verschiebedatum' using xlsxwriter
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    result.to_excel(writer, index=False, sheet_name='Termine')
    workbook = writer.book
    worksheet = writer.sheets['Termine']
    red_format = workbook.add_format({'font_color': 'red'})
    blue_format = workbook.add_format({'font_color': 'blue'})
    default_format = workbook.add_format({})
    for row_idx, event_str in enumerate(result['Events'], start=1):
        if any(word in event_str.lower() for word in ['note', 'verschiebedatum']):
            events = event_str.split(', ')
            rich = []
            for i, event in enumerate(events):
                event_lower = event.lower()
                if 'note' in event_lower:
                    rich.append(red_format)
                    rich.append(event)
                elif 'verschiebedatum' in event_lower:
                    rich.append(blue_format)
                    rich.append(event)
                else:
                    rich.append(default_format)
                    rich.append(event)
                if i < len(events) - 1:
                    rich.append(default_format)
                    rich.append(', ')
            worksheet.write_rich_string(row_idx, 2, *rich)
    # (Other cells remain as written by pandas)

# Display preview
print(result.head())