"""
    This script imports code from all files in the same directory as this script,
    see https://github.com/amelvill-umich/walk_packages_test for an example
"""
import pkgutil

__all__ = []
for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    exec('%s = module' % module_name)