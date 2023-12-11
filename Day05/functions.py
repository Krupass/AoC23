def e2e(value, field):
    for record in field:
        last = int(record[0])
        first = int(record[1])
        range = int(record[2])
        if(int(value) >= first and int(value) < (first + range)):
            ret = (int(value) - first) + last
            return ret
    return int(value)
