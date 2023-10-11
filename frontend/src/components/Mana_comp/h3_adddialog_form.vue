<template>
  <el-col :span="6"
    ><el-button @click="addDialogVisible = true" size="small" type="primary"
      >添加管理员</el-button
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
        class="h3_adddialog_form"
        width="60%"
      >
        <el-form-item label="帐号" prop="account" style="width: 400px">
          <el-input v-model="addUserForm.account"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="name" style="width: 400px">
          <el-input v-model="addUserForm.name"></el-input>
        </el-form-item>
        <el-form-item label="选择学院" prop="college" style="width: 400px">
          <el-select
            v-model="addUserForm.college"
            placeholder="请选择"
            @change="changeSelect()"
            style="width: 320px"
          >
            <el-option
              v-for="(item, index) in college"
              :key="index"
              :label="item.college_title"
              :value="item.id"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="选择班级" prop="branch" style="width: 400px">
          <el-select
            v-model="addUserForm.branch"
            placeholder="请选择"
            style="width: 320px"
          >
            <el-option
              v-for="(item, index) in typeOptions"
              :key="index"
              :label="item.branch_title"
              :value="item.id"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="密码" prop="password" style="width: 400px">
          <el-input
            type="password"
            v-model="addUserForm.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="确认密码"
          prop="checkpassword"
          style="width: 400px"
        >
          <el-input
            type="password"
            v-model="addUserForm.checkpassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>
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
  props: ["data_f"],
  components: {},
  data() {
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
    return {
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
        checkpassword: "",
        passwor: "",
        college_title: "0",
        branch_title: "1",
      },

      // 添加用户的表单规则
      addUserFormRules: {
        account: [{ required: true, message: "请输入账号", trigger: "blur" }],
        name: [{ required: true, message: "请输入姓名", trigger: "blur" }],
        college: [{ required: true, message: "请选择学院", trigger: "change" }],
        branch: [{ required: true, message: "请选择班级", trigger: "change" }],
        password: [
          { required: true, validator: validatepassword, trigger: "blur" },
        ],
        checkpassword: [
          { required: true, validator: validatepassword2, trigger: "blur" },
        ],
      },
    };
  },
  mounted()
  {
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
      // 清空班级内容
      this.addUserForm.branch = "";
      this.typeOptions=[];
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
        if (this.data_f == 3) {
          const res = await this.$http.post("lowadmin/all/", this.addUserForm);
          if (res.status !== 201) {
            this.$message.error("添加用户失败!");
          }
          this.$message.success("添加用户成功!");
          // 隐藏添加用户的对话框
          this.$emit("fatherMethod");
          this.addDialogVisible = false;
        } else if (this.data_f == 4) {
          const res = await this.$http.post(
            "mediuadmin/all/",
            this.addUserForm
          );
          if (res.status !== 201) {
            this.$message.error("添加用户失败!");
          }
          this.$message.success("添加用户成功!");
          // 隐藏添加用户的对话框
          this.$emit("fatherMethod");
          this.addDialogVisible = false;
        }
      });
    },
  },
};
</script>

<style>
.h3_adddialog_form {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
}
</style>
