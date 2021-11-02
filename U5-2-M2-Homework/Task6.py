def csMaxNumberOfLambdas(text):
    lambdaFrequency = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0, 'a': 0}
    counts = []
    for eachLetter in text:
        if eachLetter in lambdaFrequency:
            lambdaFrequency[eachLetter] += 1
    for (key, value) in lambdaFrequency.items():
        counts.append(value)
    result = min(counts)
    return result

print(csMaxNumberOfLambdas("mbxcdatlas"))
print(csMaxNumberOfLambdas("lalaaxcmbdtsumbdav"))
print(csMaxNumberOfLambdas("sctlamb"))