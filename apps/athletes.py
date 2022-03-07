
from typing import Optional, Union
import click
import csv
from athlete import Athlete


def validate_filters(raw_filters: str) -> Optional[dict[int, bool]]:
    try:
        int(raw_filters)
    except:
        print("Filters must only contain integers")
        return False

    filters: dict[int, bool] = {}
    
    for raw_filter in raw_filters:
        filter = int(raw_filter)
        if 5 >= filter >= 1:
            filters[filter] = True
    return filters

def read_csv_athletes() -> list[Athlete]:
    athletes: list[Athlete] = []

    with open("./data/athlete_events.csv", newline='') as csvfile:
        raw_athletes = csv.reader(csvfile)
        raw_athletes.__next__() # Remove the column names

        for line, raw_athlete in enumerate(raw_athletes):
            try:
                athletes.append(Athlete.create_athlete(raw_athlete))
            except:
                pass
                print(f"ERROR: csvfile line {line}: invalid format")

    return athletes
            

@click.command()
def main():
    init_prompt = """
    Please enter the number of filters you want to use (e.g. 234 to filter by age, team, year):
        1. Sex
        2. Age
        3. Team
        4. Year
        5. Sport
    """
    while True:
        raw_filters = click.prompt(text=init_prompt, type=str)
        if filters := validate_filters(raw_filters):
            break
    print(f"Filters {[key for key in filters]} set.")

    filter_specs: dict[int, Union[int, str]] = {}

    for filter in filters:
        match filter:
            case 1:
                filter_specs[1] = click.prompt(text="Enter sex", type=click.Choice(["M", "F"]))
            case 2:
                filter_specs[2] = click.prompt(text="Enter age", type=int)
            case 3:
                filter_specs[3] = click.prompt(text="Enter team", type=str)
            case 4:
                filter_specs[4] = click.prompt(text="Enter year", type=int)
            case 5:
                filter_specs[5] = click.prompt(text="Enter sport", type=str)

    print(filter_specs)
    
    athletes: list[Athlete] = read_csv_athletes()
    Athlete.plot_weight_data([athlete for athlete in athletes if athlete.apply_filter(filter_specs)])


if __name__ == "__main__":
    main()
    #athletes = read_csv_athletes()
    #print(len(athletes))