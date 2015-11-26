# TODO move to some generic setup utility package
import sys
from setuptools.command.test import test as TestCommand
from setuptools import Command

try:
    from setupext import janitor
    CleanCommand = janitor.CleanCommand
except ImportError:
    CleanCommand = None

class ToxCommand(TestCommand):
    """
    Based on https://testrun.org/tox/latest/example/basic.html#integration-with-setuptools-distribute-test-commands
    """
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

class FixCopyright(Command):
    description = 'Fix copyright on all files'
    user_options = tuple()
    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""
        pass # XXX DO THE JOB HERE
