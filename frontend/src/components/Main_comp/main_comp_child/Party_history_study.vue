<template>
  <div class="Party_history_study">
    <div class="title">
      <span>党史学习</span> <el-divider class="title_divider"></el-divider>
      <div class="ph_more">
        <span
          class="ph_more_span"
          style="position: relative; text-decoration: none; font-size: 14px"
          @click="gotofile()"
          >更多</span
        >
        <i class="el-icon-arrow-right" style="margin-top: 2px"></i>
      </div>
    </div>
    <div
      class="content"
      v-for="item in Party_history_study_list.slice(0, 8)"
      :key="item.id"
    >
      <el-row class="c_row">
        <el-col :span="6" style="margin-left: 10px"
          ><span style="font-size: 14px">{{ item.data }}</span>
        </el-col>
        <el-col :span="16" style="margin-left: 8px; display: flex"
          ><span style="font-size: 14px">{{ item.title }}</span></el-col
        >
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
      Party_history_study_list: [
        {
          id: 1,
          data: "2022-8-15",
          title: "红色旅游为革命老区带来新机遇",
          link: "",
        },
        {
          id: 2,
          data: "2022-8-16",
          title: "党的一大唯一的少数民族代表邓恩铭",
          link: "",
        },
        {
          id: 3,
          data: "2022-8-17",
          title: "“三大纪律、八项注意”",
          link: "",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style>
.Party_history_study {
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
.ph_more {
  display: flex;
  margin-left: 300px;
  margin-top: -40px;
}
.ph_more_span:before {
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
.ph_more_span:hover:before {
  transform: scale(1);
}
</style>