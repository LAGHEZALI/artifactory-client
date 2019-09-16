import argparse
import re

parser = argparse.ArgumentParser()


def get_version_regex_type(s, pat=re.compile(r"^(?P<major>[0-9]+).(?P<minor>\*|[0-9]+.(?P<patch>\*|[0-9]+))$")):
    if not pat.match(s):
        raise argparse.ArgumentTypeError
    return s


class UniqueAppendAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        unique_values = set(values)
        setattr(namespace, self.dest, unique_values)


def init_arguments():
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')

    purge_parser = subparsers.add_parser('purge', help='purge_parser help')
    purge_parser.add_argument('-pm',
                              '--purge_mode',
                              help='Purge mode',
                              choices=['purge_only', 'keep_only'],
                              required=True)
    purge_parser.add_argument('-v',
                              '--version',
                              help='Concerned versions',
                              type=get_version_regex_type,
                              required=True)
    purge_parser.add_argument('-pt',
                              '--packages_type',
                              help='Packages type',
                              type=str,
                              choices=['dev', 'pr', 'rc'],
                              nargs='+',
                              action=UniqueAppendAction,
                              default=['dev', 'pr', 'rc'])

    list_parser = subparsers.add_parser('list', help='list_parser help')
    list_parser.add_argument('-lm',
                             '--list_mode',
                             help='List mode',
                             type=str,
                             choices=['all_packages', 'release_packages'],
                             required=True)

    return parser.parse_args()


if __name__ == "__main__":
    pass
