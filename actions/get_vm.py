from lib.actions import SingleVMAction

__all__ = [
    'GetVMAction'
]


class CreateVMAction(SingleVMAction):
    api_type = 'compute'

    def run(self, credentials, vm_id):
        driver = self._get_driver_for_credentials(credentials=credentials)
        node = self._get_node_for_id(node_id=vm_id, driver=driver)

        self.logger.info('Node successfully obtained: %s' % (node))
        return self.resultsets.formatter(node)
