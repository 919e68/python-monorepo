def rename_keys(aliases: dict[str, str], data: dict):
  return {
    aliases[key] if key in aliases else key:value
    for key, value in data.items()
  }
