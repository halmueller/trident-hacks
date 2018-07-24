# timestamps look like {'nanosec': 542000000, 'sec': 1531965567}
def epoch_seconds(rx_ts):
    even_seconds = rx_ts['sec']
    nanoseconds = rx_ts['nanosec']
    # print(even_seconds, nanoseconds)
    return even_seconds + nanoseconds/1000000000.0
def rx_epoch_seconds(json_element):
    rx_ts = json_element['rx_ts']
    return epoch_seconds(rx_ts)
def rx_timestamp(json_element):
    return datetime.datetime.utcfromtimestamp(rx_epoch_seconds(json_element))

