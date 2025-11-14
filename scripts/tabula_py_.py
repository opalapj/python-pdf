import locale
from pathlib import Path

import pandas as pd
import tabula


pd.options.mode.copy_on_write = True


def main():
    filepath = Path("data/Kalendarz_RTPE_na_rok_2024.pdf")
    dt_names = [
        "trade_beg_date",
        "trade_end_date",
        "real_beg_date",
        "real_end_date",
    ]
    names = [
        "contract",
        "hours",
        *dt_names,
    ]
    pandas_options = {"names": names}
    tables = tabula.read_pdf(
        input_path=filepath,
        pages="all",
        multiple_tables=False,
        pandas_options=pandas_options,
    )
    table = tables[0]
    table = table.loc[table["hours"].apply(lambda x: str(x).isdigit())]
    table["hours"] = pd.to_numeric(table["hours"])
    locale.setlocale(locale.LC_TIME, "")
    for col_name in dt_names:
        col = table[col_name]
        try:
            col = pd.to_datetime(
                arg=col,
                format="%d %B %Y",
            ).dt.date
        except ValueError as e:
            print(col_name, e)
            split = col.str.split(" ", expand=True)
            invalid_years = table.loc[split[2].apply(lambda x: x is None)]
            split.loc[invalid_years.index, 2] = 2023
            col = split.apply(lambda x: " ".join(x.astype(str)), axis=1)
            col = pd.to_datetime(
                arg=col,
                format="%d %B %Y",
            ).dt.date
        table.loc[:, col_name] = col
    locale.setlocale(locale.LC_TIME, "C")
    table.to_csv(filepath.with_name("market_calendar.csv"), index=False)


if __name__ == "__main__":
    main()
