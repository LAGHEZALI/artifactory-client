import arguments_checker as ac
import artifactory_request as ar


if __name__ == "__main__":

    args = ac.init_arguments()

    print(args)

    command = args.command

    if command == 'purge':
        mode = args.purge_mode
        version_parts = args.version.split('.')
        version = {'major': version_parts[0], 'minor': version_parts[1]}
        if len(version_parts) == 3:
            version['patch'] = version_parts[2]
        print(version)

        if mode == 'purge_only':
            pass
        elif mode == 'keep_only':
            pass
        pass
    elif command == 'list':
        pass



