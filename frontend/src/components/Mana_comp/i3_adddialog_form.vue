<template>
  <el-col :span="6"
    ><el-button @click="addDialogVisible = true" size="small" type="primary">
      <span v-if="this.data_f.valplus == 3">添加班级</span>
      <span v-if="this.data_f.valplus == 4">添加学院</span>
    </el-button>
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
        class="i3_adddialog_form"
        width="60%"
      >
        <el-form-item
          label="学院名称"
          prop="college_title"
          style="width: 400px"
        >
          <el-input
            v-model="addUserForm.college_title"
            :disabled="this.data_f.valplus == 3"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="支部名称"
          prop="branch_title"
          style="width: 400px"
          v-show="this.data_f.valplus == 3"
        >
          <el-input v-model="addUserForm.branch_title"></el-input>
        </el-form-item>
        <el-form-item label="备注" prop="remarks" style="width: 400px">
          <el-input v-model="addUserForm.remarks"></el-input>
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
    return {
      // 控制添加用户对话框的显示与隐藏
      addDialogVisible: false,
      temp: "",
      typeOptions: [],
      // 添加用户的表单数据
      addUserForm: {
        college_title: "",
        branch_title: "",
        remarks: "",
        college: "",
      },

      // 添加用户的表单规则
      addUserFormRules: {
        college_title: [
          { required: true, message: "请输入学院", trigger: "blur" },
        ],
      },
    };
  },
  created() {
    this.init();
  },
  // watch: {
  //   data_f: function (newVal) {
  //     this.addUserForm.college_title = newVal.college_title;
  //     this.addUserForm.college = newVal.college;
  //   },
  // },
  methods: {
    init() {
      if (this.data_f.college_title != null) {
        console.log(this.data_f.college_title)
        this.addUserForm.college_title = this.data_f.college_title;
        this.addUserForm.college = this.data_f.college;
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
        if (this.data_f.valplus == 3) {
          const res = await this.$http.post("branch/all/", this.addUserForm);
          if (res.status !== 201) {
            this.$message.error("添加支部失败!");
          }
          this.$message.success("添加支部成功!");
          // 隐藏添加用户的对话框
          this.$emit("fatherMethod");
          this.addDialogVisible = false;
        } else if (this.data_f.valplus == 4) {
          const res = await this.$http.post("college/all/", this.addUserForm);
          console.log(res);
          if (res.status !== 201) {
            this.$message.error("添加学院失败!");
          }
          this.$message.success("添加学院成功!");
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
.i3_adddialog_form {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-around;
  flex-direction: column;
  align-items: center;
}
</style>
