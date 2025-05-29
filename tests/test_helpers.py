import unittest
from lib.models import create_tables
from lib.models.base import SessionLocal, engine, Base
from lib.models.user import User
from lib.helpers import create_user, add_transaction, view_user, view_transactions

class BudgetBuddyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.drop_all(engine)
        create_tables()

    def setUp(self):
        self.session = SessionLocal()

    def tearDown(self):
        self.session.query(User).delete()
        self.session.commit()
        self.session.close()

    def test_create_user(self):
        create_user("TestUser", 500)
        user = self.session.query(User).filter_by(name="TestUser").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.total_budget, 500)

    def test_add_transaction(self):
        create_user("TestUser", 500)
        add_transaction("TestUser", "Snacks", 50)
        user = self.session.query(User).filter_by(name="TestUser").first()
        self.assertEqual(user.total_budget, 450)

    def test_view_user_output(self):
        create_user("Viewer", 700)
        view_user("Viewer")

    def test_view_transactions_output(self):
        create_user("Viewer", 700)
        add_transaction("Viewer", "Book", 100)
        view_transactions("Viewer")

if __name__ == '__main__':
    unittest.main()
