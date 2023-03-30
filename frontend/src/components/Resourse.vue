<template>
    <!-- Формирование списка проектов -->
    <div :id="'prefix-' + ind" v-if="TOKEN_GETTER" v-for="(project, ind) in projects" :key="ind" @dragover.prevent @dragenter.prevent @drop="onDrop($event, 'prefix-' + ind, project)">
        <!-- Имя проекта -->
        <p class="project-title">{{ project.title }}</p>

        <!-- Формирование списка задач в проекте -->
        <template v-if="tasks.filter(task => task.project === project.id).length">
        <p class="genTasks">

            <p @click="openWindowAddTask(project, ind)" class="task-small" >
                <p class="img-small">
                    <i class="fa-regular fa-square-plus gray"></i>
                </p>
                <p class="title-small">Добавить</p>
            </p>

            <p class="tasks" v-for="(task, index) in tasks" :key="index">     
                <div @dragend="onDragEnd($event, task.id)" @dragstart="onDrag($event, task.id)" :id=task.id @click="showtask(task)" @mouseover="del(task.id)" @mouseout="delout(task.id)" class="task-small" v-if="task.project === project.id" draggable="true">
                    <p class="img-small">
                        <img :src=task.icon.icon alt="">
                    </p>
                    <p class="title-small">
                        {{ task.title }} ({{ task.id }})
                    </p>
                    <p class="delete" @click.stop="deleteTask(task.id, ind)" title="Удалить задачу"><i class="fa-solid fa-circle-xmark"></i></p>
                </div>

            </p>
        </p>
        </template>
        <!-- Если нет задач -->
        <template v-else>
        <p class="genTasks">
            <p @click="openWindowAddTask(project, ind)" class="task-small" >
                <p class="img-small">
                    <i class="fa-regular fa-square-plus gray"></i>
                </p>
                <p class="title-small">Добавить</p>
            </p>
        </p>
        </template>  
    
    </div>
    <!-- Если пользователь не авторизован список проектов не формируется -->
    <div v-else>
        Контент доступен только после авторизации
    </div>

    <!-- Форма добавления задачи -->
    <div id="addTask"><AddTask :projid=this.projectid @addTask="addTask" /></div>
    <p @click="closeWindowAddTask" id="addTaskBack"></p>

</template>

<script>
import axios from 'axios'
import { ref } from 'vue'
import { mapGetters } from 'vuex'
import AddTask from './AddTask.vue'


export default {
    name: 'Resourse',
    components: {
        AddTask,
    },
    setup() {
        const projects = ref([])
        const tasks = ref([])
        const projectid = ref()


        function onDrag(e, str){
            console.log('Началось перетаскивание')
            // передаем данные от перемещаемого объекта
            e.dataTransfer.setData('item', str)
            setTimeout(function(){
                const element = document.getElementById(str);
                if (element) {
                    element.classList.add("hide");
                    // element.parentNode.remove()
                }
            }, 0)
        }   
        
        function onDragEnd(e, str) {
            // показываем объект если он небыл перемещен в другой бокс
            console.log('Закончилось перетаскивание')
            document.getElementById(str).classList.remove("hide")
        }

        async function onDrop(e, num, project){
            const itemId = e.dataTransfer.getData('item')
            const obj = document.getElementById(itemId);
            document.getElementById(itemId).remove()
            var genTasks = document.getElementById(num).querySelector('.genTasks')
            var tasks = document.createElement('p')
            tasks.classList.add("tasks")
            tasks.appendChild(obj)
            genTasks.appendChild(tasks)
            document.getElementById(itemId).classList.remove("hide")
            this.tasks = this.tasks.filter(obj => obj.id !== itemId);
            console.log(this.tasks)
            console.log(`Блок из которого взяли ${num}`)
            console.log(`Блок в который перетянули ${project.id}`)
            const data = {
                project: project.id,
            }
            const resp = await axios.patch(`http://127.0.0.1:8000/content/tasks/${itemId}/update/`, data)
        }



        
        // Запрашиваем контент с бекэнда
        async function conRes() {  
            const instance = axios.create({
                headers: {'Authorization': this.TOKEN_GETTER}
            });
            if(this.TOKEN_GETTER) {
                const response_projects = await instance.get('http://localhost:8000/content/projects/')
                this.projects = response_projects.data
                const response_tasks = await instance.get('http://localhost:8000/content/tasks/')
                this.tasks = response_tasks.data
            }
        }

        // Показать полное описание задачи
        function showtask(tasks) {
            var taskSmall = document.getElementById(tasks.id)
            taskSmall.style.pointerEvents = 'none'
            taskSmall.style.opacity = '0.5'
            var idtask = 'prefix-' + tasks.id
            var task = document.getElementById(idtask)
            const back = document.createElement('div')
            back.classList.add('taskBack')
            back.addEventListener('click', function(){hidetask(tasks)});
            document.body.appendChild(back)

            const img = document.createElement('img')
            img.setAttribute('src', tasks.icon.icon)

            const div = document.createElement('div')
            div.innerHTML = `<p class='title'>${tasks.title} <span><i class="fa-solid fa-thumbtack icon-task-status"></i> ${tasks.status.title}</span></p>
                            <p class='description'>${tasks.description}</p>
                            <p class='create'>Создано <b>${tasks.create}</b></p>
                            <p class='dedline'>Срок сдачи <b style="color: #a52a2a;">${tasks.dedline}</b></p>`;
            div.classList.add('task')
            document.body.appendChild(div)
            div.appendChild(img)
        }

        // Скрыть полное описание задачи
        function hidetask(tasks) {
            const task = document.querySelector('.task');
            const back = document.querySelector('.taskBack');
            if (task && back) {
                task.remove();
                back.remove();
            }
            var taskSmall = document.getElementById(tasks.id)
            taskSmall.style.pointerEvents = 'auto'
            taskSmall.style.opacity = '1'
        }

        // Показать кнопку удаления задачи при наведении
        function del(id) {
            var task = document.getElementById(id)
            var p = task.querySelectorAll('p')
            p.forEach(function(p_block) {
                p_block.style.display = 'block'
            }); 
        }

        // Скрыть кнопку удаления при уходе курсора с задачи
        function delout(id) {
            var task = document.getElementById(id)
            var p = task.querySelectorAll('p')
            p[2].style.display = 'none'
        }

        // Удаление задачи
        function deleteTask(id, ind) {
            // Проверяем есть ли задачи в массиве
            if (this.tasks.filter(task => task.project === this.projects[ind].id).length === 0) {
            var indexid = 'prefix-' + ind
            var tasksBlock = document.getElementById(indexid)
            tasksBlock.innerHTML = `<p class="project-title">${this.projects[ind].title}</p><p class="noTasks"><i class="fa-regular fa-circle-dot silver"></i> В этом проекте еще нет задач</p>`
            } 
            // Если есть, удаляем необходимую задачу
            else {
                this.tasks = this.tasks.filter(task => task.id !== id);
                axios.delete(`http://localhost:8000/content/tasks/${id}/delete/`)
            }
        }

        function openWindowAddTask(project, ind) {
            var addTask= document.getElementById('addTask')
            addTask.style.display = 'block'
            var addTask= document.getElementById('addTaskBack')
            addTask.style.display = 'block'
            this.projectid = project.id
        }

        function closeWindowAddTask() {
            var addTask= document.getElementById('addTask')
            addTask.style.display = 'none'
            var addTask= document.getElementById('addTaskBack')
            addTask.style.display = 'none'
        }

        return {
            conRes,
            projects,
            tasks,
            projectid,
            showtask,
            hidetask,
            del,
            delout,
            deleteTask,
            openWindowAddTask,
            closeWindowAddTask,
            onDrag,
            onDragEnd,
            onDrop
        }
    },

    methods: {
        addTask(data){
            this.closeWindowAddTask()
            this.conRes()

        }
    },

    mounted() {
        this.conRes()
    },
    computed: {
    ...mapGetters(['TOKEN_GETTER'])
    },
    watch: {
        TOKEN_GETTER: function(New, Old) {
            this.conRes()
        }
    }
}
</script>


<style>

.hide {
    display: none;
}

#addTask {
    display: none;
    position: fixed;
    left: 200px;
    right: 200px;
    bottom: 150px;
    top: 150px;
    z-index: 10;
    animation-name: task;
    animation-duration: 1s;
    animation-delay: .5s;
    animation-fill-mode: both;
    box-shadow: 0px 0px 40px black;
}

#addTaskBack {
    background: rgba(0, 0, 0, 0.596);
    position: fixed;
    left: 0px;
    right: 0px;
    bottom: 0px;
    top: 0px;
    display: none;
    transition: all 2s;
    animation-name: taskBack;
    animation-duration: .5s;
    animation-fill-mode: both;
}

.project-title {
    font-size: 24px;
    margin-bottom: 20px;
    margin-left: 5px;
}

.genTasks {
    display: flex;
    justify-content:flex-start;
    flex-wrap: wrap;
}

.task-small {
    width: 120px;
    position: relative;
    margin-bottom: 10px;
}

.task-small:hover .title-small {
    color: blueviolet;
    cursor: pointer;
}

.task-small:hover .img-small {
    background-color: rgb(206, 153, 255);
    cursor: move;
}

.task-small:hover .gray {
    color: rgb(133, 64, 133);
}

.img-small{
    background-color: rgb(230, 230, 230); 
    overflow: hidden;
    margin: 0 20px 5px 20px;
    width: 80px;
    height: 80px;
    padding: 10px;
    border-radius: 20px;
    font-size: 60px;
    text-align: center;
    line-height: 30px;
    color: rgb(100, 100, 100);
}

.gray {
    color: rgb(165, 165, 165);
}



.img-small img {
    width: 60px;
    height: 60px;
    top: 10px;
    right: 10px;
}

.task-small .title-small {
    font-size: 12px;
    font-weight: normal;
    width: 120px;
    text-align: center;
}

.task-small .delete {
    display: none;
    position: absolute;
    top: -5px;
    right: 15px;
}

.task-small .delete:hover {
    cursor: pointer;
    font-size: 20px;
    margin: -5px -5px 0 0;

}

.task {
    margin-bottom: 10px;
    overflow-y: scroll;
    background-color: rgb(255, 255, 255);
    border-radius: 15px;
    padding: 20px;
    position: fixed;
    opacity: 0;
    left: 200px;
    right: 200px;
    bottom: 50px;
    top: 50px;
    animation-name: task;
    animation-duration: 1s;
    animation-delay: .5s;
    animation-fill-mode: both;
    box-shadow: 0px 0px 40px black;
}

@keyframes task {
    from {top: 50px; bottom: 50px; opacity: 0;}
    to {top: 150px; bottom: 150px; opacity: 1;}
}

.taskBack {
    background: rgba(0, 0, 0, 0.596);
    position: fixed;
    left: 0px;
    right: 0px;
    bottom: 0px;
    top: 0px;
    transition: all 2s;
    animation-name: taskBack;
    animation-duration: .5s;
    animation-fill-mode: both;
}

@keyframes taskBack {
    from {opacity: 0;}
    to {opacity: 1;}
}

.task .title {
    margin-top: 0px;
    font-size: 18px;
}

.task .title span {
    color: forestgreen;
    padding-left: 20px;
}

.icon-task-status {
    color: forestgreen;
    font-size: 15px;
}

.task .description {
    margin-top: 15px;
    font-weight: normal;
}

.task img {
    width: 30px;
    float: right;
    top: 20px;
    right: 20px;
    position: absolute;
}

.task .create {
    font-weight: lighter;
    font-size: 14px;
    margin-top: 10px;
    position: absolute; 
    bottom: 20px;
    left: 20px;
}

.task .dedline {
    font-weight: lighter;
    font-size: 14px;
    bottom: 20px;
    right: 20px;
    position: absolute; 
    color: #a52a2a;
}

.task .dedline span {
    font-weight: bold;
    color: brown;
}

/* .tasks:last-child .task:last-child {
    margin-bottom: 0px;
} */

.task .close {
    position: absolute;
    top: -5px;
    right: 0px;
}
.task .close:hover {
    cursor: pointer;
}

.noTasks {
    margin-top: -10px;
    margin-bottom: 10px;
    color:rgb(114, 114, 114);
    font-weight: normal;
}

.silver {
    color:rgb(114, 114, 114);
}

::-webkit-scrollbar {
  background: rgba(0, 0, 0, 0);
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0);
}

::-webkit-scrollbar-thumb {
  background: rgba(0, 0, 0, 0);
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 0, 0, 0);
}

</style>
