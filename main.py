from google.cloud import spanner
import settings

spanner_client = spanner.Client()
table = settings.TBL_NAME
src_instance = spanner_client.instance(settings.SRC_INSTANCE_ID)
src_database = src_instance.database(settings.SRC_DATABASE)

data = []
with src_database.snapshot() as snapshot:
    results = snapshot.execute_sql("SELECT * FROM " + table)
    for row in results:
        data.append(row)
        print(row)

columns = []
with src_database.snapshot() as snapshot:
    results = snapshot.execute_sql("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = @tableName", 
    params = {"tableName": table}, param_types={"tableName": spanner.param_types.STRING},)
    for row in results:
        columns.append(row[0])

dst_instance = spanner_client.instance(settings.DST_INSTANCE_ID)
dst_database = dst_instance.database(settings.DST_DATABASE)

with dst_database.batch() as batch:
    batch.insert(
        table=table,
        columns= columns,
        values= data,
    )
