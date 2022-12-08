import random
chance= random.randint(1,300)

if chance>=1 and chance <= 5:print("legendary")
elif chance>=6 and chance <= 20:print("epic")
elif chance>=21 and chance <= 80:print("rare")
elif chance>=81 and chance <= 150:print("uncommon")
elif chance>=151 and chance <= 300:print("common")