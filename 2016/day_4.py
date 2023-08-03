"""This code is dedicated to C8, without whom it could not have been written."""

"""

def extract_elements(room):
    chunks = room.split("-")
    code = "".join(chunks[:-1])  # Take the hyphens out of the name
    id, checksum = chunks[-1][:-1].split("[")  # Isolate the checksum

    return [code, id, checksum]


def is_valid_room(code: str, checksum: str) -> bool:


    # Count up the letters in the code
    counts = {}
    for c in set(code):
        counts[c] = code.count(c)

    # Sort the dict alphabetically by keys
    counts = sorted(counts.items(), key=lambda x: x[0]) # for each key:value pair, sort them ASC based on the key

    # Sort the dict in descending order by value
    counts = sorted(counts, key=lambda x: x[1], reverse=True) # for each key:value pair, sort them DESC based on the value

    # Take just the letters out of counts
    decrypted = "".join([x[0] for x in counts[:5]]) # [(a, 1), (b, 2)]

    # Check if the top five are equal to the checksum

    return decrypted == checksum


def sum_valid_sector_ids(data):

    total = 0
    for row in data:
        elements = extract_elements(row)
        if is_valid_room(elements[0], elements[2]):
            total += int(elements[1])
    return total


def load_data(filename="data.txt"):

    with open(filename) as f_obj:
        return (x.strip() for x in f_obj.readlines())


def second_star(data):
    return "Not solved"


def solution(source):
    data = load_data(source)
    print("Day 4")
    print("First star:", str(sum_valid_sector_ids(data)))
    print("Second star:", str(second_star(data)))
    print("-------------------------------------")


if __name__ == "__main__":
    solution("data.txt")
