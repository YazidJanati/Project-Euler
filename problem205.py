#problem205


'''def distinguishableDecomp(Number,DecompIn,bounds = range(4,1,-1)):
    howMany= 0
    if DecompIn > Number :
        return 0
    if DecompIn == Number :
        return 1
    else:
        for n in bounds:
            howMany += distinguishableDecomp(Number-n,DecompIn-1,range(n,1,-1))
    return howMany

print(distinguishableDecomp(23,9))
PetersOmega = range(9,37)
ColinsOmega = range(6,37)

howManyPeter = {n: distinguishableDecomp(n,9) for n in PetersOmega}
howManyColins = {n: distinguishableDecomp(n,6,range(6,1,-1)) for n in ColinsOmega}
ColinLosesDict = {n: howManyColins[n]*sum([howManyPeter[j] for j in PetersOmega if j > n]) for n in ColinsOmega}
ColinLoses = sum([ColinLosesDict[n] for n in ColinsOmega])
NumberOfPsblties = sum([howManyColins[n] for n in ColinsOmega])*sum([howManyPeter[n] for n in PetersOmega])

print(ColinLoses/NumberOfPsblties)'''


def distinguishableDecomp(Number,DecompIn,bounds):
    howMany = 0
    if DecompIn == 2:
        for n in bounds:
            if bounds[0] <= Number - n <= bounds[-1]:
                howMany += 1
        return howMany
    else:
        for n in bounds:
            toAdd = distinguishableDecomp(Number-n,DecompIn-1,bounds)
            if toAdd == 0:
                continue
            howMany+= toAdd
    return howMany


PetersOmega = range(9,37)
ColinsOmega = range(6,37)

howManyPeter = {n: distinguishableDecomp(n,9,range(1,5)) for n in PetersOmega}
howManyColins = {n: distinguishableDecomp(n,6,range(1,7)) for n in ColinsOmega}
ColinLosesDict = {n: howManyColins[n]*sum([howManyPeter[j] for j in PetersOmega if j > n]) for n in ColinsOmega}
ColinLoses = sum([ColinLosesDict[n] for n in ColinsOmega])
NumberOfPsblties = sum([howManyColins[n] for n in ColinsOmega])*sum([howManyPeter[n] for n in PetersOmega])

print(ColinLoses/NumberOfPsblties)
