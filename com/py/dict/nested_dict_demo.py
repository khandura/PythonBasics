import pandas as pd


def create_sqad():
    squad = {
        'batsman': {
            'rohit sharma': {
                'matches': 205,
                'runs': 12045,
                'avg': 56.2},
            'virat kohli': {
                'matches': 311,
                'runs': 16145,
                'avg': 62.2},
            'kl rahul': {
                'matches': 115,
                'runs': 6145,
                'avg': 42.2}
        },
        'bowler': {
            'jasprit bumrah': {
                'matches': 110,
                'wickets': 335,
                'eco': 4.5},
            'mohammad shami': {
                'matches': 130,
                'wickets': 370,
                'eco': 5.5},
            'bhuvi kumar': {
                'matches': 90,
                'wickets': 180,
                'eco': 6.1}
        }
    }
    return squad


def lookup_on_dict(squad):
    # batsman = pd.DataFrame(squad['batsman'])
    # print('batsman list :', batsman)
    for name, profile in squad.get('batsman').items():
        print(name, profile)


sq = create_sqad()
lookup_on_dict(sq)
