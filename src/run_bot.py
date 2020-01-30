import sys
import ext_author_client as eac


def main():
    # Check arguments
    args = sys.argv
    if len(args) != 4:
        print(f'[ERROR] Usage: python {__file__} <token> <author id> <channel id>', file=sys.stderr)
        sys.exit(1)

    token      = args[1]
    author_id  = int(args[2])
    channel_id = int(args[3])

    # Run bot
    bot_cli = eac.ExtAuthorClient(author_id, channel_id)
    bot_cli.run(token)


if __name__ == '__main__':
    main()
