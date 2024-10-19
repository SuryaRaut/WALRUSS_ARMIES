#print("hello world!!")

from extractor.qualys import get_host_from_qualys
from extractor.crowdstrike import get_host_from_crowdstrikes
from transformation.qualys_transformation import qualys_host_transformation
from transformation.crowdstrikes_transformation import crowdstrikes_host_transformation
from data_dedups.data_deduper import find_duplicate_hosts
from storage.mongo_storage import persist_dedups_hosts
from visualization.visualization import op_sys_vizualize, older_host_and_new_host_visualization
from config import Q_C_API_KEY


def main():

    #fetching data from qualys
    get_qualys_hosts = get_host_from_qualys(Q_C_API_KEY)
    #fetching data from crowdstrikes
    get_crowdstrikes_hosts = get_host_from_crowdstrikes(Q_C_API_KEY)

    #data modeling
    transform_host = [qualys_host_transformation(host) for host in get_qualys_hosts]
    transform_host.extend([crowdstrikes_host_transformation(host) for host in get_crowdstrikes_hosts])

    #filtering duplicate hosts
    dup_hosts =  find_duplicate_hosts(transform_host)

    #persisting in db
    persist_dedups_hosts(dup_hosts)

    #data visualization

    op_sys_vizualize(dup_hosts)
    older_host_and_new_host_visualization(dup_hosts)

if __name__ == "__main__":
    main()

