def removeWhiteSpace(a):
    ns = a.strip()
    while '  ' in ns:
        ns = ns.replace('  ', ' ')
    return ns