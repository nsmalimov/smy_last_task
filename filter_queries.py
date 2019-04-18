from helper import read_queries, write_queries

words = [
    'чемпионат',
    'чемпионату',
    'чемпионате',

    'мира',

    'футбол',
    'футболу',

    # '2018',
    'чм',
    'матчи',
    'раписание',
]

def filter_prepare(filename):
    queries_start = read_queries('original_by_time_period/' + filename,
                                 need_split=False, need_remove_stop_words=False)

    print (len(queries_start))

    choosed_queries = []

    num = 0

    for query in queries_start:
        for word in words:
            if word in query:
                choosed_queries.append(query)
                break

        if num % 10000 == 0:
            print (num)

        num += 1

    print ("num for: ", filename, len(choosed_queries))

    write_queries('filtered_prepared/' + filename, choosed_queries)

if __name__ == "__main__":
    filter_prepare('queries_start')
    filter_prepare('queries_middle')
    filter_prepare('queries_end')
