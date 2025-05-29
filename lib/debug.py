from lib.helpers import create_user, add_transaction, view_user, view_transactions

create_user("Mwendwa", 1000)
add_transaction("Mwendwa", "Lunch", 200)
view_user("Mwendwa")
view_transactions("Mwendwa")
