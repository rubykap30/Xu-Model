#XU MODEL NO SCARCITY
import random

def generatePerson():
    person = {'Gender':getGender(), 'Race':getRace(), 'Town':getTown()}
    return person

def getGender():
    p = random.random()
    if p < .5:
        return 'Male'
    else:
        return 'Female'

def getRace():
    p = random.random()
    if p < .636:
        return 'White'
    elif p < .731:
        return 'Black'
    elif p < .804:
        return 'Asian'
    elif p < .991:
        return 'Hispanic'
    else:
        return 'American Indian'

def getTown():
    p = random.random()
    if p < .2:
        return 1
    elif p < .4:
        return 2
    elif p < .6:
        return 3
    elif p < .8:
        return 4
    else:
        return 5

totalCVS = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
totalWalgreens = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
totalRiteAid = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
population = {'White': 0.593, 'Black': 0.136, 'Asian':0.061, 'Hispanic':0.189, 'American Indian':0.013}


for n in range(100):
    suppliers = {'CVS':300, 'Walgreens':500, 'RiteAid':200}
    totalCount = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
    cvs = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
    walgreens = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
    riteaid = {'White':0, 'Black':0, 'Asian':0, 'Hispanic':0, 'American Indian':0}
    for i in range(5000):
        human = generatePerson()
        ratio = totalCount[human['Race']]/1000
        if human['Town'] == 1 or human['Town'] == 2:
            if random.random() < .5:
                if suppliers['CVS'] != 0 and ratio <= population[human['Race']]:
                    totalCount[human['Race']] +=1
                    suppliers['CVS'] -= 1
                    race = human['Race']
                    match race:
                        case 'White':
                            cvs['White'] += 1
                        case 'Black':
                            cvs['Black'] += 1
                        case 'Asian':
                            cvs['Asian'] += 1
                        case 'Hispanic':
                            cvs['Hispanic'] += 1
                        case 'American Indian':
                            cvs['American Indian'] += 1
            else:
                if suppliers['Walgreens'] != 0 and ratio <= population[human['Race']]:
                    totalCount[human['Race']] +=1
                    suppliers['Walgreens'] -= 1
                    race = human['Race']
                    match race:
                        case 'White':
                            walgreens['White'] += 1
                        case 'Black':
                            walgreens['Black'] += 1
                        case 'Asian':
                            walgreens['Asian'] += 1
                        case 'Hispanic':
                            walgreens['Hispanic'] += 1
                        case 'American Indian':
                            walgreens['American Indian'] += 1
        elif human['Town'] == 3:
            if suppliers['Walgreens'] != 0 and ratio <= population[human['Race']]:
                totalCount[human['Race']] +=1
                suppliers['Walgreens'] -= 1
                race = human['Race']
                match race:
                    case 'White':
                        walgreens['White'] += 1
                    case 'Black':
                        walgreens['Black'] += 1
                    case 'Asian':
                        walgreens['Asian'] += 1
                    case 'Hispanic':
                        walgreens['Hispanic'] += 1
                    case 'American Indian':
                        walgreens['American Indian'] += 1
        else:
            if random.random() < .5:
                if suppliers['Walgreens'] != 0 and ratio <= population[human['Race']]:
                    totalCount[human['Race']] +=1
                    suppliers['Walgreens'] -= 1
                    race = human['Race']
                    match race:
                        case 'White':
                            walgreens['White'] += 1
                        case 'Black':
                            walgreens['Black'] += 1
                        case 'Asian':
                            walgreens['Asian'] += 1
                        case 'Hispanic':
                            walgreens['Hispanic'] += 1
                        case 'American Indian':
                            walgreens['American Indian'] += 1
            else:
                if suppliers['RiteAid'] != 0 and ratio <= population[human['Race']]:
                    totalCount[human['Race']] +=1
                    suppliers['RiteAid'] -= 1
                    race = human['Race']
                    match race:
                        case 'White':
                            riteaid['White'] += 1
                        case 'Black':
                            riteaid['Black'] += 1
                        case 'Asian':
                            riteaid['Asian'] += 1
                        case 'Hispanic':
                            riteaid['Hispanic'] += 1
                        case 'American Indian':
                            riteaid['American Indian'] += 1
    for key in cvs:
        totalCVS[key] += cvs[key]/300
    for key in walgreens:
        totalWalgreens[key] += walgreens[key]/500
    for key in riteaid:
        totalRiteAid[key] += riteaid[key]/200
print("XU ALGORITHM")
print("-----STATS-----\n")
print("CVS")
for key in totalCVS:
    print("% of " + key + " Population Vaccinated: " + "{0:.3f}".format(totalCVS[key]/100))
print("\nWalgreens")
for key in totalWalgreens:
    print("% of " + key + " Population Vaccinated: " + "{0:.3f}".format(totalWalgreens[key]/100))
print("\nRiteAid")
for key in totalRiteAid:
    print("% of " + key + " Population Vaccinated: " + "{0:.3f}".format(totalRiteAid[key]/100))
print("\nAverage Vaccines Distributed Amongst Race:")
for key in totalCVS:
  print(key + ": " + "{0:.3f}".format((totalCVS[key] + totalWalgreens[key] + totalRiteAid[key])/3) + "%")

'''
Average Vaccines Distributed Amongst Race:
White: 62.478%
Black: 9.467%
Asian: 6.733%
Hispanic: 20.111%
American Indian: 1.211%
'''
