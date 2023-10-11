<template>
  <div class="e">
    <el-form
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="150px"
      class="form_e"
    >
      <el-form-item
        label="加入党组织日期"
        prop="j_data"
        disabled
        style="width: 400px"
        size="medium"
      >
        <el-input
          v-model="ruleForm.j_data"
          placeholder="此处为管理员填写"
          disabled
        ></el-input>
      </el-form-item>
      <el-form-item
        label="转为正式党员日期"
        prop="formal_date"
        disabled
        style="width: 400px"
        size="medium"
      >
        <el-input
          v-model="ruleForm.formal_date"
          placeholder="此处为管理员填写"
          disabled
        ></el-input>
      </el-form-item>
      <el-form-item
        label="支部大会时间"
        prop="dbm_time2"
        disabled
        style="width: 400px"
        size="medium"
      >
        <el-input
          v-model="ruleForm.dbm_time2"
          placeholder="此处为管理员填写"
          disabled
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
    return {
      ruleForm: {
        j_data: "",
        formal_date: "",
        dbm_time2: "",
      },
      rules: {
        j_data: [
          {
            required: true,
            message: "请输入加入党组织日期",
            trigger: "blur",
          },
        ],
        formal_date: [
          {
            required: true,
            message: "请输入转为正式党员日期",
            trigger: "blur",
          },
        ],
        dbm_time2: [
          {
            required: true,
            message: "请输入支部大会时间",
            trigger: "blur",
          },
        ],
      },
    };
  },
  created() {
    this.showmessage();
  },
  methods: {
    async showmessage() {
      this.temp = JSON.parse(localStorage.getItem("account"));
      const res = await this.$http.get("/user/get6/" + this.temp);
      console.log(res);
      this.ruleForm.j_data = res.data.probation_date;
      this.ruleForm.formal_date = res.data.formal_date;
      this.ruleForm.dbm_time2 = res.data.formal_date;
    },
  },
};
</script>

<style>
.e {
  width: 100%;
  height: 100%;
  background: #fff;
}
.form_e{
  margin-top: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>