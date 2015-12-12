# TODO move to some generic setup utility package
import sys
from setuptools.command.test import test as TestCommand
from setuptools import Command
import setuptools

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
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

class FixHeader(setuptools.Command):
    description = 'fix header files'
    user_options = [
                    ('baselines', 'b', 'list of all baselines to use, comma separated (default: setup.py)')
                    ]
    
    def initialize_options(self):
        print 'initilize'
        self.baselines = None
        
    def finalize_options(self):
        print 'finalize'
        #self.set_undefined_options('baselines', ('baselines', 'baselines'))
#        self.set_undefined_options('baselines', 'setup.py')

    def run(self):
        print '*** printing %s' % self.baselines
        
