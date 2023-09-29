from functions import functions

def data_processing():
    tab = functions.clear_input("input.txt", " ")
    return {tab[i][0]: {'speed': int(tab[i][3]), 'duration': int(tab[i][6]), 'resting_time': int(tab[i][-2]), 'time_to_go' : 1} for i in range(len(tab))}


def ex14():
    reindeers = data_processing()
    distances = {key: 0 for key in reindeers.keys()}
    points = {key: 0 for key in reindeers.keys()}

    for clock in range(1, 2504):
        for renne in reindeers.keys():
            if reindeers[renne]['time_to_go'] + reindeers[renne]['duration'] > clock >= reindeers[renne]['time_to_go']:
                distances[renne] += reindeers[renne]['speed']
            elif clock == reindeers[renne]['time_to_go'] + reindeers[renne]['duration']:
                reindeers[renne]['time_to_go'] += reindeers[renne]['resting_time'] + reindeers[renne]['duration']

        for renne in reindeers.keys():
            if distances[renne] == max(distances.values()):
                points[renne] += 1
    return max(distances.values()), max(points.values())



def ex15();
    