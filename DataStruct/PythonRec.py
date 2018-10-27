def recmc(coinvaluelist, change):
    mincoins = change
    if change in coinvaluelist:
        return 1
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + recmc(coinvaluelist, change - i)
            if numcoins < mincoins:
                mincoins = numcoins
    return mincoins


def recDC(coinvaluelist, change, knowResults):
    mincoins = change
    if change in coinvaluelist:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + recDC(coinvaluelist, change - i, knowResults)
            if numcoins < mincoins:
                mincoins = numcoins
            knowResults[change] = mincoins
    return mincoins


def dpmakechange(coinvaluelist, change, mincoins, coinsused):
    for cents in range(change + 1):
        coincount = cents
        newcoin = 1
        for j in [c for c in coinvaluelist if c <= cents]:
            if mincoins[cents - j] + 1 < coincount:
                coincount = mincoins[cents - j] + 1
                newcoin = j
        mincoins[cents] = coincount
        coinsused[cents] = newcoin
    return mincoins[change]


def printcoins(coinsused, change):
    coin = change
    while coin > 0:
        thiscoin = coinsused[coin]
        print(thiscoin)
        coin = coin - thiscoin
