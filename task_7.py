import json

with open('7.json', 'w') as fw:
    with open('old7.txt', encoding='utf-8') as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        print(profit)
        #result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]
        print(result)
    #json.dump(result, fw, ensure_ascii=False, indent=5)