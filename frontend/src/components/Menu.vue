<template>
<div id="menu">
    <div class="menu-block"><a href=""><i class="fa-solid fa-briefcase"></i>&ensp;Задачи</a></div>
    <div class="menu-block"><a href=""><i class="fa-solid fa-box-archive"></i>&ensp;Материалы</a></div>
    <div class="menu-block"><a href=""><i class="fa-solid fa-folder-open"></i>&ensp;Файлы</a></div>
</div>
</template>

<script>

</script>

<style>
#menu {
  background-color: white;
  margin-top: 10px;
  padding: 20px;
  border-radius: 30px;
  width: 100%;
  box-shadow: 0px 20px 20px rgba(0, 0, 0, 0.192);
}

.menu-block {
    padding: 10px 0;
    transition: all .5s;
}
.menu-block:hover {
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.13);
    border-radius: 30px;
}
.menu-block a {
    text-decoration: none;
    transition: all .5s;
}
.menu-block:hover a {
    color: #4ba18a;
    padding-left: 15px;
}
</style>