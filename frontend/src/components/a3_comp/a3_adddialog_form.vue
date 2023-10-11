<template>
  <el-col :span="3"
    ><el-button @click="addDialogVisible = true" size="small"
      >添加用户</el-button
    >
    <!-- 添加用户对话框 -->
    <el-dialog
      title="添加用户"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed"
      :modal-append-to-body="false"
    >
      <!-- 添加用户内容主体区域 -->
      <el-form
        :model="addUserForm"
        :rules="addUserFormRules"
        ref="addUserFormRef"
        label-width="80px"
        class="a3_adddialog_form"
        width="60%"
      >
        <div class="a3_left">
          <el-form-item label="学号" prop="account" style="width: 300px">
            <el-input v-model="addUserForm.account"></el-input>
          </el-form-item>
          <el-form-item label="姓名" prop="name" style="width: 300px">
            <el-input v-model="addUserForm.name"></el-input>
          </el-form-item>
          <el-form-item label="选择学院" prop="college" style="width: 300px">
            <el-select
              v-model="addUserForm.college"
              placeholder="请选择"
              @change="changeSelect()"
            >
              <el-option
                v-for="(item, index) in college"
                :key="index"
                :label="item.college_title"
                :value="item.id"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="选择支部" prop="branch" style="width: 300px">
            <el-select v-model="addUserForm.branch" placeholder="请选择">
              <el-option
                v-for="(item, index) in typeOptions"
                :key="index"
                :label="item.branch_title"
                :value="item.id"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="性别" prop="gender" style="width: 300px">
            <el-input v-model="addUserForm.gender" disabled></el-input>
          </el-form-item>

          <el-form-item label="民族" prop="nation" style="width: 300px">
            <el-input
              v-model="addUserForm.nation"
              placeholder="如：满族"
            ></el-input>
          </el-form-item>
          <el-form-item label="班级" prop="classx" style="width: 300px">
            <el-input
              v-model="addUserForm.classx"
              placeholder="如：20计算机科学与技术二班"
            ></el-input>
          </el-form-item>
        </div>
        <div class="a3_right">
          <el-form-item
            label="身份证"
            prop="identity_card"
            style="width: 300px"
          >
            <el-input v-model="addUserForm.identity_card"></el-input>
          </el-form-item>

          <el-form-item label="出生日期" prop="birthday" style="width: 300px">
            <el-input v-model="addUserForm.birthday" disabled></el-input>
          </el-form-item>

          <el-form-item label="籍贯" prop="native" style="width: 300px">
            <el-input
              v-model="addUserForm.native"
              placeholder="如：湖南湘潭"
              size="small"
            ></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password" style="width: 300px">
            <el-input
              type="password"
              v-model="addUserForm.password"
              autocomplete="off"
            ></el-input>
          </el-form-item>
          <el-form-item
            label="确认密码"
            prop="checkpassword"
            style="width: 300px"
          >
            <el-input
              type="password"
              v-model="addUserForm.checkpassword"
              autocomplete="off"
            ></el-input>
          </el-form-item>

          <el-form-item label="手机号" prop="phone" style="width: 300px">
            <el-input v-model="addUserForm.phone" clearable></el-input>
          </el-form-item>
        </div>
      </el-form>
      <!-- 添加用户内容底部区域 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </span>
    </el-dialog>
  </el-col>
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
    var validatepassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.addUserForm.checkpassword !== "") {
          this.$refs.addUserFormRef.validateField("checkpassword");
        }
        callback();
      }
    };
    var validatepassword2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.addUserForm.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
    };
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
    return {
      Wi: [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2],
      ValideCode: [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2],
      // 控制添加用户对话框的显示与隐藏
      addDialogVisible: false,
      college: [],
      branch: {},
      temp: "",
      typeOptions: [],
      // 添加用户的表单数据
      addUserForm: {
        account: "",
        name: "",
        college: "",
        branch: "",
        gender: "",
        nation: "",
        classx: "",
        identity_card: "",
        birthday: "",
        native: "",
        checkpassword: "",
        phone: "",
      },

      // 添加用户的表单规则
      addUserFormRules: {
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
        college: [{ required: true, message: "请选择学院", trigger: "change" }],
        branch: [{ required: true, message: "请选择支部", trigger: "change" }],
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
  mounted() {
    this.getmessage();
  },
  methods: {
    async getmessage() {
      const res = await this.$http.get("college/all");
      const temp= await this.$http.get("branch/all");
      this.college=res.data;
      this.branch=temp.data;
    },
    changeSelect() {
      // 清空支部内容
      this.addUserForm.branch = "";
      this.typeOptions=[];

      // 遍历学院的下拉选项数组
      for (const k in this.college) {
        // 学院内容 是否等于 学院的下拉选择数组中的某一项
        if (this.addUserForm.college === this.college[k].id) {
          for(const t in this.branch)
          {
            if(this.college[k].college_title==this.branch[t].college_title)
            {
              this.typeOptions.push(this.branch[t]);
            }
          }
        }
      }
    },
    // 监听添加用户对话框的:close关闭事件,清除数据(resetFields)
    addDialogClosed() {
      this.$refs.addUserFormRef.resetFields();
    },
    // 点击按钮，添加用户,validate(预校验)
    addUser() {
      this.$refs.addUserFormRef.validate(async (valid) => {
        if (!valid) return;
        // 成功后向api发出添加用户的网络请求
        const res = await this.$http.post("user/create/", this.addUserForm);
        console.log(res);
        if (res.status !== 200) {
          this.$message.error("添加用户失败!");
        } else {
          this.$message.success("添加用户成功!");
          this.$emit("fatherMethod");
        }
        // 隐藏添加用户的对话框
        this.addDialogVisible = false;
      });
    },
    // 检测身份证
    checkCard() {
      if (!this.addUserForm.identity_card) return;
      let CardId = this.addUserForm.identity_card;
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
      let iden = this.addUserForm.identity_card;
      let gender = null;
      let birthday = null;
      let myDate = new Date();
      let month = myDate.getMonth() + 1;
      let day = myDate.getDate();

      if (val === 18) {
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
      }
      if (val === 15) {
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
      }

      if (gender % 2 === 0) gender = "女";
      else gender = "男";
      this.addUserForm.gender = gender;
      this.addUserForm.birthday = birthday;
    },
  },
};
</script>

<style>
.a3_adddialog_form {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-around;
}
</style>