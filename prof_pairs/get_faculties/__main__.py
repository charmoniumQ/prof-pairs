import json
from prof_pairs import get_faculties

faculties = get_faculties.get_faculties()
print(json.dumps(list(faculties)))
