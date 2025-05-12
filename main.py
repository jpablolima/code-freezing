import yaml


with open("config.yml") as f:
    config = yaml.safe_load(f)
    bypass_group = config["bypass_group"]
    freezing_dates = config["freezing_dates"]

    for period, date in freezing_dates.items():
        print(f"{period} goes from {date["from"]} unit {date["to"]}")


