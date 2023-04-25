# questdb_py


## Docker run
To run questDB, first create a directory to mount the docker volume 
(ref: https://questdb.io/docs/get-started/docker/): 

```bash
mkdir -p questdb/location
```
Then run the docker container:
```bash
docker run -p 9000:9000 -p 9009:9009 -p 8812:8812 -p 9003:9003 -v "$HOME/questdb/location:/var/lib/questdb"  questdb/questdb:7.1.1
```

## Install dependencies

Install dependencies listed in the `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Data insertion

To run the data insertion:

```bash
python3 questdb_insert_data.py conf_april_april32gb
```

## Data fetch

To fetch inserted data:
```bash
python3 questdb_fetch_data  conf_april_april32gb
```