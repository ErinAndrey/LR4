import json

def sum_product(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    total_sum = 0
    for item in data:
        score = item['score']
        weight = item['weight']
        product = score * weight
        total_sum += product

    return total_sum

