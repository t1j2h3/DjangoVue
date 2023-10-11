<template>
  <div class="main">
    <Register_title> </Register_title>
    <div class="head_right">
      <el-button
        type="text"
        icon="el-icon-edit"
        class="h_btn"
        @click="cgpwdVisible = true"
        >修改密码</el-button
      >
      <!-- 修改密码界面 -->
      <el-dialog
        title="修改密码"
        width="30%"
        :visible.sync="cgpwdVisible"
        :close-on-click-modal="false"
        :modal-append-to-body="false"
        @close="handleCloseDialog"
      >
        <el-form
          :model="dataForm"
          label-width="100px"
          :rules="dataFormRules"
          ref="dataForm"
          label-position="right"
        >
          <el-form-item label="旧密码:" prop="oldpassword">
            <el-input
              v-model="dataForm.oldpassword"
              type="password"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item label="新密码:" prop="newpassword" label-width="100px">
            <el-input
              v-model="dataForm.newpassword"
              type="password"
              auto-complete="off"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="确认密码:"
            prop="checkpassword"
            label-width="100px"
          >
            <el-input
              v-model="dataForm.checkpassword"
              type="password"
              auto-complete="off"
            ></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer" style="margin-top: 5px">
          <el-button type="primary" @click.native="handleUpdataPw"
            >确认</el-button
          >
          <el-button @click.native="cgpwdVisible = false" type="danger"
            >取消</el-button
          >
        </div>
      </el-dialog>

      <el-button
        type="text"
        icon="el-icon-switch-button"
        class="h_btn"
        @click="exit()"
        >退出</el-button
      >
    </div>
    <div class="row_box">
      <el-row type="flex" class="row-bg" style="height: 40px">
        <el-col :span="2" v-for="index of menulist" :key="index.id">
          <div class="row1">
            <el-button
              class="btn"
              @click="Fn(index.method)"
              type="text"
              style="width: 80px"
              >{{ index.text }}</el-button
            >
          </div></el-col
        >
      </el-row>
    </div>

    <div class="comp">
      <keep-alive>
        <component
          :is="currentcomp"
          :counts="allcounts"
          style="height: 100%; background-color: #f6f6f6"
        ></component>
      </keep-alive>
    </div>
  </div>
</template>

<script>
import Register_title from "@/components/Register_title.vue";
import main_comp from "@/components/Main_comp/main_comp.vue";
import infor_change from "@/components/Main_comp/infor_change.vue";
import infor_manage from "@/components/Main_comp/infor_manage.vue";
export default {
  props: {},
  components: {
    Register_title,
    main_comp,
    infor_change,
    infor_manage,
  },
  data() {

    var checkNewPw = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("请再次输入密码"));
      }
      if (this.dataForm.newpassword !== value) {
        callback(new Error("密码不一致"));
      } else {
        callback();
      }
    };
    return {
      menulist: [],
      temp: "",
      cgpwdVisible: false,
      currentcomp: "main_comp",
      allcounts: "",
      cgpwdVisible: false,
      dataForm: {
        oldpassword: "",
        newpassword: "",
        checkpassword: "",
      },
      dataFormRules: {
        oldpassword: [
          {
            required: true,
            message:'请输入旧密码',
            trigger: "blur",
          },
        ],
        newpassword: [
          {
            required: true,
            message:'请输入新密码',
            trigger: "blur",
          },
        ],
        checkpassword: [
          {
            required: true,
            validator: checkNewPw,
            trigger: "blur",
          },
        ],
      },
    };
  },
  mounted() {
    const val = JSON.parse(localStorage.getItem("id"));
    if (val == 1) {
      this.menulist = [
        {
          id: 1,
          text: "首页",
          method: "gomain",
        },
        {
          id: 2,
          text: "信息修改",
          method: "goinfor_change",
        },
      ];
    } else {
      this.menulist = [
        {
          id: 1,
          text: "首页",
          method: "gomain",
        },
        {
          id: 2,
          text: "信息管理",
          method: "goinfor_manage",
        },
      ];
    }
  },
  methods: {
    Fn(method) {
      this[method]();
    },
    exit() {
      // 清除状态保持
      window.localStorage.clear();
      this.$router.push({ path: "/" });
    },
    gomain() {
      this.currentcomp = "main_comp";
    },
    goinfor_manage() {
      this.currentcomp = "infor_manage";
    },
    goinfor_change() {
      this.currentcomp = "infor_change";
    },
    //关闭时候清空表单
    handleCloseDialog() {
      this.$refs.dataForm.resetFields();
    },
    //修改密码，调用接口更改
    handleUpdataPw() {
      this.$refs["dataForm"].validate(async (valid) => {
        if (valid) {
          const tempid = JSON.parse(localStorage.getItem("id"));
          this.temp= JSON.parse(localStorage.getItem("account"));
          let res;
          if (tempid == 1) {
            res = await this.$http.put(
              "user/password/" + this.temp,
              this.dataForm,
              {
                withCredentials: true,
              }
            );
          } else if (tempid == 2) {
            res = await this.$http.put(
              "lowadmin/password/" + this.temp,
              this.dataForm,
              {
                withCredentials: true,
              }
            );
          } else if (tempid == 3) {
            res = await this.$http.put(
              "mediuadmin/password/" + this.temp,
              this.dataForm,
              {
                withCredentials: true,
              }
            );
          } else {
            res = await this.$http.put(
              "highadmin/password/" + this.temp,
              this.dataForm,
              {
                withCredentials: true,
              }
            );
          }
          if (res.status == 200) {
            this.$message({
              message: "修改成功",
              type: "success",
            });
            this.cgpwdVisible = false;
            localStorage.removeItem("token");
            this.$router.push({ path: "/" });
          } else {
            this.$message.error(res.data.entail);
          }
        }
      });
    },
  },
};
</script>

<style>
.main {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  background-color: #f6f6f6;
  width: 100%;
  height: 100%;
}
.head_right {
  display: flex;
  justify-content: right !important;
  margin-top: -50px;
  margin-left: 1200px;
}
.h_btn {
  color: #fff;
}
.h_btn:hover {
  background-color: #f13227 !important;
  color: #fff !important;
}
.row_box {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80%;
  height: 40px;
  margin-top: 10px;
}
.row1 {
  background: #6ee2fb;
  color: #fff;
  width: 100%;
  height: 40px;
}
.row2 {
  background: #f45648;
  width: 100%;
  height: 40px;
  align-items: center;
  display: flex;
  justify-content: center;
}
.row3 {
  background: #f45648;
  width: 100%;
  height: 40px;
}
.row-bg {
  background-color: #6ee2fb;
  width: 100%;
}
.main_btn {
  border: #f13227;
  color: aliceblue;
  font-size: 16px;
  font-weight: bold;
}
.message_btn {
  background-color: #f45648;
  border: #f13227;
  color: aliceblue;
  font-size: 16px;
  font-weight: bold;
}
.btn {
  background-color: #f45648;
  border: #f13227;
  color: aliceblue;
  font-size: 16px;
  font-weight: bold;
}
.btn:hover {
  background-color: #f13227 !important;
  color: #fff !important;
}
.btn:focus {
  background-color: #df1c1d !important;
  color: #fff !important;
}
.main_btn:hover {
  background-color: #f13227 !important;
  color: #fff !important;
}
.main_btn:focus {
  background-color: #df1c1d !important;
  color: #fff !important;
}
.message_btn:hover {
  background-color: #f13227 !important;
  color: #fff !important;
}
.message_btn:focus {
  background-color: #df1c1d !important;
  color: #fff !important;
}
.el-dropdown-link {
  background-color: #f45648;
  border: #f13227;
  color: aliceblue;
  font-size: 16px;
  font-weight: bold;
  align-items: center;
}
.comp {
  width: 80%;
  height: 100%;
}
</style>
