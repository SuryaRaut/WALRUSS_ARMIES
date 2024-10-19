def qualys_host_transformation(raw_hosts: dict) -> dict:
    try:
        return {
            "id": raw_hosts.get("id", "Unknown Id"),
            "hostname": raw_hosts.get("dnsHostName", "Unkown host"),
            "os": raw_hosts.get("agentInfo", {}).get("platform", "Uknown OS"),
            "last_seen": raw_hosts.get("lastVulnScan", {}).get("$date", "Uknown last seen"),
            "source": "qualys"
        }
    except Exception as ex:
        print(f"Error transforming Qualys host: {ex}")