import src.extract_mysql as em
import src.transform_mysql as tm
import src.load_ssms as ls
import src.performance_from_mysql as pf

table_name = input('Enter table name')
df=em.extract_table(table_name)
tdata=tm.transform_data(df)
ls.load_data(tdata)
print(pf.performance())