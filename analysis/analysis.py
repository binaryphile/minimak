def to_dict(cell):
    return dict(zip(cell.vertical, Cell(cell.row, cell.col + 1).vertical))

def sum_freq(letters, freqs):
    return sum([freqs[letter] for letter in letters])

def sum_cells(locs, freqs):
    for loc in locs:
        cell = Cell(loc)
        Cell(cell.row, cell.col + 1).value = sum_freq(cell.value, freqs)

def sweet_spot():
    freqs = to_dict(Cell('d1'))
    freqs[';'] = 0
    locs = ['g45', 'g46', 'g49', 'g50', 'g51', 'g52', 'j49', 'j50', 'j51', 'j52']
    sum_cells(locs, freqs)

def row_jumps():
    left_upper = CellRange('g41:k41')
    left_lower = CellRange('g43:k43')
    right_upper = CellRange('l41:p41')
    right_lower = CellRange('l43:m43')

    pairs = to_dict(Cell('a1'))

    results = union_(left_upper.value, left_lower.value, pairs)
    results += union_(right_upper.value, right_lower.value, pairs)
    results.sort(reverse=True)
    names = [result[1] for result in results]
    freqs = [result[0] for result in results]
    Cell('m46').vertical = names
    Cell('n46').vertical = freqs

def union_(first, second, pairs):
    result = []
    for one in first:
        for two in second:
            pair = [one, two]
            pair.sort()
            pair = ''.join(pair)
            if pair in pairs:
                result += [(pairs[pair], pair)]
    return result

sweet_spot()
row_jumps()
