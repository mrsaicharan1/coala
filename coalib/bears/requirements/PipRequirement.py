from coalib.bears.requirements.PackageRequirement import PackageRequirement
from coalib.misc.Shell import call_without_output
import sys


class PipRequirement(PackageRequirement):
    """
    This class is a subclass of ``PackageRequirement``. It specifies the proper
    type for ``python`` packages automatically and provides functions to check
    for and install the requirement.
    """

    def __init__(self, package, version=""):
        """
        Constructs a new ``PipRequirement``, using the ``PackageRequirement``
        constructor.

        >>> pr = PipRequirement('setuptools', '19.2')
        >>> pr.type
        'pip'
        >>> pr.package
        'setuptools'
        >>> pr.version
        '19.2'

        :param package: A string with the name of the package to be installed.
        :param version: A version string. Leave empty to specify latest version.
        """
        PackageRequirement.__init__(self, 'pip', package, version)

    def install_command(self):
        """
        Creates the installation command for the instance of the class.

        :param return: A list with the installation command parameters.
        """
        result = [sys.executable, '-m', 'pip', 'install',
                  self.package + '==' + self.version if self.version
                  else self.package]
        return result

    def is_installed(self):
        """
        Checks if the dependency is installed.

        :param return: True if dependency is installed, false otherwise.
        """
        return not call_without_output((sys.executable, '-m', 'pip',
                                        'show', self.package))
