#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests
from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import ssl

def get_vmware_license_info(hostname, username, password):
    # Ignore SSL certificate verification errors
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Connect to vCenter server
    try:
        si = SmartConnect(host=hostname, user=username, pwd=password, sslContext=context)
        if not si:
            raise SystemExit("Failed to connect to vCenter server.")

        # Get license assignment manager
        content = si.RetrieveContent()
        # Retrieve all licenses
        licenses = content.licenseManager.licenses
        vcenter_licenses = []
        for license in licenses:
            license_entry = {
                'name': license.name,
                'license_key': license.licenseKey,
                'license_total': license.total,
                'license_used': license.used,
                'license_package': license.costUnit,
                }
            if license_entry not in vcenter_licenses:
                vcenter_licenses.append(license_entry)

        license_assignment_manager = content.licenseManager.licenseAssignmentManager
        # Retrieve all licenses
        licenses = license_assignment_manager.QueryAssignedLicenses()
        # Retrieve all hosts
        host_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.HostSystem], True)
        hosts = host_view.view

        # Create a dictionary to store licenses assigned to each host
        host_licenses = {}

        # Loop through each license assignment
        for assignment in licenses:
            assigned_host = assignment.entityDisplayName
            assigned_license = {
                'name': assignment.assignedLicense.name,
                'license_key': assignment.assignedLicense.licenseKey,
                }
            # If the host is not in the dictionary, add it
            if assigned_host not in host_licenses:
                host_licenses[assigned_host] = [assigned_license]
            else:
                host_licenses[assigned_host].append(assigned_license)
        # Disconnect from vCenter server
        Disconnect(si)

        return {'vcenter_licenses': vcenter_licenses, 'host_licenses':host_licenses}

    except Exception as e:
        raise e

def main():
    module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True, no_log=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params['password']

    try:
        result = get_vmware_license_info(hostname, username, password)
        module.exit_json(changed=False, ansible_facts=result)
    except Exception as e:
        module.fail_json(msg="Failed to retrieve license information: %s" % str(e))

if __name__ == '__main__':
    main()

