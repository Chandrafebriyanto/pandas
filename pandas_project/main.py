import pandas as pd

df = pd.read_csv('students.csv')

print("\n5 baris pertama:")
print(df.head())

df.info()
print(df.describe())

df['status'] = ['lulus' if Grade >=80  else 'tidak lulus' for Grade in df['Grade']]
df.to_csv('student_baru.csv', index=False)
print(df)

rata_rata_grade = df['Grade'].mean
print(rata_rata_grade)

kelompok = df.groupby('status').size()
print(kelompok)

