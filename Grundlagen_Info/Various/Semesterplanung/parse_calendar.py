"""
This script downloads an ICS calendar file from a specified URL,
parses it, and exports the events to a multi-sheet Excel file:
- One sheet per class
- Rows: calendar weeks (KW)
- Columns: lessons (extracted from SUMMARY or time slot)
- Cell: event description
"""

import requests
import pandas as pd
from icalendar import Calendar
from datetime import datetime, timedelta
import re

# Download the ICS file
url = "https://intranet.tam.ch/klw/rest/ics/type/timetable/date/1688045566/auth/gr001%40Y3lyaWwud2VuZGw=%3ANTQ2MTNhODk5YTAzMjVjNzg1Y2Q4MDQ0ZTlkZGUyYTkwNzZlYTIzOA==/calendar.ics"
response = requests.get(url)
response.raise_for_status()

# Parse the ICS file
cal = Calendar.from_ical(response.content)

# Prepare event list
events = []
for component in cal.walk():
    if component.name == "VEVENT":
        summary = str(component.get("SUMMARY", ""))
        dtstart = component.get("DTSTART").dt
        dtend = component.get("DTEND").dt
        location = str(component.get("LOCATION", ""))
        description = str(component.get("DESCRIPTION", ""))
        # Normalize dates (remove time for all-day events)
        if isinstance(dtstart, datetime):
            start_date = dtstart.date()
        else:
            start_date = dtstart
        if isinstance(dtend, datetime):
            end_date = dtend.date()
        else:
            end_date = dtend
        # Extract class (e.g. 1g, 2d, etc.) from summary
        m = re.search(r"[1-4][a-z]", summary)
        klasse = m.group(0) if m else "Alle"
        # Extract lesson (e.g. 1h, 2d, 3./4. Lektion, or time)
        # For Halbklassen, add label like 2d%1 instead of just 1/2
        m2 = re.search(r"([1-9])%([12])", summary)
        if m2 and klasse != "Alle":
            lesson = f"{klasse}%{m2.group(2)}"
        else:
            m3 = re.search(r"\b[1-9][a-z]?\b", summary)
            lesson = m3.group(0) if m3 else "-"
        # For events spanning multiple days, add for each week
        current = start_date
        while current <= end_date:
            monday = current - timedelta(days=current.weekday())
            kw = monday.isocalendar()[1]
            events.append({
                "KW": kw,
                "Woche": monday,
                "Klasse": klasse,
                "Lektion": lesson,
                "Event": summary,
                "Datum": current,
                "Ort": location,
                "Beschreibung": description
            })
            # Next week
            current += timedelta(days=7 - current.weekday())

# In DataFrame
df = pd.DataFrame(events)

# Pivot: one sheet per class, rows=KW, columns=Lektion, cell=Event (join if multiple)
with pd.ExcelWriter("Grundlagen_Info/Various/Semesterplanung/events_by_class.xlsx") as writer:
    for klasse in sorted(df['Klasse'].unique(), key=lambda x: (x == 'Alle', x)):
        tab_name = 'Andere' if klasse == 'Alle' else klasse
        sub = df[df['Klasse'] == klasse]
        # Pivot table: index=KW, columns=Lektion, values=Event
        pivot = sub.pivot_table(index=['KW', 'Woche'], columns='Lektion', values='Event', aggfunc=lambda x: '\n'.join(x), fill_value='')
        # Sort by KW
        pivot = pivot.sort_index()
        pivot.to_excel(writer, sheet_name=tab_name)

print("Exported events by class to events_by_class.xlsx")