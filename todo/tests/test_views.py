from logging import error
from todo.models import Todo
from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup
from django.shortcuts import redirect

class TestViews(TestSetup):

    def test_should_create_todo(self):
        user = self.create_test_user()
        self.client.post(reverse("authentication:login"), {
            'username' : user.username,
            'password' : "getyours",
        })
        todos = Todo.objects.all()

        self.assertEqual(todos.count(), 0)

        response = self.client.post(reverse('todo:create-todo'), { "owner" : user, "title" : "Hello Do this", "description" : "Remember your chores"})
        

        updated_todos = Todo.objects.all()
        self.assertEqual(updated_todos.count(), 1)
        self.assertEqual(response.status_code, 302)

    # def test_should_update_todo(self):
    #     user = self.create_test_user()
    #     self.client.post(reverse("authentication:login"), {
    #         'username' : user.username,
    #         'password' : "getyours",
    #     })
    #     todos = Todo.objects.all()

    #     self.assertEqual(todos.count(), 0)

    #     response = self.client.post(reverse('todo:create-todo'), { "owner" : user, "title" : "Hello Do this", "description" : "Remember your chores"})
        
    #     todo = Todo.objects.get(pk=1)

    #     response = self.client.post(redirect('todo:todo-edit', id=todo.id), { "title" : "title edited", "description" : "New description"})
        

    #     self.assertEqual(todo.id, 1)

    #     updated_todos = Todo.objects.all()
    #     self.assertEqual(updated_todos.count(), 1)
    #     self.assertEqual(response.status_code, 302)