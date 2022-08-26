def exlude_keys(excluded_keys: list, data: dict):
  return {
    key: data[key]
    for key in data
    if key not in excluded_keys
  }
