const API = "http://http://127.0.0.1:5000/employees";

async function loadEmployees() {
    const response = await fetch(API);
    const employees = await response.json();

    let list = document.getElementById("employeeList");
    list.innerHTML = "";

    employees.forEach(emp => {
        list.innerHTML += `
            <li>
                ${emp.name} -
                ${emp.email} -
                ${emp.department}
            </li>
        `;
    });
}

async function addEmployee() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const department = document.getElementById("department").value;

    await fetch(API, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name,
            email,
            department
        })
    });

    loadEmployees();
}

loadEmployees();
