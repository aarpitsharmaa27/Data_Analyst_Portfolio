import numpy as np
import statistics as stats

baked_food = [100,200,140,260,230,150,150]
a = np.array(baked_food)

print(np.mean(a))       # Sum of all values/ Number of total values
print(np.median(a))     # After sorting, Sum of two middle vales divide by 2
print(stats.mode(a))    # most repeating value
print(np.std(a))
print(np.var(a))        # Varience Square of SD


tobacco_consumption = [42,532,54,36,431,35,51]
Deaths = [35,161,1234,3214321,434441,512,35]
print(np.corrcoef([tobacco_consumption,Deaths]))
