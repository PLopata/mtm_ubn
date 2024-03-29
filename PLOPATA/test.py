import current_model.model as mod
import matplotlib.pyplot as plt
from scipy.stats import norm

pixel_dimenision = 75
fig_size = 40
fig_size_integral = 1800

x = mod.Model(35, pixel_dimenision, 2200)
y = mod.Model(50, pixel_dimenision, 2200)

# print(x.charge_distribution)
# print(y.charge_distribution)
P = [0] * 9
P_Noise = [0] * 9
for i in range(len(x.charge_distribution)):
    if -pixel_dimenision <= x.charge_distribution[i] < 0 and pixel_dimenision <= y.charge_distribution[i] < 2*pixel_dimenision:
        P[0] = P[0] + 1
    elif 0 <= x.charge_distribution[i] < pixel_dimenision and pixel_dimenision <= y.charge_distribution[i] < 2*pixel_dimenision:
        P[1] = P[1] + 1
    elif pixel_dimenision <= x.charge_distribution[i] < 2*pixel_dimenision and pixel_dimenision <= y.charge_distribution[i] < 2*pixel_dimenision:
        P[2] = P[2] + 1
    elif -pixel_dimenision <= x.charge_distribution[i] < 0 and 0 <= y.charge_distribution[i] < pixel_dimenision:
        P[3] = P[3] + 1
    elif 0 <= x.charge_distribution[i] < pixel_dimenision and 0 <= y.charge_distribution[i] < pixel_dimenision:
        P[4] = P[4] + 1
    elif pixel_dimenision <= x.charge_distribution[i] < 2*pixel_dimenision and 0 <= y.charge_distribution[i] < pixel_dimenision:
        P[5] = P[5] + 1
    elif -pixel_dimenision <= x.charge_distribution[i] < 0 and -pixel_dimenision <= y.charge_distribution[i] < 0:
        P[6] = P[6] + 1
    elif 0 <= x.charge_distribution[i] < pixel_dimenision and -pixel_dimenision <= y.charge_distribution[i] < 0:
        P[7] = P[7] + 1
    elif pixel_dimenision <= x.charge_distribution[i] < 2*pixel_dimenision and -pixel_dimenision <= y.charge_distribution[i] < 0:
        P[8] = P[8] + 1

# Generate noise for each pixel. Unit in electrons
for i in range(len(P_Noise)):
    P_Noise[i] = P[i] + norm.rvs(0, 50, 1)[0]

print(P)
print(P_Noise)

# Bird's eye view of a hit
plt.title(f"Bird's eye view of post hit electron collection")
plt.scatter(x.charge_distribution, y.charge_distribution, s=4)
plt.hlines(0, -75, 150, colors="black")
plt.hlines(75, -75, 150, colors="black")
plt.vlines(0, -75, 150, colors="black")
plt.vlines(75, -75, 150, colors="black")
plt.show()

# *********************************************************************************************************************
# Plots without noise
# *********************************************************************************************************************

fig, axs = plt.subplots(2, 2)
# X axis distribution
axs[0, 0].set_title(f"X axis of generated hit", size=12)
axs[0, 0].hist(x.charge_distribution, bins=len(x.pixel_coordinates))
axs[0, 0].vlines(-x.pixel_dim,    0, fig_size,   colors="black")
axs[0, 0].vlines(0,               0, fig_size,   colors="black")
axs[0, 0].vlines(x.pixel_dim,     0, fig_size,   colors="black")
axs[0, 0].vlines(2*x.pixel_dim,   0, fig_size,   colors="black")
axs[0, 0].vlines(x.real_hit,      0, fig_size/2, colors="red",   label="real hit position")
axs[0, 0].legend()
# Y axis distribution
axs[0, 1].set_title(f"Y axis of generated hit", size=12)
axs[0, 1].hist(y.charge_distribution, bins=len(y.pixel_coordinates))
axs[0, 1].vlines(-y.pixel_dim,    0, fig_size,   colors="black")
axs[0, 1].vlines(0,               0, fig_size,   colors="black")
axs[0, 1].vlines(y.pixel_dim,     0, fig_size,   colors="black")
axs[0, 1].vlines(2*y.pixel_dim,   0, fig_size,   colors="black")
axs[0, 1].vlines(y.real_hit,      0, fig_size/2, colors="red",   label="real hit position")
axs[0, 1].legend()
# X axis charge integral
axs[1, 0].set_title(f"X axis electron count integral", size=12)
axs[1, 0].bar([-x.pixel_dim, 0, x.pixel_dim], [(P[0] + P[3] + P[6]), (P[1] + P[4] + P[7]), (P[2] + P[5] + P[8])], x.pixel_dim, align='edge')
axs[1, 0].vlines(-x.pixel_dim,    0, fig_size_integral, colors="black")
axs[1, 0].vlines(0,               0, fig_size_integral, colors="black")
axs[1, 0].vlines(x.pixel_dim,     0, fig_size_integral, colors="black")
axs[1, 0].vlines(2*x.pixel_dim,   0, fig_size_integral, colors="black")
axs[1, 0].vlines(x.real_hit,      0, fig_size_integral/2, colors="red", label="real hit position")
axs[1, 0].legend()
# Y axis charge integral
axs[1, 1].set_title(f"Y axis electron count integral", size=12)
axs[1, 1].bar([-y.pixel_dim, 0, y.pixel_dim], [(P[6] + P[7] + P[8]), (P[3] + P[4] + P[5]), (P[0] + P[1] + P[2])], y.pixel_dim, align='edge')
axs[1, 1].vlines(-y.pixel_dim,    0, fig_size_integral, colors="black")
axs[1, 1].vlines(0,               0, fig_size_integral, colors="black")
axs[1, 1].vlines(y.pixel_dim,     0, fig_size_integral, colors="black")
axs[1, 1].vlines(2*y.pixel_dim,   0, fig_size_integral, colors="black")
axs[1, 1].vlines(y.real_hit,      0, fig_size_integral/2,  colors="red", label="real hit position")
axs[1, 1].legend()
# Print plots
plt.show()

# *********************************************************************************************************************
# Plots with noise
# *********************************************************************************************************************

fig, axs = plt.subplots(2, 2)
# X axis distribution
axs[0, 0].set_title(f"X axis of generated hit", size=12)
axs[0, 0].hist(x.charge_distribution, bins=len(x.pixel_coordinates))
axs[0, 0].vlines(-x.pixel_dim,    0, fig_size,   colors="black")
axs[0, 0].vlines(0,               0, fig_size,   colors="black")
axs[0, 0].vlines(x.pixel_dim,     0, fig_size,   colors="black")
axs[0, 0].vlines(2*x.pixel_dim,   0, fig_size,   colors="black")
axs[0, 0].vlines(x.real_hit,      0, fig_size/2, colors="red",   label="real hit position")
axs[0, 0].legend()
# Y axis distribution
axs[0, 1].set_title(f"Y axis of generated hit", size=12)
axs[0, 1].hist(y.charge_distribution, bins=len(y.pixel_coordinates))
axs[0, 1].vlines(-y.pixel_dim,    0, fig_size,   colors="black")
axs[0, 1].vlines(0,               0, fig_size,   colors="black")
axs[0, 1].vlines(y.pixel_dim,     0, fig_size,   colors="black")
axs[0, 1].vlines(2*y.pixel_dim,   0, fig_size,   colors="black")
axs[0, 1].vlines(y.real_hit,      0, fig_size/2, colors="red",   label="real hit position")
axs[0, 1].legend()
# X axis charge integral
axs[1, 0].set_title(f"X axis electron count integral", size=12)
axs[1, 0].bar([-x.pixel_dim, 0, x.pixel_dim], [(P_Noise[0] + P_Noise[3] + P_Noise[6]),
                                               (P_Noise[1] + P_Noise[4] + P_Noise[7]),
                                               (P_Noise[2] + P_Noise[5] + P_Noise[8])], x.pixel_dim, align='edge')
axs[1, 0].vlines(-x.pixel_dim,    -100, fig_size_integral,    colors="black")
axs[1, 0].vlines(0,               -100, fig_size_integral,    colors="black")
axs[1, 0].vlines(x.pixel_dim,     -100, fig_size_integral,    colors="black")
axs[1, 0].vlines(2*x.pixel_dim,   -100, fig_size_integral,    colors="black")
axs[1, 0].vlines(x.real_hit,      -100, fig_size_integral/2,  colors="red", label="real hit position")
axs[1, 0].hlines(0,              -x.pixel_dim, 2*x.pixel_dim, colors="black")
axs[1, 0].legend()
# Y axis charge integral
axs[1, 1].set_title(f"Y axis electron count integral", size=12)
axs[1, 1].bar([-y.pixel_dim, 0, y.pixel_dim], [(P_Noise[6] + P_Noise[7] + P_Noise[8]),
                                               (P_Noise[3] + P_Noise[4] + P_Noise[5]),
                                               (P_Noise[0] + P_Noise[1] + P_Noise[2])], y.pixel_dim, align='edge')
axs[1, 1].vlines(-y.pixel_dim,    -100, fig_size_integral,    colors="black")
axs[1, 1].vlines(0,               -100, fig_size_integral,    colors="black")
axs[1, 1].vlines(y.pixel_dim,     -100, fig_size_integral,    colors="black")
axs[1, 1].vlines(2*y.pixel_dim,   -100, fig_size_integral,    colors="black")
axs[1, 1].vlines(y.real_hit,      -100, fig_size_integral/2,  colors="red", label="real hit position")
axs[1, 1].hlines(0,              -y.pixel_dim, 2*y.pixel_dim, colors="black")
axs[1, 1].legend()
# Print plots
plt.show()