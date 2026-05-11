document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const errorMessage = document.getElementById('error-message');
    
    // Config API
    const API_URL = '/api';

    // State
    let draggedTask = null;

    // Initialize
    fetchBoard();

    // Event Listeners
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = taskInput.value.trim();
        if (title) {
            await createTask(title);
            taskInput.value = '';
        }
    });

    // Drag and Drop setup for columns
    document.querySelectorAll('.task-list').forEach(list => {
        list.addEventListener('dragover', (e) => {
            e.preventDefault();
            const afterElement = getDragAfterElement(list, e.clientY);
            const draggable = document.querySelector('.dragging');
            if (draggable) {
                if (afterElement == null) {
                    list.appendChild(draggable);
                } else {
                    list.insertBefore(draggable, afterElement);
                }
                list.classList.add('drag-over');
            }
        });

        list.addEventListener('dragleave', () => {
            list.classList.remove('drag-over');
        });

        list.addEventListener('drop', async (e) => {
            e.preventDefault();
            list.classList.remove('drag-over');
            if (draggedTask) {
                const newStatus = list.getAttribute('data-status');
                const taskId = draggedTask.getAttribute('data-id');
                const currentStatus = draggedTask.getAttribute('data-status');
                
                if (newStatus !== currentStatus) {
                    await moveTask(taskId, newStatus, draggedTask);
                }
            }
        });
    });

    // Helpers
    function showError(msg) {
        errorMessage.textContent = msg;
        errorMessage.classList.add('visible');
        setTimeout(() => {
            errorMessage.classList.remove('visible');
        }, 5000);
    }

    // API Calls
    async function fetchBoard() {
        try {
            const res = await fetch(`${API_URL}/tablero`);
            if (!res.ok) throw new Error('Error al obtener el tablero');
            const data = await res.json();
            renderBoard(data);
        } catch (err) {
            showError('No se pudo conectar con el servidor.');
        }
    }

    async function createTask(title) {
        try {
            const res = await fetch(`${API_URL}/tareas`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo: title })
            });
            const data = await res.json();
            
            if (!res.ok) {
                throw new Error(data.error || 'Error al crear la tarea');
            }
            
            // Re-fetch to keep state consistent or just append
            await fetchBoard();
        } catch (err) {
            showError(err.message);
            // Re-fetch board to reset UI in case of failure
            fetchBoard();
        }
    }

    async function moveTask(id, targetStatus, taskElement) {
        // Optimistic UI update removed to rely on server state
        try {
            const res = await fetch(`${API_URL}/tareas/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ estado_destino: targetStatus })
            });
            
            const data = await res.json();
            if (!res.ok) {
                throw new Error(data.error || 'Error al mover la tarea');
            }
            // Success
            await fetchBoard();
        } catch (err) {
            showError(err.message);
            // Refresh to restore valid state
            fetchBoard();
        }
    }

    // Render Functions
    function renderBoard(board) {
        const statuses = ['TODO', 'DOING', 'DONE'];
        
        statuses.forEach(status => {
            const list = document.getElementById(`list-${status.toLowerCase()}`);
            const count = document.getElementById(`count-${status.toLowerCase()}`);
            const tasks = board[status] || [];
            
            list.innerHTML = '';
            count.textContent = tasks.length;
            
            tasks.forEach(task => {
                const card = createTaskCard(task);
                list.appendChild(card);
            });
        });
    }

    function createTaskCard(task) {
        const card = document.createElement('div');
        card.className = 'task-card';
        card.draggable = true;
        card.setAttribute('data-id', task.id_tarea);
        card.setAttribute('data-status', task.estado);

        const title = document.createElement('div');
        title.className = 'task-title';
        title.textContent = task.titulo;

        const actions = document.createElement('div');
        actions.className = 'task-actions';

        // Botones de acción manual por accesibilidad y por si el Drag&Drop falla
        if (task.estado === 'TODO') {
            const btnDoing = createButton('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>', () => moveTask(task.id_tarea, 'DOING', card));
            actions.appendChild(btnDoing);
        } else if (task.estado === 'DOING') {
            const btnDone = createButton('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>', () => moveTask(task.id_tarea, 'DONE', card));
            actions.appendChild(btnDone);
        }

        card.appendChild(title);
        card.appendChild(actions);

        // Drag events
        card.addEventListener('dragstart', () => {
            card.classList.add('dragging');
            draggedTask = card;
        });

        card.addEventListener('dragend', () => {
            card.classList.remove('dragging');
            draggedTask = null;
        });

        return card;
    }

    function createButton(svgContent, onClick) {
        const btn = document.createElement('button');
        btn.className = 'btn-move';
        btn.innerHTML = svgContent;
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            onClick();
        });
        return btn;
    }

    function getDragAfterElement(container, y) {
        const draggableElements = [...container.querySelectorAll('.task-card:not(.dragging)')];

        return draggableElements.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }
});
