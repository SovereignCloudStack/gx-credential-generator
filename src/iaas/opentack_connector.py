import openstack
impirt sys


class OpenstackConnector():
    """Abstraction for Openstack API calls."""
    def __init__(self, cloud, timeout):
        self.conn = openstack.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4)
        try:
            self.conn.authorize()
        except Exception:
            print("INFO: Retry connection with 'default' domain", file=sys.stderr)
            conn = openstack.connect(cloud=cloud, timeout=timeout, api_timeout=timeout * 1.5 + 4,
                                     default_domain='default', project_domain_id='default')
            self.conn.authorize()
