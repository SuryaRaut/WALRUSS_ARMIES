import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
from dateutil import parser

def op_sys_vizualize(hosts):
    op_sys_counter = {}
    for host in hosts:
        print(f"Host type: {type(host)}")

        print(f"Host content: {host}")
        os = host['os']
        op_sys_counter[os] = op_sys_counter.get(os, 0)+ 1
    #bar chart visualization
    plt.figure(figsize=(10, 5))
    plt.bar(op_sys_counter.keys(), op_sys_counter.values())
    plt.title("Hosts by Operating System")
    plt.xlabel("Operating Systems")
    plt.ylabel("Number of Hosts")
    plt.show()

    #piechart visualization
    plt.figure(figsize=(5, 5))
    plt.pie(op_sys_counter.values(), labels=op_sys_counter.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Hosts by Operating System")
    plt.show()

def older_host_and_new_host_visualization(hosts):
    older_host_counter, new_host_counter = 0, 0
    threshold_date = datetime.now(timezone.utc) - timedelta(days=30)

    for host in hosts:
        #last_seen_str = host['last_seen'].split('.')[0]
        last_seen_date = parser.isoparse(host['last_seen'])
        if last_seen_date < threshold_date:
            older_host_counter += 1
        else:
            new_host_counter += 1
    print(f"Total Old Host: {older_host_counter}")
    print(f"Total New Host: {new_host_counter}")

    #Bar chart visualization
    plt.figure(figsize=(10, 5))
    plt.bar(["Old Hosts", "New Hosts"], [older_host_counter, new_host_counter])
    plt.title("Older vs New Hosts")
    plt.xlabel("Host Type")
    plt.ylabel("Number of Hosts")
    plt.show()

    #Pie chart
    plt.figure(figsize=(5, 5))
    plt.pie([older_host_counter, new_host_counter], labels=["Old Hosts", "New Hosts"], autopct='%1.1f%%', startangle=90) 
    plt.title("Older vs New Hosts")
    plt.show()