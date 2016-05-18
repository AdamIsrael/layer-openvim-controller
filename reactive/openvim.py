from charms.reactive import when, when_not, set_state
from charmhelpers.core.templating import render
from charmhelpers.core.hookenv import status_set

import subprocess

@when_not('openvim.installed')
def install_openvim():
    status_set("maintenance", "installing openvim controller")
    render(
        source="init-controller.sh",
        target="/tmp/init-controller.sh",
        owner="ubuntu",
        perms=0o775,
        context={}
    )
    subprocess.check_call("sudo -u ubuntu /tmp/init-controller.sh", shell=True)
    set_state('openvim.installed')
