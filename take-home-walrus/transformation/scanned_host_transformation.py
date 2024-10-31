def scanned_host_transformation(raw_hosts: dict) -> dict:
    try:
        return {
            "id": raw_hosts.get("id") or raw_hosts.get("tenable_id") or "Unknown Id",
            "hostname": raw_hosts.get("host_name") or raw_hosts.get("name") or "unknown",
            "os": raw_hosts.get("display_operating_system", "Unknown OS"),
            "last_seen": raw_hosts.get("last_observed", {}).get("$date", "Unknown last seen"),
            "source": "tenable"
        }
    except AttributeError as ex:
        print(f"Attribute error in transforming Tenable host: {ex} - Host data: {raw_hosts}")
        return {}
    except Exception as ex:
        print(f"Error transforming Tenable host: {ex}")
        return {}
