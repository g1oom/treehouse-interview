def computeLayer(x):
    if x == 1:
        return [1]
    elif x == 2:
        return [1, 1]
    else:
        previousLayer = computeLayer(x - 1)
        newLayer = [1]
        for i in range(len(previousLayer) - 1):
            newLayer.append(previousLayer[i] + previousLayer[i + 1])
        newLayer.append(1)
        return newLayer

def main():
    n = int(input("Which layer?"))
    print(computeLayer(n))

main()