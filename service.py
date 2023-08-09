import sys
import json
from typing import Dict

def save_service(num_services: int, service_name_prefix: str, filename: str) -> Dict:
    service_json = {f"{service_name_prefix}{i+1}": 
                    {"url": f"http://{service_name_prefix}{i+1}.default.127.0.0.1.sslip.io:8080", 
                     "exec_time": i+1} 
                    for i in range(num_services)}
    with open(filename, 'w') as fh:
        json.dump(service_json, fh, indent=2)

if __name__ == '__main__':
    num_services = int(sys.argv[1])
    save_service(num_services, 'service', 'service.json')