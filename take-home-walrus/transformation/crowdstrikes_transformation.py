def crowdstrikes_host_transformation(raw_hosts: dict) -> dict:
    try:
        return {
            "id": raw_hosts.get("device_id", "Unknown ID"),
            "hostname": raw_hosts.get("hostname", "Unknown Hostname"),
            "os": raw_hosts.get("os_version", "Unoknwon OS"),
            "last_seen": raw_hosts.get("last_seen", "Unknown last seen"),
            "source": "crowdstrike"
        }
    except Exception as ex:
        print(f"Error transfering Crowdstrike host: {ex}")