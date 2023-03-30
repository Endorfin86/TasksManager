<template>
<p id="formAdd">
<p>Форма добавления задач</p>
<label for="form-title">Название</label>
<input v-model="formTitle" name="" id="form-title" type="text">

<!-- Тип объекта -->
<input v-model="formType" name="" type="hidden">

<label for="form-description">Описание</label>
<textarea v-model="formDescription" name="" id="form-description" type="text"></textarea>


<label for="form-dedline">Дата сдачи</label>
<input v-model="formDate" name="" id="form-dedline" type="date">

<label for="form-icon">Иконка</label>
<select v-model="formIcon" name="" id="form-icon">
    <option value="1">homework</option>
    <option value="2">desktop</option>
    <option value="3">colorwall</option>
    <option value="4">geometry</option>
    <option value="5">sizepic</option>
</select>

<!-- Статус задачи -->
<input v-model="formStatus" name="" type="hidden">

<!-- Автор -->
<input v-model="formAuthor" name="" type="hidden">

<button @click="addTask">Добавить</button>
</p>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
    name: 'AddTask',

    data() {
        return {
            formform: 2024
        }
    },

    props: {
        projid: {}
    },

    setup(props, ctx){
        // получаем текущую дату в формате yyyy-MM-dd
        const currentDate = new Date().toLocaleDateString();
        const [day, month, year] = currentDate.split('.').map(Number);
        const dateObject = new Date(year, month - 1, day);
        const newYear = dateObject.getFullYear();
        const newMonth = ('0' + (dateObject.getMonth() + 1)).slice(-2);
        const newDay = ('0' + dateObject.getDate()).slice(-2);
        const newDateString = `${newYear}-${newMonth}-${newDay}`;
        
        const formTitle = ref()
        const formType = ref('Задача')
        const formDescription = ref()
        const formDate = newDateString
        const formIcon = ref()
        const formStatus = ref(1)
        const formAuthor = ref(localStorage.getItem('id'))
        
        async function addTask() {
            
            const data = {
                title: this.formTitle,
                type: this.formType,
                description: this.formDescription,
                dedline: this.formDate,
                project: props.projid,
                icon: this.formIcon,
                status: this.formStatus,
                author: this.formAuthor 
            }
            ctx.emit('addTask', data)
            
            axios.post('http://localhost:8000/content/tasks/add/', data)
            .then(response => {
                console.log(`Успешно ${response.data}`) // Обработка успешного ответа
            })
            .catch(error => {
                console.error(`Неудача ${error}`) // Обработка ошибки
            })
            this.formTitle = ''
            this.formDescription = ''
            this.formIcon = ''
            this.formDate = newDateString
        }
        return {
            addTask,
            formTitle,
            formType,
            formDescription,
            formDate,
            formIcon,
            formStatus,
            formAuthor,
            currentDate


        }
    }
}
</script>

<style>
#formAdd {
    width: 100%;
}

#formAdd input, #formAdd textarea, #formAdd select {
  margin-bottom: 10px;
  width: 100%
}

#formAdd button {
    margin-top: 10px;
    float: right;
}

#formAdd label {
  color: rgb(129, 129, 129);
  font-size: 12px;
  padding-left: 10px;
 } 
</style>





