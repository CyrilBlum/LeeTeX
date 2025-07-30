import builtins
import inspect

builtin_classes = [name for name, obj in vars(builtins).items() if inspect.isclass(obj)]
print(builtin_classes)