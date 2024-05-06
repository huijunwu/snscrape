import pkgutil
import importlib

__all__ = []


def _import_modules():
	prefixLen = len(__name__) + 1
	for importer, moduleName, isPkg in pkgutil.iter_modules(__path__, prefix = f'{__name__}.'):
		assert not isPkg
		moduleNameWithoutPrefix = moduleName[prefixLen:]
		__all__.append(moduleNameWithoutPrefix)
		module = importlib.import_module(moduleName)
		globals()[moduleNameWithoutPrefix] = module


_import_modules()
