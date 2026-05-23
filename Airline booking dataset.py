# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# %%
df = pd.read_csv(r"C:\Users\india\OneDrive\Desktop\customer_booking.csv", encoding='latin1')
# %%
df.head()

# %%
print(df.shape)
# %%
df.info(0)
# %%
df.describe()
# %% [markdown]
# ## if copmay want only India custmar
# %%
japan = df[df['booking_origin'] == 'Japan']
print (japan.head)
# %%
df['booking_origin']
# %%
df["num_passengers"]
# %%
df["flight_day"]
# %%
df['booking_origin'] == 'japan'
# %%
india[['num_passengers', 'flight_day']]
# %%
japan [['num_passengers', 'flight_day']]
# %% [markdown]
# ##Jin customers ne extra baggage liya
# 
# %%
bag = df[df['wants_extra_baggage'] == 1]

print(bag.head())
# %%
df['wants_extra_baggage']
# %%
df['wants_in_flight_meals']
# %% [markdown]
# ##RoundTrip customers count
# %%
df['trip_type']
# %%
##Sabse jyada booking kis country se hui?
# %%
df['booking_origin'].value_counts().head(10)
# %% [markdown]
# ##Average flight duration kya h
# %%
df['flight_duration'].mean()
# %%
## which day max filight
# %% [markdown]
# 
# %%
df['flight_day'].value_counts()
# %%
##GroupBy
 Country wise average passengers
1st we do groupy by booking_orginal
# %%
df.groupby('booking_origin')['num_passengers'].mean()
# %%
###Trip type wise booking complete %

# %%
df.groupby("trip_type") ['booking_complete'].mean()
# %%
df['flight_day'].value_counts().plot(kind='bar')

plt.xlabel("Day")
plt.ylabel("Bookings")

plt.show()
# %%
df['booking_complete'].value_counts().plot(kind='pie', autopct='%1.1f%%')

plt.show()
# %%

# %% [markdown]
# 
# %%
