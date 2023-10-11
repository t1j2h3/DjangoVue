<template>
  <div>
    <slideshow style="width: 100%; height: 440px"></slideshow>
    <div class="top">
      <el-row
        :gutter="20"
        style="
          width: 100%;
          display: flex;
          justify-content: space-around;
          height: 400px;
        "
      >
        <el-col :span="8"><notice></notice></el-col>
        <el-col :span="8">
          <Party_lecture_style></Party_lecture_style>
        </el-col>
      </el-row>
    </div>
    <div class="buttom">
      <el-row
        :gutter="20"
        style="
          width: 100%;
          display: flex;
          justify-content: space-around;
          height: 400px;
        "
      >
        <el-col :span="8"><Party_history_study ></Party_history_study ></el-col>
        <el-col :span="8">
          <membership_process></membership_process>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import slideshow from "@/components/Main_comp/main_comp_child/slideshow.vue";
import notice from "@/components/Main_comp/main_comp_child/notice.vue";
import Party_lecture_style from "@/components/Main_comp/main_comp_child/Party_lecture_style.vue";
// import Party_history_study from "@/components/Main_comp/main_comp_child/Party_history_study.vue";
// import membership_process from "@/components/Main_comp/main_comp_child/membership_process.vue";

export default {
  props: {},
  components: {
    slideshow,
    notice,
    Party_lecture_style,
    // membership_process,
    // Party_history_study
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style>
.top {
  width: 100%;
  align-items: center;
  height: 400px !important;
}
.el-divider--horizontal {
  margin: 10px !important;
}
.buttom {
  width: 100%;
  align-items: center;
  height: 400px !important;
}
</style>
