from rdap.common.utils import get_suffix, get_domain

def form_hostname(data:dict) -> str or None:
    domain = get_domain(data)
    suffix = get_suffix(data)

    if domain != '' and suffix != '':
        return "{0}.{1}".format(domain, suffix)
    return None