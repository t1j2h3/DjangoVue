<template>
  <div class="log_main">
    <div class="background">
      <img src="../assets/background.jpg" />
    </div>
    <div class="form_box">
      <div class="login_title">就业预测-综测信息管理平台</div>
      <div class="choice">
        <el-button
          class="user_btn"
          type="text"
          style="color: #fff"
          @click="user_longin()"
          >用户登录</el-button
        >
        <el-button
          class="lowadmin_btn"
          type="text"
          style="color: #fff"
          @click="class_longin()"
          >班级管理员登录</el-button
        >
        <el-button
          class="mediadmin_btn"
          type="text"
          style="color: #fff"
          @click="collage_longin()"
          >院管理员登录</el-button
        >
        <el-button
          class="highadmin_btn"
          type="text"
          style="color: #fff"
          @click="school_longin()"
          >校管理员登录</el-button
        >
      </div>
      <el-form
        :model="ruleForm"
        :rules="rules"
        ref="ruleForm"
        label-width="80px"
        class="form"
        :hide-required-asterisk="false"
      >
        <el-form-item :label="mess_s" prop="account ">
          <el-input
            v-model="ruleForm.account"
            :placeholder="mess_i"
            hide-required-asterisk="true"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password ">
          <el-input
            v-model="ruleForm.password"
            placeholder="请输入密码"
            type="password"
          ></el-input>
        </el-form-item>

        <el-form-item prop="verifycode" label="验证码">
          <el-input
            v-model="ruleForm.verifycode"
            placeholder="请输入验证码"
            class="identifyinput"
          >
          </el-input>
        </el-form-item>
        <el-form-item>
          <div class="identifybox">
            <div @click="refreshCode">
              <s-identify :identifyCode="identifyCode"></s-identify>
            </div>
            <el-button @click="refreshCode" type="text" class="textbtn"
              >看不清，换一张</el-button
            >
          </div>
        </el-form-item>

        <el-form-item class="login_btn">
          <el-button class="login_button" @click="submitForm('ruleForm')"
            >登录</el-button
          >
          <el-button @click="registerForm('ruleForm')">注册</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>


<script>
import SIdentify from "@/views/Identify.vue";
import $ from "jquery";
export default {
  props: {},
  components: {
    SIdentify,
  },
  data() {
    /* 自定义验证码规则 */
    const validateVerifycode = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入验证码"));
      } else if (value !== this.identifyCode) {
        callback(new Error("验证码不正确!"));
        this.refreshCode();
      } else {
        callback();
      }
    };
    // const erraccount = (rule, value, callback) => {
    //   if (value === "") {
    //     this.refreshCode();
    //   } else {
    //     callback();
    //   }
    // };
    // const errpassword = (rule, value, callback) => {
    //   if (value === "") {
    //     this.refreshCode();
    //   } else {
    //     callback();
    //   }
    // };
    return {
      id: 1,
      mess_p: "student_num",
      mess_s: "学号",
      mess_i: "请输入学号",
      token: "",
      ruleForm: {
        account: "",
        password: "",
      },
      identifyCodes: "1234567890abcdefghijklmnopqrstuvwxyz",
      identifyCode: "",
      student_mean: [],
      rules: {
        account: [
          { required: true, message: "请输入学号或账号", trigger: "blur" },
          { message: "学号为12位", trigger: "blur" },
        ],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          { message: "请输入密码", trigger: "blur"},
        ],
        verifycode: [
          {
            required: true,
            trigger: "blur",
            validator: validateVerifycode,
          },
        ],
      },
    };
  },
  mounted() {
    this.identifyCode = "";
    this.makeCode(this.identifyCodes, 4);
    history.pushState(null, null, document.URL);
    if (window.history && window.history.pushState) {
      $(window).on("popstate", function () {
        window.history.pushState("forward", null, "");
        window.history.forward(1);
      });
      window.history.pushState("forward", null, ""); //在IE中必须得有这两行
      window.history.forward(1);
    }
  },
  methods: {
    changeText(item) {
      // 将对象格式化成字符串
      var test = JSON.stringify(item); // JSON.stringify()用于将JavaScript对象或值转换为JSON字符串
      var test2 = test.slice(1, test.length - 1);
      var test3 = [];
      for (var i = 0; i < test2.length; i++) {
        test3.push(test2[i].replace('"', ""));
      }
      for (var j = 0; j < test3.length; j++) {
        if (test3[j] === "") {
          test3.splice(j, 1);
        }
      }
      this.token = test3.join("");
    },
    user_longin() {
      this.id = 1;
      this.mess_s = "账号";
      this.mess_i = "请输入账号";
      this.ruleForm.account = "";
      this.ruleForm.password = "";
      this.refreshCode();
    },
    class_longin() {
      this.id = 2;
      this.mess_s = "帐号";
      this.mess_i = "请输入班级管理员帐号";
      this.ruleForm.account = "";
      this.ruleForm.password = "";
      this.refreshCode();
    },
    collage_longin() {
      this.id = 3;
      this.mess_s = "帐号";
      this.mess_i = "请输入院管理员帐号";
      this.ruleForm.account = "";
      this.ruleForm.password = "";
      this.refreshCode();
    },
    school_longin() {
      this.id = 4;
      this.mess_s = "帐号";
      this.mess_i = "请输入校管理员帐号";
      this.ruleForm.account = "";
      this.ruleForm.password = "";
      this.refreshCode();
    },
    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          if (this.id == 1) {
            const res = await this.$http.post("/user/login/", this.ruleForm, {
              withCredentials: true,
            });
            if (res.data.status == true) {
              localStorage.setItem(
                "account",
                JSON.stringify(this.ruleForm.account)
              );
              localStorage.setItem("id", JSON.stringify(this.id));
              localStorage.setItem(
                "from_college",
                JSON.stringify(res.data.from_college)
              );
              this.changeText(res.data.token);
              localStorage.setItem("token", this.token);
              const res1 = await this.$http.get(
                "/user/get1/" + this.ruleForm.account
              );
              localStorage.setItem("name", JSON.stringify(res1.data.name));
              this.$router.push({ path: "/Main" }).catch(() => {});
            } else {
              this.$message.error(res.data.errors);
            }
          } else if (this.id == 2) {
            const res = await this.$http.post(
              "lowadmin/login/",
              this.ruleForm,
              {
                withCredentials: true,
              }
            );
            console.log(res);
            if (res.data.status == true) {
              localStorage.setItem(
                "account",
                JSON.stringify(this.ruleForm.account)
              );
              localStorage.setItem("id", JSON.stringify(this.id));
              localStorage.setItem(
                "from_class",
                JSON.stringify(res.data.from_class)
              );
              localStorage.setItem(
                "from_college",
                JSON.stringify(res.data.from_college)
              );
              this.changeText(res.data.token);
              localStorage.setItem("token", this.token);
              this.$router.push({ path: "/Main" }).catch(() => {});
            } else {
              this.$message.error(res.data.errors);
            }
          } else if (this.id == 3) {
            const res = await this.$http.post(
              "mediuadmin/login/",
              this.ruleForm,
              {
                withCredentials: true,
              }
            );
            console.log(res);
            if (res.data.status == true) {
              localStorage.setItem(
                "account",
                JSON.stringify(this.ruleForm.account)
              );
              localStorage.setItem("id", JSON.stringify(this.id));
              localStorage.setItem(
                "from_college",
                JSON.stringify(res.data.from_college)
              );
              this.changeText(res.data.token);
              localStorage.setItem("token", this.token);
              this.$router.push({ path: "/Main" }).catch(() => {});
            } else {
              this.$message.error(res.data.errors);
            }
          } else {
            const res = await this.$http.post(
              "highadmin/login/",
              this.ruleForm,
              {
                withCredentials: true,
              }
            );
            console.log(res);
            if (res.data.status == true) {
              localStorage.setItem(
                "account",
                JSON.stringify(this.ruleForm.account)
              );
              localStorage.setItem("id", JSON.stringify(this.id));
              this.changeText(res.data.token);
              localStorage.setItem("token", this.token);
              this.$router.push({ path: "/Main" }).catch(() => {});
            } else {
              this.$message.error(res.data.errors);
            }
          }
        } else {
          this.$message.error("登录失败");
          return false;
        }
      });
    },
    registerForm(formName) {
      this.$router.push({ path: "/Register" }).catch(() => {});
    },
    randomNum(min, max) {
      return Math.floor(Math.random() * (max - min) + min);
    },
    // 切换验证码
    refreshCode() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
    },
    makeCode(o, l) {
      for (let i = 0; i < l; i++) {
        this.identifyCode +=
          this.identifyCodes[this.randomNum(0, this.identifyCodes.length)];
      }
      console.log(this.identifyCode);
      /* alert(this.identifyCode) */
    },
  },
};
</script>

<style>
.log_main {
  display: flex;
  height: 690px;
  width: 100%;
}
.form_box {
  width: 100%;
  height: 450px;
  margin-top: 50px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  /* background-image: linear-gradient(to right, #ee3535, #f16464); */
  position: absolute;
  border-radius: 50px;
  /* 设置绝对定位 */
  left: 50%;
  /* 距离左50% */
  top: 50%;
  /* 距离上50% */
  transform: translate(-50%, -50%);
  /* 回退上，左50% */
}
.user_btn:focus {
  background: #ef7575;
}
.lowadmin_btn:focus {
  background: #ef7575;
}
.mediadmin_btn:focus {
  background: #ef7575;
}
.highadmin_btn:focus {
  background: #ef7575;
}
.form {
  margin-top: 50px;
  width: 380px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.login_title {
  font-size: 65px;
  width: 100%;
  display: flex;
  justify-content: space-around;
  color: #fff;
  margin-top: 50px;
}
.background {
  display: flex;
  justify-content: space-around;
  margin-left: 0px;
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
}
.login_button {
  background-color: #f04633;
  color: #fff;
}
.el-form-item__label {
  color: #303133;
  font-size: 14px;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
}
.identifybox {
  display: flex;
  justify-content: space-around;
  margin-top: 7px;
}
.identify {
  display: flex;
  justify-content: space-around;
}
.textbtn {
  color: #fff;
}
.choice {
  width: 25%;
  display: flex;
  margin-left: 500px;
}
</style>
