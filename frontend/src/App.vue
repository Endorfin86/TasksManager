<template>
  <header>
    <p id="logo">Логотип</p>
  </header>
  <main>
    <aside>
      <Auth />
      <Menu />
    </aside>
    <div id="content">
      <Resourse />
    </div>
  </main>
</template>

<script>
import Auth from './components/Auth.vue'
import Resourse from './components/Resourse.vue'
import Menu from './components/Menu.vue'
export default {
  components: {
    Auth,
    Resourse,
    Menu,
  },
}

</script>

<style>
* {
  padding: 0px;
  margin: 0px;
  box-sizing: border-box;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #3b444e;
  font-weight: bold;
}

body {
  background-color: #f5f7fb;
}

header {
  background-color: #224b6f;
  color: white;
  padding: 20px 50px 100px 50px;
  border-bottom-left-radius: 150px;
  border-bottom-right-radius: 150px;
  position: absolute;
  top: 0px;
  width: 100%;
  z-index: -1;

}

header #logo {
  color: white;
  font-weight: bold;
  font-size: 20px;
}

@media (width <= 1366px) {
main {
  display: flex;
  margin: 100px 50px 100px 50px;
}
}

@media (width > 1366px) {
main {
  display: flex;
  margin: 100px 300px 100px 300px;
} 
} 

aside {
  width: calc(30% - 20px);
  margin-right: 20px;
}

#content {
  width: 70%;
}

#content > div {
  background-color: #ffffff;
  padding: 20px 20px 20px 20px;
  margin-bottom: 10px;
  border-radius: 30px;
  box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.192);
  overflow: hidden;
  opacity: 0;
  animation-name: div-content;
  animation-duration: .5s;
  animation-delay: .5s;
  animation-fill-mode: both;
}

@keyframes div-content {
  from {margin-top: -20px; opacity: 0;}
  to {margin-top: 0px; opacity: 100%;}
}

button {
  background-color: #63d2b4;
  border: 0px;
  border-radius: 30px;
  padding: 8px 40px;
  color: white;
  font-size: 14px;
}

button:hover {
  background-color: #4ba18a;
  cursor: pointer;
}

input {
  border: 1px solid silver;
  border-radius: 30px;
  padding: 8px 10px;
  outline: none;
  font-size: 14px;
  display: block;
  font-weight: normal;
}

select {
  border: 1px solid silver;
  border-radius: 30px;
  padding: 8px 10px;
  outline: none;
  font-size: 14px;
  display: block;
  font-weight: normal;
}

option {
  border: 1px solid silver;
  border-radius: 30px;
  padding: 8px 10px;
  outline: none;
  font-size: 14px;
  display: block;
  font-weight: normal;
}

textarea {
  margin-bottom: 10px;
  border: 1px solid silver;
  border-radius: 15px;
  padding: 8px 10px;
  outline: none;
  min-height: 150px;
  max-height: 400px;
  resize: vertical;
  font-size: 14px;
  display: block;
  font-weight: normal;
}

form {
  background-color: white;
  padding: 20px;
  border-radius: 30px;
  width: 100%;
  box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.192);
}

form label {
  color: rgb(129, 129, 129);
  font-size: 12px;
  padding-left: 10px;
}

form input, form textarea, form select {
  margin-bottom: 10px;
  width: 100%
}

form button {
  margin-top: 10px;
}
</style>
