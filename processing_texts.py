import datetime
from datetime import datetime as dt


# full count: 39 789 519

# c 14 июня 2018
# по 15 июля 2018

def write_texts_to_file(filename, texts):
    f = open(filename, 'w')

    for i in texts:
        f.write(i + '\n')

    f.close()

def read_file():
    first = True

    count_all = 0

    datetime_set = {}

    queries_start = []
    queries_middle = []
    queries_end = []

    # todo: по хорошему надо прочитать как csv и pandas-ом отфильтровать по дате

    with open("football") as infile:
        for line in infile:
            if first:
                first = False
                continue

            count_all += 1

            line_splitted = line.replace('\n', '').split('\t')

            query = line_splitted[0]
            datetime_var = line_splitted[-1]

            if not datetime_var in datetime_set:
                datetime_set[datetime_var] = None

            datetime_object = dt.strptime(datetime_var, '%Y-%m-%d %H:%M:%S')

            if datetime_object <= datetime_start_1:
                queries_start.append(query)
            elif datetime_object <= datetime_end_0:
                queries_middle.append(query)
            elif datetime_object <= datetime_end_1:
                queries_end.append(query)
            else:
                print (datetime_object)
                print('no one, check you clauses')

            if count_all % 10000 == 0:
                print(count_all, len(datetime_set))

    print(len(queries_start))
    print(len(queries_middle))
    print(len(queries_end))

    write_texts_to_file('./data/queries_start', queries_start)
    write_texts_to_file('./data/queries_middle', queries_middle)
    write_texts_to_file('./data/queries_end', queries_end)

    datetime_set = sorted(datetime_set.keys())
    print('full: ' + str(count_all))
    print(datetime_set[0], datetime_set[-1])


datetime_start_0 = datetime.datetime(2018, 6, 14)
# start
datetime_start_1 = datetime.datetime(2018, 6, 24)
# middle
datetime_end_0 = datetime.datetime(2018, 7, 5)
# end 1 день для правильного условия
datetime_end_1 = datetime.datetime(2018, 7, 16)

if __name__ == "__main__":
    data = read_file()
