import sys
import csv


data = {
    'Afghanistan': {
        1990: 0,
        1991: 1,
    }
}


with open('number-of-internet-users-by-country.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    count = 0

    for row in spamreader:
        count += 1
        if count == 1:
            # skip title
            continue

        if len(row) == 4:
            # print(row)
            entity, code, year, user = row

            if entity not in data:
                data[entity] = {}

            pair = data[entity]
            pair[year] = user
            # data[entity]

            # [year] = user

# data = {
#     'Afghanistan': {
#         1990: 0,
#         1991: 1,
#     }
# }


# print(data)


def get_user_by_country_year(country, year):
    return str(data[country].get(str(year), 0))

    # # for k, v in record.items():
    #     print(k, v)
    #     row += 1
    #     if row == 5:
    #         break

header = ','.join(['year'] + list(data.keys()))
lines = [header]
for year in range(2000, 2016 + 1):
    # line = [v[year] for k, v in data.items() if year in v]
    # line = get_user_by_country_year('Afghanistan', year)
    line_parts = [str(year)] + [get_user_by_country_year(country, year)
                                for country in data.keys()]
    # print(line_parts)
    lines.append(','.join(line_parts))

print(*lines, sep='\n')
with open('out.csv', 'w') as fw:
    fw.write('\n'.join(lines))
