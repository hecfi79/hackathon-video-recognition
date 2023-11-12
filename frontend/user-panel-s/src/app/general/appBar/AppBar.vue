<template>
  <div id="header">
    <div id="navbar">
      <div id="logo">
        <router-link to="/">#команда_хайпа</router-link>
      </div>
      <div id="control">
        <router-link to="/aboutModel">О модели</router-link>
        <router-link to="/aboutUs">О нас</router-link>
      </div>
    </div>
    <h1>Распознавание действий человека по видео</h1>
    <p>Сервис видеоаналитики</p>
  </div>
</template>

<style scoped lang="scss">
#navbar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
#header {
  padding: 30px 140px;
  background: url("../../../assets/img/background.png") no-repeat right bottom;
  color: #fff;
  height: 300px;
}
#control a:last-child {
  margin-left: 60px;
}
h1 {
  // font-family: RussianRail G Pro;
  font-size: 50px;
  font-weight: 700;
  line-height: 57px;
  letter-spacing: 0em;
  text-align: left;
  width: 800px;
  margin-bottom: 10px;
  font-family: RussianRail;
}
p {
  font-size: 25px;
  font-weight: 300;
  line-height: 32px;
  letter-spacing: 0em;
  text-align: left;
  margin: 0;
}
a, a:visited {
  color:#fff;
  text-decoration: none;
}

</style>
