> NOTE:
>
> The project should still work as long as you have an approved API key from Riot Games and a subscription to X (twitter) API.

### What it does?
This a simple TFT rank checker, what it does is that every hour it will pull data of a given TFT player from Riot Games checking if the player has reached a given Rank once it reaches the rank it will post a Tweet to X (twitter) and also a notification to discord through webhook then it will exit, if the player hasn't reached the goal rank it will post a tweet as an update with current rank and current LP points to date.

| Values      | Meaning      |
| ------------- | ------------- |
| Division | Player Rank (eg. Diamond, Platinum, etc) |
| Div_rank | Rank division (The number after the rank eg. 4, 3 , 2 ,1) |
| LP | League Points (player ranking points) |
| Wins | Player Current Wins |
| Losses | Player Current losses |

### Usage
Create a python environment and install the requirements from `requirements.txt`

```python
python3 -m venv venv

pip install -r requirements.txt
```
### Environment Variables
Rename the `.env.example` to `.env` and put your credentials
> As stated before the Riot API KEY should be an allowed application to access the required data, and since this project was before the X (twitter) API changes now you require a subscription to their API.

### Run

```python
python3 ./rank.py
```

## FAQ
#### How do i pass the TFT player?
You pass the TFT player in the form of their summonerId you get this from the Riot Games API and put it in the `RIOT_API_URI`
