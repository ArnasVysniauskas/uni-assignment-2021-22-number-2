from dataclasses import dataclass
from enum import Enum
from typing import Optional
import matplotlib.pyplot as plt

class Sex(Enum):
    MALE = "M"
    FEMALE = "F"

class Medal(Enum):
    GOLD = "Gold"
    SILVER = "Silver"
    BRONZE = "Bronze"
    NA = "NA"

@dataclass(init=True, frozen=True)
class Athlete:
    id: int
    name: str
    sex: Sex
    age: Optional[int]
    height: Optional[int]
    weight: Optional[int]
    team: Optional[str]
    noc: Optional[str]
    games: Optional[str]
    year: Optional[int]
    season: Optional[str]
    city: Optional[str]
    sport: Optional[str]
    event: Optional[str]
    medal: Medal

    def apply_filter(self, filter_specs: dict) -> bool:
        for filter, spec in filter_specs.items():
            match filter:
                case 1:
                    if self.sex != Sex(spec):
                        return False
                case 2:
                    if self.age != spec:
                        return False
                case 3:
                    if self.team != spec:
                        return False
                case 4:
                    if self.year != spec:
                        return False
                case 5:
                    if self.sport != spec:
                        return False
        return True
    
    @classmethod
    def plot_weight_data(cls, data: list["Athlete"]):
        length_of_data_set = len(data)
        if 0 < length_of_data_set <= 100:
            x = []
            y = []
            for athlete in data:
                if athlete.weight is not None:
                    x.append(athlete.id)
                    y.append(athlete.weight)

            plt.scatter(x, y)
            plt.xlabel("ID")
            plt.ylabel("Weight, kg")
            plt.title("Scatterplot of weight")
            plt.savefig("./data/scatter.png", )

            message = f"""
            ======================================================
            {length_of_data_set} records
            File scatter.png saved
            ======================================================
            """
        elif length_of_data_set > 100:
            x = [athlete.weight for athlete in data if athlete.weight is not None]
            bins = 12

            plt.hist(x=x, bins=bins)
            plt.xlabel("Weight, kg")
            plt.ylabel("Number of athletes")
            plt.title("Histogram of weight")
            plt.savefig("./data/hist.png")

            message = f"""
            ======================================================
            {length_of_data_set} records
            File hist.png saved
            ======================================================
            """
        else:
            message = """
            ======================================================
            No athletes found on with the provided filter
            ======================================================
            """
        print(message)

    @classmethod
    def create_athlete(cls, data: list[str]) -> "Athlete":
        return Athlete(
            id = int(data[0]),
            name = data[1],
            sex = Sex(data[2]),
            age = cls.validate_age(data[3]),
            height = cls.validate_height(data[4]),
            weight = cls.validate_weight(data[5]),
            team = cls.validate_team(data[6]),
            noc = cls.validate_noc(data[7]),
            games = cls.validate_games(data[8]),
            year = cls.validate_year(data[9]),
            season = cls.validate_season(data[10]),
            city = cls.validate_city(data[11]),
            sport = cls.validate_sport(data[12]),
            event = cls.validate_event(data[13]),
            medal = Medal(data[14]),
        )
    
    @classmethod
    def validate_age(cls, age) -> Optional[int]:
        try:
            return int(age)
        except:
            return None
    @classmethod
    def validate_height(cls, height) -> Optional[int]:
        try:
            return int(height)
        except:
            return None
    @classmethod
    def validate_weight(cls, weight) -> Optional[int]:
        try:
            return int(weight)
        except:
            return None
    @classmethod
    def validate_team(cls, team) -> Optional[str]:
        if team == "NA":
            return None
        else:
            return team
    @classmethod
    def validate_noc(cls, noc) -> Optional[str]:
        if noc == "NA":
            return None
        else:
            return noc
    @classmethod
    def validate_games(cls, games) -> Optional[str]:
        if games == "NA":
            return None
        else:
            return games
    @classmethod
    def validate_year(cls, year) -> Optional[int]:
        try:
            return int(year)
        except:
            return None
    @classmethod
    def validate_season(cls, season) -> Optional[str]:
        if season == "NA":
            return None
        else:
            return season
    @classmethod
    def validate_city(cls, city) -> Optional[str]:
        if city == "NA":
            return None
        else:
            return city
    @classmethod
    def validate_sport(cls, sport) -> Optional[str]:
        if sport == "NA":
            return None
        else:
            return sport
    @classmethod
    def validate_event(cls, event) -> Optional[str]:
        if event == "NA":
            return None
        else:
            return event