<template>
  <div class="aa">
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="100px"
      class="form_a"
    >
      <div class="left">
        <el-form-item label="学号" prop="account" style="width: 340px" size="medium">
          <el-input v-model.number="ruleForm.account"></el-input>
        </el-form-item>

        <el-form-item label="姓名" prop="name" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>

        <el-form-item label="性别" prop="gender" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.sex" disabled></el-input>
        </el-form-item>

        <el-form-item label="民族" prop="nation" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.nation" placeholder="如：满族"></el-input>
        </el-form-item>

        <el-form-item label="身份证" prop="identity_card" style="width: 340px" size="medium" >
          <el-input v-model="ruleForm.identity_card"></el-input>
        </el-form-item>
        <el-form-item label="出生日期" prop="birthday" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.birthday" disabled></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="phone" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.phone"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.email"></el-input>
        </el-form-item>
      </div>
      <div class="right">
        <el-form-item label="籍贯" prop="native" style="width: 340px" size="medium">
          <el-input
            v-model="ruleForm.native"
            placeholder="如：湖南湘潭"
          ></el-input>
        </el-form-item>
        <el-form-item label="学院" prop="college_title" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.college_title" disabled></el-input>
        </el-form-item>
        <el-form-item label="支部" prop="branch_title" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.branch_title" disabled></el-input>
        </el-form-item>
        <el-form-item label="班级" prop="classx" style="width: 340px" size="medium">
          <el-input
            v-model="ruleForm.classx"
            placeholder="如：20计算机科学与技术二班"
          ></el-input>
        </el-form-item>

        <el-form-item label="班主任" prop="headmaster" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.headmaster"></el-input>
        </el-form-item>
        <el-form-item label="学生工作职位" prop="job" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.job"></el-input>
        </el-form-item>
        <el-form-item label="住址" prop="address" style="width: 340px" size="medium">
          <el-input v-model="ruleForm.address"></el-input>
        </el-form-item>
      </div>
    </el-form>
    <div class="aa_btn">
      <el-button @click="saveForm('ruleForm')">保存</el-button>
      <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    let validatePhone = (rule, value, callback) => {
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
      temp_message: {
        option: [
          "status",
          "gender",
          "investigation_registration",
          "developer_date",
        ],
        Chinese: [
          "所处阶段",
          "性别",
          "积极分子考察登记表是否上传",
          "列为发展对象的日期",
        ],
      },
      temp: "",
      Wi: [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2],
      ValideCode: [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2],
      ruleForm: {
        account: "",
        name: "",
        gender: "",
        nation: "",
        classx: "",
        identity_card: "",
        birthday: "",
        native: "",
        phone: "",
        college_title: "",
        branch_title: "",
        email: "",
        headmaster: "",
        job: "",
        address: "",
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
        phone: [{ required: true, validator: validatePhone, trigger: "blur" }],
      },
    };
  },
  created() {
    this.showmessage();
  },
  methods: {
    // 检测身份证
    checkCard() {
      if (!this.ruleForm.identity_card) return;
      let CardId = this.ruleForm.identity_card;
      if (CardId.length == 15) {
        if (this.is15Card(CardId)) {
          this.go(CardId.length);
        } else {
          return this.$message({
            type: "error",
            message:
              "您的身份证号有误！请输入你真实的身份证号，确保你的利益得到保障！",
          });
        }
      } else if (CardId.length == 18) {
        let a_iden = CardId.split("");
        if (this.is18Card(CardId) && this.is18CardEnd(a_iden)) {
          // && this.is18CardEnd(a_iden)
          this.go(CardId.length);
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
      let sex = null;
      let birthday = null;
      let myDate = new Date();
      let month = myDate.getMonth() + 1;
      let day = myDate.getDate();
      //   let age = 0;

      if (val === 18) {
        // age = myDate.getFullYear() - iden.substring(6, 10) - 1;
        sex = iden.substring(16, 17);
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
        sex = iden.substring(13, 14);
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

      if (sex % 2 === 0) sex = "女";
      else sex = "男";
      this.ruleForm.sex = sex;
      //   this.baseInfo.age = age;
      this.ruleForm.birthday = birthday;
      //   this.ruleForm.birthplace = this.area[iden.substring(0, 2)];
      //   console.log(this.baseInfo);
    },
    async showmessage() {
      this.temp = JSON.parse(localStorage.getItem("account"));
      const res = await this.$http.get("/user/get1/" + this.temp);
      console.log(res);
      this.ruleForm.account = res.data.account;
      this.ruleForm.name = res.data.name;
      this.ruleForm.gender = res.data.gender;
      this.ruleForm.nation = res.data.nation;
      this.ruleForm.classx = res.data.classx;
      this.ruleForm.identity_card = res.data.identity_card;
      this.checkCard();
      this.ruleForm.native = res.data.native;
      this.ruleForm.phone = res.data.phone;
      this.ruleForm.branch_title = res.data.branch_title;
      this.ruleForm.college_title = res.data.college_title;
      this.ruleForm.job = res.data.job;
      this.ruleForm.email = res.data.email;
      this.ruleForm.headmaster = res.data.headmaster;
      this.ruleForm.address = res.data.address;
    },
    saveForm(ruleForm) {
      this.$refs[ruleForm].validate((valid) => {
        if (valid) {
          localStorage.setItem(
            "Personal_information",
            JSON.stringify(this.ruleForm)
          );
          this.$message({
            message: "保存成功",
            type: "success",
          });
        } else {
          this.$message.error("保全信息不完整，请继续填写完整");
          return false;
        }
      });
    },
    async submitForm(ruleForm) {
      // const res1 = await this.$http.post("export/all/", this.temp_message);
      // console.log(res1);
      this.$refs[ruleForm].validate(async (valid) => {
        if (valid) {
          const res = await this.$http.put(
            "user/put1/" + this.temp,
            this.ruleForm
          );
          if (res.status == 200) {
            this.$message({
              message: "提交成功",
              type: "success",
            });
          }
          else
          {
            this.$message.error("提交失败");
          }
        } else {
          this.$message.error("保全信息不完整，请继续填写完整");
          return false;
        }
      });
    },
  },
};
</script>

<style>
.aa {
  width:85%;
  height: 100%;
  background: #fff;
}
.aa_btn {
  display: flex;
  justify-content: center;
}
.form_a {
  width: 100%;
  height: 85%;
  display: flex;
  justify-content: center;
  margin-left: 70px;
}
.left {
  width: 50%;
}
.right {
  width: 50%;
}
</style>