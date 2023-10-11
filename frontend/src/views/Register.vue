<template>
  <div class="admin_main">
    <Register_title> </Register_title>
    <div class="A_title" v-html="'用&#8197;户&#8197;注&#8197;册'"></div>
    <div class="te_reg_main">
      <div class="step_box">
        <el-steps
          :active="code - 0"
          finish-status="success"
          simple
          style="margin-top: 100px"
          class="step"
        >
          <el-step title="选择学院" class="T_text"></el-step>
          <el-step title="填写个人资料" class="T_text"></el-step>
          <el-step title="设置密码" class="T_text"></el-step>
        </el-steps>
      </div>
      <keep-alive>
        <component :is="currentview" ref="form_for"></component>
      </keep-alive>
      <div class="A_btn">
        <el-button v-model="code" type="primary" @click="A_ret()"
          >返回</el-button
        >
        <el-button v-model="code" @click="A_next()">{{ message }}</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import Register_title from "@/components/Register_title.vue";
import A_component1 from "@/components/Reg_comp/component1.vue";
import A_component2 from "@/components/Reg_comp/component2.vue";
import A_component3 from "@/components/Reg_comp/component3.vue";
export default {
  props: {},
  components: {
    Register_title,
    A_component1,
    A_component2,
    A_component3,
  },
  data() {
    return {
      currentview: "A_component1",
      code: "0",
      message: "下一步",
    };
  },
  methods: {
    A_next() {
      if (this.currentview == "A_component1") {
        let flag = this.$refs.form_for.validateForm();
        if (flag) {
          this.code = "1";
          this.currentview = "A_component2";
        } else {
          this.$message.error("保全信息不完整，请继续填写完整");
        }
      } else if (this.currentview == "A_component2") {
        let flag = this.$refs.form_for.validateForm();
        if (flag) {
          this.code = "2";
          this.currentview = "A_component3";
          this.message = "注册";
        } else {
          this.$nextTick(() => {
            this.$message.error("保全信息不完整或者有误，请继续填写完整或修改");
          });
        }
      } else {
        this.$refs.form_for.validate(async (valid) => {
          if (valid) {
            //验证通过
            const res = await this.$http.post(
              "registration/create/",
              JSON.parse(localStorage.getItem("list"))
            );
            console.log(res);
            if (res.status != 201) {
              this.$message.error(res.data.entail);
            } else {
              this.code = "3";
              this.$message({
                undefined,
                message: "注册请求已提交，等待管理员审核",
                type: "success",
              });
            }
            this.$router.push({ path: "/" });
          }
        });
      }
    },
    A_ret() {
      if (this.currentview == "A_component1") {
        this.code = "0";
        this.$router.push({ path: "/" });
      } else if (this.currentview == "A_component2") {
        this.code = "1";
        this.currentview = "A_component1";
      } else {
        this.code = "2";
        this.currentview = "A_component2";
        this.message = "下一步";
      }
    },
  },
};
</script>

<style>
.admin_main {
  background-color: #f2f5f8;
}
.step_box {
  width: 80%;
  height: 20px;
  margin-left: 110px;
  margin-top: -70px;
}
.step {
  height: 30px;
  background-color: #e7f0f8;
}
.A_title {
  margin-top: -35px;
  font-size: 20px;
  color: #fff;
  display: flex;
  justify-content: center;
  margin-left: 1000px;
}
.te_reg_main {
  width: 80%;
  height: 600px;
  border: 1px solid #f0f0f0;
  border-radius: 4px;
  margin-left: 130px;
  margin-top: 40px;
  background-color: #fff;
}
.A_btn {
  margin-top: 50px;
  display: flex;
  justify-content: center;
}
</style>
