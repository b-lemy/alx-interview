from datetime import datetime

date_string = "2023-7-20"
format_string = "%Y-%m-%d"

parsed_date = datetime.strptime(date_string, format_string)
print(parsed_date)