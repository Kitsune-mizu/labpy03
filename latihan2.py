modal_awal = 100000000
laba = 0
total_laba = 0

# Bulan 1 & 2: Belum ada laba
for bulan in range(1, 3):
    print(f"laba bulan ke- {bulan} sebesar: {laba}")
# Bulan 3: Laba 1%
laba = 0.1 * modal_awal
print(f"laba bulan ke- 3 sebesar: {laba}")
total_laba += laba

# Bulan 4: Laba 1%
print(f"laba bulan ke- 4 sebesar: {laba}")
total_laba += laba

# Bulan 5 - 7: Laba 5%
laba = 0.5 * modal_awal
for bulan in range(5, 8):
    print(f"laba bulan ke- {bulan} sebesar: {laba}")
    total_laba += laba
# Bulan 8: Laba 3%
laba = 0.3 * modal_awal
print(f"laba bulan ke- 8 sebesar: {laba}")
total_laba += laba

print(f"Total laba adalah: {total_laba}")
