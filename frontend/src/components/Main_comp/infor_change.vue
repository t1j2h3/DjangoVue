<template>
  <div class="infor_change">
    <el-container style="height: 595px; border: 1px solid #eee; width: 100%">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-active="currentrouter" router>
          <el-menu-item index="/aa" @click="showrouter()">
            <span slot="title">个人信息</span>
          </el-menu-item>
          <el-menu-item index="/a" @click="showrouter1()">
            <span slot="title">提交成绩单</span>
          </el-menu-item>
          <el-menu-item index="/b" @click="showrouter2()">
            <span slot="title">提交综测信息</span>
          </el-menu-item>
          <el-menu-item index="/c" @click="showrouter3()">
            <span slot="title">就业预测</span>
          </el-menu-item>
          <el-menu-item index="/d" @click="showrouter4()">
            <span slot="title">操作记录</span>
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-container>
        <el-header
          style="
            text-align: center;
            font-size: 14px;
            height: 25px;
            align-items: center;
            display: flex;
            justify-content: start;
          "
          class="router"
        >
          <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/Main' }"
              >首页</el-breadcrumb-item
            >
            <el-breadcrumb-item>信息修改</el-breadcrumb-item>
            <el-breadcrumb-item>{{ message }}</el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>
        <el-main class="change_main">
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  props: ["counts"],
  components: {},
  data() {
    return {
      message: "",
      currentrouter: "",
      role: "",
    };
  },

  mounted() {
    this.$nextTick(() => {
      this.showtext();
    });
  },
  methods: {
    showtext() {
      if (this.counts == "a") {
        this.currentrouter = "/a";
        this.message = "提交成绩单";
      } else if (this.counts == "b") {
        this.currentrouter = "/b";
        this.message = "提交综测信息";
      } else if (this.counts == "c") {
        this.currentrouter = "/c";
        this.message = "就业预测";
      } else if (this.counts == "d") {
        this.currentrouter = "/d";
        this.message = "操作记录";
      }  else {
        this.currentrouter = "/aa";
        this.message = "个人信息";
      }
    },
    showrouter() {
      this.message = "个人信息";
    },
    showrouter1() {
      this.message = "提交成绩单";
    },
    showrouter2() {
      this.message = "提交综测信息";
    },
    showrouter3() {
      this.message = "就业预测";
    },
    showrouter4() {
      this.message = "操作记录";
    },
  },
};
</script>

<style>
.infor_change {
  width: 100%;
  height: 100%;
  background-color: #fff;
}
.router {
  display: flex;
  justify-content: start;
  align-items: center;
  background-color: #e7e3e3;
}
.change_main {
  width: 100%;
  height: 100%;
  background-color: #fff;
  display: flex;
  justify-content: center;
}
</style>
