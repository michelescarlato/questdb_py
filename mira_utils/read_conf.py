import configparser

def read_conf(conf_file):
    config = configparser.ConfigParser()
    config.read(conf_file)
    config.sections()
    # Store the URL of your InfluxDB instance
    my_url = config['questdb.parameters']['url']
    secs_interval = config['questdb.parameters']['secs_interval']

    return my_url, secs_interval #my_bucket, my_org, my_token,