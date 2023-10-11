<template>
  <div class="all_title">
    <div class="image">
      <!-- <img src="../assets/logo.jpg" /> -->
    </div>
    <div class="R_text">
      就 业 预 测 - 综 测 信 息 管 理 平 台
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {};
  },
  methods: {},
};
</script>

<style>
.all_title {
  background-color: #001862;
  height: 70px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image {
  display: flex;
  width: 40px;
  height: 40px;
  position: -1;
  margin-left: 150px;
}

.R_text {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 40px;
  color: #fff;
}
</style>
