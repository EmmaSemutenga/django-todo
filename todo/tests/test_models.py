from utils.setup_test import TestSetup
from todo.models import Todo


class TestModels(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()
        todo = Todo.objects.create(title="title", description="description", owner=user)
        self.assertEqual(str(todo), "title")