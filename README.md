# yacs-BI
Repo for yacs data analysis.

## Setup the Env
1. Make sure you have docker running.

2. Build images and containers.
```
$ ./scripts/init.sh
```

Wait till you see the terminal says "MongoDB configured successfully. You may now connect to the DB."

3. DB migrationg
```
$ cd ./scripts
$ ./db_migrate.sh
```

4. vola, you are all set!