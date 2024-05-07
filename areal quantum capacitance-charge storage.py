import datetime
import calendar
authors = ["Maryam Masoudi", "Fatemeh Shirvani", "Aliasghar Shokri", "M.S. Akhoundi Khezrabad" ]
print("Authors:")
for author in authors:
    print("- " + author)
print("Year:", 2024)
month_number = 5
month_name = calendar.month_name[month_number]
print("Month:", month_name)
import numpy as np
import pandas as pd
e = 1.6 * (10 ** -19)
T = 300
KbT = (1.38 * T) / 16000  # ev
path_E = input("Enter the path to the E.txt file: ")
path_dos = input("Enter the path to the dos.txt file: ")
surface = float(input("Please put the value of surface (the lattice constants should be considered in Angstrom): "))
A = pd.read_csv(path_E, header=None).values
B = pd.read_csv(path_dos, header=None).values
V_values = np.arange(-1, 1.005, 0.005)
df_V = pd.DataFrame(columns=['V'])
df_CQ = pd.DataFrame(columns=['CQ'])
df_q = pd.DataFrame(columns=['q'])
for V in V_values:
    S = 1 / np.cosh((A - V) / (2 * KbT))
    CQ = np.sum(B * (S ** 2) * (A[1, 0] - A[0, 0]), axis=0)
    CQ = e * 10 ** 22 / (4 * KbT * surface) * CQ
    qq = CQ * V
    df_V.loc[len(df_V)] = V
    df_V.columns = ['V(Volt)']
    df_CQ.loc[len(df_CQ)] = CQ
    df_CQ.columns = ['CQ (µF/cm²)']
    df_q.loc[len(df_q)] = qq
    df_q.columns = ['q (µC/cm²)']
epsilon = 1e-10
df_V.loc[np.abs(df_V['V(Volt)']) < epsilon, 'V(Volt)'] = 0
df_CQ.loc[np.abs(df_CQ['CQ (µF/cm²)']) < epsilon, 'CQ (µF/cm²)'] = 0
df_q.loc[np.abs(df_q['q (µC/cm²)']) < epsilon, 'q (µC/cm²)'] = 0
df_V.to_csv('V.txt', index=False)
df_CQ.to_csv('CQ.txt', index=False)
df_q.to_csv('q.txt', index=False)