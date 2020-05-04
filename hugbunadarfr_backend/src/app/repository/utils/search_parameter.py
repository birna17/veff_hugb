"""Cleaning."""


def _clean_field_value(param, splitter):
    split_param = param.split(splitter)
    if len(split_param) < 2:
        raise TypeError(f"Search parameter invalid: {param}")
    field, value = split_param[0], split_param[1]
    return field.strip(), value.strip()


def search_parameter(param):
    """Searching."""
    if "==" in param:
        field, value = _clean_field_value(param, "==")
        return lambda x: str(x.__dict__.get(field)) == str(value)
    elif "!=" in param:
        field, value = _clean_field_value(param, "!=")
        return lambda x: str(x.__dict__.get(field)) != str(value)
    elif "<=" in param:
        field, value = _clean_field_value(param, "<=")
        return lambda x: str(x.__dict__.get(field)) <= str(value)
    elif ">=" in param:
        field, value = _clean_field_value(param, ">=")
        return lambda x: str(x.__dict__.get(field)) >= str(value)
    elif "<" in param:
        field, value = _clean_field_value(param, "<")
        return lambda x: str(x.__dict__.get(field)) < str(value)
    elif ">" in param:
        field, value = _clean_field_value(param, ">")
        return lambda x: str(x.__dict__.get(field)) > str(value)
    raise TypeError(f"Search parameter invalid: {param}")
