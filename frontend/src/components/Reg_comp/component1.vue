<template>
  <div class="A_input">
    <el-form
      ref="form1"
      :model="form"
      label-width="100px"
      :rules="rules"
      :validate-on-rule-change="false"
    >
      <el-form-item label="选择学院" prop="college">
        <el-select
          v-model="form.college"
          placeholder="请选择"
          @change="changeSelect"
          style="width: 300px"
        >
          <el-option
            v-for="(item, index) in college"
            :key="index"
            :label="item.college_title"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="选择支部" prop="branch">
        <el-select
          v-model="form.branch"
          placeholder="请选择"
          style="width: 300px"
        >
          <el-option
            v-for="(item, index) in typeOptions"
            :key="index"
            :label="item.branch_title"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  props: {},
  components: {},
  data() {
    return {
      college: [],
      branch: {},
      typeOptions: [],
      form: {
        college: "",
        branch: "",
      },
      rules: {
        college: [{ required: true, message: "请选择学院", trigger: "change" }],
        branch: [{ required: true, message: "请选择支部", trigger: "change" }],
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
      const temp = await this.$http.get("branch/all");
      this.college = res.data;
      this.branch = temp.data;
    },
    changeSelect() {
      // 清空支部内容
      this.form.branch = "";
      this.typeOptions=[];
      // 遍历学院的下拉选项数组
      for (const k in this.college) {
        // 学院内容 是否等于 学院的下拉选择数组中的某一项
        if (this.form.college === this.college[k].id) {
          for (const t in this.branch) {
            if (this.college[k].college_title == this.branch[t].college_title) {
              this.typeOptions.push(this.branch[t]);
            }
          }
        }
      }
    },
    //子组件校验，传递到父组件
    validateForm() {
      let flag = null;
      this.$refs["form1"].validate(async (valid) => {
        if (valid) {
          flag = true;
          localStorage.setItem("list", JSON.stringify(this.form));
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
.A_input {
  display: flex;
  justify-content: space-around;
  margin-top: 80px;
  width: 100%;
}
.el-form-item__label {
  color: #303133;
  font-size: 14px;
  background-color: #f0f0f0;
  display: flex;
  justify-content: center;
}
</style>