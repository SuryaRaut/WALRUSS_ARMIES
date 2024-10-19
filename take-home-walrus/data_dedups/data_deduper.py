def find_duplicate_hosts(hosts: list) -> list:
    seen = set()
    deduped_hosts = []
    for host in hosts:
        key = host["hostname"]
        if key not in seen:
            seen.add(key)
            deduped_hosts.append(host)
    return deduped_hosts