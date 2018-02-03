# yacs-BI
Repo for yacs data analysis.

## Setup the Env
1. Make sure you have docker running.

2. Build images and containers.
```
$ ./scripts/init.sh
```

Wait till you see the terminal says "MongoDB configured successfully. You may now connect to the DB."

3. (If you have mongo installed)DB migration
```
$ cd ./scripts
$ ./db_migrate.sh
```
3.5 For ppl who don't have mongo installed,use this to get into the mongo container

```
$ ./exec_mongo.sh
```

4. vola, you are all set!