<template>
  <div class="A_main3">
    <el-form
      :model="ruleForm"
      status-icon
      :rules="rules"
      ref="form3"
      label-width="80px"
      class="demo-ruleForm"
      v-if="flag != undefined"
    >
      <el-form-item label="密码" prop="password">
        <el-input
          type="password"
          v-model="ruleForm.password"
          autocomplete="off"
        ></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="checkpassword">
        <el-input
          type="password"
          v-model="ruleForm.checkpassword"
          autocomplete="off"
        ></el-input>
      </el-form-item>

      <el-form-item label="手机号" prop="phone">
        <el-input v-model="ruleForm.phone" clearable></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    var validatepassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.ruleForm.checkpassword !== "") {
          this.$refs.form3.validateField("checkpassword");
        }
        callback();
      }
    };
    var validatepassword2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.ruleForm.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
    let validatePhone = (rule, value, callback) => {
      /*console.log(rule);
      console.log(value);
      console.log(callback);*/
      if (!value) {
        callback(new Error("手机号不能为空"));
      }
      //使用正则表达式进行验证手机号码
      if (!/^1[3456789]\d{9}$/.test(value)) {
        callback(new Error("手机号不正确"));
      }
      //自定义校验规则 需要调用callback()函数！
      callback();
    };
    return {
      flag: "",
      templist: JSON.parse(localStorage.getItem("list")),
      password: "",
      ruleForm: {
        checkpassword: "",
        phone: "",
      },
      rules: {
        password: [
          { required: true, validator: validatepassword, trigger: "blur" },
        ],
        checkpassword: [
          { required: true, validator: validatepassword2, trigger: "blur" },
        ],
        phone: [{ required: true, validator: validatePhone, trigger: "blur" }],
      },
    };
  },
  methods: {
    validate(callback) {
      //这个ruleFormRef是子组件内部el-form 的ref="ruleFormRef"
      this.$refs.form3.validate((valid) => {
        const temp = Object.assign({}, this.templist, this.ruleForm);
        localStorage.setItem("list", JSON.stringify(temp));
        callback(valid);
      });
    },
  },
};
</script>

<style>
.A_main3 {
  display: flex;
  justify-content: space-around;
  margin-top: 80px;
}
.el-form-item__label {
  color: #303133;
  font-size: 14px;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
}
.num_code {
  display: flex;
  justify-content: space-around;
}
.permit {
  width: 350px;
  font-size: 8px;
}
</style>