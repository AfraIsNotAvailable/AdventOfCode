def part1(file_txt):
    file_txt = open(file_txt, 'r')
    diff_sum = 0
    first = []
    second = []
    for line in file_txt:
        numbers = line.split()
        first.append(int(numbers[0]))
        second.append(int(numbers[1]))

    first.sort()
    second.sort()

    for i in range(len(first)):
        diff_sum += abs(first[i] - second[i])
    return first, second

def part2(file_txt):
    first, second = part1(file_txt)
    similarity = 0
    for e in first:
        similarity += e * second.count(e)

    print(similarity)

if __name__ == '__main__':
    part2("input")