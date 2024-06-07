## Refer to Ansible documentation to determine where to copy the get_vmware_license_info.py module

## The sample playbook looks like this: 
````
---
- name: Get VMware License Information
  hosts: localhost
  gather_facts: no

  tasks:
    - name: Retrieve VMware License Information
      get_vmware_license_info:
        hostname: "myVCenter.home.lab"
        username: "administrator@vsphere.local"
        password: "Password123"
      register: license_info

    - name: Display License Information
      debug:
        var: license_info
````


## With the resulting output looking like this:  
````
TASK [Display License Information] 
ok: [localhost] => {
    "license_info": {
        "ansible_facts": {
            "host_licenses": {
                "192.168.86.xx": [
                    {
                        "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                        "name": "vSphere 8 Enterprise Plus"
                    }
                ],
                "192.168.86.xx": [
                    {
                        "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                        "name": "vSphere 8 Enterprise Plus"
                    }
                ],
                "192.168.86.xx": [
                    {
                        "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                        "name": "vSphere 8 Enterprise Plus"
                    }
                ],
                "192.168.86.xx": [
                    {
                        "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                        "name": "vSphere 8 Enterprise Plus"
                    }
                ],
                "vcenter.home.lan": [
                    {
                        "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                        "name": "vCenter Server 8 Standard"
                    }
                ]
            },
            "vcenter_licenses": [
                {
                    "license_key": "00000-00000-00000-00000-00000",
                    "license_package": "",
                    "license_total": 0,
                    "license_used": null,
                    "name": "Product Evaluation"
                },
                {
                    "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                    "license_package": "cpuPackage:32core",
                    "license_total": 32,
                    "license_used": 4,
                    "name": "vSphere 8 Enterprise Plus"
                },
                {
                    "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                    "license_package": "cpuPackage:32core",
                    "license_total": 32,
                    "license_used": 0,
                    "name": "vSAN Enterprise"
                },
                {
                    "license_key": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX",
                    "license_package": "server",
                    "license_total": 2,
                    "license_used": 1,
                    "name": "vCenter Server 8 Standard"
                }
            ]
        },
        "changed": false,
        "failed": false
    }
}
