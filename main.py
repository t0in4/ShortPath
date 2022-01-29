import re
def short_path():
    points = {
        "Почтовое отделение": (0, 2),
        "Ул. Бейкер стрит, 221б": (5, 2),
        "Ул. Большая Садовая, 302-бис": (6, 6),
        "Вечнозелёная Аллея, 742": (8, 3),
        "Ул. Грибоедова, 104/25": (2, 5),

    }
    paths = {}
    excludeOnes = ["Почтовое отделение"]
    shortPath = {}
    count = 0
    while (count < len(points) - 1):
        for (key, values) in points.items():
            #pdb.set_trace()
            if key in excludeOnes: continue
            paths[key] = ((values[0] - points[excludeOnes[count]][0]) ** 2 + (values[1] - points[excludeOnes[count]][1]) ** 2) ** 0.5
            # find key by minimal value
            lKey = [key for key, value in paths.items() if value == min(paths.values())][0]
        excludeOnes.append(lKey)
        shortPath[lKey] = min(paths.values())
        paths.clear()
        count += 1
    shortPath[''.join(list(points.keys())[0])] = (([value for key, value in points.items() if key == list(points.keys())[0]][0][0]
                                              - [value for key, value in points.items() if key == list(shortPath.keys())[-1]][0][0]) ** 2
                                             + ([value for key, value in points.items() if key == list(points.keys())[0]][0][1]
                                                - [value for key, value in points.items() if key == list(points.keys())[0]][0][1]) ** 2) ** 0.5

    result = f"{re.sub(r'[*]*','',convertTuple([value for key, value in points.items() if key == list(shortPath.keys())[-1]]))} " \
             f" -> {re.sub(r'[*]*','',convertTuple([value for key, value in points.items() if key == list(shortPath.keys())[0]]))}" \
             f"{[value for key, value in shortPath.items() if key == list(shortPath.keys())[0]]}" \
             f" -> {re.sub(r'[*]*','',convertTuple([value for key, value in points.items() if key == list(shortPath.keys())[1]]))}" \
             f"{[value for key, value in shortPath.items() if key == list(shortPath.keys())[1]]}" \
             f" -> {re.sub(r'[*]*','',convertTuple([value for key, value in points.items() if key == list(shortPath.keys())[2]]))}" \
             f"{[value for key, value in shortPath.items() if key == list(shortPath.keys())[2]]}" \
             f" -> {re.sub(r'[*]*','',convertTuple([value for key, value in points.items() if key == list(shortPath.keys())[3]]))}" \
             f"{[value for key, value in shortPath.items() if key == list(shortPath.keys())[3]]}" \
             f" -> {re.sub(r'[*]*','',convertTuple([value for key, value in points.items() if key == list(shortPath.keys())[4]]))}" \
             f"{[value for key, value in shortPath.items() if key == list(shortPath.keys())[4]]}" \
             f" = {sum(shortPath.values())}"
    return result
# function for converting tuple into string for re.sub
def convertTuple(tup):
    stringResult = ''.join(map(str, tup))
    return stringResult

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(short_path())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
