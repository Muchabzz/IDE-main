carspeed = (input('enter car speed: '))
speedlimit = int(carspeed) >= 40 and int(carspeed) <= 140

print(f'Speed is valid: {speedlimit}')