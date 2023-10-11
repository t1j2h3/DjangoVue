<template>
  <div class="infor_manage">
    <el-container style="height: 595px; border: 1px solid #eee; width: 100%">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-active="this.$router.path" router>
          <el-menu-item index="/f3" @click="fmessage()">
            <span slot="title">申请信息</span>
          </el-menu-item>
          <el-menu-item index="/g3" @click="gmessage()" v-show="file">
            <span slot="title">公示文件上传</span>
          </el-menu-item>
          <el-menu-item index="/h3" @click="hmessage()" v-show="power">
            <span slot="title">权限管理</span>
          </el-menu-item>
          <el-menu-item index="/i3" @click="imessage()" v-show="organization">
            <span slot="title">组织管理</span>
          </el-menu-item>
          <el-menu-item index="/j3" @click="jmessage()" v-show="pwdreset">
            <span slot="title">重置密码</span>
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
            <el-breadcrumb-item>信息管理</el-breadcrumb-item>
            <el-breadcrumb-item>{{ message }}</el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>
        <keep-alive>
          <el-main style="margin-top: -14px; height: 588px">
            <router-view></router-view>
          </el-main>
        </keep-alive>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      role: "",
      power: false,
      file: false,
      organization: false,
      pwdreset:false
    };
  },
  mounted() {
    const val = JSON.parse(localStorage.getItem("id"));
    if (val > 2) {
      this.power = true;
      this.file = true;
      this.organization = true;
    }
    if(val==2)
    {
      this.pwdreset=true;
    }
  },
  methods: {
    amessage() {
      this.message = "入党申请人";
    },
    bmessage() {
      this.message = "入党积极分子";
    },
    cmessage() {
      this.message = "发展对象";
    },
    dmessage() {
      this.message = "预备党员";
    },
    emessage() {
      this.message = "正式党员";
    },
    fmessage() {
      this.message = "申请信息";
    },
    gmessage() {
      this.message = "文件上传";
    },
    hmessage() {
      this.message = "权限管理";
    },
    imessage() {
      this.message = "组织管理";
    },
    jmessage() {
      this.message = "重置密码";
    },
  },
};
</script>

<style>
.infor_manage {
  width: 100%;
  height: 100%;
  background-color: #fff;
}
</style>

