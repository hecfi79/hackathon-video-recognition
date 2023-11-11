<template>
  <div>
    <h1 ref="msg">Попробуйте сейчас!</h1>
    <div class="data-block">
      <div class="standby" v-if="state === 'standby'">
        <button id="uploadButton" @click="open"><h2>Загрузить видео</h2></button>
        <input ref="inp" type="file" id="videoInput" accept="video/*" @change="proceed">
      </div>
      <div class="upload-placeholder" v-else-if="state === 'uploading'">
        <img class="loader" src="/video.gif">
        <p>Загружаем видео и запускаем магию🪄</p>
      </div>
      <div class="result" v-else-if="state === 'done'">
        <!-- <div class="result-vid"></div> -->
        <video width="640" height="360" controls>
          <source :src="sourceVideo" type="video/mp4">
        </video>
        <div class="tabs">
          <div class="tab timing" @click="() => show('time')" :class="{'active': showing === 'time'}">По времени</div>
          <div class="tab percents" @click="() => show('percents')" :class="{'active': showing === 'percents'}">В процентах</div>
        </div>
        <apexchart class="chart" v-if="showing === 'percents'" width="380" type="donut" :options="options" :series="series"></apexchart>
        <div v-else-if="showing === 'time'" class="predictions">
          <div class="row">
            <div class="act">coding</div>
            <div class="timecode">0:00-2:04</div>
          </div>
          <div class="divider"></div>
          <div class="row">
            <div class="act">thinking</div>
            <div class="timecode">2:04-2:12</div>
          </div>
          <div class="divider"></div>
          <div class="row">
            <div class="act">coding</div>
            <div class="timecode">2:12-4:54</div>
          </div>
          <div class="divider"></div>
          <div class="row">
            <div class="act">chatting</div>
            <div class="timecode">4:54-5:00</div>
          </div>
        </div>
      </div>
      <button v-if="state === 'done'" id="resetButton" @click="reset"><h4>Попробовать ещё раз</h4></button>
    </div>
    <div class="err" v-if="err">{{ err }}</div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const inp = ref()

const state = ref<string>('standby')
const err = ref<string>('')
const msg = ref()
const sourceVideo = ref<string>('')
const showing = ref<string>('time')

const options = { labels: ['Apple', 'Mango', 'Orange', 'Watermelon'] }
const series = [44, 55, 13, 33]

const open = () => {
  inp.value.click()
}

const show = (state: string) => {
  console.log(state)
  showing.value = state
}

const proceed = (event: Event) => {
  const inputElement = event.target as HTMLInputElement

  // Проверяем, что inputElement.files не равно null или undefined
  if (inputElement.files?.length) {
    // Обрабатываем изменения в файле
    const selectedFile = inputElement.files[0]
    console.log('Выбран файл:', selectedFile.name)
    state.value = 'uploading'
    msg.value.innerText = 'Подождите...'
    setTimeout(() => {
      state.value = 'done'
      msg.value.innerText = 'Готово!'
    }, 5000)

    // console.log(videoPlayer.value)
    // console.log(URL.createObjectURL(selectedFile))

    sourceVideo.value = URL.createObjectURL(selectedFile)

    // Example: Create object URL from Blob
    // const videoUrl = URL.createObjectURL(blob)

    // Example: Set video source dynamically
    // if (videoPlayer.value) {
    //   const source = document.createElement('source')
    //   source.src = URL.createObjectURL(selectedFile)
    //   source.type = 'video/mp4'
    //   videoPlayer.value.appendChild(source)
    // }
  } else {
    err.value = 'Вы не выбрали файл!'
  }
}
const reset = () => {
  msg.value.innerText = 'Попробуйте сейчас!'
  state.value = 'standby'
}
const base64StringToBlob = (base64String: string, contentType: string) => {
  const sliceSize = 1024
  const byteCharacters = atob(base64String)
  const byteArrays = []

  for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
    const slice = byteCharacters.slice(offset, offset + sliceSize)

    const byteNumbers = new Array(slice.length)
    for (let i = 0; i < slice.length; i++) {
      byteNumbers[i] = slice.charCodeAt(i)
    }

    const byteArray = new Uint8Array(byteNumbers)
    byteArrays.push(byteArray)
  }

  const blob = new Blob(byteArrays, { type: contentType })
  return blob
}
</script>

<style scoped lang="scss">
input {
  display: none;
}
button {
  background-color: #DA1616;
  border: none;
  color: white;
  border-radius: 10px;
  padding: 5px 20px;
}
button:hover {
  cursor: pointer;
}
h1, h2, h3, h4 {
  font-family: RussianRail;
}
h1 {
  text-align: center;
}
.data-block {
  display: flex;
  justify-content: center;
  margin-bottom: 150px;
  flex-direction: column;
  align-items: center;
}
.loader {
  width: 70px;
}
.upload-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.tabs {
  margin: auto;
  margin-top: 20px;
  width: 420px;
  background-color: #EEEEEE;
  border-radius: 20px;
  display: flex;
}

.tabs div.tab {
  width: 50%;
  height: 100%;
  cursor: pointer;
  padding: 10px;
  border-radius: 20px;
  text-align: center;
}

.tabs div.active {
  background-color: #D9D9D9;
}
.row {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}
.predictions, .chart {
  margin: auto;
  margin-top: 25px;
}
.act {
  font-weight: bold;
}
.result-vid {
  height: 200px;
  background-color: gray;
}
#resetButton {
  margin-top: 10px;
}
.divider {
  border-bottom: 1px dashed;
  margin: 4px 0;
}
</style>
