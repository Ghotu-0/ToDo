import gi
import datetime

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib


class AddRemoveUtility:

    def __init__(self, app):
        self.App = app
        self.TodoContainer = self.App.Builder.get_object("TodoContainer")
        self.newTodoButton = self.App.Builder.get_object("createNewTodo")
        self.discardTodoButton = self.App.Builder.get_object("discardNewTodo")

        print("Initialized Todo Creation Functionality")

    def getTodoContainerChild(self):
        return Gtk.Box.get_children(self.TodoContainer)

    def addTodoComp(self, title):
        todoComponent = self.App.TodoTCompClass.Todo(
            {"title": title, "counter": str(len(self.getTodoContainerChild()) + 1)})
        Gtk.Box.add(self.TodoContainer, todoComponent.todo)
        return todoComponent

    def wantsToCreateTodo(self, widget, data=None):
        data = self.App.Input.getInputForTodo()
        todo = self.addTodoComp(data.get("title"))
        self.App.TodoList.append(todo)
        created = {"data": data, "time": str(datetime.datetime.now()), "state": todo.state, "progress": 0}
        self.App.Store.saveToStore(created)
        self.App.Events.addDefaultTodoHandlers(todo, (len(self.App.TodoList) - 1))

    def removeTodo(self, index):
        if self.App.TodoList[index].state == "Playing":
            del self.App.TodoList[index]
            self.App.Store.removeFromStoreByIndex(index)
            if len(self.App.TodoList) > 0:
                self.App.PlayPauseTUtility.playpauseTodo(0, self.App.TodoList[0], 0)
        else:
            del self.App.TodoList[index]
            self.App.Store.removeFromStoreByIndex(index)

    def removeTodoExcited(self, button, comp):
        index = self.App.TodoList.index(comp)
        self.TodoContainer.remove(comp.todo)
        self.removeTodo(index)
        self.correctLabelCounter(index)

    def correctLabelCounter(self, index):
        length = len(self.App.TodoList)
        for i in range(index, length):
            todoComp = self.App.TodoList[i]
            todoComp.todoCounter.set_text(str(i + 1))
