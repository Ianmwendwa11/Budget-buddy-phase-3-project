import argparse
from lib.helpers import create_user, add_transaction, view_user, view_transactions

def main():
    parser = argparse.ArgumentParser(description="Budget Buddy CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Create user
    create_user_parser = subparsers.add_parser("create-user")
    create_user_parser.add_argument("name")
    create_user_parser.add_argument("budget", type=float)

    # Add transaction
    add_tx_parser = subparsers.add_parser("add-transaction")
    add_tx_parser.add_argument("name")
    add_tx_parser.add_argument("description")
    add_tx_parser.add_argument("amount", type=float)

    view_user_parser = subparsers.add_parser("view-user")
    view_user_parser.add_argument("name")

    view_tx_parser = subparsers.add_parser("view-transactions")
    view_tx_parser.add_argument("name")

    args = parser.parse_args()

    if args.command == "create-user":
        create_user(args.name, args.budget)
    elif args.command == "add-transaction":
        add_transaction(args.name, args.description, args.amount)
    elif args.command == "view-user":
        view_user(args.name)
    elif args.command == "view-transactions":
        view_transactions(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
