<template>
  <div class="wraper">
    <div
      v-for="pr of profiles"
      :key="pr.name"
      class="card"
    >
      <img :src="pr.photo" :alt="pr.name">
      <div>
        <h2>{{ pr.name }}</h2>
        <p>{{ pr.role }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const profiles: {
  photo: string
  name: string
  role: string
}[] = [{
  photo: '/photos/Luda.png',
  name: 'Олесова Людмила',
  role: 'UX/UI Designer'
}, {
  photo: '/photos/Artem.png',
  name: 'Мирошниченко Артём',
  role: 'Frontend Developer'
}, {
  photo: '/photos/Mike.png',
  name: 'Смирнов Михаил',
  role: 'ML-engineer'
}, {
  photo: '/photos/Ruslan.png',
  name: 'Гулянов Руслан',
  role: 'Data Scientist'
}, {
  photo: '/photos/Alex.png',
  name: 'Чернов Александр',
  role: 'Backend Developer'
}]
</script>

<style scoped lang="scss">
div.card img {
  border-radius: 100%;
  width: 155px;
}
div.card:nth-child(odd) img {
  margin-right: 40px;
}
div.card:nth-child(even) img {
  margin-left: 40px;
}
div.card {
  display: flex;
  align-items: center;
}
div.card:nth-child(odd) {
  flex-direction: row;
}
div.card:nth-child(even) {
  flex-direction: row-reverse;
}
h2 {
  color: #E50707;
}
.wraper {
  padding: 0 45px;
}
.card p {
  font-size: 18px;
}
</style>
