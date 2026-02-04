import { useEffect, useState } from "react";
import API from "../api";

function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  API.get("tasks/")
    .then((res) => {
      console.log("Tasks data:", res.data);
      setTasks(res.data);
      setLoading(false);
    })
    .catch((err) => {
      console.error("Error fetching tasks:", err);
      setLoading(false);
    });
}, []);


  if (loading) {
    return <p>Loading tasks...</p>;
  }

  return (
    <div>
      <h2>My Tasks</h2>

      {tasks.length === 0 ? (
        <p>No tasks found</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <strong>{task.title}</strong> —{" "}
              {task.completed ? "Done" : "Pending"}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Tasks;
