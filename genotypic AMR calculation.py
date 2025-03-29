import pandas as pd

# ARG risk index file
df_number = pd.read_excel("risk index data.xlsx")
df_number.head()

# experimental data file
df_location = pd.read_excel("ARG_cell_number.xlsx" )
df_location.head()

# blast
df_number = df_number[['ARO Term','Human accessibility','Clinical availability','Proportion','Mobility']]
df_number.head()

df_merge = pd.merge(left=df_location, right=df_number, left_on="ARO Term", right_on="ARO Term")
df_merge.head()

# results output
df_merge.to_excel("output_blast_results.xlsx", index=False, sheet_name='Sheet1')