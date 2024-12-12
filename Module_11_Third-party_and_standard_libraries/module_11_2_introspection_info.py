from pprint import pprint
import inspect


def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    value_methods = []
    value_attr = []
    for attr_name in dir(obj):
        if 'method' in str(type(getattr(obj, attr_name))):
            value_methods.append(attr_name)
        else:
            value_attr.append(attr_name)
    result['methods'] = value_methods
    result['attributes'] = value_attr
    result['module'] = inspect.getmodule(obj)
    return result


number_info = introspection_info(42)
pprint(number_info)
