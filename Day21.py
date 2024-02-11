import math
def whowins(stats_player: list, stats_boss: list) -> bool:
    ttk_player = math.ceil(stats_player[0] / (stats_boss[1] - stats_player[2]))
    ttk_boss = math.ceil(stats_boss[0] / (stats_player[1] - stats_boss[2]))
    return ttk_player >= ttk_boss


weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3]]