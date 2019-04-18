from nltk.corpus import stopwords

nltk_stop_words = list(stopwords.words('english'))
nltk_stop_words += list(stopwords.words('russian'))


# todo: stemming, lemming
def read_queries(filename, need_split=False, need_remove_stop_words=False, max_count=None):
    queries = []

    num = 0

    with open("./data/" + filename) as infile:
        for line in infile:
            line = line.replace('\n', '')

            if need_remove_stop_words:
                s_splitted_line = line.split()
                s_splitted_line = [i for i in s_splitted_line if i not in nltk_stop_words]

                if need_split:
                    queries.append(s_splitted_line)
                else:
                    queries.append(' '.join(s_splitted_line))
            else:
                if need_split:
                    queries.append(line.split())
                else:
                    queries.append(line)

            num += 1

            if num % 100000 == 0:
                print(num)

            if max_count is not None:
                if max_count == num:
                    break

    print(' ')

    return queries


def write_queries(filename, queries):
    f = open("./data/" + filename, 'w')

    for i in queries:
        f.write(i + '\n')

    f.close()
