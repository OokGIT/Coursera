import csv

hosts = [["Node48.local", "192.168.0.48"], ["Webserver.cloud", "10.0.0.12"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
