# -*- encoding:utf-8 -*-
from typing import Dict, Any, Tuple


def parse_kv_document(text: str) -> Dict[str, Any]:
    """
    Parse a simple custom key-value document with sections like:
    #key: value
        ##subkey: value
    Multiline values supported with trailing lines indented under the key.
    Returns a nested dict.
    """
    result: Dict[str, Any] = {}
    current_key = None
    current_subkey = None
    lines = text.splitlines()

    def set_value(key: str, value: str):
        result[key] = value

    for raw in lines:
        line = raw.rstrip("\n\r")
        if not line.strip():
            continue
        # Top-level key: '#key: value'
        if line.startswith('#') and not line.startswith('##'):
            current_subkey = None
            try:
                after_hash = line[1:]
                key, value = [x.strip() for x in after_hash.split(':', 1)] if ':' in after_hash else (after_hash.strip(), '')
            except ValueError:
                continue
            current_key = key
            if value == '':
                # create a nested dict for section if not exists or convert existing scalar to dict preserving scalar as '_value'
                cur = result.get(current_key)
                if isinstance(cur, dict):
                    pass
                elif isinstance(cur, str):
                    result[current_key] = {'_value': cur}
                else:
                    result[current_key] = {}
            else:
                # set scalar; if previously a dict, store scalar in '_value'
                if isinstance(result.get(current_key), dict):
                    result[current_key]['_value'] = value
                else:
                    result[current_key] = value
        # Sub-key: '##sub: value'
        elif line.strip().startswith('##') and current_key is not None:
            sub = line.strip()[2:]
            subkey, subval = [x.strip() for x in sub.split(':', 1)] if ':' in sub else (sub.strip(), '')
            if not isinstance(result.get(current_key), dict):
                # convert scalar to dict preserving scalar as '_value'
                prev = result.get(current_key)
                result[current_key] = {'_value': prev} if isinstance(prev, str) else {}
            if subval == '':
                result[current_key][subkey] = ''
            else:
                result[current_key][subkey] = subval
            current_subkey = subkey
        else:
            # multiline append to the last key or subkey
            if current_key is not None and isinstance(result.get(current_key), dict) and current_subkey:
                prev = result[current_key].get(current_subkey, '')
                if prev:
                    result[current_key][current_subkey] = prev + "\n" + line
                else:
                    result[current_key][current_subkey] = line
            elif current_key is not None and isinstance(result.get(current_key, ''), str):
                prev = result.get(current_key, '')
                if prev:
                    result[current_key] = prev + "\n" + line
                else:
                    result[current_key] = line
    return result
