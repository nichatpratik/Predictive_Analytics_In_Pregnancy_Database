import matplotlib as mpl
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np 
import time
import sys
import json

X=pd.read_csv('routes/comp.csv')
X.dropna(axis = 0, how = 'any', inplace = True)
X.drop('MODE_OF_DELIVERY', axis = 1, inplace = True)
X.drop('COMPLICATIONS', axis = 1, inplace = True)


X.BLOOD_GP=X.BLOOD_GP.map({'O-': 0,'O+': 1,'A+': 2,'B+': 3,'AB+': 4,'AB-': 5,'A-': 6,'B-': 7}) 
X.PREVIOUS_LSCS=X.PREVIOUS_LSCS.map({'Y': 1,'N': 0,})
X.CONTRACTED_PELVIS=X.CONTRACTED_PELVIS.map({'Y': 1,'N': 0,})
X.AMMENORRHOEA=X.AMMENORRHOEA.map({'Y': 1,'N': 0,})
X.VOMITTING=X.VOMITTING.map({'Y': 1,'N': 0,'E': 2})
X.WEAKNESS=X.WEAKNESS.map({'Y': 1,'N': 0,})
X.PAIN_IN_ABDOMEN=X.PAIN_IN_ABDOMEN.map({'Y': 1,'N': 0,})
X.OEDEMA_FEET=X.OEDEMA_FEET.map({'Y': 1,'N': 0,})
X.LETHARGY=X.LETHARGY.map({'Y': 1,'N': 0,})
X.SPOTTING_PV=X.SPOTTING_PV.map({'Y': 1,'N': 0,})
X.HEADACHE=X.HEADACHE.map({'Y': 1,'N': 0,})
X.LEG_CRAMPS=X.LEG_CRAMPS.map({'Y': 1,'N': 0,})
X.BURNING_IN_MICTURATION=X.BURNING_IN_MICTURATION.map({'Y': 1,'N': 0,})
X.PEDAL_AND_ABDOMINAL_WALL_OEDEMA=X.PEDAL_AND_ABDOMINAL_WALL_OEDEMA.map({'Y': 1,'N': 0,})
X.HISTORY_OF_GESTATIONAL_DM=X.HISTORY_OF_GESTATIONAL_DM.map({'Y': 1,'N': 0,})
X.HISTORY_OF_HYPERTENSION=X.HISTORY_OF_HYPERTENSION.map({'Y': 1,'N': 0,})
X.EXCESSIVE_WEIGHT_GAIN=X.EXCESSIVE_WEIGHT_GAIN.map({'Y': 1,'N': 0,})
X.FEVER_WITH_COLD_AND_COUGH=X.FEVER_WITH_COLD_AND_COUGH.map({'Y': 1,'N': 0,})
X.LEAKING_PV=X.LEAKING_PV.map({'Y': 1,'N': 0,})
X.URINE=X.URINE.map({'NAD': 0,'PROTEIN+': 1,'PROTEIN++': 2,'PROTEIN+++': 3,'PROTEIN++++': 4,'KETONES+': 5,'KETONES++': 6,'KETONES+++': 7,'KETONES++++': 8,'KETONES_NIL': 9,'ALBUMIN++': 10,'BACTERIA+':11})
X.LIE=X.LIE.map({'N': 0,'T': 1,'O': 2})
X.AMNIOTIC_FLUID=X.AMNIOTIC_FLUID.map({'H': 2,'L': 1,'N': 0,})

X.dropna(axis = 0, how = 'any', inplace = True)
y = X.TREATMENT
y.fillna(0, inplace = True)
X.drop('TREATMENT', axis = 1, inplace = True)


#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 7)


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
model.fit(X,y)

#print model.oob_score_
#score = model.score(X_test, y_test)

#print(score*100)

lines = sys.stdin.readlines()

Z = json.loads(lines[0])

W = np.array(Z)
if(model.predict(W.reshape(1,-1))== 0):
	print("No Treatment As Of Now Needed")
elif(model.predict(W.reshape(1,-1))== 1):
	print("Folic Acid, Antiemetic")
elif(model.predict(W.reshape(1,-1))== 2):
	print("Iron, Calcium")
elif(model.predict(W.reshape(1,-1))== 3):
	print("Folic Acid, Iron, Calcium, Protein Supplements")
elif(model.predict(W.reshape(1,-1))== 4):
	print("Folic Acid, Iron, Calcium")
elif(model.predict(W.reshape(1,-1))== 5):
	print("Folic Acid, Diet Advice")
elif(model.predict(W.reshape(1,-1))== 6):
	print("Injectable iron, Calcium, Protein")
elif(model.predict(W.reshape(1,-1))== 7):
	print("Injection Progesterone weekly, Folic Acid")
elif(model.predict(W.reshape(1,-1))== 8):
	print("Iron, Calcium, Smooth Muscle Relexant")
elif(model.predict(W.reshape(1,-1))== 9):
	print("Folic Acid")
elif(model.predict(W.reshape(1,-1))== 10):
	print("Rest, Anti-anxiety Medication, iron, calcium")
elif(model.predict(W.reshape(1,-1))== 11):
	print("Anti-hypertensive")
elif(model.predict(W.reshape(1,-1))== 12):
	print("Need to be Admitted")
elif(model.predict(W.reshape(1,-1))== 13):
	print("IV, Glucose, Protein Supplement")
elif(model.predict(W.reshape(1,-1))== 14):
	print("Admitted, Anti-Hypertensive")
elif(model.predict(W.reshape(1,-1))== 15):
	print("Folic Acid, Injectable iron, Calcium, Protein")
elif(model.predict(W.reshape(1,-1))== 16):
	print("Os Tightening, Rest, Smooth Muscle Relaxant, Injection Progesterone")
elif(model.predict(W.reshape(1,-1))== 17):
	print("Iron,calcium,protein")
elif(model.predict(W.reshape(1,-1))== 18):
	print("Folic acid,antiemetic,IV fluids")
elif(model.predict(W.reshape(1,-1))== 19):
	print("Iron,Calcium,protein,thyroxine")
elif(model.predict(W.reshape(1,-1))== 20):
	print("Iron,Calcium,protein,dietary advice")
elif(model.predict(W.reshape(1,-1))== 21):
	print("Iron,Calcium,protein,anti diabetic medicine")
elif(model.predict(W.reshape(1,-1))== 22):
	print("Started injectable anti-diabetic")
elif(model.predict(W.reshape(1,-1))== 23):
	print("Antibiotics,antihistaminics,folic acid")
elif(model.predict(W.reshape(1,-1))== 24):
	print("Rest,Smooth muscle relaxant,injection progesterone")
elif(model.predict(W.reshape(1,-1))== 25):
	print("Folic acid,iron,calcium,IV protein,10% dextrose infusion")
elif(model.predict(W.reshape(1,-1))== 26):
	print("Rest,Folic Acid,iron,calcium,protein,Smooth muscle relaxant,injectable progesterone")
elif(model.predict(W.reshape(1,-1))== 27):
	print("Folic acid,iron,calcium,IV protein,10% dextrose infusion,antihypertensive")
elif(model.predict(W.reshape(1,-1))== 28):
	print("Rest,anti-anxiety,iron,calcium")
elif(model.predict(W.reshape(1,-1))== 29):
	print("Plenty of oral fluids,alkalizers,antibiotics,iron,calcium")
elif(model.predict(W.reshape(1,-1))== 30):
	print("Rest,Smooth muscle relaxant,injection progesterone,thyroxine")
elif(model.predict(W.reshape(1,-1))== 31):
	print("rest,injection progesterone weekly,folic acid")
