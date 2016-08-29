months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

acro = dict((m[:3].lower(), m) for m in months)


def valid_month(month):
    if month:
        return acro.get(month[:3].lower())


def valid_day(day):
    if day.isdigit():
        if 0 < int(day) < 32:
            return int(day)
    return None


def valid_year(year):
    if year.isdigit():
        if 1900 <= int(year) < 2020:
            return int(year)
    return None
