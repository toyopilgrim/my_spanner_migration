from google.cloud import spanner
import settings

spanner_client = spanner.Client()
# Write the target table
table = settings.TBL_NAME
src_instance = spanner_client.instance(settings.SRC_INSTANCE_ID)
src_database = src_instance.database(settings.SRC_DATABASE)

columns = []
with src_database.snapshot() as snapshot:
    results = snapshot.execute_sql("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = @tableName", 
    params = {"tableName": table}, param_types={"tableName": spanner.param_types.STRING},)
    for row in results:
        columns.append(row[0])

output ='{ \n'
output += '  [\n'

with src_database.snapshot() as snapshot:
    # Wirte where statement for the target table   
    where = "WHERE exampleId = '1234'"
    results = snapshot.execute_sql("SELECT * FROM " + table + " " + where,
        params = {"tableName": table}, param_types={"tableName": spanner.param_types.STRING},)
    for row in results:
        output += '    { \n'
        for i in range(len(columns)):
            kv = '      ' + str(columns[i]) + ' : ' + str(row[i]) + ', \n'
            output += kv
        output += '    }, \n'
output += '  ]\n'
output += '}'

print(output)
f = open("output/json_gen.txt",'w')
f.write(output)
