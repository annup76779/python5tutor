{k: v for k, v in val.items() if v.resource_type.value in ('model', 'seed', 'source')}

d= {}
for k, v in val.items():
    if v.resource_type.value in ('model', 'seed', 'source'):
        d[k] = v