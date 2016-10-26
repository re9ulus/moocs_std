# python2

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[] for i in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(raw_input().split())

    def index(self, arr, elem):
        try:
            ind = arr.index(elem)
        except ValueError:
            ind = -1
        return ind

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.elems[query.ind])
        else:
            hash_value = self._hash_func(query.s)
            if query.type == 'find':
                self.write_search_result(self.index(self.elems[hash_value], query.s) != -1)
            elif query.type == 'add':
                if self.index(self.elems[hash_value], query.s) == -1:
                    self.elems[hash_value].insert(0, query.s)
            else: # pop
                ind = self.index(self.elems[hash_value], query.s)
                if ind != -1:
                    self.elems[hash_value].pop(ind)

    def process_queries(self):
        n = int(raw_input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(raw_input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
