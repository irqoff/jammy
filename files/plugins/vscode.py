#!/usr/bin/python

# Copyright (c) 2022, Aleksandr Usov <irqoff@gmail.com>

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule


class VSCodePlugins(object):

    def __init__(self, module, check_mode=False):
        self.module = module
        self.check_mode = check_mode
        # Check if vscode binary exists
        self.vscode_bin = self.module.get_bin_path('code-insiders', required=True)

    def install(self, name):
        command = [self.vscode_bin, "--install-extension", name]

        rc, out, err = self.module.run_command(command)

        if rc != 0:
            self.module.fail_json(msg='code-insiders failed while installing extension with error: %s' % err,
                                  out=out,
                                  err=err)
        print(out)
        print(type(out))

        if 'was successfully installed' in out:
            value = out.rstrip('\n')
        else:
            value = None

        return value

    def uninstall(self, name):
        command = [self.vscode_bin, "--uninstall-extension", name]

        rc, out, err = self.module.run_command(command)

        if rc != 0 and 'is not installed' not in err:
            self.module.fail_json(msg='code-insiders failed while uninstalling extension with error: %s' % err,
                                  out=out,
                                  err=err)

        if 'was successfully uninstalled' in out:
            value = out.rstrip('\n')
        else:
            value = None

        return value


def main():
    # Setup the Ansible module
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True, type='str', no_log=False)
        ),
        supports_check_mode=True
    )

    # Create wrapper instance.
    vscode = VSCodePlugins(module, module.check_mode)

    # Process based on different states.
    if module.params['state'] == 'present':
        changed = vscode.install(module.params['name'])
        module.exit_json(changed=changed)
    elif module.params['state'] == 'absent':
        changed = vscode.uninstall(module.params['name'])
        module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
