import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import tkinter as tk

#This is for the evaluate the most possible smeell detected.
def Flower(rose, lily, margaret, air):
    highest = rose
    name = 'Rose'

    if lily > highest:
        highest = lily
        name = 'Lily'

    if margaret > highest:
        highest = margaret
        name = 'Margaret'

    if air > highest:
        highest = air
        name = 'Air'

    #print("The highest value is:", highest)
    return name, highest


rose1 = 10
lily1 = 20
margaret1 = 15
air1 = 30

# Call the Flower function
flower_name, highest_value = Flower(rose1, lily1, margaret1, air1)

# Access the returned values
print("The highest flower is:", flower_name)
print("The highest value is:", highest_value)


plt.style.use('ggplot')
subjects=['Rose','Lily','Margaret','Air']
flower=[60,40,68,94]

angles=np.linspace(0,2*np.pi,len(subjects), endpoint=False)
print(angles)

angles=np.concatenate((angles,[angles[0]]))
print(angles)

subjects.append(subjects[0])
flower.append(flower[0])

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
#basic plot
ax.plot(angles,flower, 'o--', color='g', label='Flower')
#fill plot
ax.fill(angles, flower, alpha=0.25, color='g')
#Add labels
ax.set_thetagrids(angles * 180/np.pi, subjects)
plt.grid(True)
plt.tight_layout()
plt.legend()


plt.text(0,0,'Temperature is 30 degree',fontsize=12)
plt.show()

