// Lista de tareas
let tasks = [];

function addTask() {
    const input = document.getElementById("taskInput");
    const task = input.value;

    if (task === "") return;

    tasks.push(task);
    input.value = "";
    renderTasks();
}

function renderTasks() {
    const list = document.getElementById("taskList");
    list.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.textContent = task;
        list.appendChild(li);
    });
}
