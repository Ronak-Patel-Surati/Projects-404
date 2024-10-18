import { useState } from "react";
import "./App.css";
import NavBar from "./components/NavBar";

function App() {
  const [todo, setTodo] = useState("");
  const [todos, setTodos] = useState([]);

  const handleEdit = (index) => {
    const newTodos = [...todos];
    const currentTodo = newTodos[index].todo;
    const updatedTodo = prompt("Edit your todo:", currentTodo);
    if (updatedTodo !== null && updatedTodo.trim() !== "") {
      newTodos[index].todo = updatedTodo;
      setTodos(newTodos);
    }
  };

  const handleDelete = (index) => {
    const newTodos = todos.filter((_, i) => i !== index);
    setTodos(newTodos);
  };

  const handleAdd = () => {
    if (todo.trim() !== "") {
      setTodos([...todos, { todo, isCompleted: false }]);
      setTodo("");
    }
  };

  const handleChange = (e) => {
    setTodo(e.target.value);
  };

  const toggleCompletion = (index) => {
    const newTodos = [...todos];
    newTodos[index].isCompleted = !newTodos[index].isCompleted;
    setTodos(newTodos);
  };

  return (
    <>
      <NavBar />
      <div className="container bg-blue-100 mx-auto my-5 rounded-xl px-4 py-4">
        <div className="addToDo mx-auto">
          <h1 className="text-2xl py-4 font-bold w-full px-2 flex justify-center">
            Add a Todo
          </h1>
          <div className="inputs mx-2 py-1 flex justify-center">
            <input
              type="text"
              className="rounded-xl py-3 px-4  outline-gray-500 w-2/3"
              placeholder="Add your todo here"
              onChange={handleChange}
              value={todo}
            />
            <button
              className="mx-3 text-white font-semibold bg-blue-700 px-7 py-1 rounded-xl hover:bg-blue-500"
              onClick={handleAdd}
            >
              Add
            </button>
          </div>
        </div>
        <div className="toDos mx-auto w-2/3 px-2">
          {todos.length === 0 ? (
            <p className="text-center text-gray-500">No todos available.</p>
          ) : (
            todos.map((item, index) => (
              <div
                key={index}
                className="todo flex my-2 items-center justify-between bg-white p-3 rounded shadow"
              >
                <div
                  className={`text ${item.isCompleted ? "line-through text-green-500" : ""
                    } cursor-pointer`}
                  onClick={() => toggleCompletion(index)}
                >
                  {item.todo}
                </div>
                <div className="btn flex">
                  <button
                    className="mx-2 text-white bg-blue-500 px-4 rounded-xl py-1 hover:bg-blue-400"
                    onClick={() => handleEdit(index)}
                  >
                    Edit
                  </button>
                  <button
                    className="mx-2 text-white bg-red-500 px-4 rounded-xl py-1 hover:bg-red-400"
                    onClick={() => handleDelete(index)}
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </>
  );
}

export default App;
