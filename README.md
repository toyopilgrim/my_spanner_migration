# my_spanner_migration

This tool is to migrate Spanner data to another table having the same schema spanned over two different instances/databases in a GCP project.

#### Setup

Install dependencies.
```
pip install -r requirements.txt
```

Create your own .env file in the current directory.
```
SRC_INSTANCE_ID=original-instance
SRC_DATABASE=original-database
DST_INSTANCE_ID=another-instance
DST_DATABASE=your-own-database
TBL_NAME=SampleTable
```

### Run

```
python main.py
```