<template>
  <div class="Party_lecture_style">
    <div class="title">
      <span>往届去向悉知</span>
      <el-divider class="title_divider"></el-divider>
      <div class="pl_more">
        <span
          class="pl_more_span"
          style="position: relative; text-decoration: none; font-size: 14px"
          @click="gotofile()"
        >更多</span
        >
        <i class="el-icon-arrow-right" style="margin-top: 2px"></i>
      </div>
    </div>
    <div
      class="content"
      v-for="item in Party_lecture_style_list.slice(0,8)"
      :key="item.id"
    >
     <el-row class="c_row">
       <el-col :span="16" style="display: flex; justify-content: center;">
         <span style="font-size:14px;">{{ item.title }}</span>
       </el-col>
       <el-col :span="6" style="margin-left: auto;">
         <a :href="item.link" style="font-size:14px;">查看详情</a>
       </el-col>
     </el-row>

      <el-divider class="content_divider"></el-divider>
    </div>

  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      Party_lecture_style_list: [
        {
          id: 1,
          title: "22届毕业生去向",
          link: "./files",
        },
        {
          id: 2,
          title: "21届毕业生去向",
          link: "./files",
        },
        {
          id: 3,
          title: "20届毕业生去向",
          link: "./files",
        },
        {
          id: 4,
          title: "19届毕业生去向",
          link: "./files",
        },
        {
          id: 5,
          title: "18届毕业生去向",
          link: "./files",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style>
.Party_lecture_style {
  background: white;
  width: 100%;
}

.title_divider {
  background: rgb(255, 98, 0);
  width: 80px;
}

.content_divider {
  width: 364px;
}

.title {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.el-col-18 {
  display: flex;
  justify-content: start;
  align-items: flex-start;
  text-align: start;
}

.pl_more {
  display: flex;
  margin-left: 300px;
  margin-top: -40px;
}

.pl_more_span:before {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  height: 2px;
  width: 100%;
  background: #000;
  transform: scale(0);
  transition: all 0.3s;
}

.pl_more_span:hover:before {
  transform: scale(1);
}
</style>
