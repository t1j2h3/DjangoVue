<template>
  <el-carousel class="lun_imgs" indicator-position="outside" ref="carousel" @click.native="linkTo" >
    <el-carousel-item v-for="item in imgs" v-bind:key="item.url" style="width: 100%; height: 100%">
      <el-image
      style="width: 100%; height: 100%"
      :src="item.url"
      fit="fill"></el-image>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      imgs: [
        { url: require("@/assets/1.jpg"), link: "http://cpc.people.com.cn/n1/2023/0524/c164113-32693937.html" },
        { url: require("@/assets/2.jpg"), link: "http://edu.people.com.cn/n1/2023/0411/c1006-32661376.html" },
        { url: require("@/assets/3.jpg"), link: "http://finance.people.com.cn/n1/2022/0713/c444648-32474095.html" },
        { url: require("@/assets/4.jpg"), link: "http://finance.people.com.cn/n1/2022/0916/c444648-32527858.html" },
      ],
    };
  },
  methods: {
    linkTo() {
      let activeIndex = this.$refs.carousel.activeIndex;
     window.open(this.imgs[activeIndex].link,"_blank")
    },
  },
};
</script>

<style>
.lun_imgs{
    width: 100%;
    height: 460px !important;
}
.el-carousel__container{
    width: 100%;
    height: 90% !important;
}
</style>
