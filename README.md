# uni-assignment-2021-22-number-2
## To start using the applications

Prerequisite:
 - python 3.10 or above
 - poetry

1. Pull the repository from github

1. Initialise the environment
   ```
   poetry env use /usr/local/opt/python@3.10/bin/python3
   ```

1. Connect to the environment
   ```
   source <environment_path>/bin/activate
   ```

1. Install dependencies
   ```
   poetry isntall
   ```

1. Download athlete data (https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results?select=athlete_events.csv) and put it into data folder

1. Run any of the three applications
    ```
    python3 apps/hybrid_sort.py
    ```

    ```
    python3 apps/image_filter.py
    ```

    ```
    python3 apps/athletes.py
    ```