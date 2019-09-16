import re


def filter_package_by_version(packages, version_pattern, packages_types):
    filtered_packages = []
    for pkg in packages:
        m = re.match(r'^(?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)(?P<type>\w+)$', pkg)
        if m:
            pkg_version = {
                'major': m.group('major'),
                'minor': m.group('minor'),
                'patch': m.group('patch'),
                'type': m.group('type')
            }

            if pkg_version['major'] == version_pattern['major']:
                if version_pattern['minor'] == '*':
                    filtered_packages.append(pkg)
                elif version_pattern['minor'] == pkg_version['minor']:
                    if version_pattern['patch'] == '*':
                        filtered_packages.append(pkg)
                    elif version_pattern['patch'] == pkg_version['patch'] and pkg_version['type'] in packages_types:
                        filtered_packages.append(pkg)
    return filtered_packages


if __name__ == "__main__":
    pass
