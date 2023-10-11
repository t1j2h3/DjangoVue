<template>
  <div class="A_main2">
    <el-form :model="ruleForm" :rules="rules" ref="form2" label-width="80px">
      <el-form-item label="学号" prop="account" size="small">
        <el-input
          v-model.number="ruleForm.account"
          size="small"
          style="width: 300px"
        ></el-input>
      </el-form-item>

      <el-form-item
        label="姓名"
        prop="name"
        size="small"
        style="margin-top: -5px"
      >
        <el-input v-model="ruleForm.name" size="small"></el-input>
      </el-form-item>

      <el-form-item
        label="性别"
        prop="gender"
        size="small"
        style="margin-top: -5px"
      >
        <el-input v-model="ruleForm.gender" size="small" disabled></el-input>
      </el-form-item>

      <el-form-item
        label="民族"
        prop="nation"
        size="small"
        style="margin-top: -5px"
      >
        <el-input
          v-model="ruleForm.nation"
          placeholder="如：满族"
          size="small"
        ></el-input>
      </el-form-item>

      <el-form-item
        label="班级"
        prop="classx"
        size="small"
        style="margin-top: -5px"
      >
        <el-input
          v-model="ruleForm.classx"
          placeholder="如：20计算机科学与技术二班"
          size="small"
        ></el-input>
      </el-form-item>

      <el-form-item
        label="身份证"
        prop="identity_card"
        size="small"
        style="margin-top: -5px"
      >
        <el-input v-model="ruleForm.identity_card" size="small"></el-input>
      </el-form-item>

      <el-form-item
        label="出生日期"
        prop="birthday"
        size="small"
        style="margin-top: -5px"
      >
        <el-input v-model="ruleForm.birthday" size="small" disabled></el-input>
      </el-form-item>

      <el-form-item
        label="籍贯"
        prop="native"
        size="small"
        style="margin-top: -5px"
      >
        <el-input
          v-model="ruleForm.native"
          placeholder="如：湖南湘潭"
          size="small"
        ></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    var validatePass = (rule, value, callback) => {
      let reg = this.checkCard();
      if (!value) {
        callback(new Error("请输入身份证"));
      } else if (!reg) {
        callback(new Error());
      } else {
        callback();
      }
    };
    return {
      templist:JSON.parse(localStorage.getItem("list")),
      Wi: [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2],
      ValideCode: [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2],
      id_right:false,
      ruleForm: {
        account: "",
        name: "",
        gender: "",
        nation: "",
        classx: "",
        identity_card: "",
        birthday: "",
        native: "",
      },
      rules: {
        account: [
          { required: true, message: "请输入正确学号", trigger: "blur" },
        ],
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }],
        nation: [{ required: true, message: "请输入民族", trigger: "blur" }],
        classx: [{ required: true, message: "请输入班级", trigger: "blur" }],
        identity_card: [
          { required: true, message: "身份证号不能为空", trigger: "blur" },
          { validator: validatePass, trigger: "blur" },
        ],
        native: [{ required: true, message: "请输入籍贯", trigger: "blur" }],
      },
    };
  },
  methods: {
    // 检测身份证
    checkCard() {
      if (!this.ruleForm.identity_card) return;
      let CardId = this.ruleForm.identity_card;
      if (CardId.length == 15) {
        if (this.is15Card(CardId)) {
          this.go(CardId.length);
          this.id_right=true;
        } else {
          return this.$message({
            type: "error",
            message:
              "您的身份证号有误！请输入你真实的身份证号",
          });
        }
      } else if (CardId.length == 18) {
        let a_iden = CardId.split("");
        if (this.is18Card(CardId) && this.is18CardEnd(a_iden)) {
          // && this.is18CardEnd(a_iden)
          this.go(CardId.length);
          this.id_right=true;
          return this.is18Card(CardId);
        } else {
          return this.$message({
            type: "error",
            message:
              "您的身份证号有误！请输入你真实的身份证号，确保你的利益得到保障！",
          });
        }
      } else {
        return this.$message({
          type: "error",
          message:
            "您的身份证号有误！请输入你真实的身份证号，确保你的利益得到保障！",
        });
      }
    },

    // 检测18位身份证号最后一位是否符合要求
    is18CardEnd(a_idCard) {
      let sum = 0;
      if (a_idCard[17].toLowerCase() == "X") {
        a_idCard[17] = 10;
      }
      for (var i = 0; i < 17; i++) {
        sum += this.Wi[i] * a_idCard[i];
      }
      let valCodePosition = sum % 11;
      if (a_idCard[17] == this.ValideCode[valCodePosition]) {
        return true;
      } else {
        return false;
      }
    },

    // 验证最后一位校正码
    is18Card(idCard18) {
      let year = idCard18.substring(6, 10);
      let month = idCard18.substring(10, 12);
      let day = idCard18.substring(12, 14);
      let temp_date = new Date(year, parseFloat(month) - 1, parseFloat(day));
      if (
        temp_date.getFullYear() != parseFloat(year) ||
        temp_date.getMonth() != parseFloat(month) - 1 ||
        temp_date.getDate() != parseFloat(day)
      ) {
        return false;
      } else {
        return true;
      }
    },

    is15Card(idCard15) {
      let year = idCard15.substring(6, 8);
      let month = idCard15.substring(8, 10);
      let day = idCard15.substring(10, 12);
      let temp_date = new Date(year, parseFloat(month) - 1, parseFloat(day));
      if (
        temp_date.getYear() != parseFloat(year) ||
        temp_date.getMonth() != parseFloat(month) - 1 ||
        temp_date.getDate() != parseFloat(day)
      ) {
        return false;
      } else {
        return true;
      }
    },

    // 实现自动生成生日，性别，年龄
    go(val) {
      let iden = this.ruleForm.identity_card;
      let gender = null;
      let birthday = null;
      let myDate = new Date();
      let month = myDate.getMonth() + 1;
      let day = myDate.getDate();
      //   let age = 0;

      if (val === 18) {
        // age = myDate.getFullYear() - iden.substring(6, 10) - 1;
        gender = iden.substring(16, 17);
        birthday =
          iden.substring(6, 10) +
          "-" +
          iden.substring(10, 12) +
          "-" +
          iden.substring(12, 14);
        if (
          iden.substring(10, 12) < month ||
          (iden.substring(10, 12) == month && iden.substring(12, 14) <= day)
        );
        //   age++;
      }
      if (val === 15) {
        // age = myDate.getFullYear() - iden.substring(6, 8) - 1901;
        gender = iden.substring(13, 14);
        birthday =
          "19" +
          iden.substring(6, 8) +
          "-" +
          iden.substring(8, 10) +
          "-" +
          iden.substring(10, 12);
        if (
          iden.substring(8, 10) < month ||
          (iden.substring(8, 10) == month && iden.substring(10, 12) <= day)
        );
        //   age++;
      }

      if (gender % 2 === 0) gender = "女";
      else gender = "男";
      this.ruleForm.gender = gender;
      //   this.baseInfo.age = age;
      this.ruleForm.birthday = birthday;
    },

    //子组件校验，传递到父组件
    validateForm() {
      let flag = null;
      this.$refs.form2.validate(async (valid) => {
        if (valid && this.id_right==true) {
          flag = true;
          const temp= Object.assign({},this.templist,this.ruleForm)
          localStorage.setItem("list", JSON.stringify(temp));
        } else {
          flag = false;
        }
      });
      return flag;
    },
  },
};
</script>

<style>
.A_main2 {
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
</style>