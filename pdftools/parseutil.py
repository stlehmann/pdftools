import argparse
from pdftools import __version__

parentparser = argparse.ArgumentParser(add_help=False)
parentparser.add_argument(
    '--version',
    action='version',
    version='%(prog)s (pdftools) ' + __version__
)


def limit(val, min_, max_):
    if val < min_:
        return min_
    elif val > max_:
        return max_
    return val


def parse_rangearg(args, max_: int, min_: int=1):
    if args is None:
        return None
    pageset = set()
    for arg in args:
        if '-' in arg:
            try:
                start, stop = arg.split('-', 2)
                if start == '' and stop == '':
                    raise ValueError("Please supply a valid range expression.")
                elif start == '':
                    start = min_
                    stop = limit(int(stop), min_, max_)
                elif stop == '':
                    start = limit(int(start), min_, max_)
                    stop = max_
                else:
                    start, stop = map(int, [start, stop])
                    start, stop = map(lambda val: limit(val, min_, max_),
                                      [start, stop])
                pageset.update(range(start - 1, stop))
            except ValueError as err:
                raise ValueError("Please supply Integer values or range "
                                 "expressions")
        else:
            try:
                i = int(arg)
                pageset.add(i - 1 if i < max_ else max_ - 1)
            except ValueError as err:
                print("ValueError: Please supply Integer values or ranges")

    return list(pageset)
