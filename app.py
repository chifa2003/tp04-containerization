import pandas as pd

# قراءة ملف الـ CSV
df = pd.read_csv('online_retail_II.csv', encoding='latin1')

print("--- تم قراءة ملف البيانات بنجاح داخل Docker! ---")
print("عدد الصفوف والأعمدة:", df.shape)
print("\nأول 5 أسطر من البيانات:")
print(df.head())